# W2 D3 周三 · 2h — 函数

- **阶段**：1 Python 突击 | **周次**：W2 | **状态**：⬜
- **主题**：def / `*args` / `**kwargs` / lambda / 作用域

---

## 🎯 今日目标（3 项）

- [ ] 学函数定义与返回值
- [ ] 学 `*args` / `**kwargs` / lambda
- [ ] 写练习 4（JSON 解析）

---

## ✅ 任务清单（2h）

### 📖 阅读（80min）

- [ ] **[40min]** 看 [Real Python: Defining Functions](https://realpython.com/defining-your-own-python-function/)
  - `def function_name(args):`
  - `return` 可返回多个值（元组）
  - 默认参数 `def foo(x, y=10):`
  - 文档字符串（docstring）

- [ ] **[40min]** 看 [`*args` 和 `**kwargs`](https://realpython.com/python-kwargs-and-args/)
  - `*args`：收集成元组
  - `**kwargs`：收集成字典
  - lambda：`lambda x: x*2`

### 💻 练习 4：JSON 解析（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex04_json_parser.py`：
  ```python
  """接收 JSON 字符串返回 dict，校验错误抛异常"""
  import json
  
  def parse_json(text: str) -> dict:
      """解析 JSON 字符串
      
      Args:
          text: JSON 字符串
      
      Returns:
          解析后的 dict
      
      Raises:
          ValueError: JSON 格式错误
      """
      if not text or not text.strip():
          raise ValueError("输入为空")
      try:
          return json.loads(text)
      except json.JSONDecodeError as e:
          raise ValueError(f"JSON 格式错误: {e}") from e
  
  # 测试
  if __name__ == "__main__":
      # 正常
      data = parse_json('{"name": "Alice", "age": 30}')
      print(f"正常: {data}")
      
      # 错误：空字符串
      try:
          parse_json("")
      except ValueError as e:
          print(f"空输入错误: {e}")
      
      # 错误：格式错误
      try:
          parse_json("not json")
      except ValueError as e:
          print(f"格式错误: {e}")
  ```
  - 跑通 3 个测试用例
  - 产出：截图

---

## 📚 关键概念

| 概念 | 例子 | 用途 |
|---|---|---|
| `def` | `def foo():` | 定义函数 |
| `return` | `return x, y` | 返回值 |
| `*args` | `def foo(*args):` | 不定长位置参数 |
| `**kwargs` | `def foo(**kwargs):` | 不定长关键字参数 |
| lambda | `lambda x: x*2` | 匿名函数 |
| docstring | 函数下三引号 | 函数说明 |

---

## ✅ 当日验收

- [ ] 练习 4 跑通，3 个测试都触发正确异常
- [ ] 能解释 `*args` 和 `**kwargs` 的区别
- [ ] 能写出一个有 docstring 的函数

---

## 💡 明日预告

**W2 D4 周四**：异常处理 + 文件读写 + 第一个 chatbot 实战