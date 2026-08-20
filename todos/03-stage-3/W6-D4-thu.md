# W6 D4 周四 · 2h — Chroma 向量库

- **阶段**：3 RAG 完整链路 | **周次**：W6 | **状态**：⬜
- **主题**：向量存储 + 检索

---

## 🎯 今日目标（3 项）

- [ ] 装 Chroma
- [ ] 把 chunks 存入 Chroma
- [ ] 用 query 检索 top-k

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [Chroma 快速入门](https://docs.trychify.com/getting-started)

### 💻 实战（60min）

- [ ] **[60min]** 创建 `chroma_store.py`：

  ```python
  """用 Chroma 存储并检索"""
  import chromadb
  from sentence_transformers import SentenceTransformer
  from langchain_community.document_loaders import PyPDFLoader
  from langchain_text_splitters import RecursiveCharacterTextSplitter
  
  CHROMA_DIR = "projects/02-rag-system/chroma_db"
  client = chromadb.PersistentClient(path=CHROMA_DIR)
  collection = client.get_or_create_collection(name="pdf_docs", metadata={"hnsw:space": "cosine"})
  
  model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
  def embed_fn(texts):
      return model.encode(texts).tolist()
  
  # 加载 + 切片 + 入库
  pages = PyPDFLoader("data/attention.pdf").load()
  chunks = RecursiveCharacterTextSplitter(chunk_size=500).split_documents(pages)
  collection.delete(where={})
  collection.add(
      ids=[f"chunk-{i}" for i in range(len(chunks))],
      documents=[c.page_content for c in chunks],
      metadatas=[c.metadata for c in chunks],
      embeddings=embed_fn([c.page_content for c in chunks]),
  )
  
  def search(query, k=3):
      results = collection.query(query_embeddings=embed_fn([query])[0], n_results=k)
      for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
          print(f"\n--- 来源：{meta.get('source', '?')} 第 {meta.get('page', '?')} 页 ---")
          print(doc[:200])
  
  if __name__ == "__main__":
      search("什么是 attention 机制？")
  ```

  - 安装：`uv pip install chromadb`
  - 跑通

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week6/day4-chroma.md`

---

## ✅ 当日验收

- [ ] chroma_store.py 跑通
- [ ] chunks 存入 Chroma
- [ ] 检索返回合理结果

---

## 💡 明日预告

**W6 D5 周五**：端到端 Naive RAG