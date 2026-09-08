# 🐍 Python 零基础前置路线 · 通往 Agent 工程师

> **你的画像**：每天 1.5-2h · 完全零 Python 基础 · 目标 Agent 开发
> **总投入**：6 周 × 5 天 × 2h = 60h（前置路线）
> **方法论**：做出什么 > 学过什么（与主路线一致，源自 AgentGuide）
>
> **文档定位**：本路线是 [`learning-roadmap.md`](learning-roadmap.md) 的**前置补丁**。
> 完整版路线 W2-W4 的「Python 强化」阶段假设你已会基础语法；本路线从零开始，**用 6 周把那个前提补齐**。
> 完成本路线后，从完整版路线的 **W5（First 7 Days Sprint）** 继续。
>
> **v1 · 6 周完整版**

---

## 📌 三个最重要的原则

> ⚠️ **本路线是核心路线**——所有内容都是 P0，不可跳过。

1. **看 ≠ 会**：每个知识点学完必须**亲手写**30 行以上代码用起来。无输出 = 没学。
2. **报错 = 朋友**：不要 AI 一路帮你 debug，自己读报错 30 分钟再问。
3. **每天 commit**：每天至少 1 次 git commit，养成习惯是工程师的基本素养。

---

## 🗺 6 周全景图

```
Week  1 ━━ 阶段 A1：基础语法（变量/循环/函数）
Week  2 ━━ 阶段 A2：文件 + 异常 + 模块 + 第一个 CLI 项目
Week  3 ━━ 阶段 B1：类与对象 + 装饰器 + pydantic
Week  4 ━━ 阶段 B2：async/await + 现代 Python + 第一个 LLM 调用
Week  5 ━━ 阶段 C1：venv + pytest + logging + Git 工程化
Week  6 ━━ 阶段 C2：流式对话 + tool calling + 第一个 Agent 雏形
       ↓
  衔接主路线 W5：First 7 Days Sprint（200 行手写最小 Agent）
```

| 阶段 | 周 | 总时长 | 核心产出 | 阶段验收标准 |
|---|---|---|---|---|
| A · 入门语法 | W1-W2 | 20h | 9 个练习 + 1 个 TODO CLI | 不看资料写 BMI 计算器 + 猜数字 |
| B · 进阶语法 | W3-W4 | 20h | 5 个练习 + 1 个 LLM chat | 能用 dataclass/pydantic/async |
| C · 工程能力 | W5-W6 | 20h | 1 个重构项目 + 1 个 weather bot | venv/pytest/logging/Git 全会 |
| **总计** | **6 周** | **60h** | **能调通 LLM API + 第一个 tool calling** | **进入主路线 W5 的能力门槛** |

---

## ⏰ 每日 2h 时间分配模板

```
┌──────────────────────────────────────────────────────┐
│ 每日 2h 标准分配（不可调整）                         │
├──────────────────────────────────────────────────────┤
│  0-20 min  昨日复盘（10 min）+ 今日计划（10 min）    │
│ 20-50 min  概念输入（看视频/文档，30 min）           │
│ 50-110 min 动手实战（写代码/做练习/调试，60 min）    │
│ 110-120min 当日笔记（5 行）+ git commit（10 min）    │
└──────────────────────────────────────────────────────┘
```

**核心比例**：15% 复盘 + 25% 输入 + 50% 实战 + 10% 记录。
**核心原则**：**只看不练 = 没学**。

---

## 📦 阶段 A · 入门语法（W1-W2 · 20h）

> **目标**：能独立写 50 行内的小脚本（输入 → 处理 → 输出）
> **关键产出**：9 个 `sandbox/ex*.py` 练习 + `01-todo-cli/` 项目

### 阶段 A · Python 内功清单（Agent 开发相关度）

| 知识点 | Agent 相关度 | 阶段 |
|---|---|---|
| 变量/数据类型/f-string | 🔴 P0 | W1 |
| 列表/字典/元组/集合 | 🔴 P0 | W1 |
| 条件/循环 | 🔴 P0 | W1 |
| 函数 + `*args` / `**kwargs` | 🔴 P0 | W1 |
| 文件读写 + `with` | 🔴 P0 | W2 |
| `try/except/finally` | 🔴 P0 | W2 |
| `import` / `pip` | 🔴 P0 | W2 |
| 列表推导式 / `enumerate` / `zip` | 🟡 P1 | W2 |

---

### W1 · D1（周一 · 2h）— 环境 + 第一个程序

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 装 Python 3.11+（[官网](https://www.python.org/downloads/)）| `python3 --version` 能输出 3.11+ |
| 30-60 min | 装 VS Code（[官网](https://code.visualstudio.com/)）+ 装 Python 扩展 | VS Code 能高亮 Python 代码 |
| 60-90 min | 在桌面建文件夹 `agent-learning/`，用 VS Code 打开 | 文件夹结构就绪 |
| 90-110 min | 写 `hello.py`：`print("你好 Python")` + `name = input("你叫什么？")` + `print(f"你好 {name}")` | 能交互输入名字 |
| 110-120 min | 终端 `git init` + 第一次 commit：`feat: hello python` | Git 仓库初始化 |

**验收**：
- [ ] `python3 --version` 输出 ≥ 3.11
- [ ] VS Code 能高亮 + 自动补全
- [ ] `hello.py` 能问名字并打印回复
- [ ] Git 第一次 commit 成功

**环境配置参考**：
```bash
# macOS / Linux
python3 --version   # 检查
which python3

# 如果版本低，用 pyenv 或 brew 装新版
brew install python@3.11

# 或者直接用 uv（推荐，10x 更快）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.11
```

---

### W1 · D2（周二 · 2h）— 变量与数据类型

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学变量命名规则、4 种数据类型（int/str/float/bool） | 笔记 `notes/week1/day2-variables.md` |
| 30-50 min | 学 f-string 格式化（`f"你好 {name}"`） | 笔记 1 页 |
| 50-110 min | 练习 1：BMI 计算器（输入身高体重 → 输出 BMI 值 + 偏胖/正常/偏瘦） | `sandbox/ex01_bmi.py` |
| 110-120 min | git commit | commit 记录 |

**练习 1 模板**（不要直接抄，自己写）：
```python
# 输入身高(米)和体重(公斤)
# 计算 BMI = 体重 / 身高²
# 输出分类
height = float(input("身高(米): "))
weight = float(input("体重(公斤): "))
bmi = weight / (height ** 2)
print(f"你的 BMI: {bmi:.1f}")
# if bmi < 18.5: 偏瘦
# 18.5-24: 正常
# 24-28: 偏胖
# >28: 肥胖
```

**验收**：
- [ ] 输入 1.75 / 70 → 输出 BMI 22.9 + 分类"正常"
- [ ] 能解释 int / str / float / bool 区别

---

### W1 · D3（周三 · 2h）— 容器类型

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学列表（`[]`）基本操作：增删改查、`len()`、`in` | 笔记 |
| 30-50 min | 学字典（`{}`）：键值对、`dict["key"]`、`dict.get()` | 笔记 |
| 50-80 min | 学元组（`()`）和集合（`set()`）的区别 | 笔记 |
| 80-110 min | 练习 2 + 3：5 个名字排序 / 一段文字词频统计 | `ex02_sort.py` `ex03_wordcount.py` |
| 110-120 min | git commit | commit |

**练习 2 参考**（独立写）：
```python
# 输入 5 个名字，按字母排序输出
names = []
for i in range(5):
    name = input(f"第 {i+1} 个名字: ")
    names.append(name)
print("排序后:", sorted(names))
```

**练习 3 参考**：
```python
# 统计一段文字里每个词出现次数
text = "python is great python is dynamic python is popular"
words = text.split()
counter = {}
for w in words:
    counter[w] = counter.get(w, 0) + 1
print(counter)
```

**验收**：
- [ ] 能说出 list / dict / tuple / set 各自的使用场景
- [ ] 练习 2 输入 5 个名字能正确排序输出
- [ ] 练习 3 词频统计正确

---

### W1 · D4（周四 · 2h）— 条件 + 循环

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 `if/elif/else` 嵌套 + 比较运算符 | 笔记 |
| 30-50 min | 学 `for` 循环 + `range()` + `for...else`（else 是循环没被 break 时执行） | 笔记 |
| 50-80 min | 学 `while` 循环 + `break` / `continue` | 笔记 |
| 80-110 min | 练习 4：猜数字游戏（1-100，猜错给大小提示，最多 7 次） | `ex04_guess.py` |
| 110-120 min | git commit | commit |

**练习 4 参考**（独立写）：
```python
import random
target = random.randint(1, 100)
for attempt in range(7):
    guess = int(input(f"第 {attempt+1} 次猜 (1-100): "))
    if guess == target:
        print(f"🎉 答对了！{attempt+1} 次")
        break
    elif guess < target:
        print("再大一点")
    else:
        print("再小一点")
else:
    print(f"💀 游戏结束，正确答案是 {target}")
```

**验收**：
- [ ] 猜数字游戏能跑通且 7 次内必须结束
- [ ] 能解释 `for...else` 中 else 何时执行

---

### W1 · D5（周五 · 2h）— 函数

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 `def` / `return` / 参数 / 默认值 | 笔记 |
| 30-50 min | 学 `*args`（变长位置参数）+ `**kwargs`（变长关键字参数）| 笔记 |
| 50-70 min | 学 `lambda` 表达式（一行小函数） | 笔记 |
| 70-110 min | 练习 5：写一个 `average(scores)` 函数，接收数字列表返回平均分 | `ex05_avg.py` |
| 110-120 min | 写 `notes/week1/summary.md` 本周总结 + git commit | commit |

**练习 5**：
```python
def average(scores: list[float]) -> float:
    """返回平均分，列表为空返回 0"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

# 测试
print(average([90, 80, 70]))    # 80.0
print(average([]))              # 0
```

**验收**：
- [ ] 能解释 `*args` 和 `**kwargs` 区别
- [ ] 练习 5 跑通 + 用 type hint
- [ ] `notes/week1/` 至少 3 篇笔记

---

### ✅ W1 周日验收

**知识**（不看书回答）：
- [ ] int / str / float / bool 各自的字面量写法？
- [ ] list / tuple / dict / set 各自什么时候用？
- [ ] `for...else` 的 else 什么时候执行？
- [ ] `*args` 和 `**kwargs` 区别？
- [ ] f-string 怎么在字符串里嵌入变量？

**实践**：
- [ ] `ex01_bmi.py` 跑通
- [ ] `ex02_sort.py` / `ex03_wordcount.py` 跑通
- [ ] `ex04_guess.py` 跑通（猜数字游戏）
- [ ] `ex05_avg.py` 跑通（带 type hint）
- [ ] 至少 3 篇 `notes/week1/*.md` 笔记
- [ ] 至少 3 次 git commit

---

### W2 · D1（周一 · 2h）— 文件读写

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 `open()` + `read()` / `readlines()` / `write()` | 笔记 |
| 30-50 min | 学 `with open(...) as f:`（上下文管理器，自动关文件） | 笔记 |
| 50-80 min | 学 `pathlib.Path`（`Path("notes") / "week1.txt"`）| 笔记 |
| 80-110 min | 练习 6：读 `notes.txt` → 统计行数 → 写到 `output.txt` | `ex06_file.py` |
| 110-120 min | git commit | commit |

**练习 6**：
```python
from pathlib import Path

src = Path("notes.txt")
dst = Path("output.txt")

with src.open("r", encoding="utf-8") as f:
    lines = f.readlines()

with dst.open("w", encoding="utf-8") as f:
    f.write(f"共 {len(lines)} 行\n")
    for i, line in enumerate(lines, 1):
        f.write(f"{i}: {line}")
```

**验收**：
- [ ] 能说出为什么用 `with` 而不是手动 `open/close`
- [ ] `ex06_file.py` 跑通，能写入统计结果

---

### W2 · D2（周二 · 2h）— 异常处理

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学常见异常：`ValueError` / `TypeError` / `KeyError` / `FileNotFoundError` | 笔记 |
| 30-50 min | 学 `try/except/finally` + `raise` 主动抛异常 | 笔记 |
| 50-110 min | 练习 7：写一个"健壮的输入函数" `safe_input_int()`，输入非法时不崩溃 | `ex07_safe_input.py` |
| 110-120 min | git commit | commit |

**练习 7**：
```python
def safe_input_int(prompt: str) -> int:
    """反复询问直到用户输入合法整数"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️  请输入整数")

# 测试
age = safe_input_int("年龄: ")
print(f"你 {age} 岁")
```

**验收**：
- [ ] 能说出 5 种常见异常名字
- [ ] `ex07_safe_input.py` 输入 "abc" 不崩溃

---

### W2 · D3（周三 · 2h）— 模块与第三方包

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 `import` 语句 + `from ... import ...` + `as` 别名 | 笔记 |
| 30-50 min | 学 `pip install` + `requirements.txt` | 笔记 |
| 50-80 min | 装 `requests`：`pip install requests` | 包就绪 |
| 80-110 min | 练习 8：用 `requests.get()` 拿 [JSONPlaceholder](https://jsonplaceholder.typicode.com/todos/1) 的 JSON | `ex08_api.py` |
| 110-120 min | git commit | commit |

**练习 8**：
```python
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
resp.raise_for_status()
data = resp.json()
print(f"标题: {data['title']}")
print(f"完成: {data['completed']}")
```

**验收**：
- [ ] 知道 `import module` 和 `from module import func` 区别
- [ ] `requests` 装好
- [ ] `ex08_api.py` 能输出 JSONPlaceholder 返回的标题

---

### W2 · D4（周四 · 2h）— Pythonic 风格入门

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学列表推导式 `[x*2 for x in nums if x > 0]` | 笔记 |
| 0-40 min | 学字典推导式 `{k: v for k, v in items}` | 笔记 |
| 40-60 min | 学 `enumerate()`（带索引的循环）+ `zip()`（并行遍历）| 笔记 |
| 60-110 min | 练习 9：把 W1 D3 的练习 3 改成 1 行推导式 | `ex09_pythonic.py` |
| 110-120 min | git commit | commit |

**练习 9**：
```python
text = "python is great python is dynamic python is popular"

# 旧写法（你之前写的）
words = text.split()
counter = {}
for w in words:
    counter[w] = counter.get(w, 0) + 1

# 改写成 1 行
counter = {w: text.split().count(w) for w in set(text.split())}
print(counter)
```

**验收**：
- [ ] 能写出至少 3 种推导式（list / dict / set）
- [ ] 能用 `enumerate` 替代 `range(len(x))`

---

### W2 · D5（周五 · 4h）— 综合项目 TODO CLI

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 设计：5 个命令（add / list / done / remove / save）| 设计草稿 `notes/week2/day5-todo-design.md` |
| 30-180 min | 实现：~80 行 Python，`todo.json` 存数据 | `sandbox/tiny-projects/01-todo-cli/todo.py` |
| 180-210 min | 写 3+ 条测试：加任务 / 列任务 / 删任务 | `tests/test_todo.py` |
| 210-230 min | 写 README（怎么跑、怎么测） | `README.md` |
| 230-240 min | git commit：`feat(todo-cli): MVP with file persistence` | commit |

**项目骨架**：
```python
import json
from pathlib import Path
import sys

DATA = Path(__file__).parent / "todo.json"

def load() -> list[dict]:
    if DATA.exists():
        return json.loads(DATA.read_text(encoding="utf-8"))
    return []

def save(todos: list[dict]) -> None:
    DATA.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")

def add(task: str) -> None:
    todos = load()
    todos.append({"task": task, "done": False})
    save(todos)

def list_tasks() -> None:
    for i, t in enumerate(load(), 1):
        mark = "✅" if t["done"] else "⬜"
        print(f"{i}. {mark} {t['task']}")

# 类似实现 done / remove ...
# CLI 入口（if __name__ == "__main__"）
```

**验收**：
- [ ] TODO CLI 能加任务、列任务、删任务
- [ ] **关掉重开数据还在**（用 `todo.json` 持久化）
- [ ] 至少 3 条测试跑通
- [ ] README 完整

---

### ✅ W2 周日验收 · 阶段 A 毕业

**知识**：
- [ ] `with open` 相对手动 `open/close` 的优势？
- [ ] `try/except` 的执行流程？`finally` 何时执行？
- [ ] 至少 3 种推导式的语法？
- [ ] `pathlib.Path` 比 `os.path` 好在哪？

**实践**：
- [ ] `ex06-ex09` 4 个练习跑通
- [ ] `01-todo-cli/` 端到端跑通 + 至少 3 条测试
- [ ] 累计 git commit ≥ 8 次
- [ ] `notes/week1/` + `notes/week2/` 笔记共 ≥ 6 篇

---

## 📦 阶段 B · 进阶语法（W3-W4 · 20h）

> **目标**：能写 200 行模块化程序，会用 dataclass / pydantic / async
> **关键产出**：5 个练习 + `02-llm-chat/` 项目（首次调用 DeepSeek API）

### 阶段 B · Python 内功清单（Agent 开发关键）

| 知识点 | Agent 相关度 | 阶段 |
|---|---|---|
| `class` / `__init__` / `self` | 🔴 P0（Agent 主循环都是类） | W3 |
| `@dataclass` | 🔴 P0（Agent schema 基础） | W3 |
| 装饰器 `@decorator` | 🔴 P0（LangChain 全是装饰器） | W3 |
| `pydantic.BaseModel` | 🔴 P0（Agent 数据校验标配） | W3 |
| 类型提示 `def foo(x: int) -> str` | 🔴 P0 | W3 |
| `async/await` | 🔴 P0（Agent 全异步） | W4 |
| `asyncio.gather` | 🟡 P1（并发调用） | W4 |
| 上下文管理器 `@contextmanager` | 🟡 P1 | W4 |
| 生成器 `yield` | 🟡 P1 | W4 |
| `pathlib` | 🟡 P1 | W4 |

---

### W3 · D1（周一 · 2h）— 类与对象

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 `class` / `__init__` / `self` / 实例方法 | 笔记 |
| 30-50 min | 学属性 vs 实例属性的区别 | 笔记 |
| 50-110 min | 练习 10：把 W2 TODO CLI 重写为 `TodoList` 类（`add / list / done / remove` 都是方法）| `ex10_todo_class.py` |
| 110-120 min | git commit | commit |

**练习 10 骨架**：
```python
class TodoList:
    def __init__(self, data_file: Path):
        self.data_file = data_file
        self.todos = self._load()

    def _load(self) -> list[dict]:
        ...

    def _save(self) -> None:
        ...

    def add(self, task: str) -> None:
        ...

    def list(self) -> list[dict]:
        return self.todos

    def done(self, index: int) -> None:
        ...

    def remove(self, index: int) -> None:
        ...
```

**验收**：
- [ ] 能解释 `self` 是什么
- [ ] `TodoList` 类版 CLI 跑通

---

### W3 · D2（周二 · 2h）— 继承

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学继承语法 `class Dog(Animal)` + `super().__init__()` | 笔记 |
| 40-60 min | 学方法重写（override） | 笔记 |
| 60-110 min | 练习 11：写 `Animal` → `Dog` / `Cat`（重写 `speak()` 方法）| `ex11_inherit.py` |
| 110-120 min | git commit | commit |

**练习 11**：
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "汪汪"

class Cat(Animal):
    def speak(self) -> str:
        return "喵喵"

animals = [Dog("旺财"), Cat("小花")]
for a in animals:
    print(f"{a.name}: {a.speak()}")
```

**验收**：
- [ ] 能解释继承的意义（代码复用）
- [ ] `Dog` / `Cat` 重写 `speak()` 输出不同

---

### W3 · D3（周三 · 2h）— `@dataclass`（Agent 必备）

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `@dataclass` 自动生成 `__init__` / `__repr__` / `__eq__` | 笔记 |
| 40-60 min | 学 `@dataclass(frozen=True)`（不可变）和 `field(default_factory=...)` | 笔记 |
| 60-110 min | 练习 12：把 `TodoList` 里的 todo 字典改成 `@dataclass class Todo` | `ex12_dataclass.py` |
| 110-120 min | git commit | commit |

**练习 12**：
```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Todo:
    task: str
    done: bool = False
    created_at: datetime = field(default_factory=datetime.now)

todo = Todo("学 Python")
print(todo)
print(todo.done)

todo.done = True
print(todo)
```

**验收**：
- [ ] 能口述 `@dataclass` 相对手写 `__init__` 的优势
- [ ] `Todo` dataclass 跑通

---

### W3 · D4（周四 · 2h）— 装饰器（Agent 工程师必懂）

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学装饰器本质：函数嵌套 + 返回函数 | 笔记 |
| 40-60 min | 学 `@functools.wraps`（保留原函数信息）| 笔记 |
| 60-110 min | 练习 13：写一个"计时装饰器" `@timer`，打印函数执行耗时 | `ex13_timer.py` |
| 110-120 min | git commit | commit |

**练习 13**：
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️  {func.__name__} 耗时 {elapsed:.3f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(1)
    return "done"

print(slow())
```

**验收**：
- [ ] 能说出装饰器本质（函数嵌套 + 返回函数）
- [ ] `@timer` 能正确打印耗时

---

### W3 · D5（周五 · 2h）— 类型提示 + pydantic 入门

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学类型提示语法：`def foo(x: int) -> str` + `Optional[str]` + `list[int]` | 笔记 |
| 40-60 min | 装 `pydantic`：`pip install pydantic` | 包就绪 |
| 60-110 min | 练习 14：用 pydantic 定义 `User` 模型（id / email / age），故意传错 age=200 看错误信息 | `ex14_pydantic.py` |
| 110-120 min | 写 `notes/week3/summary.md` + git commit | commit |

**练习 14**：
```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    email: EmailStr
    age: int = Field(ge=0, le=150)  # 必须在 0-150 之间

# 合法
u = User(id=1, email="a@b.com", age=30)
print(u)

# 非法：age 太大
try:
    bad = User(id=2, email="c@d.com", age=200)
except Exception as e:
    print(f"❌ 校验失败: {e}")
```

**验收**：
- [ ] 能口述"类型提示 + pydantic 在 Agent 开发里为什么是标配"
- [ ] `User` 模型能正确拒绝 `age=200`

---

### ✅ W3 周日验收

**知识**：
- [ ] 类 vs dataclass 什么时候用哪个？
- [ ] 装饰器的本质是什么？`@wraps` 干嘛用？
- [ ] pydantic 相对手写校验的优势？

**实践**：
- [ ] `ex10-ex14` 5 个练习跑通
- [ ] 累计 git commit ≥ 12 次
- [ ] `notes/week3/` 至少 3 篇笔记

---

### W4 · D1（周一 · 2h）— `async/await` 基础

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学协程概念 + `async def` / `await` 语法 | 笔记 |
| 40-60 min | 学 `asyncio.run()` 启动异步函数 | 笔记 |
| 60-110 min | 练习 15：写 `async def fetch(url)` 用 `await asyncio.sleep(1)` 模拟延迟 | `ex15_async.py` |
| 110-120 min | git commit | commit |

**练习 15**：
```python
import asyncio

async def fetch(url: str) -> str:
    print(f"开始下载 {url}")
    await asyncio.sleep(1)  # 模拟网络延迟
    return f"{url} 的内容"

async def main():
    result = await fetch("https://example.com")
    print(result)

asyncio.run(main())
```

**验收**：
- [ ] 能解释 `async` 和普通函数的区别
- [ ] `fetch()` 能正确 await

---

### W4 · D2（周二 · 2h）— `asyncio.gather` 并发

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `asyncio.gather` 并发执行多个协程 | 笔记 |
| 40-60 min | 学 `asyncio.create_task` 创建任务 | 笔记 |
| 60-110 min | 练习 16：并发"下载"3 个 URL，对比串行总耗时 | `ex16_concurrent.py` |
| 110-120 min | git commit | commit |

**练习 16**：
```python
import asyncio
import time

async def fetch(url: str) -> str:
    await asyncio.sleep(1)
    return f"{url} done"

async def main():
    urls = [f"https://api.example.com/{i}" for i in range(3)]

    # 串行
    start = time.perf_counter()
    for u in urls:
        await fetch(u)
    print(f"串行耗时: {time.perf_counter() - start:.2f}s")

    # 并发
    start = time.perf_counter()
    results = await asyncio.gather(*[fetch(u) for u in urls])
    print(f"并发耗时: {time.perf_counter() - start:.2f}s")
    print(results)

asyncio.run(main())
```

**验收**：
- [ ] 串行 3s，并发 ≈1s（节省 2/3 时间）
- [ ] 能解释 `gather` 的并行原理

---

### W4 · D3（周三 · 2h）— 上下文管理器 + 生成器

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `@contextmanager` 装饰器自定义上下文管理器 | 笔记 |
| 40-70 min | 学生成器 `yield`（惰性求值）+ `next()` | 笔记 |
| 70-110 min | 练习 17：写一个"计时上下文管理器" + 用生成器逐行读大文件 | `ex17_context.py` |
| 110-120 min | git commit | commit |

**练习 17**：
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name: str):
    start = time.perf_counter()
    yield
    print(f"⏱️  {name}: {time.perf_counter() - start:.3f}s")

# 使用
with timer("读取大文件"):
    with open("big.txt") as f:
        for line in f:
            process(line)

# 生成器
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line
```

**验收**：
- [ ] `@contextmanager` 自定义计时器跑通
- [ ] 生成器逐行读大文件跑通

---

### W4 · D4（周四 · 2h）— `pathlib` + 现代 Python 杂项

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `pathlib.Path` 的常用方法（`read_text` / `glob` / `mkdir`）| 笔记 |
| 40-70 min | 学 `Counter`（`collections`）词频统计、`defaultdict` | 笔记 |
| 70-110 min | 练习 18：用 pathlib 批量重命名（`Path.glob` 找所有 `.txt`）| `ex18_pathlib.py` |
| 110-120 min | git commit | commit |

**练习 18**：
```python
from pathlib import Path
from collections import Counter

# 批量重命名：把 test/ 下所有 .txt 加 .bak 后缀
for f in Path("test").glob("*.txt"):
    new = f.with_suffix(".txt.bak")
    f.rename(new)
    print(f"{f.name} → {new.name}")

# Counter 词频
text = "python is great python is dynamic python"
print(Counter(text.split()))
```

**验收**：
- [ ] `pathlib.glob` 能找到所有 txt 文件
- [ ] `Counter` 词频统计正确

---

### W4 · D5（周五 · 4h）— 综合项目：第一个 LLM 对话

> 🎯 **本路线第一个里程碑**：用 DeepSeek API 跟 AI 对话

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 注册 DeepSeek 开放平台 → 充值 10 元 → 拿 API Key | Key 保存到 `.env` |
| 30-60 min | 装 `openai` SDK：`pip install openai`（DeepSeek 兼容 OpenAI 协议） | 包就绪 |
| 60-180 min | 写 `chat.py`：循环输入 → 调 API → 打印回复 | `sandbox/tiny-projects/02-llm-chat/chat.py` |
| 180-210 min | 加错误处理：超时 / 网络异常 / API 限流 | 加 try/except |
| 210-240 min | 加 `.env` + `.gitignore`（**Key 不能 commit**）+ README + git commit | commit |

**项目骨架**：
```python
# sandbox/tiny-projects/02-llm-chat/chat.py
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

async def chat(user_msg: str) -> str:
    resp = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_msg}]
    )
    return resp.choices[0].message.content

async def main():
    print("🤖 DeepSeek 对话 (输入 quit 退出)")
    while True:
        msg = input("你: ").strip()
        if msg == "quit":
            break
        try:
            reply = await chat(msg)
            print(f"AI: {reply}\n")
        except Exception as e:
            print(f"❌ 出错了: {e}\n")

asyncio.run(main())
```

```bash
# .env（不 commit）
DEEPSEEK_API_KEY=sk-xxxxxx

# .gitignore
.env
```

**验收**：
- [ ] 输入"你好"能收到 AI 回复
- [ ] 网络断了不崩溃（try/except 兜底）
- [ ] `.env` 已加入 `.gitignore`（**Key 没 commit**）
- [ ] README 写清楚怎么配 Key 怎么跑

---

### ✅ W4 周日验收 · 阶段 B 毕业

**知识**：
- [ ] `async/await` 相对同步函数的核心区别？
- [ ] `asyncio.gather` 怎么并发？
- [ ] 上下文管理器解决什么问题？
- [ ] pydantic 在 Agent 开发里的核心作用？

**实践**：
- [ ] `ex15-ex18` 4 个练习跑通
- [ ] `02-llm-chat/` 能跟 DeepSeek 对话
- [ ] 累计 git commit ≥ 17 次
- [ ] `notes/week4/` 至少 3 篇笔记

---

## 📦 阶段 C · 工程能力（W5-W6 · 20h）

> **目标**：能写可维护、可测试、可部署的 Python 项目
> **关键产出**：1 个重构项目 + 1 个 weather bot

### 阶段 C · Python 内功清单（Agent 工程化）

| 知识点 | Agent 相关度 | 阶段 |
|---|---|---|
| 虚拟环境 `venv` / `uv` | 🔴 P0（隔离依赖） | W5 |
| `requirements.txt` | 🔴 P0 | W5 |
| `logging` / `structlog` | 🔴 P0（Agent 可观测） | W5 |
| `pytest` 基础 | 🔴 P0（测 Agent 必须） | W5 |
| `unittest.mock` | 🔴 P0（mock LLM response） | W5 |
| Git 进阶（branch / log / diff） | 🔴 P0 | W5 |
| 流式 API（`stream=True`） | 🟡 P1（Agent 必备体验） | W6 |
| 多轮对话（维护 history） | 🟡 P1 | W6 |
| `tool calling`（让 LLM 调函数） | 🔴 P0 | W6 |

---

### W5 · D1（周一 · 2h）— 虚拟环境 + 包管理

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `python3 -m venv .venv` + `source .venv/bin/activate` | `.venv/` 目录就绪 |
| 40-70 min | 学 `uv pip install`（比 pip 快 10x）或 `pip install -r requirements.txt` | requirements.txt 就绪 |
| 70-110 min | 把 `02-llm-chat/` 加 `.venv` + `requirements.txt`（`openai` / `python-dotenv`）| 项目能干净装 |
| 110-120 min | git commit（**`.venv/` 不 commit**，加 `.gitignore`）| commit |

**验收**：
- [ ] 能口述"为什么用 venv 而不是全局 pip"
- [ ] 删除 `.venv` 后能按 `requirements.txt` 重装

---

### W5 · D2（周二 · 2h）— `logging` 日志

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `logging` 模块：`basicConfig` + `getLogger` + 5 个级别 | 笔记 |
| 40-70 min | 学 `structlog`：`pip install structlog` | 包就绪 |
| 70-110 min | 把 `02-llm-chat/` 的 `print` 全部换成 logger | 日志格式规范 |
| 110-120 min | git commit | commit |

**练习**：
```python
import logging
import structlog

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = structlog.get_logger()

log.info("chat.start", user_input="你好")
log.warning("api.timeout", retry_count=2)
log.error("api.failed", error="network unreachable")
```

**验收**：
- [ ] 能解释 INFO / WARNING / ERROR 各自的使用场景
- [ ] `02-llm-chat` 输出带时间戳的日志

---

### W5 · D3（周三 · 2h）— pytest 测试

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 `pytest` 基础：`def test_xxx()` + `assert` | 笔记 |
| 40-70 min | 学 `pytest.fixture`（共享测试数据）| 笔记 |
| 70-100 min | 给 `02-llm-chat/` 写 5 条测试（不调真实 API） | `tests/test_chat.py` |
| 100-110 min | 用 `unittest.mock` mock OpenAI client | mock 跑通 |
| 110-120 min | git commit | commit |

**测试模板**：
```python
# tests/test_chat.py
import pytest
from unittest.mock import AsyncMock, patch
from chat import chat

@pytest.mark.asyncio
async def test_chat_returns_ai_reply():
    mock_resp = AsyncMock()
    mock_resp.choices = [AsyncMock()]
    mock_resp.choices[0].message.content = "你好！我是 AI"

    with patch("chat.client.chat.completions.create", return_value=mock_resp):
        reply = await chat("你好")
        assert "AI" in reply

def test_chat_handles_empty_input():
    # 边界测试
    ...
```

**验收**：
- [ ] 至少 5 条测试跑通
- [ ] 测试**不调真实 API**（用 mock）
- [ ] 覆盖率 > 60%

---

### W5 · D4（周四 · 2h）— Git 进阶

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 `git branch` / `git checkout -b` / `git merge` | 笔记 |
| 30-60 min | 学 `git log --oneline --graph` 看历史 | 笔记 |
| 60-90 min | 学 `git diff` / `git stash` | 笔记 |
| 90-110 min | 实战：建 feature branch `feat/logging` → 改代码 → commit → merge 回 main | 走完一遍 |
| 110-120 min | git commit + 写 notes/week5/d4-git.md | commit |

**验收**：
- [ ] 能用 branch 隔离实验性改动
- [ ] 能用 `git log --oneline --graph` 看合并历史

---

### W5 · D5（周五 · 4h）— 综合项目：标准结构重构

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 设计标准项目结构：`src/` `tests/` `pyproject.toml` `README.md` `.env.example` | 设计图 |
| 30-150 min | 把 `02-llm-chat/` 重构为 `03-llm-chat-pro/`：拆分为 `src/client.py` `src/chat.py` `src/config.py` | 项目结构规范 |
| 150-180 min | 加 `pyproject.toml` + `.env.example`（模板，不含真 key） | 配置规范 |
| 180-210 min | 写 5+ 条测试覆盖主路径 | 测试完整 |
| 210-230 min | 写 README（功能 / 安装 / 配置 / 使用 / 测试 5 段）| README 完整 |
| 230-240 min | git commit：`refactor: standard project layout` | commit |

**项目结构**：
```
03-llm-chat-pro/
├── src/
│   ├── __init__.py
│   ├── config.py        # 读 .env
│   ├── client.py        # OpenAI client 封装
│   └── chat.py          # 对话逻辑
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   └── test_chat.py
├── .env.example         # 模板
├── .gitignore           # 忽略 .venv .env __pycache__
├── pyproject.toml       # 项目元数据 + 依赖
└── README.md
```

**验收**：
- [ ] 新 clone 的人按 README 30 分钟内能跑起来
- [ ] `pyproject.toml` + `.env.example` 完整
- [ ] 测试覆盖主路径

---

### ✅ W5 周日验收

**知识**：
- [ ] venv 的隔离作用？
- [ ] `INFO / WARNING / ERROR` 区别？
- [ ] 为什么测 Agent 必须 mock？
- [ ] `.env` 为什么必须加 `.gitignore`？

**实践**：
- [ ] `03-llm-chat-pro/` 标准结构跑通
- [ ] 5+ 条 pytest 跑通 + mock 真实 API
- [ ] 累计 git commit ≥ 22 次
- [ ] `notes/week5/` 至少 3 篇笔记

---

### W6 · D1（周一 · 2h）— Agent 概念入门

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 读 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 3 句话总结 |
| 40-80 min | 读 [`docs/concept-notes.md`](concept-notes.md) 抄写 5 级能力模型（L0-L5） | 笔记 |
| 80-110 min | 写 `notes/week6/day1-agent-concept.md`：chatbot vs workflow vs agent vs multi-agent 区别 | 笔记 |
| 110-120 min | git commit | commit |

**验收**：
- [ ] 能口述 4 个概念的区别
- [ ] 能列出 L0-L5 能力模型

---

### W6 · D2（周二 · 2h）— 流式对话

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 OpenAI SDK 的 `stream=True` 参数 | 笔记 |
| 40-110 min | 改 `03-llm-chat-pro/`：用 `async for chunk in stream` 实现打字机输出 | `sandbox/03-stream-chat/` |
| 110-120 min | git commit | commit |

**练习**：
```python
async def stream_chat(user_msg: str):
    stream = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_msg}],
        stream=True
    )
    print("AI: ", end="", flush=True)
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()
```

**验收**：
- [ ] 流式输出能看到一个字一个字出来
- [ ] 不再等 AI 全部生成完才显示

---

### W6 · D3（周三 · 2h）— 多轮对话

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 学 messages 列表结构（`[{"role": "user/assistant/system", "content": ...}]`）| 笔记 |
| 30-110 min | 维护 `history: list[dict]`，每轮 append user + assistant | `sandbox/04-multi-turn/` |
| 110-120 min | git commit | commit |

**练习**：
```python
async def multi_turn_chat():
    history = [{"role": "system", "content": "你是友好的助手"}]
    print("多轮对话 (输入 quit 退出)")
    while True:
        msg = input("你: ").strip()
        if msg == "quit":
            break
        history.append({"role": "user", "content": msg})
        resp = await client.chat.completions.create(
            model="deepseek-chat",
            messages=history
        )
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        print(f"AI: {reply}\n")
```

**验收**：
- [ ] AI 能记住你前面说过的话
- [ ] 多轮 history 正确维护

---

### W6 · D4（周四 · 2h）— Tool Calling 入门

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 学 OpenAI `tools` 参数（让 LLM 决定调哪个函数）| 笔记 |
| 40-110 min | 写一个"天气查询工具"，让 LLM 自动决定调不调 | `sandbox/05-tool-call/` |
| 110-120 min | git commit | commit |

**练习**：
```python
import json

def get_weather(city: str) -> str:
    """模拟天气 API"""
    return f"{city}：晴，25°C"

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询城市天气",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"]
        }
    }
}]

async def tool_chat(user_msg: str):
    resp = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_msg}],
        tools=tools
    )
    msg = resp.choices[0].message
    if msg.tool_calls:
        for call in msg.tool_calls:
            if call.function.name == "get_weather":
                args = json.loads(call.function.arguments)
                weather = get_weather(args["city"])
                print(f"[调工具] get_weather({args['city']}) → {weather}")
    else:
        print(f"AI: {msg.content}")
```

**验收**：
- [ ] 输入"北京天气怎么样"→ LLM 决定调 `get_weather("北京")`
- [ ] 输入"你好"→ LLM 不调工具，直接回复

---

### W6 · D5（周五 · 4h）— 毕业项目：Weather Bot

> 🎯 **本路线毕业项目**：能查天气的对话机器人（CLI）

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 设计：1 个 CLI，多轮 history + tool calling + pydantic 配置 | 设计图 |
| 30-180 min | 实现：~150 行 Python | `sandbox/tiny-projects/04-weather-bot/` |
| 180-210 min | 写 5+ 条测试 + README + `.env.example` | 完整项目 |
| 210-240 min | git commit：`feat(weather-bot): MVP with tool calling` | commit |

**项目结构**：
```
04-weather-bot/
├── src/
│   ├── config.py        # pydantic Settings
│   ├── tools.py         # get_weather + TOOL_REGISTRY
│   └── bot.py           # 主循环
├── tests/
│   └── test_bot.py      # mock LLM
├── .env.example
└── README.md
```

**验收**：
- [ ] 输入"北京今天冷不冷" → LLM 调 `get_weather("北京")` → 总结成自然语言
- [ ] 多轮对话能记住上下文
- [ ] 5+ 测试跑通
- [ ] README 完整

---

### ✅ W6 周日验收 · 6 周路线毕业

**知识**：
- [ ] 流式 API 怎么节省延迟？
- [ ] Tool Calling 的核心原理？
- [ ] pydantic + dotenv + async 怎么组合用？
- [ ] 为什么 Agent 工程必须 mock 测试？

**实践**：
- [ ] `04-weather-bot/` 端到端跑通
- [ ] 至少 30 次 git commit
- [ ] `notes/` 累计 ≥ 18 篇笔记
- [ ] **累计代码量 ≥ 1500 行**

---

## 🔗 衔接主路线

W6 结束时你具备的能力：

```
✅ Python 基础语法（变量/容器/函数/类/异常）
✅ 现代 Python（async/await / dataclass / pydantic / 装饰器）
✅ 工程化（venv / pytest / logging / Git）
✅ LLM 接入（OpenAI SDK + 流式 + 多轮 + tool calling）
✅ 项目结构（src/ + tests/ + pyproject.toml + .env）
```

**W7 起 → 主路线 `TODO.md` 的 W5（First 7 Days Sprint）**：
- 用 7 天手写 200 行最小 Agent（不依赖 LangChain）
- 理解 Agent 主循环 / 工具设计 / context engineering / eval

你已经为这个阶段做好了所有底层准备。

---

## 📚 资源清单（按优先级）

| 用途 | 资源 | 用法 |
|---|---|---|
| 中文视频入门 | [莫烦 Python](https://mofanpy.com/) 1-5 集 | W1 D1 后看 |
| 英文文字教程 | [Real Python: Python Basics](https://realpython.com/python-basics/) | 当字典查 |
| Pythonic 风格 | [《流畅的Python》第 1-3 章](https://www.ituring.com.cn/book/2386) | W3 之后看 |
| async 教程 | [Real Python: asyncio](https://realpython.com/async-io-python/) | W4 D1 |
| pydantic 文档 | [pydantic 官方](https://docs.pydantic.dev/) | W3 D5 / W6 D5 |
| pytest 教程 | [Real Python: pytest](https://realpython.com/pytest-python-testing/) | W5 D3 |
| Git 教程 | [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN) | W5 D4 |
| API 调试 | [DeepSeek 开放平台](https://platform.deepseek.com/) | W4 D5 起 |
| 包管理 | [`uv`](https://github.com/astral-sh/uv)（10x 比 pip 快）| W5 D1 |
| Agent 概念 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | W6 D1 |

---

## 🛠 调整与砍掉的策略

### 时间不够时的优先级
**P0（绝不砍）**：
- W2 D5 TODO CLI 项目（第一个完整作品）
- W4 D5 LLM chat 项目（接触 API）
- W6 D5 weather bot（tool calling 第一次）

**P1（可压缩）**：
- W3 D2 继承 → 可合并到 D1
- W4 D4 pathlib → 可推迟到 W6

**P2（第一个砍）**：
- UI / 美化 / 装饰
- 多模型对比实验
- 进阶 LeetCode

### 卡住了怎么办
- **单个 task 卡 < 30 min**：直接 Google / 查文档
- **单个 task 卡 > 1h**：先跳过，明天再回来看
- **整个 stage 卡**：回看本路线 + [`learning-roadmap.md`](learning-roadmap.md) 末尾「风险预案」

---

## ⚠️ 三个最容易踩的坑

### 坑 1：把"看完教程"当成"学会了"
**症状**：看了 10 小时教程，写不出 50 行代码。
**对策**：看完立刻动手，30 行起步。无输出 = 没学。

### 坑 2：跳过 W4 D5 直接看 LangChain
**症状**："我想直接学 LangGraph，不想学底层 API"。
**真相**：没有 API 调用基础，你连 LangGraph 的节点在调什么都看不懂。
**对策**：W4 D5 必须自己写 chat.py 调通 DeepSeek。

### 坑 3：不写测试
**症状**："Agent 程序能跑就行，为什么要测试？"
**真相**：Agent 调用 LLM 一次几毛钱，不 mock 测 100 次要花 30 元。
**对策**：W5 D3 起，**每个 LLM 函数必须有 mock 测试**。

---

## 📌 维护说明

### 怎么更新进度
1. 完成任务把 `[ ]` 改成 `[x]`
2. 每完成一个周，在 W6 验收处更新 `累计 git commit` 数
3. 卡住的任务不动它，列出问题下次问

### 怎么 commit
```bash
git add .
git commit -m "feat(w1d2): BMI calculator with f-string"
git push
```

### 怎么跑测试
```bash
source .venv/bin/activate
pytest tests/ -v
```

### 文档版本
- **v1** · 6 周零基础版（2026-08-24）
- 配套：[`learning-roadmap.md`](learning-roadmap.md)（主路线）+ 本文档（前置路线）

---

## 🎯 6 周毕业时的最低标准

- [ ] **30+ git commit**（每天 ≥ 1）
- [ ] **18+ 篇笔记**（每天 1 篇）
- [ ] **1500+ 行 Python 代码**（含 4 个 sandbox 项目）
- [ ] **能调通 DeepSeek API**
- [ ] **能写第一个 tool calling**
- [ ] **venv + pytest + logging + Git 全会**

满足以上 6 条，**直接进入主路线 W5（First 7 Days Sprint）**。

---

**祝你 6 周后写出第一个 Agent 雏形。** 🎉

> 卡在哪一步、报错信息看不懂、装环境出问题——随时贴给我。