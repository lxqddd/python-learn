# W1 D2 周二 · 2h — 5 级能力模型 + 本地模型

> **阶段**：0 定方向 | **周次**：W1 | **状态**：⬜ 未开始
> **主题**：5 级能力模型 + Ollama 本地模型

---

## 🎯 今日目标（4 项）

- [ ] 理解 5 级能力模型（L0-L5）
- [ ] 装好 Ollama 拉本地小模型
- [ ] 第一次在本地用 LLM
- [ ] 理解 Transformer 是什么

---

## ✅ 任务清单（2h）

### 📖 概念输入（1h）

- [ ] **[30min]** 重读 [`../../docs/concept-notes.md`](../../docs/concept-notes.md) 的「五级能力模型」章节
  - 抄写 L0-L5 表格到 `notes/week1/capability-levels.md`
  - 重点记住：**求职 sweet spot 是 L3-L4**

- [ ] **[30min]** 看 [3Blue1Brown Transformer 视频](https://www.youtube.com/watch?v=wjZofJX0H4A) 前 10 分钟
  - 目标：直观理解 LLM 怎么"读懂"文字
  - 产出：`notes/week1/transformer-intuition.md` 写一句话总结

### 🔧 本地环境（1h）

- [ ] **[60min]** 安装 Ollama + 拉模型
  ```bash
  # macOS
  brew install ollama
  
  # 启动 ollama 服务
  ollama serve
  
  # 另开终端，拉一个小模型（约 1GB）
  ollama pull llama3.2:1b
  
  # 对话测试
  ollama run llama3.2:1b "你好，请用一句话介绍你自己"
  ```
  - 产出：截图存到 `notes/week1/ollama-first-run.png`

### 📝 笔记（20min）

- [ ] **[20min]** 在 `notes/week1/day2-reflection.md` 写：
  1. 一句话总结 Transformer
  2. L0-L5 我现在在哪一级
  3. 求职 sweet spot 是哪级？为什么

---

## 📚 关键概念（今日必须理解）

| 级别 | 名称 | 特征 | 例子 |
|---|---|---|---|
| L0 | Prompt App | 没工具，纯文本 | 简单摘要 |
| L1 | Tool-Using App | 单轮工具调用 | "查天气" |
| L2 | Workflow Agent | 多步但固定 | RAG 流水线 |
| L3 | Autonomous Agent | 模型自主决策 | 研究 Agent |
| L4 | Long-running Agent | 持久状态、可恢复 | Coding Agent |
| L5 | Multi-Agent | 多角色协作 | 团队 Agent |

**为什么 L3-L4 是 sweet spot？** 因为它们有真实业务价值（不只是 Demo），同时实现难度适中。

---

## 🔗 资源链接

- [3Blue1Brown Transformer 视频](https://www.youtube.com/watch?v=wjZofJX0H4A)
- [Ollama 官网](https://ollama.com/)
- [llama3.2 模型](https://ollama.com/library/llama3.2)
- [docs/concept-notes.md](../../docs/concept-notes.md)

---

## 📊 进度

```
W1 D2:        [░░░░░░░░░░] 0/4
W1 整体:      [░░░░░░░░░░] 0/23
阶段 0:       [░░░░░░░░░░] 0/23
```

---

## ✅ 当日验收

- [ ] 能口述 L0-L5 每一级是什么
- [ ] Ollama 装好，能跑 `ollama run llama3.2:1b`
- [ ] 本地 LLM 有输出
- [ ] Transformer 笔记写完

---

## 💡 明日预告

**W1 D3 周三**：Python 第一次体验 + 第一次调 DeepSeek API

---

**完成后**：把当日所有 `[ ]` 改成 `[x]`，明天打开 [`W1-D3-wed.md`](W1-D3-wed.md)