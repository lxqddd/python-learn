# W13 D2 周二 · 4h — 项目 2 · 搜索 + 抓取

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：Tavily 搜索 + Jina Reader

---

## 🎯 今日目标（3 项）

- [ ] 接入 Tavily / SerpAPI
- [ ] 接入 Jina Reader
- [ ] 实现 Researcher Agent

---

## ✅ 任务清单（4h）

### 🔑 API 配置（30min）

- [ ] **[30min]** 注册 Tavily + Jina，加到 `.env`

### 🔧 工具实现（90min）

- [ ] **[90min]** `backend/tools.py`：

  ```python
  import os
  import requests
  
  TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
  JINA_API_KEY = os.getenv("JINA_API_KEY")
  
  def tavily_search(query, max_results=5):
      resp = requests.post(
          "https://api.tavily.com/search",
          json={"api_key": TAVILY_API_KEY, "query": query, "max_results": max_results, "search_depth": "advanced"},
          timeout=30,
      )
      data = resp.json()
      return [
          {"title": r["title"], "url": r["url"], "snippet": r["content"][:500]}
          for r in data.get("results", [])
      ]
  
  def jina_reader(url):
      headers = {"Authorization": f"Bearer {JINA_API_KEY}", "X-Return-Format": "markdown"}
      resp = requests.get(f"https://r.jina.ai/{url}", headers=headers, timeout=30)
      if resp.status_code != != 200:
          return f"❌ 抓取失败"
      text = resp.text
      return text[:10000] if len(text) > 10000 else text
  ```

### 🤖 Researcher Agent（120min）

- [ ] **[120min]** `backend/agents/researcher.py`：

  ```python
  from langchain_openai import ChatOpenAI
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from typing import TypedDict, Annotated
  import os
  
  from tools import tavily_search, jina_reader
  
  llm = ChatOpenAI(model="deepseek-chat")
  
  class ResearcherState(TypedDict):
      messages: Annotated[list, add_messages]
      topic: str
      findings: list[str]
  
  def search_node(state):
      results = tavily_search(state["topic"], max_results=5)
      summary = "\n\n".join([f"[{i+1}] {r['title']}\n{r['snippet']}\nURL: {r['url']}" for i, r in enumerate(results)])
      return {"messages": [HumanMessage(content=f"搜索结果：\n{summary}")]}
  
  def read_node(state):
      last_msg = state["messages"][-1].content
      import re
      urls = re.findall(r"URL: (https?://\S+)", last_msg)
      if not urls:
          return {"messages": [HumanMessage(content="无 URL可读")]}
      content = jina_reader(urls[0])
      return {"messages": [HumanMessage(content=f"网页内容：\n{content[:5000]}")] if content else None, "findings": state.get("findings", []) + [content[:2000]]}
  
  def extract_node(state):
      content = state["messages"][-1].content
      prompt = f"从以下内容中提取 5 条关键信息：\n{content}"
      response = llm.invoke([SystemMessage(content="你是研究员"), HumanMessage(content=prompt)])
      return {"messages": [response], "findings": state.get("findings", []) + [response.content]}
  
  graph = StateGraph(ResearcherState)
  graph.add_node("search", search_node)
  graph.add_node("read", read_node)
  graph.add_node("extract", extract_node)
  graph.add_edge(START, "search")
  graph.add_edge("search", "read")
  graph.add_edge("read", "extract")
  graph.add_edge("extract", END)
  researcher = graph.compile()
  ```

### 🧪 测试（40min）

- [ ] **[40min]** 跑测试

---

## ✅ 当日验收

- [ ] Tavily 跑通
- [ ] Jina Reader 跑通
- [ ] Researcher Agent 跑通

---

## 💡 明日预告

**W13 D3 周三 · 4h**：阅读 + 总结 Agent