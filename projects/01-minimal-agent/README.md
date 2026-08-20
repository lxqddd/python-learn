# 📌 Project 01 · 最小 Agent（First 7 Days Sprint）

> 这是整个学习路径的**核心里程碑**。
> 完成 = 你真正理解了 Agent 是什么，而不是"会用 LangChain"。

---

## 🎯 项目目标

构建一个**200 行的最小 Agent**：
- 2 个工具：`search_notes(query)` + `write_summary(text)`
- 最多 5-6 步循环
- 每步写 JSONL trace
- 5 层 context builder
- 20 条 eval cases
- README + eval_report + demo_script 三件套

---

## 🗂 文件结构

```
01-minimal-agent/
├── README.md              ← 本文件
├── requirements.txt       ← 依赖
├── .env.example           ← 环境变量模板
├── agent.py               ← ⭐ 核心循环（run_agent）
├── tools.py               ← 2 个工具实现
├── prompts.py             ← 5 层 context builder
├── mock_model.py               ← 不用花钱的 Mock 实现
├── tool_cards/             ← 工具卡文档
│   ├── search_notes.md
│   └── write_summary.md
├── trace/                 ← Trace 日志
│   ├── schema.json        ← Trace schema 定义
│   └── *.jsonl            ← 实际 trace
├── eval_cases.jsonl       ← 20 条 eval
├── eval_report.md         ← 跑分结果
├── demo_script.md         ← 演示脚本
└── tests/
    └── test_smoke.py      ← 冒烟测试
```

---

## 🚀 快速开始

```bash
# 1. 准备环境
cd projects/01-minimal-agent
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. 跑冒烟测试（不需要 API key）
python tests/test_smoke.py

# 3. 跑 20 条 eval
python eval_runner.py

# 4. 看 trace
ls trace/*.jsonl
```

---

## 📅 7 天任务分配

| Day | 任务 | 产出 |
|---|---|---|
| **D1** | 读 [`docs/concept-notes.md`](../../docs/concept-notes.md)，想清楚场景 | 流程图 + 7 问清单 |
| **D2** | 实现 `agent.py` + `tools.py` + `mock_model.py` | 能跑通的 5 个任务 |
| **D3** | 写 2 个 tool card | `tool_cards/*.md` |
| **D4** | 实现 5 层 context builder（`prompts.py`） | prompt 结构稳定 |
| **D5** | 写 20 条 eval cases，跑一遍 | `eval_report.md` |
| **D6** | 写 README + eval_report + demo_script | 别人能 clone-and-run |
| **D7** | 复盘 + 简历 bullet | 一段能贴进简历的文字 |

详细任务见 [`docs/first-7-days-checklist.md`](../../docs/first-7-days-checklist.md)。

---

## 🛠 我的工具列表

| 工具 | 类型 | 权限 | Tool Card |
|---|---|---|---|
| search_notes | 只读 | 安全 | [link](tool_cards/search_notes.md) |
| write_summary | 写 | HITL | [link](tool_cards/write_summary.md) |

---

## 📊 评估指标（Day 5 记录）

- 任务成功率：__ / 20
- 平均步数：__
- 工具调用成功率：__
- 失败类型分布：__

---

## 📦 完成后产出清单

- [ ] `agent.py` ≤ 250 行
- [ ] 2 个 tool card
- [ ] 5 层 context builder
- [ ] 20 条 eval cases + 跑分
- [ ] README + eval_report + demo_script
- [ ] 1 段简历 bullet
- [ ] 1 个 git commit