# W9 D2 周二 · 2h — State 管理

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：Reducer / 消息历史

---

## 🎯 今日目标（3 项）

- [ ] 学 Reducer 函数
- [ ] 学状态更新模式
- [ ] 在图里加对话历史

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 看 [LangGraph State 文档](https://langchain-ai.github.io/langgraph/concepts/low_level/)

### 💻 实战（80min）

- [ ] **[80min]** 创建 `agent_v2.py`：

  ```python
  """带对话历史的 Agent"""
  from typing import TypedDict, Annotated
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langgraph.checkpoint.memory import MemorySaver
  
  class AgentState(TypedDict):
      messages: Annotated[list, add_messages]
  
  # ...（接昨天的 call_model 和 call_tool）...
  
  memory = MemorySaver()
  app = graph.compile(checkpointer=memory)
  
  if __name__ == "__main__":
      config = {"configurable": {"thread_id": "user-1"}}
      result = app.invoke({"messages": [HumanMessage(content="我叫 Alice")]}, config=config)
      result = app.invoke({"messages": [HumanMessage(content="我叫什么？")]}, config=config)
      print(result["messages"][-1].content)
  ```

### 💻 状态调试（30min）

- [ ] **[30min]** 加 print_state 调试

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week8/day2-state.md`

---

## ✅ 当日验收

- [ ] 多轮对话能记住上下文
- [ ] 第二轮能正确回答"我叫什么"

---

## 💡 明日预告

**W9 D3 周三**：Conditional Edge