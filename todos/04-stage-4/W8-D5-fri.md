# W9 D5 周五 · 2h — 人在回路（HITL）

- **阶段**：4 Agent 框架 | **周次**：W9 | **状态**：⬜
- **主题**：高风险动作前暂停确认

---

## 🎯 今日目标（3 项）

- [ ] 学 `interrupt_before`
- [ ] 实现写操作前的用户确认
- [ ] 看完整图可视化

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [LangGraph HITL](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/)

### 💻 实现 HITL（60min）

- [ ] **[60min]** 创建 `agent_hitl.py`：

  ```python
  """人在回路 Agent：写文件前必须确认"""
  from typing import TypedDict, Annotated
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langgraph.checkpoint.memory import MemorySaver
  from langchain_core.messages import HumanMessage
  from langchain_core.tools import tool
  import os
  
  @tool
  def write_summary(text: str, filename: str = "summary.md") -> str:
      """⚠️ 高风险：写文件到磁盘。"""
      out_path = f"output/{filename}"
      os.makedirs("output", exist_ok=True)
      with open(out_path, "w", encoding="utf-8") as f:
          f.write(text)
      return f"已写入 {out_path}"
  
  # State + LLM 配置（同前，略）
  
  graph = StateGraph(State)
  graph.add_node("agent", agent_node)
  graph.add_node("tools", tools_node)
  graph.add_node("confirm_write", confirm_write_node)
  
  graph.add_edge(START, "agent")
  graph.add_conditional_edges("agent", router, {"tools": "tools", "end": END})
  graph.add_edge("tools", "confirm_write")
  graph.add_edge("confirm_write", "agent")
  
  app = graph.compile(
      checkpointer=MemorySaver(),
      interrupt_before=["confirm_write"],
  )
  
  if __name__ == "__main__":
      config = {"configurable": {"thread_id": "hitl-demo"}}
      result = app.invoke(
          {"messages": [HumanMessage(content="写一篇关于 Python 异步的总结到 summary.md")]},
          config=config,
      )
      print(f"\n⚠️ Agent 暂停，等待写文件确认...")
      user_input = input("\n是否允许写文件？(y/n): ").strip().lower()
      if user_input == "y":
          result = app.invoke(None, config=config)
          print(f"\n✅ 继续执行，最终：{result['messages'][-1].content}")
      else:
        print("❌ 用户拒绝，任务终止")
  ```

  - 跑通
  - 验证：执行到写文件前会暂停

### 🎨 完整图可视化（20min）

- [ ] **[20min]** 画完整的 HITL 图：

  ```python
  png = app.get_graph().draw_mermaid_png()
  with open("hitl_graph.png", "wb") as f:
      f.write(png)
  ```

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week8/day5-hitl.md`

---

## ✅ 当日验收

- [ ] HITL Agent 跑通，写文件前暂停
- [ ] 输入 `y` 后继续
- [ ] 图可视化包含 confirm_write 节点

---

## 📊 进度

```
W9 D5:    [░░░░░░░░░░] 0/3
W9 整体:  [░░░░░░░░░░] 0/19
阶段 4:   [░░░░░░░░░░] 0/33
```

---

## 💡 周末预告

**W9 周日**：打开 [`W9-review.md`](W9-review.md) 做验收