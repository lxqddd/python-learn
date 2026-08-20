# W6 D5 周五 · 4h — 端到端 Naive RAG

- **阶段**：3 RAG 完整链路 | **周次**：W6 | **状态**：⬜
- **主题**：query → retrieve → prompt → LLM → answer

---

## 🎯 今日目标（3 项）

- [ ] 写 `rag.py`：完整 RAG pipeline
- [ ] 接入 FastAPI `/chat` 接口
- [ ] curl 能问到 PDF 里的信息

---

## ✅ 任务清单（4h）

### 💻 `rag.py`：核心 pipeline（90min）

- [ ] **[90min]** 创建 `rag.py`：

  ```python
  """Naive RAG 完整流程"""
  import os
  from open import OpenAI
  from dotenv import load_dotenv
  from chromadb import PersistentClient
  from sentence_transformers import SentenceTransformer
  
  load_dotenv()
  
  client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL"))
  chroma_client = PersistentClient(path="projects/02-rag-system/chroma_db")
  collection = chroma_client.get_collection("pdf_docs")
  embed_model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
  
  def retrieve(query, k=3):
      query_emb = embed_model.encode([query]).tolist()
      results = collection.query(query_embeddings=query_emb, n_results=k)
      return [
          {"content": doc, "metadata": meta, "score": 1 - dist}
          for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0])
      ]
  
  def generate(question, context_docs):
      context_text = = "\n\n".join(d["content"][:500] for d in context_docs)
      sources = "\n".join(f(f"- [{d['metadata'].get('source', '?')} 第 {d['metadata'].get('page', '?')} 页]" for d in context_docs)
      prompt = f"基于以下资料回答问题：\n\n{context_text}\n\n来源：{sources}\n\n问题：{question}"
      response = client.chat.completions.create(
          model="deepseek-chat",
          messages=[
              {"role": "system", "content": "你是文档问答助手。只基于提供的资料回答。"},
              {"role": "user", "content": prompt},
          ],
      )
      return response.choices[0].message.content
  
  def rag_query(question):
      docs = retrieve(question)
      if not docs:
          return {"answer": "未找到相关信息", "sources": []}
      answer = generate(question, docs)
      return {"answer": answer, "sources": [{"source": d["metadata"].get("source"), "page": d["metadata"].get("page")} for d in docs]}
  ```

### 💻 接入 FastAPI（60min）

- [ ] **[60min]** 创建 `app.py`：

  ```python
  """FastAPI 服务"""
  from fastapi import FastAPI
  from pydantic import BaseModel
  from rag import rag_query
  
  app = FastAPI(title="RAG API")
  
  class ChatRequest(BaseModel):
      question: str
  
  class ChatResponse(BaseModel):
      answer: str
      sources: list[dict]
  
  @app.post("/chat", response_model=ChatResponse)
  def chat(req: ChatRequest):
      result = rag_query(req.question)
      return ChatResponse(answer=result["answer"], sources=result["sources"])
  
  @app.get("/")
  def root():
      return {"status": "ok", "service": "RAG"}
  ```

### 🧪 验证（30min）

- [ ] **[30min]** 跑 5 个 query 验证

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week6/day5-naive-rag.md`

---

## ✅ 当日验收

- [ ] `/chat` 接口能调通
- [ ] 5 个测试 query 表现合理
- [ ] 答案含来源标注

---

## 💡 周末预告

**W6 周日**：打开 [`W6-review.md`](W6-review.md) 做验收