# W5 D3 周三 · 2h — 工具设计（tool card）

- **阶段**：2 First 7 Days Sprint | **周次**：W5 | **状态**：⬜
- **主题**：让工具对模型友好

---

## 🎯 今日目标（3 项）

- [ ] 阅读 Anthropic 工具设计文章
- [ ] 写 `search_notes` tool card
- [ ] 写 `write_summary` tool card

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 读 [Anthropic: Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
  - 重点：
    - 工具名用 `verb_noun`
    - 返回结构化错误
    - 限制结果数量
    - 注释 token 成本

### 📝 写 `search_notes.md` tool card（40min）

- [ ] **[40min]** 在 `projects/01-minimal-agent/tool_cards/search_notes.md` 写卡片（参考 [`../../docs/tool-card-template.md`](../../docs/tool-card-template.md)）：

  ```markdown
  # 工具名：search_notes
  
  ## 一句话描述
  在个人笔记库中搜索关键词
  
  ## 何时使用 ✅
  - 用户说「搜索 / 查找 / 笔记」
  
  ## 何时不使用 ❌
  - 工具已经返回过，应该 final_answer
  
  ## 参数
  | 参数 | 类型 | 必填 | 说明 |
  |---|---|---|---|
  | query | string | ✅ | 搜索关键词 |
  | limit | int | ❌ | 返回数量（1-10） |
  
  ## 返回
  成功：`{"ok": true, "count": 2, "results": [...]}`
  失败：`{"ok": false, "error": "empty_query", "hint": "..."}`
  
  ## 权限
  - [x] 只读安全
  
  ## 例子（至少 1 正常 + 1 错误）
  ```

### 📝 写 `write_summary.md` tool card（30min）

- [ ] **[30min]** 在 `projects/01-minimal-agent/tool_cards/write_summary.md` 写卡片，重点写：
  - **高风险**：需要 HITL
  - **路径校验**：禁 `../` 和 `/`
  - **错误码**：empty_text / invalid_filename

### 💻 完善 `tools.py`（20min）

- [ ] **[20min]** 增强 `tools.py`：
  - [ ] 加超时（5 秒）
  - [ ] 加更严格的参数校验
  - [ ] 加更详细的错误码（参考 tool card）

---

## 📚 关键概念

| 原则 | 例子 |
|---|---|
| **动词_名词** | `search_notes` 不是 `notes` |
| **结构化错误** | `{ok, error, retryable, hint}` |
| **限制结果** | `limit=3` 防 context 爆炸 |
| **HITL** | 写操作前必须人确认 |

---

## 📊 进度

```
W5 D3:    [░░░░░░░░░░] 0/3
W5 整体:  [░░░░░░░░░░] 0/21
阶段 2:   [░░░░░░░░░░] 0/21
```

---

## ✅ 当日验收

- [ ] `search_notes.md` tool card 完整（schema / 错误码 / 例子）
- [ ] `write_summary.md` tool card 完整
- [ ] `tools.py` 增强版能跑
- [ ] 试一个"边界场景"：调 `search_notes("")` 看是否优雅报错

---

## 💡 明日预告

**W5 D4 周四**：Context Engineering（5 层 context builder）