# W1 D1 周一 · 2h — 概念入门

> **阶段**：0 定方向 | **周次**：W1 | **状态**：⬜ 未开始
> **主题**：理解 Agent 是什么 + 环境准备

---

## 🎯 今日目标（4 项）

- [ ] 阅读 Anthropic 文章，建立 Agent 基础认知
- [ ] 写完 `concept-notes.md` 的「我的理解」6 个填空
- [ ] 环境装好：Python 3.11+ / `uv` / VS Code / Git
- [ ] 注册 DeepSeek + 拿到 API Key

---

## ✅ 任务清单（2h）

### 📖 概念输入（1h）

- [ ] **[30min]** 阅读 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
  - 重点看：workflow vs agent 的区别、并行化时机
  - 产出：在 `notes/week1/day1-anthropic-summary.md` 写 3 句话总结

- [ ] **[30min]** 打开 [`../../docs/concept-notes.md`](../../docs/concept-notes.md)，把「我的理解」6 个填空用自己的话写完

### 🔧 环境准备（1h）

- [ ] **[60min]** 安装 4 个工具：
  - **Python 3.11+**：https://www.python.org/downloads/
  - **uv**（Python 包管理器，比 pip 快 100 倍）：`curl -LsSf https://astral.sh/uv/install.sh | sh`
  - **VS Code**：https://code.visualstudio.com/ + 装 Python 扩展
  - **Git**：https://git-scm.com/
  - 产出：环境截图存到 `notes/week1/environment.png`

### 🔑 API 注册（20min）

- [ ] **[20min]** 注册 DeepSeek + 充值 10 元
  - URL：https://platform.deepseek.com/
  - 拿到 API Key 后保存到密码管理器（**绝不能 commit 到 git！**）

---

## 📚 关键概念（今日必须理解）

| 概念 | 一句话解释 |
|---|---|
| **Chatbot** | 只回答问题，不调用工具 |
| **Workflow** | 固定步骤处理任务，路径僵化 |
| **Agent** | 模型根据状态自主决定下一步 |
| **ReAct** | Reasoning + Acting 循环 |
| **L0-L5 模型** | Prompt App → Multi-Agent 的 5 级能力 |

**Anthropic 核心观点**：很多任务用 workflow 就够了。**只有路径无法硬编码时才上 Agent**。

---

## 🔗 资源链接

- [Anthropic 文章](https://www.anthropic.com/engineering/building-effective-agents)
- [docs/concept-notes.md](../../docs/concept-notes.md)
- [docs/learning-roadmap.md](../../docs/learning-roadmap.md)（阶段 0 章节）
- [resources.md](../../resources.md)（其他资源索引）

---

## 📊 进度

```
W1 D1:        [░░░░░░░░░░] 0/4
W1 整体:      [░░░░░░░░░░] 0/23
阶段 0:       [░░░░░░░░░░] 0/23
```

---

## ✅ 当日验收

完成后勾选：

- [ ] 能口述 ReAct 是什么
- [ ] 能说出 Agent 和 Chatbot 的根本区别
- [ ] Python / uv / VS Code / Git 都装好（`uv --version` 能输出版本）
- [ ] DeepSeek API Key 已保存到密码管理器
- [ ] GitHub 第一个 commit（明天的任务，今天先准备）

---

## 💡 明日预告

**W1 D2 周二**：5 级能力模型 + Ollama 本地模型 + 第一次调 API

---

**完成后**：把当日所有 `[ ]` 改成 `[x]`，更新进度条，明天打开 [`W1-D2-tue.md`](W1-D2-tue.md)