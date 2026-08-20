# W6 D2 周二 · 2h — 文档加载与切片

- **阶段**：3 RAG 完整链路 | **周次**：W6 | **状态**：⬜
- **主题**：PDF/Markdown 解析 + 切片策略

---

## 🎯 今日目标（3 项）

- [ ] 学 LangChain Document Loaders
- [ ] 学切片策略
- [ ] 加载并切片一个 PDF

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 看 [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [ ] **[20min]** 看 [Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)

### 💻 实战：加载 PDF（60min）

- [ ] **[60min]** 在 `projects/02-rag-system/` 下创建 `load_and_split.py`：

  ```python
  """加载 PDF + 切片"""
  from langchain_community.document_loaders import PyPDFLoader
  from langchain_text_splitters import RecursiveCharacterTextSplitter
  
  PDF_PATH = "projects/02-rag-system/data/attention.pdf"
  
  loader = PyPDFLoader(PDF_PATH)
  pages = loader.load()
  print(f"加载 {len(pages)} 页")
  
  splitter = RecursiveCharacterTextSplitter(
      chunk_size=500,
      chunk_overlap=50,
      separators=["\n\n", "\n", "。", ".", " ", ""],
  )
  chunks = splitter.split_documents(pages)
  print(f"切成 {len(chunks)} 个 chunk")
  ```

  - 安装：`uv pip install langchain langchain-community pypdf`
  - 下载测试 PDF
  - 跑通

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week6/day2-chunking.md`

---

## ✅ 当日验收

- [ ] 加载 1 个 PDF 成功
- [ ] 切出 ≥ 10 个 chunk

---

## 💡 明日预告

**W6 D3 周三**：Embedding 向量化