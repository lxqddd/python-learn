# 🚀 First 7 Days Sprint · 任务清单

> **整个计划的核心里程碑**——7 天内产出 1 个可演示、可评估、有 trace 的最小 Agent。
> 方法论来源：[AgentGuide/02-first-7-days.md](https://github.com/adongwanai/AgentGuide)

---

## 📅 整体节奏

| Day | 主题 | 核心交付物 |
|---|---|---|
| **D1** | 建立边界 | 1 页概念笔记 + 项目场景说明 |
| **D2** | 手写最小 Agent Loop | 200 行 Python，循环 ≤5 步，2 个工具，JSONL trace |
| **D3** | 工具设计 | 每个工具写 tool card（schema / 错误 / 例子） |
| **D4** | Context Engineering | 5 层 context builder |
| **D5** | 20 条 Eval | 10 正常 + 5 边界 + 5 安全 |
| **D6** | 项目打包 | README + eval_report + demo_script |
| **D7** | 复盘 + 简历表达 | 用模板产出简历 bullet |

---

## Day 1 · 建立边界（约 2h）

**目标**：想清楚你的最小 Agent 要解决什么问题，**不要写代码**。

- [ ] 阅读 [`docs/concept-notes.md`](../docs/concept-notes.md)，用自己的话写下理解
- [ ] 阅读 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [ ] 决定项目场景（推荐先做"**个人笔记搜索助手**"）：
  - 输入：用户的自然语言查询
  - 工具：`search_notes(query)` + `write_summary(text)`
  - 输出：基于笔记内容的总结
- [ ] 画一个最小流程图：

```
┌─────────┐    ┌──────────┐    ┌──────────┐
│  用户    │ →  │  Agent   │ →  │  总结    │
│  输入    │    │  循环    │    │  输出    │
└─────────┘    └─────┬────┘    └──────────┘
                    ↓
              ┌──────────┐
              │  工具调用  │
              │ (search) │
              └──────────┘
```

- [ ] 回答 7 个问题（来自 `docs/concept-notes.md` 启动前的检查清单）

**📦 产出**：
- `docs/concept-notes.md` 中"我的理解"6 个填空
- 流程图（可手绘拍照或用 draw.io）
- 项目场景的 7 问清单

---

## Day 2 · 手写最小 Agent Loop（约 4h）

**目标**：**不参考任何框架**，纯 Python 写一个能跑的最小 Agent。

- [ ] 在 `projects/01-minimal-agent/` 下打开 `agent.py`
- [ ] 实现 `run_agent(task, tools, model, max_steps=6)` 函数
- [ ] 限制：
  - 最多 5-6 步（防无限循环）
  - 工具白名单（未知工具 → 返回 error 而不是崩）
  - 每个 step 写 JSONL trace
  - 可读错误（结构化 JSON，不用 stack trace）
- [ ] 实现 2 个工具（`tools.py`）：
  - `search_notes(query)`: 简单字符串匹配 in-memory 笔记
  - `write_summary(text)`: 写入文件
- [ ] 用 `MockModel` 先跑通（不需要 API key）

**参考代码**（来自 AgentGuide `examples/minimal-agent-loop.md`）：

```python
def run_agent(task, tools, model, max_steps=6):
    state = {"task": task, "steps": [], "final": None}
    for step_id in range(1, max_steps + 1):
        context = build_context(task=task, state=state, tools=tools)
        action = model.decide(context)
        if action.type == "final_answer":
            state["final"] = action.content
            return state
        if action.tool_name not in tools:
            observation = {"ok": False, "error": "unknown_tool"}
            continue
        try:
            observation = tools[action.tool_name].call(**action.args)
        except Exception as exc:
            observation = {"ok": False, "error": str(exc)}
        state["steps"].append({
            "step": step_id,
            "action": action,
            "observation": observation,
        })
    state["final"] = {"ok": False, "reason": "max_steps_exceeded"}
    return state
```

**📦 产出**：
- 能跑的 `agent.py` + `tools.py`
- 至少 3 条 `trace/*.jsonl` 记录
- 5 个固定任务能跑通

---

## Day 3 · 工具设计（约 2h）

**目标**：让工具"对模型友好"。

- [ ] 阅读 [Anthropic: Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [ ] 为每个工具写 tool card（用 [`docs/tool-card-template.md`](../docs/tool-card-template.md)）：
  - 工具名、用途、何时用 / 不用、参数 schema、返回 schema、错误码、例子
- [ ] 加入：分页、截断、重试、超时
- [ ] 高风险工具标记 `requires_confirmation`

**📦 产出**：
- 2 个 tool card 文件
- 工具列表（带权限分级）

---

## Day 4 · Context Engineering（约 2h）

**目标**：控制进入模型的内容。

- [ ] 实现 5 层 context builder（`prompts.py`）：
  1. **system** — 角色 + 边界 + 输出格式
  2. **task** — 用户目标 + 成功标准 + 禁止行为
  3. **memory** — 长期记忆摘要
  4. **retrieved evidence** — 当前检索到的证据
  5. **recent trace** — 最近 N 步的动作+观察摘要
- [ ] 长工具结果只保留 summary + 可追溯引用
- [ ] 同任务重复跑，prompt 结构稳定

**📦 产出**：
- `prompts.py` 实现 5 层构建
- 测试：跑 2 次同样任务，验证 prompt 一致性

---

## Day 5 · 20 条 Eval（约 3h）

**目标**：从"觉得能跑"到"可证明能跑"。

- [ ] 写 20 条 eval cases（`eval_cases.jsonl`）：
  - **10 条正常任务**：期望工具调用顺序 + 最终答案包含特定关键词
  - **5 条边界任务**：空输入、超长输入、工具返回错误、连续相同工具调用
  - **5 条安全任务**：未知工具、敏感词、注入尝试、超出步数
- [ ] 每条 case 字段：
  ```json
  {
    "id": "normal-01",
    "category": "normal | edge | safety",
    "input": "...",
    "expected_tools": ["search_notes"],
    "expected_keywords": ["..."],
    "forbidden_behavior": ["..."],
    "scoring": "exact_match | keyword_match | human_review"
  }
  ```
- [ ] 跑一遍，记录：成功率、平均步数、失败原因
- [ ] 高级可学：[Promptfoo](https://github.com/promptfoo/promptfoo) 或 [DeepEval](https://github.com/confident-ai/deepeval)

**📦 产出**：
- `eval_cases.jsonl`（20 条）
- `eval_results.md`（跑分结果）

---

## Day 6 · 项目打包（约 2h）

**目标**：别人能 clone-and-run。

- [ ] 写 `README.md`：
  - 项目目标、架构图、安装、运行、测试、限制
- [ ] 写 `eval_report.md`：
  - 测试数据、失败类型、改进计划
- [ ] 写 `demo_script.md`：
  - 3 个演示场景 + 预期输出
- [ ] 验证：从零 clone，按 README 一遍能跑通最小 demo

**📦 产出**：
- 3 个 Markdown 文档
- 一个干净的 `git commit`

---

## Day 7 · 复盘 + 简历表达（约 2h）

**目标**：把项目变成可讲的故事。

- [ ] 失败归因：失败中工具失败 / 检索失败 / 模型误判 / 权限问题 / 上下文污染各占多少？
- [ ] 用模板产出简历 bullet：

> 构建面向「个人笔记搜索」场景的 Agent 系统，采用 ReAct loop + 工具注册表 + 分层 context builder，接入 2 个外部工具并对高风险动作设置 human-in-the-loop；设计 20 条端到端 eval case（10 正常 + 5 边界 + 5 安全），任务成功率达到 X%，通过工具结果截断将平均成本降低 X%。

- [ ] 更新 `README.md` 进度表，把阶段 2 勾上 ✅

**📦 产出**：
- 简历 bullet（可贴进简历）
- 1 篇博客/笔记（可选，发到知乎或掘金）

---

## ✅ 7 天后检查清单

- [ ] 200 行最小 Agent 能跑
- [ ] 2 个工具有 tool card
- [ ] 5 层 context builder 已实现
- [ ] 20 条 eval case 跑过，分数记录
- [ ] README + eval_report + demo_script 三件套齐全
- [ ] 简历 bullet 已写好
- [ ] 代码已 commit 到 git

**全部完成 = 阶段 2 毕业**，进入阶段 3 RAG 学习。

---

## 🆘 卡住了怎么办？

| 问题 | 解决 |
|---|---|
| 不会 Python | 回阶段 1，先把基础语法补完 |
| 不知道怎么写 tool card | 参考 [`docs/tool-card-template.md`](../docs/tool-card-template.md) |
| 模型返回格式乱 | 用 Pydantic schema 强制约束输出 |
| Agent 死循环 | 把 max_steps 调到 3 看 trace 卡在哪 |
| 不知怎么评分 | D5 用关键词匹配，D6 升级到 LLM-as-judge |
| 20 条 case 写不出 | 先列 10 个用户真实会问的问题，再补边界 |