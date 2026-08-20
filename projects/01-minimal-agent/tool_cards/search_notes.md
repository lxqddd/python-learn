# 工具名：search_notes

## 一句话描述
在个人笔记库中搜索关键词，返回匹配的笔记列表（id、title、snippet、score）。

## 何时使用 ✅
- 用户说「搜索 / 查找 / 找 ... 笔记」
- 需要先检索证据再回答的问题
- 用户问「我有写过关于 X 的笔记吗？」

## 何时不使用 ❌
- 用户问的是当前日期、天气等外部信息（这工具只搜本地笔记）
- 工具结果已经够用，应该 `final_answer` 而不是再搜
- 已经连续调用 2 次且结果一样

## 参数（Input Schema）
| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| query | string | ✅ | - | 搜索关键词，支持中文 |
| limit | int | ❌ | 3 | 返回数量上限（1-10） |

## 返回（Output Schema）

成功：
```json
{
  "ok": true,
  "count": 2,
  "query": "Python 异步",
  "results": [
    {
      "id": "python-async",
      "title": "Python 异步编程笔记",
      "snippet": "asyncio 是 Python 标准库的异步框架...",
      "score": 5
    }
  ]
}
```

失败：
```json
{
  "ok": false,
  "error": "empty_query",
  "retryable": false,
  "hint": "query 不能为空字符串"
}
```

## 错误码
| error | retryable | hint |
|---|---|---|
| empty_query | false | "query 不能为空" |
| invalid_limit | false | "limit 应在 1-10 之间" |

## 权限等级
- [x] 只读安全
- [ ] 需要 human-in-the-loop

## 例子

**例子 1**：搜索 "Python 异步"
- 输入：`{"query": "Python 异步", "limit": 3}`
- 输出：返回 1 条结果（python-async）

**例子 2**：空 query
- 输入：`{"query": ""}`
- 输出：`{"ok": false, "error": "empty_query"}`

## 实现注意
- 当前是关键词匹配，**生产环境必须换成向量检索**（Chroma / Milvus）
- snippet 只截取前 80 字符，防止 context 爆炸
- score 越高越相关，模型应优先引用 score 高的结果

## 升级路径
- Day 7+：换成向量检索（sentence-transformers + FAISS）
- 阶段 3：接入 Milvus + Reranker
- 阶段 5：加入权限过滤（用户只能搜自己的笔记）