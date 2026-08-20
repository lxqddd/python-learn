# W13 D3 周三 · 4h — 项目 1 · RAG Pipeline

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：文档加载 + 切片 + 向量检索 + LangSmith

---

## 🎯 今日目标（4 项）

- [ ] 文档加载（PDF / Markdown）
- [ ] 切片 + 向量化
- [ ] 检索接口
- [ ] LangSmith trace

---

## ✅ 任务清单（4h）

### 💻 `backend/rag.py` 文档加载部分（60min）

- [ ] **[60min]**：

  ```python
  """RAG pipeline"""
  from langchain_community.document_loaders import PyPDFLoader, UnstructuredMarkdownLoader
  from langchain_text_splitters import RecursiveCharacterTextSplitter
  from langchain_chroma import Chroma
  from langchain_community.embeddings import HuggingFaceEmbeddings
  import tempfile
  from pathlib import Path
  
  embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")
  vectordb = Chroma(persist_directory="./chroma_db", collection_name="kb_docs", embedding_function=embeddings)
  splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
  
  def load_document(content, filename):
      suffix = Path(filename).suffix
      with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
          f.write(content)
          tmp_path = f.name
      try:
          if suffix.lower() == ".pdf":
              loader = PyPDFLoader(tmp_path)
          elif suffix.lower() in [".md", ".markdown"]:
              loader = UnstructuredMarkdownLoader(tmp_path)
          else:
              raise ValueError(f"不支持：{suffix}")
          docs = loader.load()
          for doc in docs:
              doc.metadata["source"] = filename
          return docs
      finally:
          Path(tmp_path).unlink(missing_ok=True)
  
  async def ingest_document(content, filename):
      docs = load_document(content, filename)
      chunks = splitter.split_documents(docs)
      vectordb.add_documents(chunks)
      vectordb.persist()
      return len(chunks)
  ```

### 🔍 检索接口（60min）

- [ ] **[60min]** 接混合检索：

  ```python
  def retrieve(query, k=3):
      return vectordb.similarity_search(query, k=k)
  ```

### 🔗 LangSmith trace（60min）

- [ ] **[60min]** 配置 `.env`：
  ```bash
  LANGCHAIN_TRACING_V2=true
  LANGCHAIN_API_KEY=lsv2_xxx
  LANGCHAIN_PROJECT=kb-assistant
  ```

  - 跑 1 个 query 看 trace

### 🧪 测试（40min）

- [ ] **[40min]** 端到端测试

---

## ✅ 当日验收

- [ ] 文档上传跑通
- [ ] 检索返回相关答案
- [ ] LangSmith trace 能看到

---

## 💡 明日预告

**W13 D4 周四 · 4h**：MCP 集成