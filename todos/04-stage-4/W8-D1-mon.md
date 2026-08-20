# W9 D1 周一 · 2h — LangGraph 入门

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：用图替代手写循环

---

## 🎯 今日目标（3 项）

- [ ] 学 LangGraph 核心概念
- [ ] 用 LangGraph 重写最小 Agent
- [ ] 看到图可视化

---

## ✅ 任务清单（2h）

### 📖 阅读（50min）

- [ ] **[50min]** 看 [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/)：
  - **StateGraph**：状态机
  - **Node**：节点（一个函数）
  - **Edge**：边
  - **Conditional Edge**：条件转移
  - **State**：TypedDict + Reducer
  - **START / END**：特殊节点

### 💻 用 LangGraph 重写最小 Agent（60min）

- [ ] **[60min]** 在 `projects/03-langgraph-agent/` 下创建 `agent_v1.py`：

  ```python
  """用 LangGraph 重写 W4 最小 Agent"""
  from typing import TypedDict, Annotated
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langchain_core.messages import HumanMessage, ToolMessage
  from langchain_openai import ChatOpenAI
  from langchain_core.tools import tool
  import os
  from dotenv import load_dotenv
  
  load_dotenv()
  
  @tool
  def search_notes(query: str, limit: int = 3) -> str:
      """在个人笔记库搜索关键词"""
      return f"找到 3 条关于「{query}」的笔记"
  
  llm = ChatOpenAI(model="deepseek-chat", temperature=0).bind_tools([search_notes])
  
  class AgentState(TypedDict):
      messages: Annotated[list, add_messages]
  
  def call_model(state):
      response = llm.invoke(state["messages"])
      return {"messages": [response]}
  
  def call_tool(state):
      last = state["messages"][-1]
      results = []
      for tc in last.tool_calls:
          if tc["name"] == "search_notes":
              result = search_notes.invoke(tc["args"])
              results.append(ToolMessage(content=str(result, tool_call_id=tc["id"])))
      return {"messages": results}
  
  def should_continue(state):
      last = state["messages"][-1]
      if last.tool_calls:
          return "continue"
      return "end"
  
  graph = StateGraph(AgentState)
  graph.add_node("agent", call_model)
  graph.add_node("tools", call_tool)
  graph.add_edge(START, "agent")
  graph.add_conditional_edges("agent", should_continue, {"continue": "tools", "end": END})
  graph.add_edge("tools", "agent")
  app = graph.compile()
  
  if __name__ == "__main__":
      result = app.invoke({"messages": [HumanMessage(content="搜索 Python 异步笔记")]})
      for m in result["messages"]:
          print(f"[{type(m).__name__}] {m.content[:100]}")
  ```

  - 安装：`uv pip install langgraph langchain-openai`
  - 跑通

### 🎨 图可视化（10min）

- [ ] **[10min]** 加可视化代码：
  ```python
  png_data = app.get_graph().draw_mermaid_png()
  with open("agent_graph.png", "wb") as f:
      f.write(png_data)
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week8/day1-langgraph-intro.md`

---

## ✅ 当日验收

- [ ] LangGraph Agent 跑通
- [ ] 图可视化 PNG 生成

---

## 💡 明日预告

**W9 D2 周二**：State 管理