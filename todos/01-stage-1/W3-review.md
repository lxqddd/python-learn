# W3 周日验收 · 阶段 1 毕业

- **阶段**：1 Python 突击 | **周次**：W3 | **状态**：⬜
- **主题**：W3 阶段验收 + 阶段 1 总结

---

## 🎯 验收目标

W3 完成后，你应该能：
- 用 Python 类组织代码
- 用装饰器增强函数
- 理解 async/await
- 用 pydantic 校验数据
- 用 dotenv 管理配置
- **关键**：读懂 LangChain 源码 60% 以上

---

## ✅ 知识验收（15min）

不看书回答：

- [ ] **class** 怎么定义？`__init__` 什么时候调用？
- [ ] **self** 是什么？所有方法都要有 self 参数吗？
- [ ] **装饰器** 本质是什么？`@wraps` 干嘛用？
- [ ] **生成器** vs 普通函数？`yield` 干嘛用？
- [ ] **async/await** 什么意思？是多线程吗？
- [ ] **pydantic BaseModel** 干嘛用？为什么 Agent 框架都用它？
- [ ] **dotenv** 为什么需要？`.env` 为什么要 gitignore？

---

## ✅ 实践验收（20min）

- [ ] 10 个练习全部完成：
  - W2：ex01-05 + chatbot
  - W3：ex07-ex10 + weather-llm
- [ ] `sandbox/tiny-projects/02-weather-llm/` 能跑通：
  - 输入真实城市 → 拿到穿衣建议
  - 输入错误城市 → 优雅报错
  - 没 API Key → 优雅报错

---

## ✅ 关键测试：LangChain 源码读懂率（10min）

- [ ] 打开 [LangChain 源码](https://github.com/langchain-ai/langchain)
- [ ] 进入 `libs/core/langchain_core/runnables/base.py`
- [ ] 随机选 50 行代码，能读懂多少？

| 读懂率 | 评估 |
|---|---|
| ≥ 80% | ✅ 阶段 1 优秀毕业 |
| 60-80% | ✅ 阶段 1 合格，可以进入 W4 |
| 40-60% | ⚠️ 需要再花 1 周补 Python |
| < 40% | 🔴 必须重做 W3（节奏太赶） |

---

## ✅ 笔记验收（5min）

- [ ] `notes/week3/summary.md` 写完
- [ ] W3 5 篇每日笔记都在

---

## 📊 阶段 1 统计

```
W2 完成度:    [░░░░░░░░░░] /16
W3 完成度:    [░░░░░░░░░░] /17
总投入时间:   __h（预计 40h）
```

---

## 🚦 下一步

| 评估 | 建议 |
|---|---|
| 全部 ≥ 60% | ✅ 周一进入 W4 First 7 Days Sprint |
| LangChain 读懂率 < 60% | 🔴 W4 延后 1 周，再练 1 周 Python |

---

## 🎉 阶段 1 毕业庆祝

完成 Python 突击后，给自己一个稍大的奖励（吃顿好的 + 1 天休息）。

你现在的能力：
- ✅ 能读懂 Agent 框架源码
- ✅ 能用 pydantic / dotenv / async
- ✅ 能写 100 行的完整 CLI 工具
- ✅ 理解类和装饰器（Agent 框架的核心）

接下来 12 周，你将用这些基础构建：
- 🚀 最小 Agent（W4）
- 🤖 完整 RAG（W5-6）
- 🕸 LangGraph 框架（W7-8）
- 🤝 多 Agent + MCP（W9-10）
- 🏆 简历级项目（W11-12）
- 💼 Offer（W13-14）

---

## 💡 下周预览

**阶段 2 · 🚀 First 7 Days Sprint（W4）**
- 这是整个路线的灵魂
- 7 天产出 1 个可演示、可评估、有 trace 的最小 Agent
- 完成后可直接写进简历

明天打开 [`../02-stage-2/W4-D1-mon.md`](../02-stage-2/W4-D1-mon.md)。