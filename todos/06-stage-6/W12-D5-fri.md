# W13 D5 周五 · 4h — 项目 1 · 前端 + 评估 + 视频

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：Streamlit + 30 eval + 视频

---

## 🎯 今日目标（4 项）

- [ ] Streamlit 前端（最小可用）
- [ ] 30 条 eval case 编写
- [ ] RAGAS 评估
- [ ] 录 demo 视频（≤ 3 分钟）

---

## ✅ 任务清单（4h）

### 🎨 Streamlit 前端（60min）

- [ ] **[60min]** `frontend/app.py`：

  ```python
  import streamlit as st
  import requests
  
  API_URL = "http://localhost:8000"
  st.title("📚 个人知识库助手")
  
  with st.sidebar:
      st.header("上传文档")
      uploaded = st.file_uploader("选择 PDF / Markdown", type=["pdf", "md"])
      if uploaded and st.button("处理"):
          files = {"file": (uploaded.name, uploaded.getvalue())}
          resp = requests.post(f"{API_URL}/upload", files=files)
          if resp.status_code == 200:
              st.success(f"✅ 已处理 {resp.json()['chunks']} 个片段")
  
  if "messages" not in st.session_state:
      st.session_state.messages = []
  
  for msg in st.session_state.messages:
      with st.chat_message(msg["role"]):
          st.write(msg["content"])
  
  if prompt := st.chat_input("问点什么..."):
      st.session_state.messages.append({"role": "user", "content": prompt})
      with st.chat_message("user"):
          st.write(prompt)
      with st.chat_message("assistant"):
          with st.spinner("思考中..."):
              resp = requests.post(f"{API_URL}/chat", json={"message": prompt, "thread_id": "streamlit-user"})
              answer = resp.json()["reply"]
              st.write(answer)
      st.session_state.messages.append({"role": "assistant", "content": answer})
  ```

### 📝 30 条 Eval（90min）

- [ ] **[90min]** `eval/cases.jsonl` 写 30 条

### 📊 RAGAS 评估（60min）

- [ ] **[60min]** 跑 RAGAS，记录分数到 `eval/results.md`

### 🎬 录 Demo 视频（30min）

- [ ] **[30min]** 录 ≤ 3 分钟 demo

### 📦 打包（10min）

- [ ] **[10min]** git commit + tag

---

## ✅ 当日验收

- [ ] Streamlit 跑通
- [ ] 30 条 eval 通过率 ≥ 80%
- [ ] Demo 视频录好

---

## 💡 周末预告

**W13 周日**：打开 [`W13-review.md`](W13-review.md) 做项目 1 验收