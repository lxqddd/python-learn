# 🛠 Tool Card 模板

> 每个工具都应该有一张"工具卡"，让 LLM 知道何时用 / 不用、怎么调、返回什么、错了怎么办。
> 参考：[Anthropic: Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

---

## Tool Card 模板

复制下面整个代码块，填到 `projects/01-minimal-agent/tool_cards/<tool_name>.md`：

```markdown
# 工具名：<verb_noun>

## 一句话描述
<这个工具做什么，一句话说清>

## 何时使用 ✅
- 用户想要 <触发场景 1>
- 需要 <触发场景 2>

## 何时不使用 ❌
- <反例 1>
- <反例 2>

## 参数（Input Schema）
| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| query | string | ✅ | 搜索关键词 |
| limit | int | ❌ | 返回数量，默认 5，最大 20 |

## 返回（Output Schema）
成功时：
```json
{
  "ok": true,
  "results": [
    {"id": "note-001", "title": "...", "snippet": "..."}
  ]
}
```

失败时：
```json
{
  "ok": false,
  "error": "rate_limited",
  "retryable": true,
  "hint": "Wait 30 seconds"
}
```

## 错误码
| error | retryable | hint |
|---|---|---|
| empty_query | false | "query 不能为空" |
| rate_limited | true | "等待 30 秒" |
| timeout | true | "重试或简化 query" |
| not_found | false | "换个关键词试试" |

## 权限等级
- [ ] 只读安全
- [x] 需要 human-in-the-loop（写操作）

## 例子

### 例子 1：正常调用
输入：`{"query": "python 异步", "limit": 3}`
返回：
```json
{"ok": true, "results": [{"id": "n1", "title": "..."}]}
```

### 例子 2：错误处理
输入：`{"query": ""}`
返回：
```json
{"ok": false, "error": "empty_query", "hint": "query 不能为空"}
```

## 实现注意
- 限制返回数量防 context 爆炸
- 截断长文本（>500 字只保留前 200 + "...")
- 添加超时（5 秒）
```

---

## 实用原则（来自 Anthropic）

1. **名字用 `verb_noun`**：`search_notes` 而不是 `notes` `read` 而不是 `get`
2. **不要让模型算 ID**：传 name 而不是 UUID
3. **返回结构化错误**：`{ok, error, retryable, hint}` 而非抛异常
4. **限制结果数量**：默认 ≤5，让模型主动请求更多
5. **注释 token 成本**：参数超过 5 个说明 schema 设计有问题
6. **测试 prompt**：把 tool card 喂给模型，看它能否正确选工具

---

## 我的工具列表

| 工具名 | 类型 | 权限 | 状态 |
|---|---|---|---|
| search_notes | 只读 | 安全 | ⬜ Day 3 完成 |
| write_summary | 写 | HITL | ⬜ Day 3 完成 |
| _ | _ | _ | _ |

填到 `projects/01-minimal-agent/README.md` 的工具表里。