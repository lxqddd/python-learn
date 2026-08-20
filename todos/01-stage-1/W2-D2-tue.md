# W2 D2 周二 · 2h — 基础语法 2：条件与循环

- **阶段**：1 Python 突击 | **周次**：W2 | **状态**：⬜
- **主题**：if / for / while / 列表推导式

---

## 🎯 今日目标（3 项）

- [ ] 学 if / elif / else
- [ ] 学 for / while / `for...else`
- [ ] 写 2 个练习（词频统计 + 奇偶拆分）

---

## ✅ 任务清单（2h）

### 📖 阅读（80min）

- [ ] **[40min]** 看 [Real Python](https://realpython.com/python-basics/) 条件语句章节
  - `if` / `else` / `elif`
  - 布尔表达式：`and` / `or` / `not`
  - 三元表达式：`x if condition else y`

- [ ] **[40min]** 看循环章节
  - `for item in list:`
  - `range(start, stop, step)`
  - `for...else`（罕见但有用）
  - `while condition:`
  - 列表推导式：`[x*2 for x in range(10) if x > 5]`

### 💻 练习 2：词频统计（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex02_word_freq.py`：
  ```python
  """统计一段文字中每个词出现的次数"""
  text = """
  Python is a programming language. Python is dynamically typed.
  Python is easy to learn. Python is widely used in AI.
  """
  
  # 1. 转小写，去标点
  text = text.lower().replace(".", "").replace("\n", " ")
  words = text.split()
  
  # 2. 统计词频
  freq = {}
  for word in words:
      freq[word] = freq.get(word, 0) + 1
  
  # 3. 按频率排序输出
  for word, count in sorted(freq.items(), key=lambda x: -x[1]):
      print(f"{word}: {count}")
  ```
  - 跑通后改成自己的一段话
  - 产出：截图

### 💻 练习 3：奇偶拆分（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex03_split_odd_even.py`：
  ```python
  """把列表按奇偶拆成两个"""
  numbers = list(range(1, 21))
  
  odds = [x for x in numbers if x % 2 == 1]
  evens = [x for x in numbers if x % 2 == 0]
  
  print(f"奇数: {odds}")
  print(f"偶数: {evens}")
  ```
  - 跑通
  - 试一下用 `for...else` 重写
  - 产出：截图

---

## 📚 关键概念

| 概念 | 例子 |
|---|---|
| `if` | `if x > 0:` |
| `elif` | `elif x == 0:` |
| `for` | `for i in range(5):` |
| `while` | `while count < 3:` |
| 列表推导式 | `[x*2 for x in lst]` |
| `for...else` | `for` 没 break 才执行 else |

---

## ✅ 当日验收

- [ ] 练习 2 跑通，能统计自己输入的文本词频
- [ ] 练习 3 跑通
- [ ] 能写出 `[x*2 for x in lst if x > 0]`

---

## 💡 明日预告

**W2 D3 周三**：函数 + `*args` / `**kwargs` + lambda