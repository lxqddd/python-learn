# W3 D2 周二 · 2h — 装饰器与生成器

- **阶段**：1 Python 突击 | **周次**：W3 | **状态**：⬜
- **主题**：装饰器 / 生成器 / 列表推导式进阶

---

## 🎯 今日目标（3 项）

- [ ] 学装饰器（理解概念）
- [ ] 学生成器（`yield`）
- [ ] 写练习 8（计时装饰器）

---

## ✅ 任务清单（2h）

### 📖 阅读（80min）

- [ ] **[40min]** 看 [Real Python: Decorators](https://realpython.com/primer-on-python-decorators/) 前 5 节
  - 函数是一等公民（可以当参数、返回值）
  - 装饰器本质：包装函数
  - `@decorator` 语法
  - `functools.wraps`（了解）

- [ ] **[40min]** 看 [Real Python: Generators](https://realpython.com/introduction-to-python-generators/)
  - `yield` 暂停并保存
  - `next()` 继续
  - 生成器表达式 `(x*2 for x in range(10))`

### 💻 练习 8：计时装饰器（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex08_timing_decorator.py`：
  ```python
  """装饰器：记录函数执行时间"""
  import time
  from functools import wraps
  
  def timing(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          t0 = time.time()
          result = func(*args, **kwargs)
          elapsed = time.time() - t0
          print(f"⏱️  {func.__name__} 耗时 {elapsed*1000:.2f}ms")
          return result
      return wrapper
  
  @timing
  def slow_function():
      time.sleep(0.5)
      return "done"
  
  @timing
  def add(a, b):
      return a + b
  
  if __name__ == "__main__":
      print(slow_function())
      print(add(1, 2))
  ```
  - 跑通，看时间打印
  - 试一下加 `@timing` 到 chatbot 的 API 调用上看 API 延迟

---

## 📚 关键概念

| 概念 | 用途 |
|---|---|
| `@decorator` | 不改原函数，加功能 |
| `wraps(func)` | 保留原函数元信息 |
| `yield` | 暂停返回，下次从这继续 |
| 生成器表达式 | 节省内存的迭代器 |

**为什么装饰器对 Agent 重要？** 框架大量用装饰器（`@tool`、`@retry`）。理解后才能看懂框架源码。

---

## ✅ 当日验收

- [ ] 练习 8 跑通
- [ ] 能解释 `@wraps` 的作用
- [ ] 能写出简单的生成器函数

---

## 💡 明日预告

**W3 D3 周三**：async/await + 类型提示 + pydantic