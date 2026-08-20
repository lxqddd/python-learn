# W13 D2 周二 · 4h — 项目 1 · 后端骨架

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：FastAPI + LangGraph + WebSocket

---

## 🎯 今日目标（4 项）

- [ ] FastAPI 项目结构
- [ ] LangGraph Agent 接入
- [ ] WebSocket 流式输出
- [ ] 跑通 `/chat` 接口

---

## ✅ 任务清单（4h）

### 🏗 项目结构（30min）

- [ ] **[30min]** 建：
  ```
  project1-kb-assistant/
  ├── backend/
  │   ├── app.py
  │   ├── agent.py
  │   ├── rag.py
  │   ├── tools.py
  │   └── config.py
  ├── frontend/
  ├── docs/
  ├── .env.example
  └── requirements.txt
  ```

### 💻 FastAPI 入口（90min）

- [ ] **[90min]** `backend/app.py`：

  ```python
  from fastapi import FastAPI, WebSocket, UploadFile, File
  from pydantic import BaseModel
  from agent import run_agent
  from rag import ingest_document
  
  app = FastAPI(title="KB Assistant")
  
  class ChatRequest(BaseModel):
      message: str
      thread_id: str = "default"
  
  @app.post("/chat")
  async def chat(req: ChatRequest):
      result = await run_agent(req.message, req.thread_id)
      return {"reply": result["reply"], "sources": result["sources"]}
  
  @app.websocket("/ws/chat")
  async def websocket_chat(ws: WebSocket):
      await ws.accept()
      try:
          while True:
              data = await ws.receive_json()
              async for chunk in run_agent_stream(data["message"], data.get("thread_id", "default")):
                  await ws.send_json({"type": "chunk", "content": chunk})
              await ws.send_json({"type": "done"})
      finally:
          await ws.close()
  
  @app.post("/upload")
  async def upload(file: UploadFile = File(...)):
      content = await file.read()
      result = await ingest_document(content, file.filename)
      return {"filename": file.filename, "chunks": result}
  
  @app.get("/")
  def root():
      return {"status": "ok", "service": "kb-assistant"}
  ```

### 🕸 LangGraph Agent（90min）

- [ ] **[90min]** `backend/agent.py`：

  ```python
  from typing import TypedDict, Annotated, Literal
  from langgraph.graph import StateGraph, START, END
  from langgraph.graph.message import add_messages
  from langgraph.checkpoint.memory import MemorySaver
  from langchain_core.messages import HumanMessage
  from langchain_openai import ChatOpenAI
  from langchain_core.tools import tool
  import os
  
  from rag import retrieve
  
  llm = ChatOpenAI(model="deepseek-chat", temperature=0)
  
  @tool
  def search_kb(query: str, k: int = 3) -> str:
      """在个人知识库搜索"""
      docs = retrieve(query, k=k)
      if not docs:
          return "未找到相关文档"
      return "\n\n".join([f"[文档{i+1}]\n{d.page_content[:500]}" for i, d in enumerate(docs)])
  
  agent_llm = llm.bind_tools([search_kb])
  
  class State(TypedDict):
      messages: Annotated[list, add_messages]
  
  def agent_node(state):
      response = agent_llm.invoke(state["messages"])
      return {"messages": [response]}
  
  def tool_node(state):
      last = state["messages"][-1]
      results = []
      for tc in last.tool_calls:
          if tc["name"] == "search_kb":
              results.append({"role": "tool", "content": search_kb.invoke(tc["args"]), "tool_call_id": tc["id"]})
      return {"messages": results}
  
  def router(state) -> Literal["tools", "end"]:
      last = state["messages"][-1]
      if hasattr(last, "tool_calls") and last.tool_calls:
          return "tools"
      return "end"
  
  graph = StateGraph(State)
  graph.add_node("agent", agent_node)
  graph.add_node("tools", tool_node)
  graph.add_edge(START, "agent")
  graph.add_conditional_edges("agent", router, {"tools": "tools", "end": END})
  graph.add_edge("tools", "agent")
  
  memory = MemorySaver()
  app_agent = graph.compile(checkpointer=memory)
  
  async def run_agent(message, thread_id="default"):
      config = {"configurable": {"thread_id": thread_id}}
      result = app_agent.invoke({"messages": [HumanMessage(content=message)]}, config=config)
      return {"reply": result["messages"][-1].content, "sources": []}
  ```

### 🧪 测试（30min）

- [ ] **[30min]** 跑通：
  ```bash
  uvicorn app:app --reload --port 8000
  curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message": "什么是 Python 异步？"}'
  ```

---

## ✅ 当日验收

- [ ] FastAPI 跑通
- [ ] `/chat` 接口返回答案
- [ ] WebSocket 接好

---

## 💡 明日预告

**W13 D3 周三 · 4h**：RAG pipeline + LangSmith