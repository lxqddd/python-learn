# W11 D2 周二 · 2h — CrewAI 多 Agent

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：角色驱动的多 Agent

---

## 🎯 今日目标（3 项）

- [ ] 学 CrewAI 角色 + 任务
- [ ] 实现顺序执行的 Crew
- [ ] 对比 AutoGen

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [CrewAI Quickstart](https://docs.crewai.com/quickstart)

### 💻 顺序执行 Crew（90min）

- [ ] **[90min]** 创建 `crewai_team.py`：

  ```python
  """CrewAI：研究报告小组"""
  from crewai import Agent, Task, Crew, Process
  from langchain_openai import ChatOpenAI
  import os
  from dotenv import load_dotenv
  
  load_dotenv()
  
  llm = ChatOpenAI(
      model="deepseek-chat",
      openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
      openai_api_base="https://api.deepseek.com/v1",
  )
  
  researcher = Agent(
      role="高级研究员",
      goal="找到关于 Python asyncio 的最关键 3 个核心机制",
      backstory="你是 10 年经验的 Python 专家",
      llm=llm,
      verbose=True,
  )
  
  writer = Agent(
      role="技术作家",
      goal="根据研究结果写一份清晰、专业的 500 字报告",
      backstory="你擅长把复杂技术讲清楚",
      llm=llm,
      verbose=True,
  )
  
  reviewer = Agent(
      role="首席审稿人",
      goal="找出报告中的错误、补充缺失、提供改进建议",
      backstory="你是 MIT 博士",
      llm=llm,
      verbose=True,
  )
  
  research_task = Task(
      description="研究 Python asyncio 的 3 个最核心机制",
      agent=researcher,
  )
  write_task = Task(
      description="基于研究结果，写一份 500 字 Markdown 报告",
      agent=writer,
      context=[research_task],
  )
  review_task = Task(
      description="审稿并提供 3 条具体改进建议。如果报告合格，回复'通过'。",
      agent=reviewer,
      context=[write_task],
  )
  
  crew = Crew(
      agents=[researcher, writer, reviewer],
      tasks=[research_task, write_task, review_task],
      process=Process.sequential,
      verbose=True,
  )
  
  if __name__ == "__main__":
      result = crew.kickoff()
      print(f"\n{'='*50}\n最终结果：\n{result}")
  ```

  - 安装：`uv pip install crewai`
  - 跑通

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week10/day2-crewai.md`

---

## ✅ 当日验收

- [ ] CrewAI 跑通
- [ ] 报告生成

---

## 💡 明日预告

**W11 D3 周三**：LangGraph 多 Agent（Supervisor）