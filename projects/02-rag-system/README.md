# 📚 Project 02 · RAG 完整链路（第 5-6 周）

> 在 First 7 Days Sprint 完成后开始。

---

## 🎯 目标

构建一个**端到端的 RAG 系统**：
- 加载 PDF / Markdown 文档
- 切片、向量化、入向量库
- 检索 + 生成回答
- 全链路可观测

---

## 🗂 待办结构

```
02-rag-system/
├── README.md              ← 本文件
├── requirements.txt       ← fastapi, langchain, chromadb, ...
├── data/                  ← 文档（PDF、Markdown）
├── ingest.py              ← 加载 → 切片 → 向量化 → 入库
├── retrieve.py            ← 检索（向量 + BM25 混合）
├── api.py                 ← FastAPI 服务
├── frontend/              ← 简单 Web UI
└── eval/                  ← RAG 评估（RAGAS）
```

---

## 📅 第 5 周任务

- [ ] 安装依赖：`pip install fastapi langchain chromadb sentence-transformers`
- [ ] 阅读 [All-in-RAG](https://github.com/datawhalechina/all-in-rag) 教程
- [ ] Day 1：FastAPI 入门（Hello World + 一个查询接口）
- [ ] Day 2：文档加载（Unstructured / Docling 解析 PDF）
- [ ] Day 3：切片策略（按段落 / 按 token / 父子切片）
- [ ] Day 4：向量化（sentence-transformers / BGE）
- [ ] Day 5：Chroma / Milvus 存储
- [ ] Day 6：端到端：query → retrieve → prompt → LLM → answer
- [ ] Day 7：Docker 打包

---

## 📅 第 6 周任务

- [ ] 升级到混合检索（向量 + BM25）
- [ ] 加 Reranker（BGE-Reranker / Cohere）
- [ ] 接入 RAGAS 做评估
- [ ] LangSmith 接入
- [ ] 性能优化（缓存、异步、并发）

---

## 📚 推荐资源

- [All-in-RAG（Datawhale）](https://github.com/datawhalechina/all-in-rag) ★★★★★
- [LangChain RAG Tutorial](https://python.langchain.com/v0.1/docs/tutorials/rag/)
- [Chroma 文档](https://docs.trychroma.com/)
- [RAGAS 文档](https://docs.ragas.io/)

---

## 🎯 完成标准

- [ ] 能处理 100+ 文档
- [ ] 检索 P99 延迟 < 500ms
- [ ] 答案有来源引用
- [ ] RAGAS 评估指标：faithfulness > 0.8, relevancy > 0.8
- [ ] README 可 clone-and-run
- [ ] 简历 bullet：
  > 构建端到端 RAG 系统，支持 PDF/Markdown 多格式文档解析，采用混合检索（向量 + BM25）+ Reranker，QPS 达到 200，P99 延迟 < 500ms，RAGAS faithfulness 评分 0.85+。