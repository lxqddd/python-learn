# W11 D3 周三 · 2h — LangGraph 多 Agent（Supervisor）

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：用 Supervisor 协调多个 Worker Agent

---

## 🎯 今日目标（3 项）

- [ ] 学 Supervisor 模式
- [ ] 实现 planner → executor → reviewer
- [ ] 学会 Agent handoff

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [LangGraph Multi-Agent](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)

### 💻 Supervisor + Worker（90min）

- [ ] **[90min]** 创建 `langgraph_supervisor.py`：

  ```python
  """LangGraph Supervisor 模式"""
  from typing import TypedDict, Annotated, Literal
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
  from langchain_openai import ChatOpenAI
  import os
  from dotenv import load_dotenv
  
  load_dotenv()
  
  llm = ChatOpenAI(model="deepseek-chat", temperature=0)
  
  class State(TypedDict):
      messages: Annotated[list, add_messages]
      next_agent: str
  
  def planner_node(state):
      prompt = f"基于用户需求拆分成 3 步研究计划。需求：{state['messages'][0].content}"
      response = llm.invoke([SystemMessage(content="你是规划师"), HumanMessage(content=prompt)])
      return {"messages": [response]}
  
  def executor_node(state):
      plan = state["messages"][-1].content
      prompt = f"执行计划：{plan}\n输出执行结果。"
      response = llm.invoke([SystemMessage(content="你是执行者"), HumanMessage(content=prompt)])
      return {"messages": [response]}
  
  def reviewer_node(state):
      result = state["messages"][-1].content
      prompt = f"审稿以下内容，给出 3 条改进建议或说'通过'：\n{result}"
      response = llm.invoke([SystemMessage(content="你是审稿人"), HumanMessage(content=prompt)])
      return {"messages": [response]}
  
  def supervisor_node(state) -> Literal["planner", "executor", "reviewer", "end"]:
      messages = state["messages"]
      step_count = len([m for m in messages if isinstance(m, AIMessage)])
      
      if step_count == 0:
          return "planner"
      elif step_count == 1:
          return "executor"
      elif step_count == 2:
          last = messages[-1].content
          if "通过" in last or step_count >= 3:
              return "end"
          return "executor"
      elif step_count == 3:
          return "reviewer"
      else:
          return "end"
  
  graph = StateGraph(State)
  graph.add_node("supervisor", lambda s: s)
  graph.add_node("planner", planner_node)
  graph.add_node("executor", executor_node)
  graph.add_node("reviewer", reviewer_node)
  
  graph.add_edge(START, "supervisor")
  graph.add_conditional_edges("supervisor", supervisor_node, {
      "planner": "planner", "executor": "executor", "reviewer": "reviewer", "end": END
  })
  
  for worker in ["planner", "executor", "reviewer"]:
      graph.add_edge(worker, "supervisor")
  
  app = graph.compile()
  
  if __name__ == "__main__":
      result = app.invoke({
          "messages": [HumanMessage(content="调研 Python asyncio 并生成报告")],
          "next_agent": "supervisor",
      })
      print(f"\n=== 最终结果（{len(result['messages'])} 步）===")
      for m in result["messages"]:
          if isinstance(m, AIMessage):
              print(f"\n{m.content[:200]}...")
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week10/day3-supervisor.md`

---

## ✅ 当日验收

- [ ] Supervisor 协调 3 个 worker 跑通

---

## 💡 明日预告

**W11 D4 周四**：MCP 协议入门