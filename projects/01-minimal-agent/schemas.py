"""
共享类型定义

把 Action / Step 拆出来避免循环引用：
- agent.py 需要 Action
- mock_model.py 也需要返回 Action
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Action:
    """模型输出的一个动作决策

    字段:
      type           - "tool_call"（调用工具） 或 "final_answer"（结束回答）
      tool_name      - 调用的工具名（仅 tool_call 时有）
      args           - 工具参数（仅 tool_call 时有）
      answer         - 最终答案（仅 final_answer 时有）
      reason_summary - 一句话解释决策原因（用于审计，不要存完整 CoT）
    """
    type: str
    tool_name: str | None = None
    args: dict | None = None
    answer: str | None = None
    reason_summary: str = ""


@dataclass
class Step:
    """单步执行记录，写入 trace JSONL"""
    step: int
    action: dict[str, Any]
    observation: dict[str, Any]
    latency_ms: float
    timestamp: float
    cost_estimate: float = 0.0  # 预留：token 成本估算