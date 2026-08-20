# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目性质

这是一个 **15 周学习工作台**（零基础 → Agent 求职就绪），不是传统代码项目。
方法论源自 [AgentGuide](https://github.com/adongwanai/AgentGuide)：**"做出什么 > 学过什么"**。

8 个阶段：定方向（W1）→ Python 强化（W2-4）→ First 7 Days Sprint（W5）→ RAG（W6-7）→ 框架（W8-9）→ 多 Agent + MCP（W10-11）→ 简历项目（W12-13）→ 求职冲刺（W14-15）。

**唯一有真实代码的子项目**：`projects/01-minimal-agent/`。其他三个项目目录（02/03/04）只有 README 占位。

## 每日工作流

用户每天打开的是 `todos/` 下对应日期的文件（91 个 markdown），不是 `TODO.md`。

1. 打开 `todos/{NN}-stage-{N}/W{周}-D{天}-{weekday}.md`
2. 逐项勾选 checkbox
3. 周末打开 `W{周}-review.md` 做周验收
4. 每天至少 commit 一次 git

总览和进度追踪在 `TODO.md`（不是 todos 文件本身）。

## 核心架构：01-minimal-agent

手写的 200 行最小 Agent（不依赖 LangChain/LangGraph），用于理解 Agent 本质。代码运行机制：

```
用户 task → run_agent() 主循环（≤5 步）
  ├─ prompts.build_context() → 5 层 context dict
  ├─ model.decide(context) → Action (tool_call | final_answer)
  ├─ tools.TOOL_REGISTRY[tool_name].func(**args) → observation
  └─ 每步 append JSONL trace 到 trace/{run_id}.jsonl
```

**关键约束**（写在每个模块的 docstring 里）：
- **工具白名单**：未知工具返回 `{"ok": false, "error": "unknown_tool"}`，不抛异常
- **结构化错误**：工具返回 `{ok, error, retryable, hint}`，永远不抛 stack trace 给上层
- **高风险工具**（`requires_confirmation: True`）触发 HITL 占位（目前只打印日志）
- **trace 可重放**：每步都写 JSONL，含 `step / action / observation / latency_ms / timestamp`

### 模块职责

| 文件 | 职责 | 注意点 |
|---|---|---|
| `agent.py` | `run_agent()` 主循环 + CLI 入口 | max_steps 默认 5 |
| `tools.py` | 2 个工具实现 + `TOOL_REGISTRY` dict | `search_notes` 是字符串匹配，生产环境换向量检索 |
| `prompts.py` | 5 层 context builder（system/task/memory/retrieved/recent_trace） | 第 3 层 memory 当前是占位 |
| `mock_model.py` | 不用 API key 的模型（用关键词匹配 + 关键词触底判断） | 用于跑 eval 无需花钱 |
| `schemas.py` | `Action` / `Step` dataclass | 拆出来避免循环引用 |
| `eval_runner.py` | 跑 `eval_cases.jsonl` 20 条 → `eval_results.json` | 评分：status / tools / keywords 三层 |
| `tests/test_smoke.py` | 冒烟测试 | 不需要 API key |

### 5 层 Context（prompts.py）

1. **system** — 角色 + 工具描述 + JSON 输出格式（可缓存）
2. **task** — 用户目标 + 成功标准
3. **memory** — 长期记忆（**当前是占位字符串**，未接入 Mem0）
4. **retrieved** — 从最近工具调用的 `ok=true` 结果中提取 evidence
5. **recent_trace** — 最近 3 步的摘要（非完整 CoT），并检测连续重复工具调用

## 常用命令

```bash
# 进入项目
cd projects/01-minimal-agent

# 创建虚拟环境（项目内有 .venv 目录）
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 跑冒烟测试（不需要 API key）
python tests/test_smoke.py

# 跑 20 条 eval（用 MockModel，无需 key）
python eval_runner.py

# CLI 模式试跑一次
python agent.py "搜索 Python 异步笔记"

# 看 trace
ls trace/*.jsonl
```

环境变量模板：`.env.example`（默认 OpenAI 兼容 DeepSeek）。MockModel 不需要任何 key。

## Eval 评分逻辑（eval_runner.py:score_case）

四档优先级 `fail_status > fail_tools > fail_keywords > fail_forbidden`，其他都算 pass。
`forbidden_called` 判定：调用了非 `search_notes`/`write_summary` 的工具 → fail。

## 新增工具的标准流程

1. 在 `tools.py` 实现函数 + 加进 `TOOL_REGISTRY`（含 `func / description / requires_confirmation / input_schema`）
2. 在 `tool_cards/<name>.md` 用 `docs/tool-card-template.md` 模板写工具卡
3. 在 `prompts.py` 的 `_build_system()` 调 `get_tool_descriptions()` 自动同步（无需手改 prompt）
4. 在 `eval_cases.jsonl` 加覆盖新工具的 case（normal + edge + safety 各一条）

## 不要做的事

- **不要直接装 LangChain/LangGraph** — 这是手写 Agent，目标是理解原理（见 requirements.txt 注释）
- **不要在 `notes/` 之外的根目录写笔记** — 笔记统一放 `notes/`
- **不要把 trace 数据 commit** — `.gitignore` 已忽略 `trace/*.jsonl`，只保留 `trace/schema.json`
- **不要暴露完整 CoT 给模型** — 只记 `reason_summary`，生产审计用