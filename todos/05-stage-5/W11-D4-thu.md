# W11 D4 周四 · 2h — Railway 部署

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：把 RAG / Agent 部署上线

---

## 🎯 今日目标（3 项）

- [ ] 注册 Railway + 装 CLI
- [ ] 部署 W6 的 RAG 系统
- [ ] 验证公开 URL

---

## ✅ 任务清单（2h）

### 🔑 注册 + CLI（30min）

- [ ] **[30min]** 注册 [Railway](https://railway.app/) + 装 CLI

### 🚀 部署（60min）

- [ ] **[60min]** 部署步骤：

  ```bash
  railway login
  cd projects/02-rag-system
  railway init
  railway variables set DEEPSEEK_API_KEY=sk-xxx
  railway variables set DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
  railway up
  railway domain
  ```

### 🧪 验证（30min）

- [ ] **[30min]** 测试：
  ```bash
  curl https://xxx.up.railway.app/
  curl -X POST https://xxx.up.railway.app/chat \
    -H "Content-Type: application/json" \
    -d '{"question": "什么是 attention？"}'
  ```

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week11/day4-deploy.md`

---

## ✅ 当日验收

- [ ] 部署成功
- [ ] 公开 URL 可访问

---

## 💡 明日预告

**W11 D5 周五**：Docker Compose 完善 + 阶段 5 收尾