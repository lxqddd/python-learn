# W7 D2 周二 · 2h — Reranker

- **阶段**：3 RAG 完整链路 | **周次**：W7 | **状态**：⬜
- **主题**：重排序提升精度

---

## 🎯 今日目标（3 项）

- [ ] 学 Reranker 概念
- [ ] 接入 BGE-Reranker
- [ ] 对比差异

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 学 Reranker：BGE-Reranker 开源，效果好

### 💻 接 Reranker（90min）

- [ ] **[90min]** 创建 `rerank.py`：

  ```python
  """Reranker：对检索结果重排序"""
  from sentence_transformers import CrossEncoder
  from hybrid_retrieve import hybrid_retrieve
  
  reranker = CrossEncoder("BAAI/bge-reranker-base")
  
  def rerank(query, docs, top_k=3):
      """用 CrossEncoder 重排序"""
      pairs = [[query, d["content"]] for d in docs]
      scores = reranker.predict(pairs)
      
      for i, doc in enumerate(docs):
          doc["rerank_score"] = float(scores[i])
      
      docs.sort(key=lambda x: x["rerank_score"], reverse=True)
      return docs[:top_k]
  
  if __name__ == "__main__":
      query = "什么是 attention 机制？"
      candidates = hybrid_retrieve(query, k=5, alpha=0.5)
      print("=== 混合检索 top-5 ===")
      for i, d in enumerate(candidates):
          print(f"[{i+1}] final={d['final_score']:.4f}")
      
      print("\n=== Rerank 后 top-3 ===")
      reranked = rerank(query, candidates, top_k=3)
      for i, d in enumerate(reranked):
          print(f"[{i+1}] rerank={d['rerank_score']:.4f}")
  ```

  - 第一次跑会下载 ~1GB 模型
  - 跑通

### 🧪 集成到 RAG（30min）

- [ ] **[30min]** 改 `rag.py`，加入 rerank：

  ```python
  def rag_query(question):
      candidates = hybrid_retrieve(question, k=10, alpha=0.5)
      docs = rerank(question, candidates, top_k=3)
      ...
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week7/day2-rerank.md`

---

## ✅ 当日验收

- [ ] rerank.py 跑通
- [ ] 至少 1 个 query 改善
- [ ] rag.py 接入 rerank

---

## 💡 明日预告

**W7 D3 周三**：RAGAS 评估