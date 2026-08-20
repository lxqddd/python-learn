# 🚀 Agent 开发学习工作台

> **零基础 → 14 周 → Agent 求职就绪**
> 学习方法论：**做出什么 > 学过什么**（源自 [AgentGuide](https://github.com/adongwanai/AgentGuide)）

---

## 📂 目录结构

```
python/
├── README.md                   ← 你在这里（进度追踪）
├── resources.md                 所有学习资源索引
├── docs/                        核心方法论文档
│   ├── learning-roadmap.md          ⭐⭐⭐ 15 周定制学习路线（**先看这个**）
│   ├── first-7-days-checklist.md    ⭐ Day 1-7 详细任务清单
│   ├── concept-notes.md             Agent 概念笔记
│   └── tool-card-template.md        工具卡模板
├── notes/                       你的学习笔记
├── sandbox/                     Python 基础练习场（阶段 1）
└── projects/                    项目实战
    ├── 01-minimal-agent/        ⭐ First 7 Days Sprint 最小 Agent
    ├── 02-rag-system/           第 6-7 周：RAG 完整链路
    ├── 03-langgraph-agent/      第 8-9 周：LangGraph 框架
    └── 04-portfolio/            第 12-13 周：简历级项目
```

---

## 🎯 学习阶段总览

| 阶段 | 周次 | 主题 | 状态 |
|---|---|---|---|
| **0** 定方向 | 第 1 周 | 概念 + 环境（不写代码） | ⬜ |
| **1** 🐍 **Python 强化** | 第 2-4 周 | 基础 + LeetCode + Pythonic + LangChain 源码 | ⬜ |
| **2** 🚀 First 7 Days | 第 5 周 | 手写最小 Agent + 20 eval cases | ⬜ |
| **3** RAG 基础 | 第 6-7 周 | FastAPI + LangChain + Chroma | ⬜ |
| **4** Agent 框架 | 第 8-9 周 | LangGraph 重点 + Tool Calling | ⬜ |
| **5** 多 Agent + MCP | 第 10-11 周 | AutoGen / CrewAI + MCP 协议 | ⬜ |
| **6** 项目实战 | 第 12-13 周 | 2 个简历级项目 | ⬜ |
| **7** 求职冲刺 | 第 14-15 周 | 简历 + 模拟面试 | ⬜ |

> **总时长**：15 周（原 14 周 · 增加 1 周 Python 强化）
> **变化**：阶段 1 从 W2-3 扩到 W2-4，新增 LeetCode + Pythonic 训练 + LangChain 源码阅读

> **每日行动**：打开 [`TODO.md`](TODO.md) 找到今天的 checkbox，完成后把 `[ ]` 改成 `[x]`。

---

## 📅 今日起步（Week 1 · Day 1-2）

- [ ] 阅读 [`docs/concept-notes.md`](docs/concept-notes.md) — 理解 Agent 是什么
- [ ] 阅读 [`docs/first-7-days-checklist.md`](docs/first-7-days-checklist.md) — 7 天冲刺全貌
- [ ] 安装环境：Python 3.11+、`uv`、VS Code、Git、Ollama
- [ ] 注册一个 LLM API（DeepSeek 起步最便宜）
- [ ] **不要装 LangChain / LangGraph**——先理解概念

---

## 🎓 核心原则（来自 AgentGuide）

1. **做出什么 > 学过什么** — 每个模块必须有可演示的产物
2. **从工作流开始，再加 Agent loop** — 不要一上来就 LLM 自主决策
3. **Trace + Eval 是 Agent 的第一公民** — 没评估 = 没产出
4. **最小闭环优先** — 能跑 200 行代码的 Agent > 看 10 篇框架文档

---

## 🔗 快速跳转

- ✅ **每日 Todo List**（勾选式进度追踪）→ [`TODO.md`](TODO.md) ⭐⭐⭐ **每天打开这个**
- 📋 **14 周定制学习路线**（每天任务、验收标准）→ [`docs/learning-roadmap.md`](docs/learning-roadmap.md)
- 📖 全部学习资源 → [`resources.md`](resources.md)
- 🚀 7 天冲刺任务清单 → [`docs/first-7-days-checklist.md`](docs/first-7-days-checklist.md)
- 🛠 第一个项目代码 → [`projects/01-minimal-agent/`](projects/01-minimal-agent/)
- 🐍 Python 练习场 → [`sandbox/`](sandbox/)