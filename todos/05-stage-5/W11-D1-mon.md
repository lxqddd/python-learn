# W11 D1 周一 · 2h — 性能优化

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：异步并发 + 缓存 + token 优化

---

## 🎯 今日目标（3 项）

- [ ] 学异步并发（asyncio.gather）
- [ ] 学 Redis 缓存策略
- [ ] 优化 token 使用

---

## ✅ 任务清单（2h）

### 💻 异步并发（60min）

- [ ] **[60min]** 创建 `async_demo.py`：

  ```python
  """异步并发：批量调 LLM"""
  import asyncio
  import time
  from openai import AsyncOpenAI
  import os
  
  client = AsyncOpenAI(
      api_key=os.getenv("DEEPSEEK_API_KEY"),
      base_url=os.getenv("DEEPSEEK_BASE_URL"),
, )
  
  async def single_call(prompt: str) -> str:
      response = await client.chat.completions.create(
          model="deepseek-chat",
          messages=[{"role": "user", "content": prompt}],
          max_tokens=100,
      )
      return response.choices[0].message.content
  
  async def batch_calls(prompts):
      tasks = [single_call(p) for p in prompts]
      return await asyncio.gather(*tasks)
  
  async def main():
      prompts = [f"用一句话介绍主题 {i}" for i in range(10)]
      
      t0 = time.time()
      for p in prompts:
          await single_call(p)
      t_serial = time.time() - t0
      
      t0 = time.time()
      await batch_calls(prompts)
      t_async = time.time() - t0
      
      print(f"串行：{t_serial:.2f}s")
      print(f"并发：{t_async:.2f}s")
      print(f"加速：{t_serial/t_async:.2f}x")
  
  if __name__ == "__main__":
      asyncio.run(main())
  ```

### 💻 缓存策略（30min）

- [ ] **[30min]** 创建 `cache_demo.py`：用 hash 作为 key 缓存 LLM 结果

### 💻 Token 优化（30min）

- [ ] **[30min]** 创建 `token_optimization.py`：

  ```python
  def truncate_context(docs, max_chars=2000):
      combined = "\n\n".join(docs)
      if len(combined) > max_chars:
          half = max_chars // 2
          combined = combined[:half] + "\n\n[...截断...]\n\n" + combined[-half:]
      return combined
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week11/day1-performance.md`

---

## 📚 关键概念

| 技巧 | 提速 / 节省 |
|---|---|
| **asyncio.gather** | N 倍（取决于并发数） |
| **结果缓存** | 重复请求 0 token |
| **Context 截断** | 节省 30-50% token |

---

## ✅ 当日验收

- [ ] asyncio 并发提速 ≥ 5x
- [ ] 缓存能命中
- [ ] Token 优化有效果

---

## 💡 明日预告

**W11 D2 周二**：安全防御