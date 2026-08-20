# W7 D5 周五 · 4h — Docker 打包

- **阶段**：3 RAG 完整链路 | **周次**：W7 | **状态**：⬜
- **主题**：RAG 系统一键启动

---

## 🎯 今日目标（3 项）

- [ ] 写 Dockerfile
- [ ] 写 docker-compose.yml
- [ ] `docker compose up` 跑通

---

## ✅ 任务清单（4h）

### 🐳 Dockerfile（60min）

- [ ] **[60min]** 创建 `Dockerfile`：

  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  EXPOSE 8000
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

  `requirements.txt`：
  ```text
  fastapi>=0.100
  uvicorn[standard]>=0.23
  pydantic>=2.0
  python-dotenv>=1.0
  openai>=1.0
  chromadb>=0.4
  sentence-transformers>=2.2
  rank_bm25>=0.3
  jieba>=0.42
  langchain>=0.1
  langchain-openai>=0.0.5
  ragas>=0.1
  ```

### 🐳 docker-compose.yml（60min）

- [ ] **[60min]** 创建 `docker-compose.yml`：

  ```yaml
  version: "3.8"
  services:
    rag-api:
      build: .
      ports:
        - "8000:8000"
      env_file:
        - .env
      volumes:
        - ./chroma_db:/app/chroma_db
        - ./data:/app/data
      restart: unless-stopped
    redis:
      image: redis:7-alpine
      volumes:
        - redis_data:/data
  volumes:
    redis_data:
  ```

### 🚀 跑通（60min）

- [ ] **[60min]** 测试：
  ```bash
  cd projects/02-rag-system
  docker compose up --build -d
  docker compose logs -f
  curl http://localhost:8000/
  curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"question": "什么是 attention？"}'
  ```

### 📝 README + 笔记（40min）

- [ ] **[40min]** 写 README + notes

---

## ✅ 当日验收

- [ ] `docker compose up` 跑通
- [ ] `/chat` 接口能调

---

## 💡 周末预告

**W7 周日**：打开 [`W7-review.md`](W7-review.md) 做阶段 3 验收