# W9 D4 周四 · 2h — Checkpoint 持久化

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：状态保存到磁盘

---

## 🎯 今日目标（3 项）

- [ ] 学 SqliteSaver / PostgresSaver
- [ ] 实现可恢复的 Agent
- [ ] 实现时间旅行（回到任意步骤）

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [LangGraph Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)：
  - Checkpointer 接口
  - `MemorySaver`：内存（重启丢）
  - `SqliteSaver`：磁盘
  - `PostgresSaver`：生产环境
  - `thread_id`：对话标识
  - Time travel：回到任意步骤

### 💻 SqliteSaver（60min）

- [ ] **[60min]** 创建 `agent_persistent.py`：

  ```python
  """持久化 Agent"""
  from langgraph.checkpoint.sqlite import SqliteSaver
  from langgraph.graph import StateGraph, START, END
  # ...（接昨天的 agent 定义）...
  
  # 1. 用 SqliteSaver
  DB_PATH = "projects/03-langgraph-agent/checkpoints.db"
  conn = sqlite3.connect(DB_PATH, check_same_thread=False)
  memory = SqliteSaver(conn)
  
  app = graph.compile(checkpointer=memory)
  
  # 2. 多轮对话（重启后能恢复）
  config = {"configurable": {"thread_id": "alice-session-1"}}
  
  # 第一轮
  result = app.invoke(
      {"messages": [HumanMessage(content="我叫 Alice，今年 30 岁")]},
      config=config,
, )
  print(f"Turn 1: {result['messages'][-1].content}")
  
  # 模拟"重启"——重新创建 app
  app = graph.compile(checkpointer=memory)
  result = app.invoke(
      {"messages": [HumanMessage(content="我多大了？")]},
      config=config,
, )
  print(f"Turn 2 (after restart): {result['messages'][-1].content}")  # 应回答"30"
  ```

  - 跑通
  - 验证重启后能恢复历史

### ⏰ 时间旅行（40min）

- [ ] **[40min]** 实现时间旅行：

  ```python
  # 查看历史 steps
  history = app.get_state_history(config)
  for i, state in enumerate(history):
      print(f"\nStep {i}:")
      print(f"  Next: {state.next}")
      print(f"  Messages: {len(state.values['messages'])}")
  
  # 回到第 2 步
  target_state = list(history)[2]
  
  # 从那个状态重新跑
  result = app.invoke(
      None,  # 从状态继续
      config={
          **config,
          "configurable": {"thread_id": "alice-session-1", "checkpoint_id": target_state.config["configurable"]["checkpoint_id"]},
      },
, )
  ```

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week7/day4-checkpoint.md`：
  - 持久化的价值（崩溃恢复、长任务）
  - thread_id 的设计
  - 时间旅行的实际用途（debug、用户回退）

---

## 📚 关键概念

| 概念 | 用途 |
|---|---|
| **Checkpointer** | 状态快照 |
| **SqliteSaver** | 本地持久化 |
| **thread_id** | 会话 ID |
| **checkpoint_id** | 单次步骤 ID |
| **Time travel** | 回到过去步骤 |

---

## ✅ 当日验收

- [ ] SqliteSaver 持久化生效
- [ ] "重启"后能恢复
- [ ] 时间旅行能回到第 N 步

---

## 💡 明日预告

**W9 D5 周五**：人在回路（HITL）