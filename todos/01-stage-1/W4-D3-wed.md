# W4 D3 周三 · 2h — Pythonic 风格训练

- **阶段**：1 Python 强化 | **周次**：W4 | **状态**：⬜
- **主题**：写出"地道"的 Python 代码

---

## 🎯 今日目标（3 项）

- [ ] 掌握 7 个 Pythonic 模式
- [ ] 改写之前的练习为 Pythonic 版
- [ ] 读《流畅的Python》前 100 页

---

## ✅ 任务清单（2h）

### 📖 7 个 Pythonic 模式（50min）

- [ ] **[50min]** 学这 7 个模式（[《流畅的Python》第 1-3 章](https://www.ituring.com.cn/book/2386)）：

  **1. 列表推导式 vs map/filter**
  ```python
  # ❌ 不 Pythonic
  result = []
  for x in items:
      if x > 0:
          result.append(x * 2)
  
  # ✅ Pythonic
  result = [x * 2 for x in items if x > 0]
  ```

  **2. 生成器表达式（省内存）**
  ```python
  # ❌ 占内存
  total = sum([x*2 for x in range(10**8)])
  
  # ✅ 流式
  total = sum(x*2 for x in range(10**8))
  ```

  **3. enumerate 而不是手动计数**
  ```python
  # ❌
  for i in range(len(items)):
      print(i, items[i])
  
  # ✅
  for i, item in enumerate(items):
      print(i, item)
  ```

  **4. zip 并行迭代**
  ```python
  # ✅
  for name, age in zip(names, ages):
      print(f"{name}: {age}")
  ```

  **5. 上下文管理器（with）**
  ```python
  # ❌ 容易忘关
  f = open("file.txt")
  data = f.read()
  f.close()
  
  # ✅ 自动关
  with open("file.txt") as f:
      data = f.read()
  ```

  **6. collections.defaultdict**
  ```python
  # ❌ 繁琐
  d = {}
  for k, v in pairs:
      if k not in d:
          d[k] = []
      d[k].append(v)
  
  # ✅
  from collections import defaultdict
  d = defaultdict(list)
  for k, v in pairs:
      d[k].append(v)
  ```

  **7. dataclass 替代 tuple**
  ```python
  # ❌ 可读性差
  point = (1, 2)
  x, y = point
  
  # ✅
  from dataclasses import dataclass
  
  @dataclass
  class Point:
      x: int
      y: int
  
  p = Point(1, 2)
  print(p.x, p.y)
  ```

### 💻 改写练习（60min）

- [ ] **[60min]** 把 W2-W3 的 5 个练习改写为 Pythonic 版本：

  - `ex01_sort_names.py` → 用 `sorted()` 而非 `.sort()`
  - `ex02_word_freq.py` → 用 `Counter` 替代手动计数
  - `ex03_split_odd_even.py` → 用 `filter` + 推导式
  - `ex04_json_parser.py` → 用 `dataclass` 替代字典
  - `ex05_csv_to_json.py` → 用 `defaultdict` 聚合

### 📚 读书（10min）

- [ ] **[10min]** 读《流畅的Python》第 1 章 1-2 节（理解 Python 数据模型）

---

## 📚 Pythonic 风格核心原则

| 原则 | 体现 |
|---|---|
| **简洁胜于复杂** | 推导式、生成器 |
| **可读性第一** | `enumerate`、`zip` |
| **显式胜于隐式** | `with`、`dataclass` |
| **扁平胜于嵌套** | 早 return |

---

## ✅ 当日验收

- [ ] 7 个模式都能讲出来
- [ ] 5 个练习改写完
- [ ] 《流畅的Python》第 1 章读了一部分

---

## 💡 明日预告

**W4 D4 周四**：读 LangChain 源码 + 写笔记