"""
最小 Agent 主循环 — First 7 Days Sprint 的核心交付物

这是 200 行内的可运行 Agent：
- 5 步循环限制（防死循环）
- 工具白名单（防未授权调用）
- 每步写 JSONL trace（可审计、可重放）
- 结构化错误（不抛 stack trace 给上层）
- 高风险工具的 human-in-the-loop 占位

理解这段代码后，再去看 LangGraph 源码会豁然开朗——
"原来 LangGraph 封装的就是这个循环"。

运行：
    python agent.py "搜索 Python 异步笔记"
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict
from pathlib import Path

from prompts import build_context
from tools import TOOL_REGISTRY
from schemas import Action


def run_agent(
    task: str,
    model,
    trace_path: Path | None = None,
    max_steps: int = 5,
) -> dict:
    """运行 Agent 主循环

    Args:
        task: 用户任务
        model: 模型对象，需要有 .decide(context, state) 方法
        trace_path: trace 输出路径（None 表示不写）
        max_steps: 最大步数（默认 5）

    Returns:
        {
          "task": "...",
          "steps": [{"step": 1, "action": {...}, "observation": {...}, ...}, ...],
          "final": <最终答案 或 {"ok": false, "reason": "..."}>,
          "status": "completed" | "failed" | "running"
        }
    """
    state: dict = {
        "task": task,
        "steps": [],
        "final": None,
        "status": "running",
    }

    # 清理旧 trace
    if trace_path and trace_path.exists():
        trace_path.unlink()

    for step_id in range(1, max_steps + 1):
        # === 1. 构建 5 层 context ===
        context = build_context(task=task, state=state, tools=TOOL_REGISTRY)
        context["_steps"] = state["steps"]  # 注入 steps 给 MockModel 用

        # === 2. 模型决策 ===
        t0 = time.time()
        action = model.decide(context)
        latency_ms = (time.time() - t0) * 1000

        # === 3. 是否最终答案 ===
        if action.type == "final_answer":
            state["final"] = action.answer
            state["status"] = "completed"
            _record_step(state, trace_path, step_id, action, {"ok": True}, latency_ms)
            return state

        # === 4. 工具白名单 ===
        if action.tool_name not in TOOL_REGISTRY:
            observation = {
                "ok": False,
                "error": "unknown_tool",
                "retryable": False,
                "hint": f"可用工具: {list(TOOL_REGISTRY.keys())}",
            }
            _record_step(state, trace_path, step_id, action, observation, latency_ms)
            continue

        tool_meta = TOOL_REGISTRY[action.tool_name]

        # === 5. 高风险工具：human-in-the-loop（占位） ===
        if tool_meta.get("requires_confirmation"):
            # 实际项目应弹窗或 CLI 询问用户
            # 这里默认通过，打印日志
            print(f"⚠️  [HITL] 调用高风险工具 {action.tool_name}，参数={action.args}")

        # === 6. 调用工具，捕获所有异常 ===
        try:
            observation = tool_meta["func"](**(action.args or {}))
        except Exception as exc:
            observation = {
                "ok": False,
                "error": "tool_exception",
                "retryable": False,
                "message": str(exc),
            }

        _record_step(state, trace_path, step_id, action, observation, latency_ms)

    # === 7. 超过 max_steps ===
    state["final"] = {"ok": False, "reason": "max_steps_exceeded"}
    state["status"] = "failed"
    return state


def _record_step(
    state: dict,
    trace_path: Path | None,
    step_id: int,
    action: Action,
    observation: dict,
    latency_ms: float,
) -> None:
    """记录一步到 state 和 trace JSONL"""
    step = {
        "step": step_id,
        "action": asdict(action),
        "observation": observation,
        "latency_ms": round(latency_ms, 2),
        "timestamp": time.time(),
    }
    state["steps"].append(step)

    if trace_path:
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        with trace_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(step, ensure_ascii=False) + "\n")


def pretty_print_result(result: dict) -> None:
    """漂亮打印 Agent 结果"""
    print("\n" + "=" * 60)
    print(f"📝 任务: {result['task']}")
    print(f"📊 状态: {result['status']}")
    print(f"🔢 步数: {len(result['steps'])}")
    print("=" * 60)

    for step in result["steps"]:
        action = step["action"]
        obs = step["observation"]
        print(f"\n--- Step {step['step']} ({step['latency_ms']}ms) ---")
        print(f"🤔 决策: {action.get('reason_summary', '')}")
        if action.get("type") == "tool_call":
            print(f"🔧 调用: {action.get('tool_name')}({action.get('args')})")
        else:
            print(f"✅ 最终答案: {action.get('answer')}")
        ok = obs.get("ok")
        if ok:
            # 只打印关键字段，不打印完整结果
            keys = [k for k in obs.keys() if k != "ok"]
            summary = {k: obs[k] for k in keys[:3]}
            print(f"👀 观察: {summary}")
        else:
            print(f"❌ 失败: {obs.get('error')} - {obs.get('hint', obs.get('message', ''))}")

    print("\n" + "=" * 60)
    print("🎯 最终结果:")
    print(json.dumps(result["final"], ensure_ascii=False, indent=2))
    print("=" * 60)


# ============================================================
# CLI 入口
# ============================================================

if __name__ == "__main__":
    import sys
    from mock_model import MockModel

    # 从命令行参数或输入框拿任务
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
    else:
        task = input("请输入任务（例：搜索 Python 异步笔记）：").strip()

    if not task:
        print("任务不能为空")
        sys.exit(1)

    trace_path = Path("./trace/run.jsonl")
    print(f"🚀 启动 Agent，trace → {trace_path}")

    result = run_agent(
        task=task,
        model=MockModel(),
        trace_path=trace_path,
        max_steps=5,
    )

    pretty_print_result(result)