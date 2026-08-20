# 🕸 Project 03 · LangGraph Agent（第 7-8 周）

> 在 RAG 项目完成后开始。重点学 LangGraph。

---

## 🎯 目标

把 Project 01 的最小 Agent 用 **LangGraph 重写**：
- 用 StateGraph 替代手写循环
- 加入 checkpoint、人在回路、可视化
- 接入持久化存储（SQLite / Postgres）

---

## 🗂 待办结构

```
03-langgraph-agent/
├── README.md
├── requirements.txt       ← langgraph, langchain-core
├── graph.py               ← StateGraph 定义
├── state.py               ← TypedDict state schema
├── nodes/                 ← 每个节点是一个函数
│   ├── decide.py
│   ├── search.py
│   ├── summarize.py
│   └── human_review.py
├── tools/                 ← 复用 01 的 tools.py
├── eval/                  ← LangSmith 接入
└── frontend/              ← Streamlit / Gradio UI
```

---

## 📅 第 7 周任务

- [ ] 阅读 [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/)
- [ ] Day 1：用 LangGraph 重写 Project 01 的最小 Agent
- [ ] Day 2：加状态 schema（TypedDict + Annotated）
- [ ] Day 3：加入 Conditional Edge（决定下一步节点）
- [ ] Day 4：加 Checkpoint（SqliteSaver）
- [ ] Day 5：加人在回路（interrupt_before）
- [ ] Day 6：可视化（draw_mermaid_png）
- [ ] Day 7：跑通 20 条 eval case

---

## 📅 第 8 周任务

- [ ] 接入 LangSmith 做 trace 监控
- [ ] 加持久化（Postgres）
- [ ] 多 Agent：用 LangGraph 的子图
- [ ] 接 MCP 协议（用 LangGraph 节点调 MCP server）
- [ ] 部署到 Railway / Fly.io
- [ ] 写技术博客

---

## 📚 推荐资源

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [LangGraph 教程合集](https://github.com/langchain-ai/langgraph/tree/main/examples)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [LangSmith](https://www.langchain.com/langsmith)

---

## 🎯 完成标准

- [ ] LangGraph 图可视化清晰
- [ ] State 管理明确（TypedDict）
- [ ] 支持 checkpoint 恢复
- [ ] 人在回路能中断 + 恢复
- [ ] LangSmith 上能看到每一步
- [ ] README 有架构图 + 流程图
- [ ] 简历 bullet：
  > 基于 LangGraph 构建生产级 Agent 系统，采用 StateGraph + Checkpoint + Human-in-Loop 设计，支持任务暂停恢复与可视化追踪；接入 LangSmith 实现全链路 trace，调试效率提升 60%。