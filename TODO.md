# 📋 17 周 Agent 开发学习 Todo List

> 配套详细路线：[`docs/learning-roadmap.md`](docs/learning-roadmap.md)（每项任务的资源链接、详细说明都在那里）
> **使用方法**：完成一项就把 `[ ]` 改成 `[x]`，周末用进度条自我验收

> **版本**：v3 · 17 周完整版（阶段 1 扩展到 W2-4 + 阶段 7 扩展到 W14-16）
> **总时长**：17 周（原 15 周 · +2 周求职冲刺）

---

## 📊 进度总览

| 阶段 | 周次 | 任务数 | 进度 | 状态 |
|---|---|---|---|---|
| 0 · 定方向 | W1 | 23 | `[░░░░░░░░░░] 0/23` | ⬜ 未开始 |
| 1 · 🐍 Python 强化 | W2-4 | 46 | `[░░░░░░░░░░] 0/46` | ⬜ 未开始 |
| 2 · 🚀 First 7 Days Sprint | W5 | 21 | `[░░░░░░░░░░] 0/21` | ⬜ 未开始 |
| 3 · RAG 完整链路 | W6-7 | 40 | `[░░░░░░░░░░] 0/40` | ⬜ 未开始 |
| 4 · Agent 框架 | W8-9 | 33 | `[░░░░░░░░░░] 0/33` | ⬜ 未开始 |
| 5 · 多 Agent + MCP | W10-11 | 38 | `[░░░░░░░░░░] 0/38` | ⬜ 未开始 |
| 6 · 简历级项目 | W12-13 | 46 | `[░░░░░░░░░░] 0/46` | ⬜ 未开始 |
| 7 · 求职冲刺 | W14-16 | 60 | `[░░░░░░░░░░] 0/60` | ⬜ 未开始 |
| **总计** | **17 周** | **~308** | `[░░░░░░░░░░] 0/308` | **0%** |

---

## 🎯 阶段 0 · 定方向（W1 · 10h）

### W1 · D1 周一 · 2h — 概念入门

- [ ] **[30min]** 阅读 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) → 产出：3 句话总结
- [ ] **[30min]** 在 [`docs/concept-notes.md`](docs/concept-notes.md) 写「我的理解」6 个填空
- [ ] **[60min]** 安装 Python 3.11+ / `uv` / VS Code / Git → 产出：环境截图存到 `notes/week1/`
- [ ] **[20min]** 注册 DeepSeek + 充值 10 元 → 产出：API Key 保存到密码管理器

### W1 · D2 周二 · 2h — 5 级能力模型

- [ ] **[30min]** 抄写 L0-L5 能力模型表到 `notes/week1/capability-levels.md`
- [ ] **[30min]** 看 [3Blue1Brown Transformer 视频](https://www.youtube.com/watch?v=wjZofJX0H4A) 前 10 分钟
- [ ] **[60min]** 装 Ollama + 拉 `llama3.2:1b` → 产出：本地跑通对话
- [ ] **[20min]** 笔记：写一句话"我现在理解的 LLM"

### W1 · D3 周三 · 2h — Python 第一次体验

- [ ] **[90min]** 看 [莫烦 Python 入门](https://mofanpy.com/) 1-5 集
- [ ] **[30min]** 写 `sandbox/hello.py` 调 DeepSeek API → 产出：第一次对话输出

### W1 · D4 周四 · 2h — 工具链完善

- [ ] **[40min]** 配置 VS Code：装 Python / Black / isort 扩展
- [ ] **[40min]** 学 Git 基础（init / add / commit / push）+ 建 `agent-learning` 仓库
- [ ] **[40min]** 写仓库 README：贴路线链接 + 第一句目标 → 第一次 git commit
- [ ] **[20min]** 把这一周 GitHub commit 截图保存

### W1 · D5 周五 · 2h — 阶段总结

- [ ] **[60min]** 重读笔记，回答 [`concept-notes.md`](docs/concept-notes.md) 末尾 4 个检验问题
- [ ] **[40min]** 浏览 [`resources.md`](resources.md) 收藏 5 个最需要的资源
- [ ] **[20min]** 写 `notes/week1/summary.md` 本周总结

### ✅ W1 周日验收

- [ ] 能口述 5 级能力模型（L0-L5）
- [ ] 能说出 chatbot / workflow / agent / multi-agent 的区别
- [ ] Python + uv + VS Code + Git + Ollama 全部就绪
- [ ] DeepSeek API 能调通
- [ ] GitHub 仓库有第一个 commit
- [ ] `notes/week1/` 至少 3 篇笔记

---

## 🐍 阶段 1 · Python 强化（W2-4 · 60h）

> **v2 强化版**：W2-3 基础 + 进阶，**W4 新增** LeetCode Easy 20 题 + Pythonic 风格 + LangChain 源码阅读 + File Manager CLI 综合项目。

### W2 · D1 周一 · 2h — 基础语法 1

- [ ] **[40min]** 看 [Real Python: Python Basics](https://realpython.com/python-basics/) 变量/数据类型/f-string
- [ ] **[40min]** 看 列表/字典/元组/集合章节
- [ ] **[40min]** 练习 1：脚本接收 5 个名字 → 按字母排序输出

### W2 · D2 周二 · 2h — 基础语法 2

- [ ] **[40min]** 看 条件/循环/`for...else` 章节
- [ ] **[40min]** 练习 2：统计一段文字的词频（用字典）
- [ ] **[40min]** 练习 3：把一个列表按奇偶拆成两个
- [ ] **[20min]** 笔记 `notes/week2/day2.md`

### W2 · D3 周三 · 2h — 函数

- [ ] **[40min]** 学函数定义 / `*args` / `**kwargs` / lambda
- [ ] **[40min]** 练习 4：函数接收 JSON 字符串返回 dict，校验错误抛异常
- [ ] **[40min]** 练习 5：CLI 读 CSV → 统计 → 写 JSON

### W2 · D4 周四 · 2h — 异常与文件

- [ ] **[30min]** 学 `try/except/finally`
- [ ] **[30min]** 学文件读写 + JSON 模块
- [ ] **[60min]** 实战 `sandbox/tiny-projects/01-chatbot/`：30 行命令行聊天机器人（用 list 存历史）

### W2 · D5 周五 · 2h — 周复盘

- [ ] **[60min]** 复盘 W2 练习 1-6，独立重写一次
- [ ] **[30min]** 写 `notes/week2/summary.md`
- [ ] **[30min]** 自测：能解释 `*args` 和 `dict comprehension`

### ✅ W2 周日验收

- [ ] 6 个练习全部跑通
- [ ] chatbot 能记住对话历史
- [ ] 自己能解释 `*args` / `dict comprehension`

### W3 · D1 周一 · 2h — 类与对象

- [ ] **[40min]** 学 `class` / `__init__` / `self` / 实例方法
- [ ] **[40min]** 练习 7：写 `ChatHistory` 类封装对话历史管理
- [ ] **[40min]** 了解继承 + 装饰器概念（不深究）

### W3 · D2 周二 · 2h — 进阶语法

- [ ] **[40min]** 学生成器（`yield`）
- [ ] **[40min]** 练习 8：写装饰器记录函数执行时间
- [ ] **[40min]** 笔记：装饰器和生成器的使用场景

### W3 · D3 周三 · 2h — 现代 Python

- [ ] **[40min]** 学 `async/await` 基本语法（理解协程）
- [ ] **[40min]** 学类型提示（`def foo(x: int) -> str:`）
- [ ] **[40min]** 练习 9：用 `pydantic` 定义 `LLMRequest` schema

### W3 · D4 周四 · 2h — 配置与工程化

- [ ] **[30min]** 学 `python-dotenv` 读 `.env`
- [ ] **[30min]** 练习 10：用 dotenv 封装 `settings.py`
- [ ] **[60min]** 整理 W2-W3 练习为可复用模块

### W3 · D5 周五 · 2h — 综合项目

- [ ] **[120min]** 综合项目 `sandbox/tiny-projects/02-weather-llm/`：城市 → LLM 决定是否调天气 API → 返回穿衣建议（pydantic + dotenv + requests，100 行内）

### ✅ W3 周日验收

- [ ] 10 个练习全部完成
- [ ] `02-weather-llm` 项目能跑
- [ ] **关键测试**：能说出 LangChain 的 1-2 个核心组件（如 Runnable / PromptTemplate / VectorStore），**源码阅读移到 W4 D4**
- [ ] 不熟悉的知识点列出来，W4 之前补完

---

### W4 · D1 周一 · 2h — LeetCode Easy · 数组 + 字符串

- [ ] **[60min]** 刷 5 道 Easy 数组题：1 两数之和 / 53 最大子数组和 / 88 合并有序数组 / 121 买卖股票最佳时机 / 169 多数元素（每题 12min）
- [ ] **[50min]** 刷 5 道 Easy 字符串题：3 无重复字符最长子串 / 5 最长回文子串 / 14 最长公共前缀 / 28 找出第一个匹配项 / 125 验证回文串
- [ ] **[10min]** 写 `notes/week4/day1-leetcode.md`（每题 3 行：思路 + 时间复杂度 + 空间复杂度）

### W4 · D2 周二 · 2h — LeetCode Easy · 哈希 + 链表

- [ ] **[60min]** 刷 5 道 Easy 哈希题：49 字母异位词分组 / 128 最长连续序列 / 146 LRU 缓存 / 169 多数元素（哈希版）/ 242 有效的字母异位词
- [ ] **[50min]** 刷 5 道 Easy 链表题：21 合并两个有序链表 / 141 环形链表 / 160 相交链表 / 206 反转链表 / 234 回文链表
- [ ] **[10min]** 写 `notes/week4/day2-leetcode.md`

### W4 · D3 周三 · 2h — Pythonic 风格训练

- [ ] **[50min]** 学 7 个 Pythonic 模式（[《流畅的Python》第 1-3 章](https://www.ituring.com.cn/book/2386)）：推导式 / 生成器 / `enumerate` / `zip` / `with` / `defaultdict` / `dataclass`
- [ ] **[60min]** 把 W2-W3 的 5 个练习改写为 Pythonic 版：`ex01` 用 `sorted()` / `ex02` 用 `Counter` / `ex03` 用 filter + 推导式 / `ex04` 用 `dataclass` / `ex05` 用 `defaultdict`
- [ ] **[10min]** 读《流畅的Python》第 1 章 1-2 节

### W4 · D4 周四 · 2h — LangChain 源码阅读

- [ ] **[10min]** 选 1 个核心文件（推荐 [`langchain_core/runnables/base.py`](https://github.com/langchain-ai/langchain/blob/main/libs/core/langchain_core/runnables/base.py)）
- [ ] **[90min]** 精读：画 UML 类图 + 列关键方法表 + 标 Pydantic 用法 + 找装饰器 + 找核心算法（看 80% 即可）
- [ ] **[20min]** 写 `notes/week4/day4-langchain-source.md`（文件作用 + 类图 + 关键方法表 + 学到的设计模式 + 怎么用到自己的 Agent）

### W4 · D5 周五 · 4h — 综合项目 File Manager CLI

- [ ] **[30min]** 设计 `sandbox/tiny-projects/03-file-manager/`：5+ 子命令（search / size / duplicates / sort-by-mtime / batch-rename / export-report）
- [ ] **[120min]** 实现：`settings.py`（pydantic 配置）+ `commands/*.py`（4 个子命令）+ `cli.py`（argparse 主入口）
- [ ] **[45min]** 写 5+ 条 pytest（`test_search.py` / `test_size.py` / `test_duplicates.py`）
- [ ] **[15min]** 写 README（安装 + 使用 + 测试）
- [ ] **[10min]** Git commit：`git commit -m "feat(sandbox): file manager CLI with argparse + pydantic"`

### ✅ W4 周日验收 · 阶段 1 毕业

**知识验收**（不看书回答）：
- [ ] f-string / 推导式 / 生成器各自的最佳场景？
- [ ] 类 vs dataclass 什么时候用哪个？
- [ ] async / await 什么意思？和多线程区别？
- [ ] 装饰器本质是什么？`@wraps` 干嘛用？
- [ ] context manager（`with`）vs 手动 open/close？
- [ ] pydantic 干嘛用？为什么 Agent 框架都用？
- [ ] Pythonic 风格 7 个模式？

**实践验收**：
- [ ] W2 练习（ex01-05 + chatbot）全部跑通
- [ ] W3 练习（ex07-10 + weather-llm）全部跑通
- [ ] W4 新增：LeetCode Easy 20 题（至少 15 题能独立写最优解）
- [ ] W4 新增：5 个 Pythonic 改写完成
- [ ] W4 新增：LangChain 源码笔记完成（含类图）
- [ ] W4 新增：file-manager CLI 跑通（≥ 5 子命令 + ≥ 5 测试）

**关键能力验证**：
- [ ] 随机抽 3 道 LeetCode 题，5 分钟内 AC
- [ ] 打开 `langchain_core/runnables/base.py`，随机 50 行代码能读懂 ≥ 80%
- [ ] 看一段代码，能指出哪里可以更 Pythonic

---

## 🚀 阶段 2 · First 7 Days Sprint（W5 · 14h）

> **整个路线的灵魂**。详细任务见 [`docs/first-7-days-checklist.md`](docs/first-7-days-checklist.md)

### W5 · D1 周一 · 2h — 建立边界

- [ ] **[40min]** 通读 [`docs/first-7-days-checklist.md`](docs/first-7-days-checklist.md) 7 天全貌
- [ ] **[30min]** 重读 [`docs/concept-notes.md`](docs/concept-notes.md) 并回答检验问题
- [ ] **[30min]** 决定项目场景（推荐：个人笔记搜索助手）
- [ ] **[20min]** 画流程图（手绘或 draw.io）→ 存到 `notes/week4/`
- [ ] **[20min]** 回答"启动项目前 7 个问题"

### W5 · D2 周二 · 2h — 手写 Agent

- [ ] **[90min]** 实现 `agent.py` + `tools.py` + `mock_model.py`（限 200 行）
- [ ] **[30min]** 跑通 5 个固定任务：搜索 / 查找 / 总结 / 空任务 / 不存在关键词
- [ ] **验收**：[ ] 跑通 + [ ] 写至少 3 条 trace JSONL

### W5 · D3 周三 · 2h — 工具设计

- [ ] **[30min]** 阅读 [Anthropic: Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [ ] **[90min]** 用 [`docs/tool-card-template.md`](docs/tool-card-template.md) 写 `search_notes` 和 `write_summary` 的 tool card
- [ ] **验收**：[ ] tool card 完整（schema/错误码/例子） + [ ] 参数校验到位

### W5 · D4 周四 · 2h — Context Engineering

- [ ] **[90min]** 实现 `prompts.py` 5 层 context builder
- [ ] **[30min]** 跑同任务 2 次，对比 prompt 结构稳定性
- [ ] **验收**：[ ] 同任务 prompt 结构稳定 + [ ] 5 层命名清晰

### W5 · D5 周五 · 2h — 20 条 Eval

- [ ] **[60min]** 写 20 条 eval cases（10 正常 + 5 边界 + 5 安全）→ `eval_cases.jsonl`，**用 [`docs/eval-case-template.md`](docs/eval-case-template.md) 模板**
- [ ] **[30min]** 跑 eval_runner.py → 产出 `eval_results.json`
- [ ] **[30min]** 失败归因分类（工具/检索/上下文/安全）
- [ ] **验收**：[ ] 20 条跑通 + [ ] 失败归因记录

### W5 · 周末（自由 2-4h）— D6 + D7

- [ ] **[60min]** D6：写 README + eval_report + demo_script（让陌生人能 clone-and-run）
- [ ] **[60min]** D7：复盘 + 用简历模板产出 bullet
- [ ] **[30min]** git commit + push + tag `v1.0-sprint`

### ✅ W5 周日验收

- [ ] 200 行最小 Agent 能跑
- [ ] 2 个 tool card 完整
- [ ] 5 层 context builder 已实现
- [ ] 20 条 eval 跑过，分数记录
- [ ] 简历 bullet 已写好
- [ ] 代码已 commit 到 GitHub

---

## 📚 阶段 3 · RAG 完整链路（W6-7 · 40h）

### W6 · D1 周一 · 2h — FastAPI 入门

- [ ] **[60min]** 看 [FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/) 第 1-4 章
- [ ] **[60min]** 练习：写 `/chat` 接口接收消息返回 mock 回复
- [ ] **验收**：[ ] uvicorn 跑通 + [ ] curl 调用成功

### W6 · D2 周二 · 2h — 文档加载

- [ ] **[40min]** 看 [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [ ] **[40min]** 学 TextLoader / PyPDFLoader
- [ ] **[40min]** 学切片策略：RecursiveCharacterTextSplitter
- [ ] **验收**：[ ] 加载一个 PDF 切好片 + [ ] chunk size 可调

### W6 · D3 周三 · 2h — 向量化

- [ ] **[40min]** 学 Embedding 概念
- [ ] **[40min]** 装 sentence-transformers 或 [BGE 中文](https://huggingface.co/BAAI/bge-small-zh-v1.5)
- [ ] **[40min]** 练习：对 10 个句子做 embedding，前 2 维 PCA 可视化
- [ ] **验收**：[ ] embedding 模型本地能跑

### W6 · D4 周四 · 2h — 向量库 Chroma

- [ ] **[40min]** 看 [Chroma 入门](https://docs.trychroma.com/getting-started)
- [ ] **[40min]** 学持久化存储 + 元数据过滤
- [ ] **[40min]** 把 W6D2 PDF chunks 存入 Chroma，查询返回 top-k
- [ ] **验收**：[ ] Chroma 持久化 + [ ] 相似度检索可用

### W6 · D5 周五 · 2h — 端到端 Naive RAG

- [ ] **[90min]** 写 `rag.py`：query → retrieve → prompt → LLM → answer
- [ ] **[30min]** 接入 FastAPI `/chat` 接口
- [ ] **验收**：[ ] curl 能问到 PDF 里的信息

### ✅ W6 周日验收

- [ ] FastAPI + RAG `/chat` 接口能调通
- [ ] Naive RAG 端到端跑通

### W7 · D1 周一 · 2h — 混合检索

- [ ] **[40min]** 学 BM25 原理（用 `rank_bm25` 库）
- [ ] **[40min]** 学混合检索：BM25 + 向量加权融合
- [ ] **[40min]** 写 `hybrid_retrieve()` 函数
- [ ] **验收**：[ ] 混合检索比单独向量好（人工对比 5 题）

### W7 · D2 周二 · 2h — Reranker

- [ ] **[30min]** 装 [BGE-Reranker](https://huggingface.co/BAAI/bge-reranker-base)
- [ ] **[60min]** 加 Reranker 到 retrieve pipeline
- [ ] **[30min]** 对比有无 Reranker 的 top-5 质量
- [ ] **验收**：[ ] Reranker 集成 + [ ] 至少 1 题明显改善

### W7 · D3 周三 · 2h — RAG 评估

- [ ] **[40min]** 看 [RAGAS 文档](https://docs.ragas.io/) Faithfulness / Relevancy / Precision / Recall
- [ ] **[40min]** 写 10 条 QA 对（基于你的 PDF 内容）
- [ ] **[40min]** 用 RAGAS 评估你的 RAG
- [ ] **验收**：[ ] faithfulness > 0.7

### W7 · D4 周四 · 2h — 可观测性

- [ ] **[30min]** 注册 [LangSmith](https://www.langchain.com/langsmith)
- [ ] **[30min]** 配置 LangSmith 环境变量
- [ ] **[60min]** 看 retrieve + generate 的延迟和 token
- [ ] **验收**：[ ] LangSmith 上能看到 trace

### W7 · D5 周五 · 2h — Docker 打包

- [ ] **[40min]** 写 `Dockerfile`（FastAPI + Chroma）
- [ ] **[40min]** 写 `docker-compose.yml`（RAG + Chroma + Redis）
- [ ] **[40min]** 本地 `docker compose up` 跑通
- [ ] **验收**：[ ] 一键启动 + [ ] 数据持久化

### ✅ W7 周日验收

- [ ] RAG 系统 Docker 一键启动
- [ ] RAGAS faithfulness > 0.7
- [ ] P99 延迟 < 2 秒
- [ ] LangSmith 上有评估记录

---

## 🕸 阶段 4 · Agent 框架（W8-9 · 40h）

### W8 · D1 周一 · 2h — LangGraph 入门

- [ ] **[60min]** 看 [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/)
- [ ] **[60min]** 用 LangGraph 重写 W5 的最小 Agent
- [ ] **验收**：[ ] StateGraph 跑通

### W8 · D2 周二 · 2h — 状态管理

- [ ] **[40min]** 学 Reducer：`add_messages` / 覆盖 vs 累加
- [ ] **[40min]** 学 State 更新模式 + `print_state()` 调试
- [ ] **[40min]** 练习：加"对话历史"节点
- [ ] **验收**：[ ] 状态变化可观察

### W8 · D3 周三 · 2h — Conditional Edge

- [ ] **[40min]** 学路由函数 + 循环检测
- [ ] **[80min]** 练习：根据"是否需要工具"决定下一步
- [ ] **验收**：[ ] 不会无限循环 + [ ] 决策可视化

### W8 · D4 周四 · 2h — Checkpoint 持久化

- [ ] **[40min]** 学 `MemorySaver` / `SqliteSaver` / `PostgresSaver`
- [ ] **[40min]** 学 `thread_id`：恢复之前的对话
- [ ] **[40min]** 学时间旅行：回到任意一步重跑
- [ ] **验收**：[ ] checkpoint 恢复可用

### W8 · D5 周五 · 2h — 人在回路（HITL）

- [ ] **[40min]** 学 `interrupt_before` / `interrupt`
- [ ] **[60min]** 练习：写文件前必须用户输入 `y` 才执行
- [ ] **[20min]** 画 LangGraph 图：`draw_mermaid_png()`
- [ ] **验收**：[ ] HITL 中断 + 恢复 + [ ] 图可视化

### ✅ W8 周日验收

- [ ] LangGraph 图可视化（`draw_mermaid_png()`）
- [ ] State 管理明确（TypedDict）
- [ ] Checkpoint 能恢复
- [ ] HITL 能中断 + 恢复

### W9 · D1 周一 · 2h — Tool Calling 深入

- [ ] **[40min]** 学 OpenAI Function Calling schema
- [ ] **[40min]** 学 Anthropic Tool Use
- [ ] **[40min]** 把 `search_notes` 换成真实向量检索
- [ ] **验收**：[ ] 真实检索可用

### W9 · D2 周二 · 2h — Pydantic AI

- [ ] **[60min]** 看 [Pydantic AI 文档](https://ai.pydantic.dev/)
- [ ] **[60min]** 用 Pydantic AI 重写最小 Agent
- [ ] **验收**：[ ] 类型化输出 + [ ] schema 强制

### W9 · D3 周三 · 2h — LangSmith 接入

- [ ] **[30min]** 配置 LangSmith 环境变量
- [ ] **[40min]** 自动 trace 调试
- [ ] **[50min]** 看每一步的输入输出
- [ ] **验收**：[ ] LangSmith 能看到 trace

### W9 · D4 周四 · 2h — 多框架对比

- [ ] **[60min]** 跑 AutoGen Demo
- [ ] **[60min]** 跑 CrewAI Demo
- [ ] **验收**：[ ] 各自有 example 跑通

### W9 · D5 周五 · 2h — 对比博客

- [ ] **[120min]** 写一篇博客对比 LangGraph / OpenAI Agents SDK / Pydantic AI / AutoGen → 发布到知乎/掘金

### ✅ W9 周日验收

- [ ] LangGraph Agent 能跑 + 可视化 + checkpoint + HITL
- [ ] LangSmith 上能看到 trace
- [ ] 框架对比博客已发布

---

## 🤖 阶段 5 · 多 Agent + MCP + 工程化（W10-11 · 40h）

### W10 · D1 周一 · 2h — AutoGen 多 Agent

- [ ] **[60min]** 看 [AutoGen Quickstart](https://microsoft.github.io/autogen/)
- [ ] **[60min]** 写"研究报告小组"：researcher / writer / reviewer
- [ ] **验收**：[ ] 3 个 Agent 协作

### W10 · D2 周二 · 2h — CrewAI 多 Agent

- [ ] **[60min]** 看 [CrewAI 文档](https://docs.crewai.com/)
- [ ] **[60min]** 用 CrewAI 重写"研究报告小组"
- [ ] **验收**：[ ] CrewAI 跑通

### W10 · D3 周三 · 2h — LangGraph 多 Agent

- [ ] **[40min]** 学子图（Subgraph）+ Supervisor 模式
- [ ] **[40min]** 学 Agent handoff
- [ ] **[40min]** 用 LangGraph 实现 planner / executor / reviewer
- [ ] **验收**：[ ] 3 Agent 跑通

### W10 · D4 周四 · 2h — MCP 入门

- [ ] **[40min]** 看 [MCP 官方文档](https://modelcontextprotocol.io/)
- [ ] **[40min]** 学 MCP 三大原语：tools / resources / prompts
- [ ] **[40min]** 装 [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [ ] **验收**：[ ] SDK 装好

### W10 · D5 周五 · 2h — 自建 MCP Server

- [ ] **[60min]** 写 MCP server 暴露 `read_file` / `list_dir`
- [ ] **[30min]** 用 Claude Desktop 连接你的 MCP server
- [ ] **[30min]** 测试：让 Claude 读你电脑上的文件
- [ ] **验收**：[ ] Claude Desktop 能连 MCP server

### ✅ W10 周日验收

- [ ] 3 Agent 协作跑通（AutoGen 或 CrewAI 或 LangGraph 任选）
- [ ] 自建 MCP server 跑通
- [ ] Claude Desktop 能连你的 MCP server

### W11 · D1 周一 · 2h — 性能优化

- [ ] **[40min]** 学异步并发（`asyncio.gather`）
- [ ] **[40min]** 学 Redis 缓存策略
- [ ] **[40min]** 学 Token 优化：截断长 context
- [ ] **验收**：[ ] 至少 1 项性能提升

### W11 · D2 周二 · 2h — 安全防御

- [ ] **[40min]** 学 Prompt Injection 类型（直接/间接）
- [ ] **[40min]** 学防御：输入过滤 / 工具白名单 / 最小权限 / Audit log
- [ ] **[40min]** 看 [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [ ] **验收**：[ ] 至少 3 种防御策略已实现

### W11 · D3 周三 · 2h — 监控日志

- [ ] **[40min]** 学 `structlog` 结构化日志
- [ ] **[40min]** 接入 OpenTelemetry / LangSmith trace
- [ ] **[40min]** 统计指标：成功率 / 延迟 / token 成本
- [ ] **验收**：[ ] 监控 dashboard 跑通

### W11 · D4 周四 · 2h — 部署 Railway

- [ ] **[30min]** 注册 [Railway](https://railway.app/) + 装 CLI
- [ ] **[60min]** 把 W3 RAG 部署到 Railway
- [ ] **[30min]** 验证公开 URL 可访问
- [ ] **验收**：[ ] demo URL 公开可访问

### W11 · D5 周五 · 2h — Docker Compose 完善 + LeetCode Medium

- [ ] **[50min]** 多服务编排（RAG + Chroma + Redis + LangSmith）
- [ ] **[30min]** 环境变量管理 + 健康检查 + 部署文档
- [ ] **[40min]** **LeetCode Medium 5 道**（动态规划 / 回溯 / 图论 精选，求职高频）：最长上升子序列 / 零钱兑换 / 课程表 / 全排列 / 单词搜索
- [ ] **验收**：[ ] 一键 `docker compose up` 全跑 + [ ] Medium 至少 3 题独立 AC

### ✅ W11 周日验收

- [ ] RAG / Agent 服务部署上线（Railway 公开 URL）
- [ ] 监控 + trace + 日志全开
- [ ] demo URL 写进简历

---

## 🏆 阶段 6 · 简历级项目（W12-13 · 40h）

### W12 · 项目 1 · 个人知识库助手

#### W12 · D1 周一 · 2h — 设计

- [ ] **[60min]** 写需求文档（用户场景 / 功能列表 / 非目标）
- [ ] **[60min]** 画架构图（FastAPI + LangGraph + Chroma + MCP + 前端）→ draw.io
- [ ] **验收**：[ ] 架构图清晰 + [ ] 需求文档完整

#### W12 · D2 周二 · 4h — 后端骨架

- [ ] **[60min]** FastAPI 骨架（路由 / 中间件 / 配置）
- [ ] **[60min]** LangGraph Agent 骨架
- [ ] **[60min]** 接入 DeepSeek / OpenAI
- [ ] **[60min]** WebSocket 流式输出
- [ ] **验收**：[ ] `/chat` 接口能流式返回

#### W12 · D3 周三 · 4h — RAG pipeline

- [ ] **[60min]** 文档加载（PDF / Markdown / Notion）
- [ ] **[60min]** 切片 + embedding + 混合检索
- [ ] **[60min]** 接入 LangGraph RAG 节点
- [ ] **[60min]** LangSmith trace 接入
- [ ] **验收**：[ ] 上传 PDF 后能问答 + [ ] LangSmith 有 trace

#### W12 · D4 周四 · 4h — MCP 集成

- [ ] **[60min]** MCP server：filesystem（read/write/list）
- [ ] **[60min]** MCP server：GitHub（搜索仓库/读 issue）
- [ ] **[60min]** Agent 工具注册 + 调度
- [ ] **[60min]** 集成测试
- [ ] **验收**：[ ] Agent 能通过 MCP 读 GitHub repo

#### W12 · D5 周五 · 4h — 前端 + 评估

- [ ] **[60min]** Streamlit / Next.js 前端（最小可用）
- [ ] **[60min]** 30 条 eval case 编写
- [ ] **[60min]** RAGAS 评估 + 修复弱项
- [ ] **[60min]** 录 demo 视频（≤ 3 分钟）
- [ ] **验收**：[ ] eval case 通过率 > 80% + [ ] demo 视频已录

### ✅ W12 周日验收

- [ ] 项目 1 端到端跑通
- [ ] 30 条 eval case 通过率 > 80%
- [ ] demo 视频 ≤ 3 分钟
- [ ] README + 架构图 + eval 报告

### W13 · 项目 2 · 自动化研究 Agent

#### W13 · D1 周一 · 2h — 设计

- [ ] **[60min]** 整体设计 + 接口定义
- [ ] **[60min]** 拆分任务：Planner / Researcher / Reviewer 三 Agent
- [ ] **验收**：[ ] 设计文档完整

#### W13 · D2 周二 · 4h — 搜索 + 抓取

- [ ] **[60min]** 接入 Tavily / SerpAPI 搜索
- [ ] **[60min]** 接入 Jina Reader 网页抓取
- [ ] **[60min]** 工具卡 + 错误处理
- [ ] **[60min]** Researcher Agent 实现
- [ ] **验收**：[ ] 能搜 + 能抓取网页

#### W13 · D3 周三 · 4h — 阅读 + 总结

- [ ] **[60min]** Planner Agent（任务拆分）
- [ ] **[60min]** 阅读 Agent（提取关键信息）
- [ ] **[60min]** 总结 Agent（生成 Markdown）
- [ ] **[60min]** 引用追踪
- [ ] **验收**：[ ] 能生成结构化报告

#### W13 · D4 周四 · 4h — Reviewer + HITL

- [ ] **[60min]** Reviewer Agent（审稿修改）
- [ ] **[60min]** HITL 中断确认
- [ ] **[60min]** Supervisor 调度
- [ ] **[60min]** 时间旅行 checkpoint
- [ ] **验收**：[ ] 人能在中途干预 + [ ] checkpoint 恢复

#### W13 · D5 周五 · 4h — 收尾

- [ ] **[60min]** 项目 2 README 完整化（架构图 + demo + 限制）
- [ ] **[60min]** 项目 2 eval case（30 条）
- [ ] **[60min]** 录项目 2 demo 视频
- [ ] **[60min]** git tag `v1.0-portfolio` + push
- [ ] **验收**：[ ] 2 个项目均完整

### ✅ W13 周日验收

- [ ] 2 个项目上线（demo URL 可访问）
- [ ] 每个项目 30 条 eval case
- [ ] 每个项目 README + 架构图 + demo 视频
- [ ] 2 段简历 bullet 已写好
- [ ] GitHub 有 2 个 star-worthy 仓库

---

## 💼 阶段 7 · 求职冲刺（W14-16 · 42h）

> **v2 扩展**：从 2 周扩到 3 周，给投递 + 刷题 + 模拟面试足够时间。W14 主投递 + 项目讲解训练，W15 刷题 + 模拟面试，W16 内推 + 真实面试准备。

### W14 · D1 周一 · 2h — 简历重写

- [ ] **[40min]** 用 STAR 法则重写项目经验 1（知识库助手）
- [ ] **[40min]** 用 STAR 法则重写项目经验 2（研究 Agent）
- [ ] **[20min]** 技能清单：Python / LangGraph / RAG / FastAPI / MCP
- [ ] **[20min]** 让 AI 朋友帮你看一遍 → 修改
- [ ] **验收**：[ ] 简历 1 页 + [ ] 项目量化指标清晰

### W14 · D2 周二 · 2h — 投递准备

- [ ] **[60min]** 写 3 句话自我介绍（项目 + 技术栈 + 优势）
- [ ] **[60min]** 在 5 个平台注册：Boss / 拉勾 / LinkedIn / V2EX / 掘金

### W14 · D3 周三 · 2h — 投递日 1

- [ ] **[20min]** 准备简历 PDF + 作品集链接
- [ ] **[100min]** 投 15 个岗位（个性化打招呼）
- [ ] **验收**：[ ] 当日 ≥ 15 投

### W14 · D4 周四 · 2h — 投递日 2

- [ ] **[120min]** 投 15 个岗位
- [ ] **验收**：[ ] 当日 ≥ 15 投

### W14 · D5 周五 · 2h — 复盘 + 内推

- [ ] **[40min]** 复盘投递情况：哪些岗位已读不回 → 改话术
- [ ] **[40min]** 在 GitHub 项目 README 加"求内推"
- [ ] **[40min]** 主动找 3 个朋友内推

### ✅ W14 周日验收

- [ ] 简历定稿
- [ ] 投递 ≥ 30 个
- [ ] 至少 3 个内推渠道已联系

### W15 · D1 周一 · 2h — 高频题复习

- [ ] **[60min]** 看 [AgentGuide 01-theory-questions](https://github.com/adongwanai/AgentGuide/blob/main/docs/04-interview/01-theory-questions.md) 100 题
- [ ] **[60min]** 看 [02-rag-questions](https://github.com/adongwanai/AgentGuide/blob/main/docs/04-interview/02-rag-questions.md) 50 题
- [ ] **验收**：[ ] 至少答出 30 道

### W15 · D2 周二 · 2h — Agent + LLM 题

- [ ] **[60min]** 看 [03-agent-questions](https://github.com/adongwanai/AgentGuide/blob/main/docs/04-interview/03-agent-questions.md) 50 题
- [ ] **[60min]** 看 [16-llm-fundamentals](https://github.com/adongwanai/AgentGuide/blob/main/docs/04-interview/16-llm-fundamentals.md) Transformer / 训练

### W15 · D3 周三 · 2h — LeetCode + 算法

- [ ] **[30min]** LeetCode Hot 100 复习（数组 / 字符串 / 哈希）
- [ ] **[60min]** LeetCode Medium 进阶（DP / 回溯 / 图，至少 5 道新题）
- [ ] **[30min]** LeetCode Hot 100（链表 / 二叉树）
- [ ] **验收**：[ ] 至少 5 题能用最优解讲清 + [ ] Medium 至少 3 题 AC

### W15 · D4 周四 · 2h — 模拟面试 1

- [ ] **[120min]** 找朋友 / 网友模拟面试（视频会议）
- [ ] **[20min]** 写复盘：哪些问题答得不好
- [ ] **验收**：[ ] 1 次完整模拟面试

### W15 · D5 周五 · 2h — 模拟面试 2 + 反问

- [ ] **[60min]** 模拟面试 2（重点讲项目）
- [ ] **[30min]** 准备 3 个反问面试官的问题
- [ ] **[30min]** 复盘 → 调整自我介绍

### ✅ W15 周日验收

- [ ] 投递 ≥ 30 个
- [ ] 模拟面试 ≥ 2 次
- [ ] 收到 ≥ 1 个面试邀请
- [ ] 30 道高频题能答出 20+

---

### W16 · D1 周一 · 2h — 内推冲刺 + 持续投递

- [ ] **[40min]** 在 GitHub 仓库、掘金、知乎发"求职动态"+ 求内推帖
- [ ] **[40min]** 主动给目标公司的 senior 发 LinkedIn 私信（≥ 10 人）
- [ ] **[40min]** 补充投递：把 W14 没投的岗位补完，目标 50 个

### W16 · D2 周二 · 2h — 项目讲解专项

- [ ] **[40min]** **5 分钟讲清项目 1**：用 STAR 法则 + 画架构图 + 量化指标（成功率 % / 延迟 ms / 成本下降 %），录视频回看
- [ ] **[40min]** **5 分钟讲清项目 2**：同上，重点突出多 Agent 协作 + HITL 设计
- [ ] **[40min]** **八大组件逐个讲解**：Goal / Policy / State / Memory / Context Builder / Tool Registry / Loop Controller / Eval & Trace（每组件 1 分钟录音）
- [ ] **[20min]** 找朋友/网友 mock 讲一遍，收反馈

### W16 · D3 周三 · 2h — 行业动态 + 公司研究

- [ ] **[30min]** 读 [Simon Willison's Weblog](https://simonwillison.net/) 最近 1 周 + [LangChain Blog](https://blog.langchain.com/) 最近 1 月 → 写 `notes/week16/industry.md`
- [ ] **[60min]** 选 3 家目标公司，深入研究：技术栈 / 团队 / 最近 Agent 相关产品 → 写 `notes/week16/companies.md`
- [ ] **[30min]** 准备 5 个"反问面试官"的高质量问题（团队当前 Agent 应用 / 技术选型理由 / 工程文化等）

### W16 · D4 周四 · 2h — 模拟面试 3 + 谈薪准备

- [ ] **[80min]** 模拟面试 3（重点：项目深挖 + 反问面试官 + 谈薪模拟）
- [ ] **[20min]** 复盘：把前 3 次模拟面试的问题归类（系统设计 / 项目细节 / 行为面试），对弱项加练
- [ ] **[20min]** 谈薪：了解 base + 期权 + RSU 计算方式，准备期望薪资区间（基于市场调研）

### W16 · D5 周五 · 2h — 复盘 + Offer 谈判

- [ ] **[40min]** 投递 / 面试 / Offer 漏斗复盘：哪个环节卡住最多 → 优化
- [ ] **[40min]** Offer 收到 → 谈判脚本（不卑不亢 / 强调对方优势 / 给对方"竞争 Offer"压力）
- [ ] **[40min]** 整理 17 周学习笔记为博客：写《零基础 17 周转行 Agent 工程师》→ 发知乎/掘金

### ✅ W16 周日验收 · 17 周毕业

- [ ] 拿到 ≥ 1 个 Offer **或** ≥ 3 个面试进入终面
- [ ] 5 分钟项目讲解视频录好
- [ ] 八大组件录音讲解完成
- [ ] 公司研究报告 + 反问问题清单完成
- [ ] 17 周博客发布
- [ ] GitHub 2 个 star-worthy 仓库

---

## 🎯 最终验收（17 周结束时自检）

### 技术产出

- [ ] GitHub 有 2 个 star-worthy 仓库（README + 能跑 + eval）
- [ ] 1 篇技术博客已发布（框架对比 / 项目总结）
- [ ] 1 个上线 demo URL（Railway / HuggingFace）

### 知识掌握

- [ ] 能用 5 分钟讲清 2 个项目（架构 + 量化指标）
- [ ] 能答 30 道高频题（不看书）
- [ ] 能现场画 Agent 架构图（LangGraph / MCP / RAG）

### 求职

- [ ] 简历 1 页（量化、清晰、可信）
- [ ] 投递 ≥ 30 个
- [ ] 至少 1 次真实面试

---

## 📌 维护说明

**怎么更新进度**：
1. 完成任务把 `[ ]` 改成 `[x]`
2. 周末数一下 `[x]` 数量 → 更新顶部进度条
3. 卡住的任务不动它，列出问题下次问

**卡住了怎么办**：
- 单个 task 卡 < 30min：直接查文档 / Google
- 单个 task 卡 > 1h：跳过，下周再回来看
- 整个 stage 卡：看 [`learning-roadmap.md`](docs/learning-roadmap.md) 末尾「风险预案」

**怎么砍**：
- UI / 装饰 / 美化 → **第一个砍**
- 多框架对比 / 多模型实验 → **第二个砍**
- 核心产出（Agent 能跑、RAG 能查、项目能 demo）→ **绝不砍**

---

## 🗂 配套文档

| 文档 | 用途 |
|---|---|
| [`README.md`](README.md) | 总览 + 进度追踪 |
| [`docs/learning-roadmap.md`](docs/learning-roadmap.md) | 每项任务的详细说明 + 资源链接 |
| [`docs/first-7-days-checklist.md`](docs/first-7-days-checklist.md) | 阶段 2 的 D1-D7 详细任务 |
| [`docs/concept-notes.md`](docs/concept-notes.md) | Agent 概念笔记模板 |
| [`docs/tool-card-template.md`](docs/tool-card-template.md) | 工具卡模板 |
| [`docs/eval-case-template.md`](docs/eval-case-template.md) | ⭐⭐ Eval case 模板（30+ 条标准 + 评分公式 + eval_runner.py 模板） |
| [`resources.md`](resources.md) | 所有外部资源索引 |
| [`TODO.md`](TODO.md) | **本文件**：每日可勾选的 todo list** |

---

**祝你 17 周后拿到 Offer 🎉**

> 进度可视化提醒：每完成一个 stage 把顶部对应行的 `[░░░░░░░░░░]` 改成对应数量的 `[▓]`，例如完成 10/22 就是 `[▓▓▓▓▓░░░░░]`。