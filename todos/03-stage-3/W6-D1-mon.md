# W6 D1 周一 · 2h — FastAPI 入门

- **阶段**：3 RAG 完整链路 | **周次**：W6 | **状态**：⬜
- **主题**：第一个 Web 接口

---

## 🎯 今日目标（3 项）

- [ ] 学 FastAPI 基本语法
- [ ] 写 `/chat` 接口
- [ ] curl 调通

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 看 [FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/) 前 4 章

  重点记：
- `@app.get("/path")` / `@app.post("/path")`
- 函数参数自动解析 query / body
- `return` 自动序列化为 JSON
- Pydantic 模型做请求/响应

### 💻 第一个 FastAPI 服务（60min）

- [ ] **[60min]** 在 `projects/02-rag-system/` 下创建 `app.py`：

  ```python
  """第一个 FastAPI 服务"""
  from fastapi import FastAPI
  from pydantic import BaseModel
  
  app = FastAPI(title="My First API")
  
  class ChatRequest(BaseModel):
      message: str
      user_id: str = "default"
  
  class ChatResponse(BaseModel):
      reply: str
      timestamp: str
  
  @app.get("/")
  def root():
      return {"status": "ok", "message": "Hello FastAPI"}
  
  @app.post("/chat", response_model=ChatResponse)
  def chat(req: ChatRequest):
      """接收消息，返回 mock 回复"""
      import datetime
      return ChatResponse(
          reply=f"你说了：{req.message}",
          timestamp=datetime.datetime.now().isoformat(),
      )
  ```

  - 安装：`uv pip install fastapi uvicorn`
  - 运行：`uvicorn app --reload --port 8000`
  - 测试：
    ```bash
    curl http://localhost:8000/
    curl -X POST http://localhost:8000/chat \
      -H "Content-Type: application/json" \
      -d '{"message": "你好"}'
    ```
  - 浏览器打开 `http://localhost:8000/docs` 看自动生成的 API 文档

### 📚 笔记（20min）

- [ ] **[20min]** 写 `notes/week6/day1-fastapi-basics.md`

---

## 📚 关键概念

| 概念 | 说明 |
|---|---|
| **FastAPI** | 现代 Python Web 框架 |
| **uvicorn** | ASGI 服务器 |
| **路由** | `@app.get/post/...` |
| **Pydantic** | 请求/响应数据校验 |
| **`/docs`** | 自动生成的 Swagger 文档 |

---

## ✅ 当日验收

- [ ] `app.py` 能跑
- [ ] `/` 返回 `{"status": "ok"}`
- [ ] `/chat` 接受 POST 返回正确 JSON
- [ ] `/docs` 自动文档能访问

---

## 💡 明日预告

**W6 D2 周二**：文档加载 + 切片