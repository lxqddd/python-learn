# W2 D4 周四 · 2h — 异常 + 文件 + 第一个 chatbot

- **阶段**：1 Python 突击 | **周次**：W2 | **状态**：⬜
- **主题**：try/except / 文件读写 / 实战项目

---

## 🎯 今日目标（4 项）

- [ ] 学 `try/except/finally`
- [ ] 学文件读写 + JSON 模块
- [ ] 写练习 5（CSV → JSON）
- [ ] **实战**：写一个 30 行 chatbot

---

## ✅ 任务清单（2h）

### 📖 阅读（60min）

- [ ] **[30min]** 学 [try/except/finally](https://realpython.com/python-exceptions/)
  - `try:` 可能出错的代码
  - `except ExceptionType:` 捕获特定异常
  - `else:` 没出错时执行
  - `finally:` 无论如何都执行（清理资源）

- [ ] **[30min]** 学 [文件读写](https://realpython.com/read-write-files-python/)
  - `with open("file.txt", "r", encoding="utf-8") as f:`
  - 模式：`r` / `w` / `a` / `x`
  - `json.dump()` / `json.load()`

### 💻 练习 5：CSV → JSON（40min）

- [ ] **[40min]** 写 `sandbox/week2-basics/ex05_csv_to_json.py`：
  ```python
  """读 CSV → 统计 → 写 JSON"""
  import csv
  import json
  from pathlib import Path
  
  # 1. 写一个测试 CSV
  csv_path = Path("sandbox/week2-basics/test_data.csv")
  csv_path.parent.mkdir(parents=True, exist_ok=True)
  with csv_path.open("w", encoding="utf-8", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["name", "score"])
      writer.writerow(["Alice", "90"])
      writer.writerow(["Bob", "85"])
      writer.writerow(["Alice", "95"])
  
  # 2. 读 CSV，统计每个人的总分
  scores = {}
  with csv_path.open("r", encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          name = row["name"]
          score = int(row["score"])
          scores[name] = scores.get(name, 0) + score
  
  # 3. 写 JSON
  json_path = Path("sandbox/week2-basics/scores.json")
  with json_path.open("w", encoding="utf-8") as f:
      json.dump(scores, f, ensure_ascii=False, indent=2)
  
  print(f"统计完成 → {json_path}")
  print(scores)
  ```
  - 跑通
  - 检查生成的 JSON 文件

### 💻 实战：30 行 chatbot（40min）

- [ ] **[40min]** 写 `sandbox/tiny-projects/01-chatbot/chatbot.py`：
  ```python
  """30 行命令行聊天机器人"""
  import os
  from openai import OpenAI
  
  client = OpenAI(
      api_key=os.getenv("DEEPSEEK_API_KEY"),
      base_url="https://api.deepseek.com/v1",
  )
  
  history = []  # 存对话历史
  
  print("🤖 Chatbot 启动（输入 'quit' 退出）")
  while True:
      user_input = input("\n你: ")
      if user_input.strip().lower() == "quit":
          break
      
      history.append({"role": "user", "content": user_input})
      response = client.chat.completions.create(
          model="deepseek-chat",
          messages=history,
      )
      answer = response.choices[0].message.content
      history.append({"role": "assistant", "content": answer})
      print(f"\nAI: {answer}")
  
  print(f"\n共聊了 {len(history) // 2} 轮")
  ```
  - 跑通，至少聊 3 轮
  - 验证 chatbot 真的记住了历史
  - 截图保存

---

## 📚 关键概念

| 概念 | 用途 |
|---|---|
| `try/except` | 错误处理，不让程序崩 |
| `with open() as f:` | 自动关闭文件 |
| `csv.DictReader` | 按列名读 CSV |
| `json.dump/load` | JSON 读写 |
| `while True: break` | chatbot 主循环 |

---

## ✅ 当日验收

- [ ] 练习 5 跑通，scores.json 生成
- [ ] chatbot.py 跑通，至少聊 3 轮
- [ ] 理解为什么 `with open()` 比 `open().close()` 好

---

## 💡 明日预告

**W2 D5 周五**：周复盘 + 重写练习