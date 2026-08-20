# W7 D3 周三 · 2h — RAGAS 评估

- **阶段**：3 RAG 完整链路 | **周次**：W7 | **状态**：⬜
- **主题**：Faithfulness / Relevancy / Precision / Recall

---

## 🎯 今日目标（3 项）

- [ ] 学 RAGAS 4 个核心指标
- [ ] 写 10 条 QA 对
- [ ] 跑评估

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [RAGAS 文档](https://docs.ragas.io/en/stable/concepts/metrics/index.html)：
  - Faithfulness
  - Answer Relevancy
  - Context Precision / Recall

### 📝 写 10 条 QA（30min）

- [ ] **[30min]** 创建 `eval_qa.jsonl` 写 10 条

### 💻 跑 RAGAS（60min）

- [ ] **[60min]** 创建 `evaluate_rag.py`：

  ```python
  """用 RAGAS 评估 RAG"""
  import json
  from datasets import Dataset
  from ragas import evaluate
  from ragas.metrics import (
      faithfulness,
      answer_relevancy,
      context_precision,
      context_recall,
  )
  from rag import rag_query
  from hybrid_retrieve import hybrid_retrieve
  from rerank import rerank
  
  qa_pairs = []
  with open("projects/02-rag-system/eval_qa.jsonl", encoding="utf-8") as f:
      for line in f:
          qa_pairs.append(json.loads(line))
  
  results = {"question": [], "answer": [], "contexts": [], "ground_truth": []}
  
  for qa in qa_pairs:
      q = qa["question"]
      result = rag_query(q)
      cands = hybrid_retrieve(q, k=10)
      docs = rerank(q, cands, top_k=3)
      
      results["question"].append(q)
      results["answer"].append(result["answer"])
      results["contexts"].append([d["content"] for d in docs])
      results["ground_truth"].append(qa["ground_truth"])
  
  dataset = Dataset.from_dict(results)
  score = evaluate(
      dataset=dataset,
      metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
  )
  print(score)
  ```

  - 安装：`uv pip install ragas datasets`
  - 跑通

### 📊 分析（20min）

- [ ] **[20min]** 写 `notes/week7/day3-ragas.md`

---

## ✅ 当日验收

- [ ] 10 条 QA 跑评估
- [ ] 4 个指标有分数

---

## 💡 明日预告

**W7 D4 周四**：LangSmith 接入