"""
冒烟测试 — Day 2 跑通证明基础架构 OK

不需要 API key，用 MockModel 跑。
跑通后说明：
- 5 步循环正常
- 工具白名单生效
- trace 能写
- context builder 正确组装

运行：
    python tests/test_smoke.py
"""

import json
import sys
from pathlib import Path

# 加项目根目录到 sys.path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from agent import run_agent, pretty_print_result
from mock_model import MockModel


# ====== 测试用例 ======

TEST_CASES = [
    ("normal", "搜索 Python 异步笔记"),
    ("normal", "查找 React Hooks"),
    ("normal", "总结 Agent 基础概念"),
    ("edge", ""),
    ("edge", "搜索 xyz999 不存在的关键词"),
]


def run_one(category: str, task: str, model, trace_dir: Path) -> dict:
    """跑一个测试用例，返回结果摘要"""
    trace_path = trace_dir / f"smoke_{category}.jsonl"
    result = run_agent(
        task=task,
        model=model,
        trace_path=trace_path,
        max_steps=5,
    )
    return {
        "task": task,
        "category": category,
        "status": result["status"],
        "step_count": len(result["steps"]),
        "has_final": result["final"] is not None,
        "trace_file": str(trace_path.name),
    }


def main():
    print("🧪 开始冒烟测试...\n")
    trace_dir = PROJECT_ROOT / "trace"
    trace_dir.mkdir(exist_ok=True)

    model = MockModel()
    results = []
    for category, task in TEST_CASES:
        print(f"\n--- [ {category} ] {task or '(空)'} ---")
        summary = run_one(category, task, model, trace_dir)
        results.append(summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))

    # 汇总
    print("\n" + "=" * 60)
    print("📊 冒烟测试汇总")
    print("=" * 60)
    completed = sum(1 for r in results if r["status"] == "completed")
    print(f"完成：{completed} / {len(results)}")

    # 简单断言
    assert completed >= 3, "至少要 3 个任务能完成"
    assert all(r["has_final"] for r in results), "所有任务都要有 final 字段"

    print("✅ 冒烟测试通过！")
    return 0


if __name__ == "__main__":
    sys.exit(main())