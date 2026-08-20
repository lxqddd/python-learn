# W3 D1 周一 · 2h — 类与对象

- **阶段**：1 Python 突击 | **周次**：W3 | **状态**：⬜
- **主题**：class / `__init__` / `self` / 方法

---

## 🎯 今日目标（3 项）

- [ ] 学 class 基本语法
- [ ] 学实例方法、`self`、属性
- [ ] 写练习 7（ChatHistory 类）

---

## ✅ 任务清单（2h）

### 📖 阅读（80min）

- [ ] **[40min]** 看 [Real Python: Classes and Objects](https://realpython.com/python3-object-oriented-programming/)
  - `class MyClass:`
  - `__init__(self, args)` 构造方法
  - `self` 指实例本身
  - 实例属性 vs 类属性
  - 实例方法（第一个参数是 self）

- [ ] **[40min]** 学继承和方法重写（简单了解）
  - `class Child(Parent):`
  - `super().__init__()`
  - 方法重写

### 💻 练习 7：ChatHistory 类（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex07_chat_history.py`：
  ```python
  """封装对话历史管理"""
  from dataclasses import dataclass, field
  from typing import List
  
  @dataclass
  class Message:
      role: str  # "user" / "assistant" / "system"
      content: str
  
  class ChatHistory:
      def __init__(self, system_prompt: str = ""):
          self.messages: List[Message] = []
          if system_prompt:
              self.messages.append(Message("system", system_prompt))
      
      def add_user(self, content: str) -> None:
          self.messages.append(Message("user", content))
      
      def add_assistant(self, content: str) -> None:
          self.messages.append(Message("assistant", content))
      
      def to_dict_list(self) -> list[dict]:
          return [{"role": m.role, "content": m.content} for m in self.messages]
      
      def __len__(self) -> int:
          return len(self.messages)
      
      def clear(self) -> None:
          # 保留 system prompt
          self.messages = [m for m in self.messages if m.role == "system"]
  
  # 测试
  if __name__ == "__main__":
      history = ChatHistory("你是一个有帮助的助手")
      history.add_user("你好")
      history.add_assistant("你好！有什么可以帮助你的？")
      history.add_user("今天天气怎么样？")
      
      print(f"消息数: {len(history)}")
      for msg in history.to_dict_list():
          print(f"[{msg['role']}] {msg['content'][:30]}")
      
      history.clear()
      print(f"清空后消息数: {len(history)}")  # 应该是 1（system prompt）
  ```
  - 跑通，理解每个方法的作用

---

## 📚 关键概念

| 概念 | 例子 |
|---|---|
| `class` | `class Dog:` |
| `__init__` | 构造方法 |
| `self` | 实例本身 |
| 实例方法 | `def method(self, x):` |
| `@dataclass` | 自动生成 `__init__` 等 |
| `super()` | 调用父类方法 |

---

## ✅ 当日验收

- [ ] 练习 7 跑通
- [ ] 能解释 `self` 是什么
- [ ] 能写出带 `__init__` 的简单类

---

## 💡 明日预告

**W3 D2 周二**：装饰器 + 生成器