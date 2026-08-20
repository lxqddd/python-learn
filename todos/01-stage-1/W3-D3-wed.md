# W3 D3 周三 · 2h — async + 类型 + pydantic

- **阶段**：1 Python 突击 | **周次**：W3 | **状态**：⬜
- **主题**：async/await / 类型提示 / pydantic BaseModel

---

## 🎯 今日目标（3 项）

- [ ] 学 async/await 基本语法
- [ ] 学类型提示（type hints）
- [ ] 写练习 9（pydantic schema）

---

## ✅ 任务清单（2h）

### 📖 阅读（80min）

- [ ] **[40min]** 看 [Real Python: async/await](https://realpython.com/async-io-python/) 前 5 节
  - `async def` 定义协程函数
  - `await` 等待异步操作
  - `asyncio.run()` 启动
  - `asyncio.gather()` 并发
  - 理解：异步 ≠ 多线程，是单线程切换

- [ ] **[40min]** 学类型提示
  - `def foo(x: int) -> str:`
  - `from typing import List, Dict, Optional`
  - Python 3.10+：`list[int]` / `dict[str, int]`（PEP 585）

### 💻 练习 9：pydantic schema（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex09_pydantic.py`：
  ```python
  """用 pydantic 定义 LLM 请求 schema"""
  from pydantic import BaseModel, Field
  from typing import Literal
  
  class LLMRequest(BaseModel):
      """LLM 请求结构"""
      model: str = Field(default="deepseek-chat", description="模型名")
      temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="温度")
      max_tokens: int = Field(default=2000, gt=0, description="最大 token")
      messages: list[dict[str, str]] = Field(..., description="消息列表")
      stream: bool = Field(default=False, description="是否流式")
  
  class LLMResponse(BaseModel):
      """LLM 响应结构"""
      content: str
      usage: dict[str, int] = Field(default_factory=dict)
      finish_reason: Literal["stop", "length", "error"] = "stop"
  
  # 测试
  if __name__ == "__main__":
      req = LLMRequest(
          model="deepseek-chat",
          messages=[{"role": "user", "content": "你好"}],
      )
      print(req.model_dump_json(indent=2))
      
      # 错误：temperature 超出范围
      try:
          bad = LLMRequest(temperature=3.0, messages=[])
      except Exception as e:
          print(f"校验失败: {e}")
  ```
  - `uv pip install pydantic`
  - 跑通，看 schema 校验

---

## 📚 关键概念

| 概念 | 用途 |
|---|---|
| `async def` | 异步函数 |
| `await` | 等待异步操作 |
| `def foo(x: int) -> str` | 类型提示 |
| `BaseModel` | pydantic 数据校验 |
| `Field(...)` | 必填字段 |

**为什么 pydantic 对 Agent 重要？** LangChain / LangGraph / Pydantic AI 全用它做数据校验。理解后看框架代码不会慌。

---

## ✅ 当日验收

- [ ] 练习 9 跑通，schema 校验生效
- [ ] 能写出 `async def` / `await` 基本用法
- [ ] 理解 pydantic 在 Agent 框架中的作用

---

## 💡 明日预告

**W3 D4 周四**：dotenv + 配置 + 模块化