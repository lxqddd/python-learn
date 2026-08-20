# W9 D1 周一 · 2h — LangGraph 入门

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：用图替代手写循环

---

## 🎯 今日目标（3 项）

- [ ] 学 LangGraph 核心概念
- [ ] 用 LangGraph 重写 W4 最小 Agent
- [ ] 看到图可视化

---

## ✅ 任务清单（2h）

### 📖 阅读（50min）

- [ ] **[50min]** 看 [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/)：
  - **StateGraph**：状态机
  - **Node**：节点（一个函数）
  - **Edge**：边（节点之间的转移）
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
  from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
  from langchain_openai import ChatOpenAI
  from langchain_core.tools import tool
  import os
  from dotenv import load_dotenv
  
  load_dotenv()
  
  # === Tool 定义 ===
  @tool
  def search_notes(query: str, limit: int = 3) -> str:
      """在个人笔记库搜索关键词"""
      # 这里用假数据（生产接真实向量库）
      return f"找到 3 条关于「{query}」的笔记"
  
  llm = ChatOpenAI(
      model="deepseek-chat",
      openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
      openai_api_base=os.getenv("DEEPSEEK_BASE_URL"),
      temperature=0,
, ).bind_tools([search_notes])
  
  # === State 定义 ===
  class AgentState(TypedDict):
      messages: Annotated[list, add_messages]
  
  # === Node 定义 ===
  def call_model(state: AgentState):
      """调 LLM 决策下一步"""
      response = llm.invoke(state["messages"])
      return {"messages": [response]}
  
  def call_tool(state: AgentState):
      """执行 tool 调用"""
      last_message = state["messages"][-1]
      tool_calls = last_message.tool_calls
      
      results = []
      for tc in tool_calls:
          if tc["name"] == "search_notes":
              result = search_notes.invoke(tc["args"])
              results.append(ToolMessage(content=str(result), tool_call_id=tc["id"]))
      return {"messages": results}
  
  def should_continue(state: AgentState):
      """决定下一步：继续调 tool 还是结束"""
      last_message = state["messages"][-1]
      if last_message.tool_calls:
          return "continue"  # 还有 tool 要调
      return "end"  # 结束
  
  # === 构建图 ===
  graph = StateGraph(AgentState)
  
  graph.add_node("agent", call_model)
  graph.add_node("tools", call_tool)
  
  graph.add_edge(START, "agent")
  graph.add_conditional_edges(
      "agent",
      should_continue,
      {"continue": "tools", "end": END},
, )
  graph.add_edge("tools", "agent")
  
  app = graph.compile()
  
  # === 运行 ===
  if __name__ == "__main__":
      result = app.invoke({
          "messages": [HumanMessage(content="搜索 Python 异步笔记")]
      })
      print("\n=== 最终结果 ===")
      for m in result["messages"]:
          print(f"[{type(m).__name__}] {m.content[:100]}")
  ```

  - 安装：`uv pip install langgraph langchain-openai`
  - 跑通
  - 看是不是 2 步：agent（调 tool） → tools（执行）→ agent（最终回答）

### 🎨 图可视化（10min）

- [ ] **[10min]** 加可视化代码：

  ```python
  from langgraph.graph import StateGraph
  
  # 画图
  png_data = app.get_graph().draw_mermaid_png()
  with open("agent_graph.png", "wb") as f:
      f.write(png_data)
  print("图已保存到 agent_graph.png")
  ```

  - 看生成的图，应该看到 `agent → tools → agent → END` 的循环

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week7/day1-langgraph-intro.md`：
  - StateGraph vs 手写循环的对比
  - Node / Edge 概念
  - 图可视化有什么帮助

---

## 📚 关键概念

| 概念 | 解释 |
|---|---|
| **StateGraph** | 有向图，每个节点是一个函数 |
| **State** | TypedDict + Reducer（控制状态如何合并） |
| **add_messages** | 消息累加，不覆盖 |
| **Conditional Edge** | 根据状态决定下一个节点 |
| **START / END** | 特殊节点，图的入口和出口 |

**为什么用 LangGraph？**
- 可视化：流程图清楚
- 持久化：checkpoint 自动保存
- 人在回路：内置 interrupt
- 可恢复：thread_id 找回历史

---

## ✅ 当日验收

- [ ] LangGraph Agent 跑通
- [ ] 图可视化 PNG 生成
- [ ] 能解释 StateGraph / Node / Edge 概念

---

## 💡 明日预告

**W9 D2 周二**：State 管理（Reducer / 消息历史）