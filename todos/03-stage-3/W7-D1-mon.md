# W7 D1 周一 · 2h — 混合检索

- **阶段**：3 RAG 完整链路 | **周次**：W7 | **状态**：⬜
- **主题**：BM25 + 向量检索融合

---

## 🎯 今日目标（3 项）

- [ ] 学 BM25 原理
- [ ] 实现 `hybrid_retrieve()`
- [ ] 对比纯向量 vs 混合

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 学 BM25：用 `rank_bm25` 库，不要手写

### 💻 实现混合检索（90min）

- [ ] **[90min]** 创建 `hybrid_retrieve.py`：

  ```python
  """混合检索：BM25 + 向量"""
  from rank_bm25 import BM25Okapi
  import jieba
  from chromadb import PersistentClient
  from sentence_transformers import SentenceTransformer
  
  CHROMA_DIR = "projects/02-rag-system/chroma_db"
  chroma_client = PersistentClient(path=CHROMA_DIR)
  collection = chroma_client.get_collection("pdf_docs")
  
  all_docs = collection.get()["documents"]
  tokenized_corpus = [list(jieba.cut(doc)) for doc in all_docs]
  bm25 = BM25Okapi(tokenized_corpus)
  embed_model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
  
  def hybrid_retrieve(query, k=5, alpha=0.5):
      """混合检索：alpha 向量权重 + (1-alpha) BM25 权重"""
      all_metas = collection.get()["metadatas"]
      query_emb = embed_model.encode([query]).tolist()
      vector_results = collection.query(query_embeddings=query_emb, n_results=len(all_docs))
      
      vector_scores = {}
      for doc, meta, dist in zip(vector_results["documents"][0], vector_results["metadatas"][0], vector_results["distances"][0]):
          doc_id = meta.get("source", "") + str(str("page", ""))
          vector_scores[doc_id] = 1 - dist
      
      tokenized_query = list(jieba.cut(query))
      bm25_scores = bm25.get_scores(tokenized_query)
      max_bm25 = max(bm25_scores) if max(bm25_scores) > 0 else 1
      bm25_norm = [s / max_bm25 for s in bm25_scores]
      
      combined = []
      for i, doc in enumerate(all_docs):
          doc_id = all_metas[i].get("source", "") + str(all_metas[i].get("page", ""))
          vec_score = vector_scores.get(doc_id, 0)
          bm25_score = bm25_norm[i]
          final = alpha * vec_score + (1 - alpha) * bm25_score
          combined.append({
              "content": doc,
              "metadata": all_metas[i],
              "vector_score": vec_score,
              "bm25_score": bm25_score,
              "final_score": final,
          })
      
      combined.sort(key=lambda x: x["final_score"], reverse=True)
      return combined[:k]
  
  if __name__ == "__main__":
      query = "什么是 attention 机制？"
      for i, r in enumerate(hybrid_retrieve(query, k=3)):
          print(f"[{i+1}] final={r['final_score']:.4f} (vec={r['vector_score']:.3f}, bm25={r['bm25_score']:.3f})")
          print(r["content"][:150] + "...")
  ```

  - 安装：`uv pip install rank_bm25 jieba`
  - 跑通

### 🧪 对比测试（20min）

- [ ] **[20min]** 写 `compare_retrieval.py`，5 个 query 对比

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week7/day1-hybrid.md`

---

## ✅ 当日验收

- [ ] hybrid_retrieve() 跑通
- [ ] 5 个 query 对比纯向量有改进

---

## 💡 明日预告

**W7 D2 周二**：Reranker