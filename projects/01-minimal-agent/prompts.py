"""
5 层 Context Builder — Context Engineering 的核心实践

5 层 context 分别是什么：
1. system       — 角色定位、行为约束、输出格式
2. task         — 用户当前任务、成功标准
3. memory       — 长期记忆（这里留接口，后续接 Mem0 / 向量库）
4. retrieved    — 当前检索到的证据（这里接 search_notes 结果）
5. recent_trace — 最近 N 步的执行摘要（不是完整 CoT）

为什么要分层？
- 控制每个层的内容，防止 context 污染
- 长期记忆可以独立缓存
- 检索证据独立更新，不影响其他层
- trace 摘要避免 prompt 越来越长

为什么要摘要 recent_trace 而不是完整 trace？
- LLM 上下文窗口有限
- 完整 trace 让模型分心
- 摘要足以让模型判断"下一步该做什么"
"""

from __future__ import annotations

from tools import get_tool_descriptions


def build_context(task: str, state: dict, tools: dict) -> dict:
    """组装 5 层 context，返回 dict（可转为 OpenAI/Anthropic 的 messages 格式）

    Args:
        task: 用户输入的任务
        state: Agent 当前 state（包含 steps 等）
        tools: 工具注册表

    Returns:
        {
          "system": "...",
          "task": "...",
          "memory": "...",
          "retrieved": "...",
          "recent_trace": "...",
          "step_count": int,
          "tool_names": [...],
          "raw_task": <原始 task，供 model.decide 用>,
        }
    """
    return {
        "system": _build_system(tools),
        "task": _build_task(task),
        "memory": _build_memory(state),
        "retrieved": _build_retrieved(state),
        "recent_trace": _build_recent_trace(state),
        "step_count": len(state.get("steps", [])),
        "tool_names": list(tools.keys()),
        "raw_task": task,
    }


def _build_system(tools: dict) -> str:
    """Layer 1: 系统层 — 永远不变的部分（可缓存）"""
    tool_desc = get_tool_descriptions()
    return f"""# 角色
你是「个人笔记搜索助手」，帮助用户在私有笔记库中检索信息并产出总结。

# 可用工具
{tool_desc}

# 输出格式（严格遵守，必须是合法 JSON）
{{
  "type": "tool_call" 或 "final_answer",
  "tool_name": "<工具名 或 null>",
  "args": {{...}} 或 null,
  "answer": "<最终答案 或 null>",
  "reason_summary": "<一句话解释你这个决策>"
}}

# 行为约束
1. 必须基于工具返回的证据回答，不要编造内容
2. 证据不足时调用更多工具，直到充分
3. 连续两次调用相同工具且结果一样 → 应该换策略或给出答案
4. 达到 5 步仍未完成 → 给出"无法完成"的最终答案
5. 不暴露内部思维过程，只输出 reason_summary"""


def _build_task(task: str) -> str:
    """Layer 2: 任务层 — 当前用户任务"""
    return f"""# 当前任务
{task}

# 成功标准
- 给出准确、简洁的回答
- 如有不确定，明确说明"未找到相关笔记\""""


def _build_memory(state: dict) -> str:
    """Layer 3: 长期记忆层（占位 — Day 4 实现，Day 7+ 升级到 Mem0）"""
    # 真实实现：从 Mem0 / 向量库加载用户长期偏好
    return "（暂无长期记忆 — 后续可接入 Mem0）"


def _build_retrieved(state: dict) -> str:
    """Layer 4: 检索证据层 — 从最近工具调用结果中提取"""
    evidence: list[str] = []
    for step in state.get("steps", []):
        obs = step.get("observation", {})
        if not obs.get("ok"):
            continue
        results = obs.get("results", [])
        for r in results:
            evidence.append(
                f"- [{r.get('id')}] {r.get('title')}: {r.get('snippet')}"
            )
    if not evidence:
        return "（暂无检索证据）"
    return "# 已检索证据\n" + "\n".join(evidence)


def _build_recent_trace(state: dict, n: int = 3) -> str:
    """Layer 5: 近期 trace 摘要 — 只看最近 N 步（不是完整历史）

    为什么是摘要不是完整 trace？
    - 防 context 爆炸
    - 防模型被旧动作干扰
    - 摘要足以判断"我下一步该做什么"
    """
    steps = state.get("steps", [])
    if not steps:
        return "（暂无执行步骤）"

    recent = steps[-n:]
    lines = [f"# 最近 {len(recent)} 步"]
    for s in recent:
        action = s["action"]
        obs = s["observation"]
        tool = action.get("tool_name") or "?"
        ok = obs.get("ok", False)
        if ok:
            lines.append(f"- Step {s['step']}: 调用 `{tool}` → ✅ 成功")
        else:
            err = obs.get("error", "unknown")
            hint = obs.get("hint", "")
            lines.append(f"- Step {s['step']}: 调用 `{tool}` → ❌ {err}（{hint}）")

    # 重复动作检测
    tool_calls = [s["action"].get("tool_name") for s in steps]
    if len(tool_calls) >= 2 and tool_calls[-1] == tool_calls[-2]:
        lines.append("\n⚠️ 你已经连续两次调用同一个工具，请考虑换策略或给出最终答案。")

    return "\n".join(lines)


# ============================================================
# 辅助：把 5 层 context 转成 OpenAI / Anthropic messages 格式
# ============================================================

def to_messages(context: dict) -> list[dict]:
    """把 context dict 转成 OpenAI 风格的 messages 列表

    用法（接真实 LLM 时）：
        ctx = build_context(task, state, tools)
        messages = to_messages(ctx)
        response = openai_client.chat.completions.create(
            model="...",
            messages=messages,
            response_format={"type": "json_object"},
        )
    """
    user_content = f"""{context['task']}

{context['retrieved']}

{context['recent_trace']}

{context['memory']}

请按 system 指定的 JSON 格式返回下一步动作。"""

    return [
        {"role": "system", "content": context["system"]},
        {"role": "user", "content": user_content},
    ]