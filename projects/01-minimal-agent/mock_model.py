"""
Mock Model — 不用 API key 也能跑 Agent 的测试模型

目的：
- Day 2 先用 MockModel 跑通整个流程
- Day 5 写 eval cases 时用它批量跑
- 后期接真实 LLM 时，对比 MockModel 和真实模型的输出差异

Mock 策略（极简关键词匹配）：
- 含 "搜索" / "查找" / "笔记" → 先 search_notes，再回答
- 含 "总结" / "写" / "保存" → search + write_summary
- 空任务 / 其他 → 直接 final_answer

生产环境替换为：
- OpenAI: openai.OpenAI().chat.completions.create(...)
- Anthropic: anthropic.Anthropic().messages.create(...)
- DeepSeek / Qwen: 用 OpenAI 兼容接口
"""

from __future__ import annotations

from schemas import Action


class MockModel:
    """极简 Mock 模型 — 用关键词匹配模拟 LLM 决策"""

    def decide(self, context: dict) -> Action:
        # 优先用 raw_task（原文），回退 task
        task = context.get("raw_task") or context.get("task", "")
        task = task.strip()

        # 检查历史步骤（agent.py 注入 _steps）
        steps = context.get("_steps", [])
        has_searched = any(
            s.get("action", {}).get("tool_name") == "search_notes"
            for s in steps
        )
        has_written = any(
            s.get("action", {}).get("tool_name") == "write_summary"
            for s in steps
        )

        # 空任务 → 直接回答
        if not task:
            return self._final_answer("（空任务）请告诉我你想搜索什么")

        wants_summary = any(kw in task for kw in ["总结", "写", "保存"])
        wants_search = any(kw in task for kw in ["搜索", "查找", "找", "笔记", "search"])

        # 总结类：search → write → answer
        if wants_summary:
            if not has_searched:
                return Action(
                    type="tool_call",
                    tool_name="search_notes",
                    args={"query": task, "limit": 3},
                    reason_summary="先搜索相关笔记",
                )
            if not has_written:
                return Action(
                    type="tool_call",
                    tool_name="write_summary",
                    args={
                        "text": f"# 关于「{task}」的总结\n\n（这是 Mock 生成的占位总结，请接入真实 LLM 生成实际内容）",
                        "filename": "summary.md",
                    },
                    reason_summary="证据已收集，写入文件",
                )
            return self._final_answer(f"已基于「{task}」生成总结，请查看 output/summary.md")

        # 搜索类：search → answer
        if wants_search:
            if not has_searched:
                return Action(
                    type="tool_call",
                    tool_name="search_notes",
                    args={"query": task, "limit": 3},
                    reason_summary="搜索笔记库",
                )
            return self._final_answer(f"已搜索「{task}」，请查看上面的检索结果")

        # 兜底：直接回答
        return self._final_answer(f"MockModel 暂不支持的任务：{task}（试试加'搜索'或'总结'关键词）")

    def _final_answer(self, answer: str) -> Action:
        return Action(
            type="final_answer",
            answer=answer,
            reason_summary="给出最终答案",
        )


# ============================================================
# 真实 LLM 接入示例（Day 7+ 启用，需要安装 openai + 设置 .env）
# ============================================================

class OpenAIModel:
    """OpenAI 兼容接口（支持 OpenAI / DeepSeek / 通义千问）

    用法：
        model = OpenAIModel(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.deepseek.com/v1",
            model="deepseek-chat",
        )
    """

    def __init__(self, api_key: str, base_url: str = "https://api.openai.com/v1", model: str = "gpt-4o-mini"):
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("请先 pip install openai")
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def decide(self, context: dict) -> Action:
        from prompts import to_messages
        from pydantic import BaseModel

        # 用 Pydantic 强制 JSON 输出
        class ActionSchema(BaseModel):
            type: str
            tool_name: str | None = None
            args: dict | None = None
            answer: str | None = None
            reason_summary: str = ""

        messages = to_messages(context)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        content = response.choices[0].message.content
        parsed = ActionSchema.model_validate_json(content)
        return Action(**parsed.model_dump())