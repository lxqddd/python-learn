# W9 D4 周四 · 2h — Checkpoint 持久化

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：状态保存到磁盘

---

## 🎯 今日目标（3 项）

- [ ] 学 SqliteSaver
- [ ] 实现可恢复的 Agent
- [ ] 实现时间旅行

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [LangGraph Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)

### 💻 SqliteSaver（60min）

- [ ] **[60min]** 创建 `agent_persistent.py`：

  ```python
  """持久化 Agent"""
  from langgraph.checkpoint.sqlite import SqliteSaver
  import sqlite3
  
  DB_PATH = "projects/03-langgraph-agent/checkpoints.db"
  conn = sqlite3.connect(DB_PATH, check_same_thread=False)
  memory = SqliteSaver(conn)
  
  app = graph.compile(checkpointer=memory)
  
  config = {"configurable": {"thread_id": "alice-session-1"}}
  
  # 第一轮
  result = app.invoke(
      {"messages": [HumanMessage(content="我叫 Alice，今年 30 岁")]},
      config=config,
  )
  print(f"Turn1: {result['messages'][-1].content}")
  
  # 模拟"重启"
  app = graph.compile(checkpointer=memory)
  result = app.invoke(
      {"messages": [HumanMessage(content="我多大了？")]},
      config=config,
  )
  print(f"Turn2: {result['messages'][-1].content}")
  ```

  - 跑通
  - 验证重启后能恢复历史

### ⏰ 时间旅行（40min）

- [ ] **[40min]** 实现时间旅行：

  ```python
  history = app.get_state_history(config)
  for i, state in enumerate(history):
      print(f"Step {i}: next={state.next}")
  
  target_state = list(history)[2]
  result = app.invoke(
      None,
      config={**config, "configurable": {"thread_id": "alice-session-1", "checkpoint_id": target_state.config["configurable"]["checkpoint_id"]}},
  )
  ```

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week8/day4-checkpoint.md`

---

## ✅ 当日验收

- [ ] SqliteSaver 持久化生效
- [ ] "重启"后能恢复
- [ ] 时间旅行能回到第 N 步

---

## 💡 明日预告

**W9 D5 周五**：人在回路（HITL）