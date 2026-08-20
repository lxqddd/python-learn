# W2 D1 周一 · 2h — 基础语法 1：变量与字典

- **阶段**：1 Python 突击 | **周次**：W2 | **状态**：⬜
- **主题**：变量、数据类型、列表、字典

---

## 🎯 今日目标（3 项）

- [ ] 学变量与基础数据类型
- [ ] 学列表 / 字典 / 元组 / 集合
- [ ] 写 1 个练习（名字排序）

---

## ✅ 任务清单（2h）

### 📖 阅读（80min）

- [ ] **[40min]** 看 [Real Python: Python Basics](https://realpython.com/python-basics/) 变量 / 数字 / 字符串章节
  - 重点：f-string 格式化（`f"你好 {name}"`）

- [ ] **[40min]** 看 列表 / 字典 / 元组 / 集合 章节
  - 重点：
    - 列表：`[1, 2, 3]`，可修改
    - 元组：`(1, 2, 3)`，不可修改
    - 字典：`{"key": "value"}`，键值对
    - 集合：`{1, 2, 3}`，去重

### 💻 练习 1（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex01_sort_names.py`：
  ```python
  """接收 5 个名字，按字母排序输出"""
  names = []
  for i in range(5):
      name = input(f"输入第 {i+1} 个名字：")
      names.append(name)
  
  names.sort()
  print("\n排序后：")
  for name in names:
      print(f"- {name}")
  ```
  - 跑 3 次，输入不同的名字
  - 试一下大小写混合（`Alice` vs `bob`）
  - 产出：能跑 + 截图

---

## 📚 关键概念

| 概念 | 例子 | 注意 |
|---|---|---|
| **变量 | `name = "Alice"` | 不用声明类型 |
| **f-string | `f"你好 {name}"` | 3.6+ 才支持 |
| **列表方法 | `list.append() / sort() / pop()` | 就地修改，返回 None |
| **字典 | `d["key"] = "value"` | key 必须可哈希 |
| **集合 | `s = {1, 2, 3}` | 自动去重 |

---

## 🔗 资源链接

- [Real Python: Python Basics](https://realpython.com/python-basics/)
- [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/)

---

## 📊 进度

```
W2 D1:    [░░░░░░░░░░] 0/3
W2 整体:  [░░░░░░░░░░] 0/16
阶段 1:   [░░░░░░░░░░] 0/33
```

---

## ✅ 当日验收

- [ ] 能解释列表 vs 元组的区别
- [ ] 练习 1 跑通，输入 5 个名字按字母排序输出
- [ ] 笔记：`notes/week2/day1-dict-vs-list.md`

---

## 💡 明日预告

**W2 D2 周二**：条件 + 循环 + 练习 2/3