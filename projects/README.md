# 🛠 Projects · 项目索引

每个项目独立目录，**完成一个再开下一个**。

| # | 项目 | 阶段 | 状态 |
|---|---|---|---|
| **01** | [minimal-agent](./01-minimal-agent/) | 🚀 First 7 Days Sprint（**最先做**） | ⬜ |
| **02** | [rag-system](./02-rag-system/) | 第 5-6 周：RAG 完整链路 | ⬜ |
| **03** | [langgraph-agent](./03-langgraph-agent/) | 第 7-8 周：LangGraph 框架 | ⬜ |
| **04** | [portfolio](./04-portfolio/) | 第 11-12 周：2 个简历级项目 | ⬜ |

---

## 项目完成度 Checklist（AgentGuide 标准）

每个项目做完前必须自检：

- [ ] 明确目标用户与场景
- [ ] 工具列表 + 权限分层 + 错误处理
- [ ] **Trace 可重放**（LangSmith 或自建 JSONL）
- [ ] **20+ 条 Eval case**（10 正常 + 5 边界 + 5 安全）
- [ ] README clone-and-run
- [ ] 简历 bullet 量化：成功率 % / 延迟 ms / 成本下降 %