# W7 D4 周四 · 2h — LangSmith 接入

- **阶段**：3 RAG 完整链路 | **周次**：W7 | **状态**：⬜
- **主题**：全链路 trace

---

## 🎯 今日目标（3 项）

- [ ] 注册 LangSmith
- [ ] 配置环境变量
- [ ] 在 LangSmith 看到 trace

---

## ✅ 任务清单（2h）

### 🔑 注册 + 配置（40min）

- [ ] **[20min]** 注册 [LangSmith](https://www.langchain.com/langsmith)
- [ ] **[20min]** 配置 `.env`：

  ```bash
  LANGCHAIN_TRACING_V2=true
  LANGCHAIN_API_KEY=lsv2_xxx
  LANGCHAIN_PROJECT=my-rag-project
  ```

### 💻 让 RAG 自动 trace（30min）

- [ ] **[30min]** 改 `rag.py` 用 LangChain 的 ChatModel：

  ```python
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  
  llm = ChatOpenAI(
      model="deepseek-chat",
      openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
      openai_api_base=os.getenv("DEEPSEEK_BASE_URL"),
  )
  
  prompt = ChatPromptTemplate.from_messages([
      ("system", "你是文档问答助手。只基于提供的资料回答，不编造。"),
      ("user", "## 资料\n{context}\n\n## 问题\n{question}"),
  ])
  
  chain = prompt | llm
  
  def generate(question, docs):
      context_text = "\n\n".join(d["content"][:500] for d in docs)
      response = chain.invoke({"context": context_text, "question": question})
      return response.content
  ```

  - 安装：`uv pip install langchain-openai`

### 🔍 看 LangSmith（20min）

- [ ] **[20min]** 打开 [smith.langchain.com](https://smith.langchain.com/)
  - 应该看到 trace

### 📝 笔记（30min）

- [ ] **[30min]** 写 `notes/week7/day4-langsmith.md`

---

## ✅ 当日验收

- [ ] LangSmith 上有 trace
- [ ] 能看到 retrieve + generate 步骤

---

## 💡 明日预告

**W7 D5 周五**：Docker 打包