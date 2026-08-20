# W9 D2 周二 · 2h — State 管理

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：Reducer / 消息历史 / 状态调试

---

## 🎯 今日目标（3 项）

- [ ] 学 Reducer 函数（add_messages）
- [ ] 学状态更新模式（覆盖 vs 累加）
- [ ] 在图里加对话历史节点

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 看 [LangGraph State 文档](https://langchain-ai.github.io/langgraph/concepts/low_level/)：
  - **Reducer**：控制状态如何合并
  - 默认行为：新值覆盖旧值
  - `add_messages`：消息追加
  - 自定义 Reducer：`Annotated[list, custom_reducer]`

### 💻 实战：加对话历史（80min）

- [ ] **[80min]** 创建 `agent_v2.py`（在昨日基础上）：

  ```python
  """带对话历史的 Agent"""
  from typing import TypedDict, Annotated
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langchain_core.messages import HumanMessage, AIMessage
  from langgraph.checkpoint.memory import MemorySaver
  
  class AgentState(TypedDict):
      messages: Annotated[list, add_messages]  # 自动累加
      user_id: str                              # 普通字段（覆盖）
      step_count: Annotated[int, lambda x, y: x + y]  # 自定义：累加
  
  # ...（接昨天的 call_model 和 call_tool）...
  
  # === 加 checkpoint ===
  memory = MemorySaver()
  app = graph.compile(checkpoint=memory)
  
  # === 多轮对话 ===
  if __name__ == "__main__":
      config = {"configurable": {"thread_id": "user-1"}}
      
      # 第一轮
      result = app.invoke(
          {"messages": [HumanMessage(content="我叫 Alice")]},
          config=config,
, )
      print(f"Turn 1: {result['messages'][-1].content}")
      
      # 第二轮（继续同一 thread_id）
      result = app.invoke(
          {"messages": [HumanMessage(content="我叫什么名字？")]},
          config=config,
, )
      print(f"Turn 2: {result['messages'][-1].content}")  # 应该回答"Alice"
      
      # 查看历史
      state_history = app.get_state(config)
      print(f"\n总消息数：{len(state_history.values['messages'])}")
  ```

  - 跑通
  - 验证第二轮能记住"我叫 Alice"

### 💻 状态调试（30min）

- [ ] **[30min]** 加 print_state 调试：

  ```python
  # 在每个 Node 后打印
  def debug_node(state):
      print(f"\n[DEBUG] 当前状态：")
      for k, v in state.items():
          if k == "messages":
              print(f"  messages: {len(v)} 条")
          else:
              print(f"  {k}: {v}")
      return state
  
  # 接入图
  graph.add_node("debug", debug_node)
  graph.add_edge("agent", "debug")
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week7/day2-state.md`：
  - Reducer 的本质
  - 覆盖 vs 累加的选择
  - 怎么调试状态

---

## 📚 关键概念

| 概念 | 说明 |
|---|---|
| **TypedDict** | 类型化的字典 |
| **Annotated[list, add_messages]** | 标记用 add_messages Reducer |
| **MemorySaver** | 内存版 checkpoint |
| **thread_id** | 对话会话标识 |
| **覆盖 vs 累加** | 默认覆盖，需要 Reducer 才累加 |

---

## ✅ 当日验收

- [ ] 多轮对话能记住上下文
- [ ] 第二轮问"我叫什么"能答对
- [ ] 能解释 Reducer 作用
- [ ] 状态调试能看到每步状态

---

## 💡 明日预告

**W9 D3 周三**：Conditional Edge（条件分支）