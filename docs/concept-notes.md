# 🧠 Agent 核心概念笔记

> 来源：[AgentGuide/docs/01-theory/01-what-is-agent.md](https://github.com/adongwanai/AgentGuide)
> 建议先用 10 分钟读完，然后用自己的话在下方「我的理解」重写一遍。

---

## 一句话定义

> **AI Agent** 是一个软件系统：给定目标和约束后，**观察环境 → 决策 → 调用工具 → 接收反馈 → 继续推进任务**。
> LLM 负责推理和生成；Agent 系统把模型放进一个**可执行、可观察、可评估**的环境里。

---

## Agent vs Chatbot vs Workflow

| 类型 | 能力 | 行动？ | 例子 |
|---|---|---|---|
| **Chatbot** | 对话 + 问答 | ❌ | 客服 FAQ |
| **Workflow** | 固定步骤处理 | ✅ 但流程僵化 | 分类 → 检索 → 生成 |
| **Agent** | 模型根据状态选下一步 | ✅ 动态路径 | 研究助手、Web Agent |
| **Multi-Agent** | 多个 Agent 协作 | ✅ | planner + executor + reviewer |

⚠️ **Anthropic 的洞察**：很多任务用 workflow 就够了。**只有路径无法硬编码时才上 Agent**。

---

## Agent 最小闭环

```
目标 → 观察状态 → 思考/规划 → 用工具行动 → 观察结果 → 停止/继续/询问人
```

这就是 **ReAct**（Reasoning + Acting）的核心思想。

**生产实践**：不要把完整 Chain-of-Thought 暴露给用户。只记录可审计的 `reason_summary`、tool calls、observations、最终判断。

---

## Agent 八大组件（面试高频）

| # | 组件 | 功能 | 面试常见问题 |
|---|---|---|---|
| 1 | **Goal** | 任务 + 成功标准 | 如何判断任务完成？ |
| 2 | **Policy** | 系统约束、安全规则 | 哪些动作需要人确认？ |
| 3 | **State** | 当前进度、历史、临时产物 | 长任务如何恢复？ |
| 4 | **Memory** | 可复用经验 + 用户偏好 | 什么值得存？什么时候忘？ |
| 5 | **Context Builder** | 组装模型输入 | 如何避免上下文污染？ |
| 6 | **Tool Registry** | 声明可调用工具 | 如何设计 schema / 错误 / 权限？ |
| 7 | **Loop Controller** | 决定下一步 + 停止条件 | 如何防止无限循环？ |
| 8 | **Eval / Trace** | 记录 + 评估行为 | 如何证明 Agent 真的能跑？ |

---

## 五级能力模型

| Level | 名称 | 特征 | 例子 |
|---|---|---|---|
| L0 | Prompt App | 没工具，纯文本 | 简单摘要器 |
| L1 | Tool-Using App | 单轮工具调用 | "查天气再回答" |
| L2 | Workflow Agent | 多步但固定流程 | RAG pipeline |
| L3 | Autonomous Agent | 模型在有界步数内自选动作 | 研究 Agent |
| L4 | Long-running Agent | 持久状态、可恢复、人在回路 | Coding Agent、Web Agent |
| L5 | Multi-Agent System | 多角色协作 | 研究员 + 写手 + 审稿人 |

🎯 **求职 sweet spot**：L3-L4。零基础不要跳到 L5。

---

## 什么时候不该用 Agent？

- ✅ 任务流程固定 → 用 workflow 更稳定
- ❌ 没成功标准 + 没人复核
- ❌ 工具高风险 + 无权限、日志、回滚
- ❌ 一次性文本生成，不需要环境反馈
- ❌ 评估成本太高，无法证明改进

---

## 启动项目前的 7 个问题

1. 用户的真实目标是什么？
2. 为什么 workflow 不够？
3. 有什么工具？哪些是危险的？
4. 状态和产物存在哪里？
5. 最大步数 + 停止条件是什么？
6. 错误如何恢复？
7. 哪些 eval case 能证明它能跑？

---

## ✍️ 我的理解（用自己的话重写）

> 在你读完后，把上面 6 个关键点用自己的话重新解释一遍。不要复制粘贴。

**1. Agent 本质上是**：

**2. 跟 Chatbot 的根本区别**：

**3. ReAct 的核心思想**：

**4. 八大组件里我觉得最重要的是**：

**5. 我目前的等级目标**：

**6. 我能想到的"不该用 Agent"的场景**：

---

## 📌 概念检验

能用自己的话答出来，说明真的懂了：
- Q: 什么是 ReAct？
- Q: Workflow 和 Agent 的本质区别？
- Q: Context Builder 解决什么问题？
- Q: 为什么 Eval/Trace 是"第一公民"？

答不上来就回去再读一遍。