# W13 D4 周四 · 4h — 项目 2 · Reviewer + Supervisor

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：审稿 + 调度

---

## 🎯 今日目标（3 项）

- [ ] Reviewer Agent
- [ ] Supervisor 调度
- [ ] 完整流程跑通

---

## ✅ 任务清单（4h）

### 🤖 Reviewer Agent（90min）

- [ ] **[90min]** `backend/agents/reviewer.py`：

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import json, re

llm = ChatOpenAI(model="deepseek-chat")

def review_report(report):
    prompt = f"审阅以下报告，输出 JSON：\n{report}\n\n格式：{{'score': 1-10, 'issues': [], 'suggestions': [], 'approved': bool}}"
    response = llm.invoke([SystemMessage(content="你是严格审稿人"), HumanMessage(content=prompt)])
    
    content = response.content
    json_match = re.search(r"\{[\s\S]*\}", content)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass
    return {"score": 5, "issues": [], "suggestions": [], "approved": False}
```

### 🎯 Supervisor 调度（90min）

- [ ] **[90min]** `backend/supervisor.py`：

```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
import os

from agents.planner import plan_research
from agents.researcher import researcher
from agents.writer import generate_report
from agents.reviewer import review_report

class State(TypedDict):
    messages: Annotated[list, add_messages]
    topic: str
    sub_questions: list[str]
    findings: list[str]
    report: str
    review: dict

def planner_node(state):
    questions = plan_research(state["topic"])
    return {"sub_questions": questions}

def researcher_node(state):
    findings = []
    for q in state["sub_questions"]:
        result = researcher.invoke({"messages": [], "topic": q})
        findings.extend(result.get("findings", []))
    return {"findings": findings}

def writer_node(state):
    result = generate_report(state["topic"], state["findings"])
    return {"report": result["report"]}

def reviewer_node(state):
    review = review_report(state["report"])
    return {"review": review}

graph = StateGraph(State)
graph.add_node("researcher", researcher_node)
graph.add_node("writer", writer_node)
graph.add_node("reviewer", reviewer_node)

graph.add_edge(START, "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", "reviewer")
graph.add_edge("reviewer", END)

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

def run_research(topic):
    config = {"configurable": {"thread_id": topic}}
    result = app.invoke(
        {"messages": [HumanMessage(content=f"研究：{topic}")], "topic": topic, "sub_questions": [], "findings": [], "report": "", "review": {}},
        config=config,
    )
    return result
```

### 🧪 测试（60min）

- [ ] **[60min]** 完整流程测试

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week13/day4-supervisor.md`

---

## ✅ 当日验收

- [ ] Reviewer 评分跑通
- [ ] 完整多 Agent 流程跑通
- [ ] 报告 ≥ 1000 字 + 评分 ≥ 7

---

## 💡 明日预告

**W13 D5 周五 · 4h**：README + 30 eval + 视频 + tag