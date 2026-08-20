# W5 D4 周四 · 2h — Context Engineering

- **阶段**：2 First 7 Days Sprint | **周次**：W5 | **状态**：⬜
- **主题**：5 层 context builder

---

## 🎯 今日目标（3 项）

- [ ] 实现 5 层 context builder
- [ ] 长工具结果截断
- [ ] 同任务重复跑验证稳定性

---

## ✅ 任务清单（2h）

### 💻 实现 `prompts.py`（90min）

- [ ] **[90min]** 在 `projects/01-minimal-agent/prompts.py` 实现 5 层：

  ```python
  def build_context(task, state, tools) -> dict:
      return {
          "system": _build_system(tools),       # 角色 + 边界 + 格式
          "task": _build_task(task),             # 当前任务
          "memory": _build_memory(state),        # 长期记忆（占位）
          "retrieved": _build_retrieved(state),  # 检索证据
          "recent_trace": _build_recent_trace(state, n=3),  # 最近 3 步
      }
  ```

  各层职责：
  - **`_build_system`**：工具描述 + 输出 JSON schema + 行为约束
  - **`_build_task`**：用户任务原文 + 成功标准
  - **`_build_memory`**：暂返回"（暂无长期记忆）"，Day 5+ 接 Mem0
  - **`_build_retrieved`**：从 steps 提取 search_notes 的 results
  - **`_build_recent_trace`**：最近 3 步的摘要（含重复动作检测警告）

  **完整代码参考**：`projects/01-minimal-agent/prompts.py`

### 💻 集成进 `agent.py`（15min）

- [ ] **[15min]** 改 `agent.py`：
  ```python
  from prompts import build_context
  
  # 在主循环里
  context = build_context(task=task, state=state, tools=TOOL_REGISTRY)
  ```

### 🧪 验证（15min）

- [ ] **[15min]** 跑同任务 2 次（如"搜索 Python 异步笔记"），验证：
  - [ ] prompt 结构稳定
  - [ ] retrieved 层每次更新
  - [ ] recent_trace 包含重复动作警告（如有）

---

## 📚 关键概念

**为什么要分层？**
- 防止 context 污染（不同来源的内容混在一起）
- 长期记忆可以独立缓存
- trace 摘要避免 prompt 越来越长

**5 层的关系：**
```
┌─────────────────────────────────────┐
│ system      永远不变（可缓存）       │
│ task        当前任务                 │
│ memory      长期记忆（Mem0/向量库） │
│ retrieved   检索证据（每次更新）     │
│ recent_trace 最近 3 步摘要          │
└─────────────────────────────────────┘
       ↓
  喂给模型
```

**为什么不存完整 trace？**
- LLM context 窗口有限
- 完整 trace 让模型分心
- 摘要足以判断"下一步"

---

## 📊 进度

```
W5 D4:    [░░░░░░░░░░] 0/3
W5 整体:  [░░░░░░░░░░] 0/21
阶段 2:   [░░░░░░░░00░] 0/21
```

---

## ✅ 当日验收

- [ ] `prompts.py` 实现 5 层
- [ ] agent.py 集成 build_context
- [ ] 同任务跑 2 次，prompt 结构一致
- [ ] 笔记：`notes/week4/day4-context-layers.md`

---

## 💡 明日预告

**W5 D5 周五**：写 20 条 eval cases + 跑分