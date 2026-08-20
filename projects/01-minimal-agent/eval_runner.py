"""
Eval Runner — 跑 20 条 eval cases，生成 eval_report

运行：
    python eval_runner.py

输出：
    eval_results.json — 每条 case 的详细结果
    eval_report.md   — 自动汇总报告（手动补充观察）
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from agent import run_agent
from mock_model import MockModel


def load_cases(path: str) -> list[dict]:
    cases = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


def score_case(case: dict, result: dict) -> dict:
    """简单评分（生产环境用 LLM-as-judge）"""
    task_tools = [s["action"].get("tool_name") for s in result["steps"] if s["action"].get("type") == "tool_call"]
    expected_tools = case.get("expected_tools", [])
    expected_status = case.get("expected_status", "completed")
    expected_keywords = case.get("expected_keywords", [])
    final_answer = str(result.get("final") or "")

    # 工具序列匹配
    tool_seq_match = all(t in task_tools for t in expected_tools)

    # 关键词匹配
    keyword_match = all(kw in final_answer for kw in expected_keywords) if expected_keywords else True

    # 状态匹配
    status_match = result["status"] == expected_status

    # 是否调用了禁止工具
    forbidden_called = any(
        t not in ["search_notes", "write_summary", None]
        for t in task_tools
    )

    score = "pass"
    if not status_match:
        score = "fail_status"
    elif expected_tools and not tool_seq_match:
        score = "fail_tools"
    elif expected_keywords and not keyword_match:
        score = "fail_keywords"
    elif forbidden_called:
        score = "fail_forbidden"

    return {
        "id": case["id"],
        "category": case["category"],
        "input": case["input"],
        "expected_tools": expected_tools,
        "actual_tools": task_tools,
        "expected_status": expected_status,
        "actual_status": result["status"],
        "step_count": len(result["steps"]),
        "has_keywords": keyword_match,
        "score": score,
    }


def main():
    cases_path = PROJECT_ROOT / "eval_cases.jsonl"
    if not cases_path.exists():
        print(f"❌ 找不到 {cases_path}")
        return 1

    print(f"📋 加载 {cases_path.name}...")
    cases = load_cases(str(cases_path))
    print(f"   共 {len(cases)} 条\n")

    model = MockModel()
    trace_dir = PROJECT_ROOT / "trace" / "eval"
    trace_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for i, case in enumerate(cases, 1):
        print(f"[{i:2d}/{len(cases)}] {case['id']:12s} {case['category']:6s} {case['input'][:30]}")
        trace_path = trace_dir / f"{case['id']}.jsonl"
        result = run_agent(
            task=case["input"],
            model=model,
            trace_path=trace_path,
            max_steps=5,
        )
        scored = score_case(case, result)
        results.append(scored)

    # 写入 JSON 结果
    output_path = PROJECT_ROOT / "eval_results.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total": len(results),
            "results": results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\n📊 详细结果 → {output_path}")

    # 汇总
    print("\n" + "=" * 60)
    by_cat = {}
    for r in results:
        by_cat.setdefault(r["category"], []).append(r)
    for cat, items in by_cat.items():
        passed = sum(1 for r in items if r["score"] == "pass")
        print(f"  {cat:8s}: {passed}/{len(items)} 通过")
    overall = sum(1 for r in results if r["score"] == "pass")
    print(f"  {'overall':8s}: {overall}/{len(results)} 通过 ({100*overall/len(results):.0f}%)")

    return 0


if __name__ == "__main__":
    sys.exit(main())