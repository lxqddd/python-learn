# W5 D2 周二 · 4h — 手写最小 Agent（最重要的一天）

- **阶段**：2 First 7 Days Sprint | **周次**：W5 | **状态**：⬜
- **主题**：200 行代码理解 ReAct 循环

---

## 🎯 今日目标（3 项）

- [ ] 实现 `agent.py` 主循环
- [ ] 实现 `tools.py`（2 个工具）
- [ ] 跑通 5 个固定任务

---

## ⚠️ 关键提醒

**不要用框架**（LangChain / LangGraph）！今天的目标是理解循环的本质。

---

## ✅ 任务清单（4h）

### 💻 实现 `agent.py`（90min）

- [ ] **[90min]** 在 `projects/01-minimal-agent/` 下创建 `agent.py`，**自己打**（不复制）：

  关键结构：
  ```python
  def run_agent(task, model, trace_path, max_steps=5):
      state = {"task": task, "steps": [], "final": None, "status": "running"}
      
      for step_id in range(1, max_steps + 1):
          # 1. 构建 context
          context = build_context(task, state, tools)
          # 2. 模型决策
          action = model.decide(context)
          # 3. 是否最终答案？
          if action.type == "final_answer":
              return ...
          # 4. 工具白名单
          if action.tool_name not in tools:
              observation = {"ok": False, "error": "unknown_tool"}
          # 5. HITL
          if tools[action.tool_name]["requires_confirmation"]:
              print("⚠️ [HITL] ...")
          # 6. 调工具，捕获异常
          try:
              observation = tools[action.tool_name]["func"](**action.args)
          except Exception as e:
              observation = {"ok": False, "error": str(e)}
          # 7. 记录 step
          _record_step(state, trace_path, step_id, action, observation)
      
      # 超过 max_steps
      return failed_state
  ```

  **完整代码参考**：`projects/01-minimal-agent/agent.py`（**先自己打，卡 30 分钟再看**）

### 💻 实现 `tools.py`（60min）

- [ ] **[60min]** 实现 2 个工具：

  - **`search_notes(query, limit=3)`**：
    - 在 `NOTES_DB` 字典里关键词匹配
    - 返回结构化结果
  
  - **`write_summary(text, filename="summary.md")`**：
    - 写入 `output/` 目录
    - 路径校验（防穿越）
    - 标记 `requires_confirmation: True`

  **完整代码参考**：`projects/01-minimal-agent/tools.py`

### 💻 实现 `mock_model.py`（30min）

- [ ] **[30min]** 实现 MockModel：
  - 用关键词匹配模拟 LLM 决策
  - 含"搜索/查找/笔记" → search_notes
  - 含"总结/写/保存" → search + write_summary
  - 其他 → final_answer

### 🧪 跑通测试（60min）

- [ ] **[60min]** 跑这 5 个任务，验证都能跑：

  | 任务 | 期望 |
  |---|---|
  | "搜索 Python 异步笔记" | 调 search → answer |
  | "查找 React Hooks" | 调 search → answer |
  | "总结 Agent 基础概念" | 调 search + write → answer |
  | ""（空） | 直接 answer |
  | "搜索 xyz999 不存在" | 调 search → answer |

  - 检查 `trace/*.jsonl` 文件有内容
  - 截图存到 `notes/week4/day2-trace.png`

---

## 📚 关键概念（必须理解）

| 概念 | 代码位置 |
|---|---|
| **5 步循环** | `for step_id in range(1, 6)` |
| **工具白名单** | `if action.tool_name not in tools` |
| **结构化错误** | `{"ok": False, "error": "..."}` |
| **JSONL trace** | 每步一行 JSON |
| **HITL** | 高风险工具的确认机制 |

---

## 📊 进度

```
W5 D2:    [░░░░░░░░░░] 0/3
W5 整体:  [░░░░░░░░░░] 0/21
阶段 2:   [░░░░░░░░░░] 0/21
```

---

## ✅ 当日验收

- [ ] `agent.py` ≤ 250 行
- [ ] `tools.py` 2 个工具跑通
- [ ] `mock_model.py` 跑通
- [ ] 5 个测试任务都返回合理结果
- [ ] `trace/*.jsonl` 至少 5 条记录

---

## ⚠️ 卡住了怎么办

| 卡点 | 解决 |
|---|---|
| Python 语法看不懂 | 回去补 W2/W3 对应章节 |
| ReAct 循环逻辑混乱 | 画一张图：context → action → observation → 下一个 context |
| MockModel 决策不对 | 简化逻辑，只匹配几个关键词 |
| 工具白名单没生效 | 加 print 看 action.tool_name 是什么 |
| Trace 文件为空 | 检查文件路径 + 用 `try/except` 包写入 |

---

## 💡 明日预告

**W5 D3 周三**：工具设计（写 tool card）