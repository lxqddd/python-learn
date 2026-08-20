# W9 周日验收

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：W9 LangGraph 入门验收

---

## ✅ 知识验收（10min）

- [ ] **StateGraph** 是什么？跟手写循环比有什么优势？
- [ ] **Node** 和 **Edge** 概念？
- [ ] **Conditional Edge** 怎么用？
- [ ] **Reducer**（如 `add_messages`）的作用？
- [ ] **Checkpoint** 的价值？哪些 Saver 可用？
- [ ] **HITL** 怎么实现？什么场景用？

---

## ✅ 实践验收（15min）

- [ ] `agent_v1.py`（StateGraph 入门）跑通
- [ ] `agent_v2.py`（多轮对话）跑通，第二轮能记住第一轮
- [ ] `agent_v3.py`（Conditional Edge）跑通
- [ ] `agent_persistent.py`（SqliteSaver）跑通，重启后能恢复
- [ ] `agent_hitl.py` 跑通，写文件前暂停
- [ ] 图可视化 PNG 都生成

---

## ✅ 关键能力验证

- [ ] 能用 LangGraph 重写任意 ReAct 循环
- [ ] 理解 State / Node / Edge / Conditional Edge
- [ ] 知道 Checkpoint 和 thread_id 的用法
- [ ] 能实现高风险工具的 HITL

---

## 📊 本周统计

```
W9 完成度:    [░░░░░░░░░░] /19
总投入:       __h
产出:        5 个 LangGraph Agent 版本
```

---

## 💡 下周预览

**W9 LangGraph 深入**：
- D1：Tool Calling 深入 + 真实检索
- D2：Pydantic AI（类型化 Agent）
- D3：LangSmith 接入
- D4：多框架对比（AutoGen / CrewAI）
- D5：写对比博客

明天打开 [`W9-D1-mon.md`](W9-D1-mon.md)。