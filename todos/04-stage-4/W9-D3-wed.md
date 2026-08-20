# W9 D3 周三 · 2h — Conditional Edge

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：根据状态决定下一步

---

## 🎯 今日目标（3 项）

- [ ] 学路由函数（决定下一步）
- [ ] 学循环检测
- [ ] 实现"是否需要工具"分支

---

## ✅ 任务清单（2h）

### 💻 路由函数（60min）

- [ ] **[60min]** 创建 `agent_v3.py`：

  ```python
  """用 Conditional Edge 实现智能分支"""
  from typing import TypedDict, Annotated, Literal
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langchain_core.messages import HumanMessage, AIMessage
  from langchain_openai import ChatOpenAI
  from langchain_core.tools import tool
  
  class State(TypedDict):
      messages: Annotated[list, add_messages]
      step_count: int
  
  @tool =
  def search_notes(query: str) -> str:
      """搜索笔记库"""
      return f"找到 5 条关于「{query}」的笔记"
  
  @tool =
  def get_weather(city: str) -> str:
      """获取天气"""
      return f"{city} 25°C 晴"
  
  llm = ChatOpenAI(model="deepseek-chat", temperature=0).bind_tools([search_notes, get_weather])
  
  def agent_node(state: State):
      response = llm.invoke(state["messages"])
      return {"messages": [response], "step_count": state.get("step_count", 0) + 1}
  
  def tools_node(state: State):
      last = state["messages"][-1]
      results = []
      for tc in last.tool_calls:
          if tc["name"] == "search_notes":
              results.append(search_notes.invoke(tc["args"]))
          elif tc["name"] == "get_weather":
              results.append(get_weather.invoke(tc["args"]))
      return {"messages": results}
  
  def router(state: State) -> Literal["tools", "end"]:
      """决定下一步
      
      规则：
      - 如果模型想调 tool → tools
      - 如果 step_count > 5 → 强制结束
      - 否则 → 结束
      """
      last = state["messages"][-1]
      step_count = state.get("step_count", 0)
      
      if step_count > 5:
          print("⚠️ 步数过多，强制结束")
          return "end"
      
      if hasattr(last, "tool_calls") and last.tool_calls:
          return "tools"
      
      return "end"
  
  # 构建图
  graph = StateGraph(State)
  graph.add_node("agent", agent_node)
  graph.add_node("tools", tools_node)
  
  graph.add_edge(START, "agent")
  graph.add_conditional_edges("agent", router, {"tools": "tools", "end": END})
  graph.add_edge("tools", "agent")
  
  app = graph.compile()
  
  if __name__ == "__main__":
      # 测试 1：搜索任务（会调 tool）
      result = app.invoke({"messages": [HumanMessage(content="搜索 Python 异步")]})
      print(f"\n搜索任务步数：{result['step_count']}")
      
      # 测试 2：闲聊任务（不调 tool）
      result = app.invoke({"messages": [HumanMessage(content="你好")]})
      print(f"\n闲聊任务步数：{result['step_count']}")
  ```

  - 跑通两个测试
  - 看步数差异

### 🔁 循环检测（60min）

- [ ] **[60min]** 加重复动作检测：

  ```python
  def detect_repeat(state: State) -> bool:
      """检测是否重复调同一个 tool"""
      messages = state["messages"]
      if len(messages) < 4:
          return False
      
      # 检查最近 4 条消息的工具调用
      recent_calls = []
      for m in messages[-4:]:
          if hasattr(m, "tool_calls") and m.tool_calls:
              for tc in m.tool_calls:
                  recent_calls.append((tc["name"], str(tc["args"])))
      
      # 如果连续 2 次相同
      if len(recent_calls) >= 2 and recent_calls[-1] == recent_calls[-2]:
          return True
      return False
  
  def smart_router(state: State) -> Literal["tools", "end", "force_end"]:
      """智能路由：加重复检测"""
      if detect_repeat(state):
          print("⚠️ 检测到重复动作，强制结束")
          return "force_end"
      # ...（其他逻辑同 router）...
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week7/day3-conditional-edge.md`：
  - router 函数的设计模式
  - 循环检测的 trade-off
  - 死循环的实际危害

---

## 📚 关键概念

| 概念 | 说明 |
|---|---|
| **Conditional Edge** | 根据状态决定下一步 |
| **Router 函数** | 返回 Literal["node_a", "node_b"] |
| **循环检测** | 防止死循环 |
| **强制结束** | 超步数强制退出 |

---

## ✅ 当日验收

- [ ] router 路由正确
- [ ] 重复动作能被检测
- [ ] step_count 限制生效

---

## 💡 明日预告

**W9 D4 周四**：Checkpoint 持久化（SqliteSaver）