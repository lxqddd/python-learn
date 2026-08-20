# W13 D3 周三 · 4h — 项目 2 · 阅读 + 总结

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：Writer Agent 生成报告

---

## 🎯 今日目标（3 项）

- [ ] 实现 Planner Agent
- [ ] 实现 Writer Agent
- [ ] 跑通"研究 → 报告"流程

---

## ✅ 任务清单（4h）

### 🤖 Planner Agent（60min）

- [ ] **[60min]** `backend/agents/planner.py`：

  ```python
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import SystemMessage, HumanMessage
  
  llm = ChatOpenAI(model="deepseek-chat")
  
  def plan_research(topic):
      prompt = f"将以下主题拆解为 3-5 个子问题：\n主题：{topic}\n输出格式（每行一个）：\n1. ...\n2. ..."
      response = llm.invoke([SystemMessage(content="你是研究规划师"), HumanMessage(content=prompt)])
      
      questions = []
      for line in response.content.split("\n"):
          line = line.strip()
          if line and (line[0].isdigit() or line.startswith("-")):
              q = line.split(".", 1)[-1].strip() if "." in line else line
              questions.append(q)
      return questions[:5]
  ```

### 🤖 Writer Agent（120min）

- [ ] **[120min]** `backend/agents/writer.py`：

  ```python
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import SystemMessage, HumanMessage
  from langchain_core.tools import tool
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langgraph.checkpoint.memory import MemorySaver
  from typing import TypedDict, Annotated
  import os
  from datetime import datetime
  
  llm = ChatOpenAI(model="deepseek-chat")
  
  REPORT_PROMPT = """你是技术作家。基于以下研究资料，撰写 ≥ 1000 字研究报告。
  
  ## 要求
  - 结构清晰（概述/主体/总结）
  - 引用具体来源（用 [1] [2]）
  - 客观中立
  
  ## 资料
  {findings}
  
  ## 主题
  {topic}
  """
  
  @tool
  def save_report(content: str, filename: str = "report.md") -> str:
      """保存报告到文件（触发 HITL）"""
      print(f"\n⚠️ [HITL] 准备写 {filename}")
      confirm = input("是否允许？(y/n): ").strip().lower()
      if confirm != "y":
          return "❌ 用户拒绝"
      from pathlib import Path
      out_dir = Path("output")
      out_dir.mkdir(exist_ok=True)
      (out_dir / filename).write_text(content, encoding="utf-8")
      return f"✅ 已保存"
  
  writer_llm = llm.bind_tools([save_report])
  
  class WriterState(TypedDict):
      messages: Annotated[list, add_messages]
      topic: str
      findings: list[str]
      report: str
  
  def write_node(state):
      findings_text = "\n\n---\n\n".join(state["findings"])
      prompt = REPORT_PROMPT.format(findings=findings_text, topic=state["topic"])
      response = writer_llm.invoke([SystemMessage(content=prompt), HumanMessage(content="请开始撰写")])
      return {"messages": [response]}
  
  def tool_node(state):
      last = state["messages"][-1]
      results = []
      for tc in last.tool_calls:
          if tc["name"] == "save_report":
              results.append({"role": "tool", "content": save_report.invoke(tc["args"]), "tool_call_id": tc["id"]})
      return {"messages": results}
  
  def router(state):
      last = state["messages"][-1]
      if hasattr(last, "tool_calls") and last.tool_calls:
          return "tools"
      return "end"
  
  graph = StateGraph(WriterState)
  graph.add_node("write", write_node)
  graph.add_node("tools", tool_node)
  graph.add_edge(START, "write")
  graph.add_conditional_edges("write", router, {"tools": "tools", "end": END})
  graph.add_edge("tools", END)
  
  memory = MemorySaver()
  writer = graph.compile(checkpointer=memory)
  
  def generate_report(topic, findings):
      filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
      config = {"configurable": {"thread_id": topic}}
      result = writer.invoke({"messages": [], "topic": topic, "findings": findings}, config=config)
      report = ""
      for m in result["messages"]:
          if hasattr(m, "content") and len(m.content) > 500:
              report = m.content
      return {"report": report}
  ```

### 🧪 端到端测试（60min）

- [ ] **[60min]** 写 `backend/main.py`，跑通"研究→报告"

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week13/day3-writer.md`

---

## ✅ 当日验收

- [ ] Planner 拆任务跑通
- [ ] Writer 生成 ≥ 1000 字
- [ ] 端到端流程跑通

---

## 💡 明日预告

**W13 D4 周四 · 4h**：Reviewer + Supervisor