# W1 周日验收 · 30-60min

> **阶段**：0 定方向 | **周次**：W1 | **状态**：⬜ 未开始
> **主题**：W1 阶段 0 完成度自检

---

## 🎯 验收目标

确认你已经完成阶段 0 的所有目标，准备好进入阶段 1（Python 突击）。

---

## ✅ 概念验收（15min）

打开 [`../../docs/concept-notes.md`](../../docs/concept-notes.md)，能口述回答：

- [ ] **Agent vs Chatbot 区别**？（Agent 能调用工具执行任务，Chatbot 只回答）
- [ ] **ReAct 是什么**？（Reasoning + Acting 循环，模型决定下一步动作）
- [ ] **5 级能力模型 L0-L5**？（Prompt App → Tool → Workflow → Agent → Long-running → Multi-Agent）
- [ ] **求职 sweet spot 是哪级**？（L3-L4）
- [ ] **Context Engineering 是什么**？（控制进入模型的 5 层 context）

答不出 → 回去再读一遍概念笔记。

---

## ✅ 环境验收（10min）

- [ ] `python --version` 输出 `Python 3.11.x` 或更高
- [ ] `uv --version` 输出版本号
- [ ] VS Code 打开 `agent-learning` 仓库，Python 扩展图标亮起
- [ ] `git log` 显示本周有 ≥ 1 次 commit
- [ ] `python sandbox/hello.py` 能跑通，输出 AI 回复
- [ ] `ollama run llama3.2:1b "你好"` 能输出

---

## ✅ 笔记验收（5min）

打开 `notes/week1/`，应该有这些文件：

- [ ] `day1-anthropic-summary.md`（3 句话总结）
- [ ] `day2-transformer-intuition.md`
- [ ] `day3-video-notes.md`（5 个语法点）
- [ ] `day4-environment.png` 或类似（环境截图）
- [ ] `capability-levels.md`（L0-L5 表格）
- [ ] `summary.md`（本周总结）

**少于 3 篇？** 这周写少了，阶段 1 开始多写。

---

## ✅ 心态验收（5min）

诚实回答自己：

- [ ] **这周我真的学进去了**，不是走马观花
- [ ] **每天都有 commit**，哪怕只是改一行 README
- [ ] **遇到卡点能 Google 解决**，不是等别人喂
- [ ] **明天开始 W2 我有动力**

---

## 📊 本周统计

```
W1 完成度:    [░░░░░░░░░░] /23
工作日产出:   D1=__ D2=__ D3=__ D4=__ D5=__
总投入时间:   __h（预计 10h）
```

---

## 🚦 下一步决策

根据本周完成度决定：

| 完成度 | 建议 |
|---|---|
| ≥ 90% | ✅ 直接进入 W2 阶段 1 |
| 70-90% | ⚠️ 花周六补完缺失项，周一进入 W2 |
| < 70% | 🔴 这周节奏太快，建议重做 W1（每天 1h 做扎实） |

---

## 🎁 奖励自己

完成 W1 后，给自己一个小奖励（吃顿好的 / 看个电影 / 买个小东西），建立正向循环。

**14 周很长，每完成一个阶段都值得庆祝。**

---

## 💡 下周预览

**阶段 1 · Python 突击（W2-3）**：
- W2：基础语法（变量、列表、字典、函数）
- W3：进阶（类、装饰器、async、pydantic）
- 目标：能读懂 LangChain 源码

明天打开 [`../01-stage-1/W2-D1-mon.md`](../01-stage-1/W2-D1-mon.md)。