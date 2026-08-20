# W6 D3 周三 · 2h — Embedding 向量化

- **阶段**：3 RAG 完整链路 | **周次**：W6 | **状态**：⬜
- **主题**：把文字变成向量

---

## 🎯 今日目标（3 项）

- [ ] 理解 Embedding 概念
- [ ] 本地跑 embedding 模型
- [ ] 验证语义相似度

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 看 Embedding 概念：
  - [OpenAI Embeddings 文档](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
  - 相似度计算：cosine similarity
  - 推荐：[BGE-small-zh-v1.5](https://huggingface.co/BAAI/bge-small-zh-v1.5)

### 💻 跑 embedding（60min）

- [ ] **[60min]** 创建 `embedding_demo.py`：

  ```python
  """Embedding 模型 demo"""
  from sentence_transformers import SentenceTransformer
  import numpy as np
  
  model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
  
  texts = [
      "Python 是一门编程语言",
      "我喜欢吃苹果",
      "今天天气真好",
      "Python 的异步编程很有意思",
  ]
  
  embeddings = model.encode(texts)
  print(f"向量维度：{embeddings.shape}")
  
  def cosine_sim(a, b):
      return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
  
  for i, t1 in enumerate(texts):
      for j, t2 in enumerate(texts):
          if i < j:
              sim = cosine_sim(embeddings[i], embeddings[j])
              print(f"  {t1[:20]} ↔ {t2[:20]}: {sim:.4f}")
  ```

  - 安装：`uv pip install sentence-transformers`
  - 跑通

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week6/day3-embedding.md`

---

## ✅ 当日验收

- [ ] embedding 模型能跑
- [ ] 看到相似度矩阵

---

## 💡 明日预告

**W6 D4 周四**：Chroma 向量库