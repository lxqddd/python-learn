# 工具名：write_summary

## 一句话描述
把总结内容写入 `output/<filename>.md` 文件。

## 何时使用 ✅
- 用户明确说「总结 / 写 / 保存到文件」
- 已经搜到充分证据，准备输出最终结果

## 何时不使用 ❌
- 用户没要求保存（只在对话里回答就行）
- 内容很短不值得写文件
- **已经写过同名文件**（避免覆盖，除非用户明确说"覆盖"）

## 参数（Input Schema）
| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| text | string | ✅ | - | 要写入的内容 |
| filename | string | ❌ | "summary.md" | 文件名（不含路径，不能含 / 或 \） |

## 返回（Output Schema）

成功：
```json
{
  "ok": true,
  "path": "output/summary.md",
  "bytes": 1234
}
```

失败：
```json
{
  "ok": false,
  "error": "invalid_filename",
  "retryable": false,
  "hint": "filename 不能包含路径分隔符或以 . 开头"
}
```

## 错误码
| error | retryable | hint |
|---|---|---|
| empty_text | false | "text 不能为空" |
| invalid_filename | false | "filename 不能含路径分隔符或以 . 开头" |

## 权限等级
- [ ] 只读安全
- [x] **需要 human-in-the-loop**（写操作）

## 例子

**例子 1**：正常写入
- 输入：`{"text": "这是总结", "filename": "report.md"}`
- 输出：`{"ok": true, "path": "output/report.md", "bytes": 12}`

**例子 2**：路径穿越攻击
- 输入：`{"filename": "../../../etc/passwd"}`
- 输出：`{"ok": false, "error": "invalid_filename"}` ← 已拦截 ✅

## 实现注意
- 文件写入 `output/` 子目录，不会污染项目根
- 禁止路径分隔符（防 `../` 攻击）
- 禁止以 `.` 开头的文件名（防写 `.gitignore` 等隐藏文件）
- **生产环境必须加**：
  - 文件大小上限（防 OOM）
  - 内容审查（防 prompt injection 写文件）
  - 用户配额（防滥用）
  - 写入日志（审计）

## 升级路径
- Day 7+：加确认 UI（CLI 询问 y/n）
- 阶段 5：换成 Notion API / 飞书 API（写到云端文档）
- 阶段 6：加 diff 预览（写入前先显示给用户看）