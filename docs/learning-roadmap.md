# 📋 Agent 开发学习路线 · 求职定制版

> **你的画像**：每天 2h · 求职/转行 · 完全零基础
> **总投入**：15 周 × 5 天 × 2h = 150h（不含周末自由复习）
> **方法论**：做出什么 > 学过什么（源自 AgentGuide）
>
> **v2 变更**：阶段 1 从 W2-3 扩到 W2-4（+1 周），新增 LeetCode + Pythonic 训练 + LangChain 源码阅读

---

## 🗺 15 周全景图

```
Week  1 ━━━ 阶段 0：定方向（不写代码）
Week 2-4 ━━ 阶段 1：🐍 Python 强化（基础 + LeetCode + 源码）
Week  5 ━━━ 阶段 2：🚀 First 7 Days Sprint（最小 Agent）
Week 6-7 ━━ 阶段 3：RAG 完整链路
Week 8-9 ━━ 阶段 4：Agent 框架（LangGraph 重点）
Week 10-11 ━ 阶段 5：多 Agent + MCP + 工程化
Week 12-13 ━ 阶段 6：2 个简历级项目
Week 14-15 ━ 阶段 7：求职冲刺
```

| 阶段 | 周 | 总时长 | 核心产出 | 阶段验收标准 |
|---|---|---|---|---|
| 0 | W1 | 10h | 1 页概念笔记 + 环境就绪 | 能复述 5 级能力模型 + 装好 Python/VS Code/API Key |
| 1 | W2-4 | 60h | 11 练习 + 3 项目 + LeetCode 20 题 | 能读懂 LangChain 源码 80% + Pythonic |
| 2 | W6 | 14h | 200 行最小 Agent + 20 eval | clone-and-run + 简历 bullet 已写 |
| 3 | W7-7 | 40h | 端到端 RAG 系统 | PDF 问答 RAG + FastAPI + Docker |
| 4 | W9-9 | 40h | LangGraph 重写 + trace | 状态可视化 + checkpoint 恢复 |
| 5 | W11-11 | 40h | 多 Agent + MCP + 性能 | 3 个 Agent 协作 + 自建 MCP server |
| 6 | W13-13 | 40h | 2 个简历级项目 | 上线可演示 + 量化指标 |
| 7 | W15-15 | 28h | 简历 + 面试冲刺 | 投递 30+ 简历 + 5 次模拟面试 |

---

## ⏰ 每日 2h 时间分配模板

```
┌──────────────────────────────────────────────────────┐
│ 每日 2h 标准分配                                     │
├──────────────────────────────────────────────────────┤
│ 0-15 min  昨日复盘（5 min）+ 今日计划（5 min）+      │
│           看昨日笔记（5 min）                        │
│ 15-50 min 概念输入（看书/看文档/看视频）             │
│ 50-110 min 动手实战（写代码/做练习/调试）            │
│ 110-120min 当日笔记 + 明日待办                       │
└──────────────────────────────────────────────────────┘
```

**核心原则**：30% 看，70% 写。**只看不练 = 没学**。

---

## 📦 阶段 0 · 定方向（第 1 周 · 10h）

> **目标**：理解 Agent 是什么，准备好工具链，**不写代码**。

### W1 · Day 1（周一 · 2h）— 概念入门

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 阅读 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)（中文版可搜"构建有效的 Agent"） | 3 句话总结 |
| 30-60 min | 阅读 `docs/concept-notes.md`，用自己的话写"我的理解"6 填空 | 完成笔记 |
| 60-90 min | 安装环境：Python 3.11+、`uv`、VS Code、Git | 环境就绪截图 |
| 90-120 min | 注册 DeepSeek 账号，开通 API Key（充值 10 元够学） | API Key 保存到密码管理器 |

**验收**：能口述 chatbot / workflow / agent / multi-agent 的区别。

### W1 · Day 2（周二 · 2h）— 5 级能力模型

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-30 min | 阅读 `docs/concept-notes.md` 的"五级能力模型"章节 | 抄写 L0-L5 表格 |
| 30-60 min | 看视频 [3Blue1Brown: Transformers](https://www.youtube.com/watch?v=wjZofJX0H4A) 前 10 分钟（直观理解 LLM） | 1 句"我现在理解的 LLM" |
| 60-120 min | 安装 Ollama + 拉一个本地小模型（llama3.2:1b 或 qwen2.5:1.5b） | 本地模型跑通 |

**验收**：本地能用 Ollama 跑模型，看到输出。

### W1 · Day 3（周三 · 2h）— Python 第一次体验

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-90 min | 看视频 [Python 入门教程（莫烦 Python）](https://mofanpy.com/) 第 1-5 集 | 笔记 |
| 90-120 min | 写第一个脚本 `hello.py`：用 `requests` 调一次 DeepSeek API，看到对话输出 | `hello.py` 文件 |

**验收**：能调通 LLM API，看到 AI 回复。

### W1 · Day 4（周四 · 2h）— 工具链完善

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-40 min | 配置 VS Code：装 Python 扩展、设置格式化（Black + isort） | VS Code 截图 |
| 40-80 min | 学 Git 基础：init / commit / push，建一个 GitHub 仓库叫 `agent-learning` | 仓库就绪 |
| 80-120 min | 写 README：贴上学习路线链接，写一句"我的目标" | 第一次 git commit |

**验收**：GitHub 仓库存在，第一个 commit。

### W1 · Day 5（周五 · 2h）— 阶段总结

| 时间 | 任务 | 产出 |
|---|---|---|
| 0-60 min | 重读自己的笔记，回答 `concept-notes.md` 末尾的 4 个检验问题 | 答案写在笔记里 |
| 60-120 min | 浏览 [resources.md](../../resources.md)，收藏 5 个觉得最需要的资源 | 收藏夹 |

### 🎯 W1 周日验收（30 min · 自由时间）

- [ ] 能口述 5 级能力模型
- [ ] Python + uv + VS Code + Git + Ollama 全部就绪
- [ ] DeepSeek API 能调通
- [ ] GitHub 仓库有第一个 commit
- [ ] 笔记 `notes/week1/` 至少 3 篇

---

## 📦 阶段 1 · 🐍 Python 强化（第 2-4 周 · 60h）

> **v2 更新**：阶段从 2 周扩到 3 周。W2-3 为基础+进阶，W4 为实战强化（LeetCode + Pythonic + LangChain 源码）。

> **目标**：能读懂 LangChain 源码片段，能写 100 行的 CLI 工具。
> **不要追求精通**——目标是"够用"。

### W2 · Day 1-2（周一-周二 · 4h）— 基础语法

**资源**：[Real Python: Python Basics](https://realpython.com/python-basics/) 或《Python编程：从入门到实践》第 1-6 章

**必学**：
- 变量、数据类型、字符串（f-string）
- 列表 / 字典 / 元组 / 集合
- 条件、循环、`for...else`

**练习**（`sandbox/week2-basics/`）：
1. 写一个脚本，输入 5 个名字，输出按字母排序
2. 写一个脚本，统计一段文字的词频（用字典）
3. 写一个脚本，把一个列表按奇偶拆成两个

### W2 · Day 3-4（周三-周四 · 4h）— 函数与异常

**必学**：
- 函数定义、`*args` / `**kwargs`
- lambda、列表推导式
- 异常处理 `try / except / finally`
- 文件读写、JSON

**练习**：
4. 写一个函数，传入 JSON 字符串返回 dict，参数校验错误抛异常
5. 写一个 CLI：读 CSV → 统计 → 写 JSON
6. **实战**：`sandbox/tiny-projects/01-chatbot/` — 写一个 30 行的命令行聊天机器人

### W2 · Day 5（周五 · 2h）— 周复盘 + 弱项补强

**验收**：能独立写出 Day 1-4 的练习。

### 🎯 W2 周日验收

- [ ] 6 个练习全部跑通
- [ ] chatbot 能记住对话历史（用 list）
- [ ] 自己能解释什么是 `*args`、什么是 `dict comprehension`

### W3 · Day 1-2（周一-周二 · 4h）— 进阶语法

**必学**：
- 类与对象：`__init__`、`self`、实例方法
- 继承（简单了解）
- 装饰器（理解概念即可，不深究）
- 生成器（`yield`）

**练习**：
7. 写一个 `ChatHistory` 类，封装对话历史的管理
8. 写一个简单的装饰器：记录函数执行时间

### W3 · Day 3-4（周三-周四 · 4h）— 现代 Python

**必学**：
- `async / await` 基本语法（理解协程概念）
- 类型提示（`def foo(x: int) -> str:`）
- `pydantic` BaseModel（Agent 项目里大量用）
- `python-dotenv` 读 .env

**练习**：
9. 用 pydantic 定义一个 `LLMRequest` schema
10. 用 dotenv 读 API key，封装成 `settings.py`

### W3 · Day 5（周五 · 2h）— 综合实战项目

**项目**：`sandbox/tiny-projects/02-weather-llm/`
- 输入城市 → LLM 决定要不要调天气 API → 返回穿衣建议
- 用 pydantic + dotenv + requests
- 100 行内

### 🎯 W3 周日验收

- [ ] 10 个练习全部完成
- [ ] `02-weather-llm` 项目能跑
- [ ] **关键测试**：打开 [LangChain 源码](https://github.com/langchain-ai/langchain)，找到 `core/runnables/base.py`，能读懂 60% 以上

---

## 📦 阶段 1 强化 · 🐍 Python 实战（第 4 周 · 20h）🆕

> **v2 新增**：在进入 Agent 之前，先用 1 周时间强化 Python 实战能力，确保求职算法题 + 源码阅读都过关。
> 详细每日任务见 [`todos/01-stage-1/W4-D1-mon.md`](../todos/01-stage-1/W4-D1-mon.md)

### W4 · Day 1（周一 · 2h）— LeetCode 数组 + 字符串
- 刷 10 道 Easy：两数之和、最大子数组和、合并有序数组、最长回文子串、字母异位词分组等
- 每题 12 分钟（思路 4min + 代码 4min + 验证 4min）

### W4 · Day 2（周二 · 2h）— LeetCode 哈希 + 链表
- 刷 10 道 Easy：LRU 缓存、合并有序链表、反转链表、回文链表等

### W4 · Day 3（周三 · 2h）— Pythonic 风格训练
- 7 个 Pythonic 模式：推导式、生成器、enumerate、zip、with、defaultdict、dataclass
- 把 W2-W3 的 5 个练习改写为 Pythonic 版

### W4 · Day 4（周四 · 2h）— 读 LangChain 源码
- 精读 `langchain_core/runnables/base.py`
- 画类图、记关键方法、总结设计模式

### W4 · Day 5（周五 · 4h）— 综合项目 File Manager CLI
- 用 argparse + pydantic + dotenv + pytest 写一个完整 CLI 工具
- ≥ 5 子命令 + ≥ 5 测试 + README

### 🎯 W4 周日验收
- [ ] LeetCode Easy 20 题（至少 15 题能独立写最优解）
- [ ] 5 个 Pythonic 改写完成
- [ ] LangChain 源码笔记完成
- [ ] file-manager CLI 跑通

---

## 📦 阶段 2 · 🚀 First 7 Days Sprint（第 5 周 · 14h）

> **整个路线的灵魂**——7 天内产出 1 个可演示、可评估、有 trace 的最小 Agent。
> 详细任务见 [`docs/first-7-days-checklist.md`](first-7-days-checklist.md)

### W6 · Day 1（周一 · 2h）— 建立边界

- 阅读 `first-7-days-checklist.md` D1 部分
- 决定项目场景：**个人笔记搜索助手**（推荐）
- 画流程图 + 回答 7 个问题

### W4 · Day 2（周二 · 2h）— 手写 Agent

- 实现 `agent.py` + `tools.py` + `mock_model.py`
- 跑通 5 个固定任务
- **关键**：这一天的代码量决定你理解 Agent 的深度

### W4 · Day 3（周三 · 2h）— 工具设计

- 写 2 个 tool card（用 `tool-card-template.md`）
- 实现工具的参数校验、错误码

### W4 · Day 4（周四 · 2h）— Context Engineering

- 实现 5 层 context builder（`prompts.py`）
- 跑同任务 2 次，验证 prompt 结构稳定

### W4 · Day 5（周五 · 2h）— 20 条 Eval

- 写 20 条 eval cases（10 正常 + 5 边界 + 5 安全）
- 跑一遍，记录分数
- 失败归因（这是 Day 7 简历材料）

### W4 · 周末（自由 2-4h）— Day 6 + Day 7

- Day 6：写 README + eval_report + demo_script
- Day 7：复盘 + 简历 bullet

### 🎯 W4 周日验收

- [ ] 200 行最小 Agent 能跑
- [ ] 2 个 tool card 完整
- [ ] 5 层 context builder 已实现
- [ ] 20 条 eval 跑过，分数记录
- [ ] 简历 bullet 已写好
- [ ] **commit 到 GitHub**

---

## 📦 阶段 3 · RAG 完整链路（第 5-6 周 · 40h）

> **目标**：端到端 RAG 系统 + FastAPI + Docker

### W6 · Day 1（周一 · 2h）— FastAPI 入门

**资源**：[FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/) 第 1-4 章

**必学**：
- 路由、`@app.get` / `@app.post`
- Pydantic 请求/响应模型
- 启动 Uvicorn

**练习**：写一个 `/chat` 接口，接收消息返回 mock 回复

### W6 · Day 2（周二 · 2h）— 文档加载

**资源**：[LangChain: Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)

**必学**：
- TextLoader、PyPDFLoader
- 切片策略：按段落、按 token（RecursiveCharacterTextSplitter）

**练习**：加载一个 PDF，切片，观察 chunk size

### W6 · Day 3（周三 · 2h）— 向量化

**资源**：[sentence-transformers](https://www.sbert.net/) 或 [BGE 中文模型](https://huggingface.co/BAAI/bge-small-zh-v1.5)

**必学**：
- Embedding 概念
- 本地跑 embedding 模型（不调 API）

**练习**：对 10 个句子做 embedding，可视化（前 2 维 PCA）

### W6 · Day 4（周四 · 2h）— 向量库

**资源**：[Chroma 快速入门](https://docs.trychroma.com/getting-started)

**必学**：
- 持久化存储
- 元数据过滤
- 相似度检索

**练习**：把 W5D2 的 PDF chunks 存入 Chroma，查询能返回 top-k

### W6 · Day 5（周五 · 2h）— 端到端 Naive RAG

**实战**：写一个 `rag.py`：
```python
def rag_query(question: str) -> str:
    chunks = chroma.similarity_search(question, k=3)
    context = "\n".join(c.page_content for c in chunks)
    prompt = f"基于以下资料回答：\n{context}\n\n问题：{question}"
    return llm_call(prompt)
```

### 🎯 W6 周日验收

- [ ] FastAPI + RAG 的 `/chat` 接口能调通
- [ ] curl 能问到 PDF 里的信息

### W7 · Day 1-2（周一-周二 · 4h）— 混合检索 + Reranker

**必学**：
- BM25 原理（不要手写，用 `rank_bm25` 库）
- 混合检索：BM25 + 向量，加权融合
- Reranker：[BGE-Reranker](https://huggingface.co/BAAI/bge-reranker-base)

**练习**：写一个 `hybrid_retrieve()` 函数，比较有无 Reranker 的检索质量

### W7 · Day 3（周三 · 2h）— RAG 评估

**资源**：[RAGAS 文档](https://docs.ragas.io/)

**必学**：
- Faithfulness（答案是否基于检索内容）
- Answer Relevancy（答案与问题的相关性）
- Context Precision / Recall

**练习**：写 10 条 QA 对，用 RAGAS 评估你的 RAG

### W7 · Day 4（周四 · 2h）— 可观测性 + 性能

**必学**：
- LangSmith 接入（[注册](https://www.langchain.com/langsmith)）
- 看每次 retrieve + generate 的延迟和 token
- 加 Redis 缓存（重复问题直接返回）

### W7 · Day 5（周五 · 2h）— Docker 打包

**实战**：
- 写 `Dockerfile`
- 写 `docker-compose.yml`（RAG + Chroma + Redis）
- 本地 `docker compose up` 跑通

### 🎯 W7 周日验收

- [ ] RAG 系统 Docker 一键启动
- [ ] RAGAS faithfulness > 0.7
- [ ] P99 延迟 < 2 秒

---

## 📦 阶段 4 · Agent 框架（第 7-8 周 · 40h）

> **目标**：用 LangGraph 重写阶段 2 的最小 Agent，掌握生产级 Agent 设计。

### W8 · Day 1（周一 · 2h）— LangGraph 入门

**资源**：[LangGraph Quickstart](https://langchain-ai.github.io/langgraph/)

**必学**：
- StateGraph 概念
- Node、Edge、Conditional Edge
- State schema（`TypedDict` + `Annotated`）

**练习**：把阶段 2 的"思考→工具→回答"用 LangGraph 重写

### W8 · Day 2（周二 · 2h）— 状态管理

**必学**：
- Reducer 函数：`add_messages`
- State 更新模式：覆盖 vs 累加
- 调试 State：用 `print_state()`

**练习**：在图里加一个"对话历史"节点

### W8 · Day 3（周三 · 2h）— Conditional Edge

**必学**：
- 路由函数：决定下一步去哪个节点
- 循环检测：避免无限循环

**练习**：根据"是否需要工具"决定下一步

### W8 · Day 4（周四 · 2h）— Checkpoint + 持久化

**必学**：
- `MemorySaver`、`SqliteSaver`、`PostgresSaver`
- `thread_id`：恢复之前的对话
- 时间旅行：回到任意一步重跑

**练习**：写一个能"暂停-恢复"的 Agent

### W8 · Day 5（周五 · 2h）— 人在回路（HITL）

**必学**：
- `interrupt_before` / `interrupt`
- 高风险工具的确认机制

**练习**：写文件前必须用户输入 `y` 才执行

### 🎯 W8 周日验收

- [ ] LangGraph 图可视化（`draw_mermaid_png()`）
- [ ] State 管理明确（TypedDict）
- [ ] Checkpoint 能恢复
- [ ] HITL 能中断 + 恢复

### W9 · Day 1-2（周一-周二 · 4h）— Tool Calling 深入

**必学**：
- OpenAI Function Calling schema
- Anthropic Tool Use
- Pydantic AI（类型化 Agent）

**练习**：把 search_notes 换成真实向量检索

### W9 · Day 3（周三 · 2h）— LangSmith 接入

**必学**：
- 环境变量配置
- 自动 trace
- 调试：看每一步的输入输出

**练习**：在 LangSmith 上看到你的 Agent 每一步

### W9 · Day 4（周四 · 2h）— Pydantic AI

**资源**：[Pydantic AI 文档](https://ai.pydantic.dev/)

**必学**：
- 类型化的 Agent 输出
- `result_type` 强制 schema

**练习**：用 Pydantic AI 重写最小 Agent

### W9 · Day 5（周五 · 2h）— 框架对比

**任务**：写一篇博客对比 LangGraph / OpenAI Agents SDK / Pydantic AI / AutoGen，列出各自优缺点

### 🎯 W9 周日验收

- [ ] LangGraph Agent 能跑 + 可视化 + checkpoint + HITL
- [ ] LangSmith 上能看到 trace
- [ ] 博客已写

---

## 📦 阶段 5 · 多 Agent + MCP + 工程化（第 9-10 周 · 40h）

> **目标**：3 Agent 协作 + 自建 MCP server + 性能优化

### W10 · Day 1-2（周一-周二 · 4h）— AutoGen / CrewAI 多 Agent

**资源**：[AutoGen Quickstart](https://microsoft.github.io/autogen/) 或 [CrewAI 文档](https://docs.crewai.com/)

**必学**：
- 多角色定义（researcher / writer / reviewer）
- Agent 间消息传递
- GroupChat 管理

**练习**：写一个"研究报告小组"：researcher 找资料 → writer 写报告 → reviewer 审稿

### W10 · Day 3（周三 · 2h）— LangGraph 多 Agent

**必学**：
- 子图（Subgraph）
- Supervisor 模式
- Agent handoff

**练习**：用 LangGraph 实现"planner → executor → reviewer"模式

### W10 · Day 4-5（周四-周五 · 4h）— MCP 协议

**资源**：[MCP 官方文档](https://modelcontextprotocol.io/)

**必学**：
- MCP 架构：client / server
- 三大原语：tools / resources / prompts
- Python SDK

**练习**：写一个 MCP server 暴露本地文件系统（`read_file` / `list_dir`），用 Claude Desktop 连接

### 🎯 W10 周日验收

- [ ] 3 个 Agent 协作跑通
- [ ] 自建 MCP server 跑通
- [ ] Claude Desktop 能连你的 MCP server

### W11 · Day 1（周一 · 2h）— 性能优化

**必学**：
- 异步并发（`asyncio.gather`）
- 缓存策略（Redis 存 LLM 结果）
- Token 优化：截断长 context、压缩 system prompt

### W11 · Day 2（周二 · 2h）— 安全与防御

**必学**：
- Prompt Injection 类型（直接注入 / 间接注入）
- 防御：输入过滤、工具白名单、最小权限、Audit log
- 沙箱：不让 Agent 直接执行 shell

**阅读**：[OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

### W11 · Day 3（周三 · 2h）— 监控与日志

**必学**：
- 结构化日志（`structlog`）
- 链路追踪（LangSmith / OpenTelemetry）
- 指标：成功率、延迟、token 成本

### W11 · Day 4-5（周四-周五 · 4h）— 部署入门

**必学**：
- Railway 一键部署 FastAPI
- Docker Compose 多服务
- 环境变量管理

**实战**：把阶段 3 的 RAG 部署到 Railway（公开 demo URL）

### 🎯 W11 周日验收

- [ ] RAG / Agent 服务部署上线
- [ ] 有可分享的 demo URL（写进简历）
- [ ] 日志、trace、监控全开

---

## 📦 阶段 6 · 简历级项目（第 11-12 周 · 40h）

> **目标**：2 个简历级项目，每个能 demo、可量化、有技术深度。

### 项目组合建议

| 背景 | 推荐组合 |
|---|---|
| 求职通用 | A. 知识库助手 + B. 自动化研究 Agent |
| 偏算法 | A. 多模态 RAG + B. Agent Eval 平台 |
| 偏应用 | A. 客户支持 Agent + B. 内容创作 Agent |

### W12 · 完整投入项目 1（40h）

#### 推荐：个人知识库助手

**功能**：
- 上传 PDF/Markdown/Notion 文档
- 对话式问答
- 多轮对话记忆
- 引用原文出处

**技术栈**：
- FastAPI + WebSocket（流式输出）
- LangGraph（Agent 编排）
- Chroma / Milvus（向量库）
- MCP server（文件系统、GitHub）
- React / Streamlit 前端

**亮点（写进简历）**：
- 混合检索（向量 + BM25）+ Reranker
- LangSmith 全链路 trace
- 30 条 eval case，RAGAS faithfulness > 0.85
- Docker Compose 一键部署
- **量化指标**：QPS、延迟、token 成本

### W12 · 每日任务

| Day | 任务 |
|---|---|
| W12 D1 | 需求文档 + 架构图（draw.io） |
| W12 D2 | 后端骨架 + FastAPI + LangGraph |
| W12 D3 | RAG pipeline + 向量库 |
| W12 D4 | MCP server（filesystem） |
| W12 D5 | 前端最小化（Streamlit 优先） |

### W13 · 完整投入项目 2（40h）

#### 推荐：自动化研究 Agent

**功能**：
- 给定主题，自动搜索 → 阅读 → 总结 → 写报告
- 多源信息（Google Scholar / arXiv / 网页）
- 报告含引用
- 中途可干预

**技术栈**：
- LangGraph（多 Agent 协作）
- Tavily / SerpAPI（搜索）
- Jina Reader（网页抓取）
- LangSmith（trace）
- 输出：Markdown 报告

**亮点**：
- Supervisor + Executor + Reviewer 三 Agent
- 人在回路（中断确认）
- 时间旅行 checkpoint
- **量化指标**：完成一份报告从 X 小时 → X 分钟

### W13 · 每日任务

| Day | 任务 |
|---|---|
| W13 D1 | 整体设计 + 接口 |
| W13 D2 | 搜索 + 抓取工具 |
| W13 D3 | 阅读 + 总结 Agent |
| W13 D4 | Reviewer + 人在回路 |
| W13 D5 | README + 录 demo 视频 |

### 🎯 W13 周日验收

- [ ] 2 个项目上线 demo URL
- [ ] 每个项目 30 条 eval case
- [ ] 每个项目 README 完整（架构图、demo、限制）
- [ ] 2 个 demo 视频已录（3 分钟内）
- [ ] 代码已 commit + tag v1.0

---

## 📦 阶段 7 · 求职冲刺（第 13-14 周 · 28h）

> **目标**：简历打磨 + 投递 + 模拟面试 + Offer

### W14 · 简历与投递（4 天 × 2h = 8h）

#### Day 1：简历重写

**模板**（基于 AgentGuide 推荐的 Star 法则）：

```text
【项目经验 - 个人知识库助手】（W12-W13）
构建端到端 RAG + Agent 系统，支持 PDF/Markdown 多格式检索与对话式问答。
技术栈：FastAPI + LangGraph + Chroma + MCP + React。
• 架构：分层 Context Builder + 工具注册表 + LangSmith 全链路 trace
• 性能：混合检索（向量 + BM25）+ BGE-Reranker，P99 延迟 480ms
• 质量：30 条 eval case，RAGAS faithfulness 0.87
• 部署：Docker Compose + Railway，已上线 demo.example.com
```

#### Day 2-4：批量投递

- **目标**：投递 30+ 简历
- **渠道**：
  - Boss 直聘（Agent / AI 应用相关岗位）
  - 拉勾（互联网公司 AI 岗位）
  - LinkedIn（外企 / 海外岗位）
  - V2EX、掘金、知乎（社区招聘）
- **话术**：准备 3 句话自我介绍，能讲清 2 个项目

### W15 · 面试准备（4 天 × 2h = 8h）

#### Day 1：高频题复习

**资源**：[AgentGuide `docs/04-interview/`](https://github.com/adongwanai/AgentGuide/tree/main/docs/04-interview)

**必看**：
- 01-theory-questions.md（100 题）
- 02-rag-questions.md（50 题）
- 03-agent-questions.md（50 题）
- 16-llm-fundamentals.md（Transformer / 训练）

#### Day 2-3：算法题（每天 30 分钟 LeetCode + 90 分钟模拟面试）

**资源**：[LeetCode Hot 100](https://leetcode.cn/studyplan/top-100-liked/)

**重点**：
- 数组、字符串、哈希表（基础）
- 链表、二叉树（中等）
- 动态规划（看情况）

#### Day 4：模拟面试

**资源**：
- AgentGuide `18-agent-interview-playbooks/`（STAR 法则面试模板）
- 找朋友 / 网友模拟面试（视频会议）

**准备**：
- 5 句话讲清项目
- 3 个技术深挖问题的答案
- 3 个反问面试官的问题

### 🎯 W15 周日验收

- [ ] 投递 30+
- [ ] 模拟面试 3+ 次
- [ ] 收到至少 1 个面试邀请（不是目标，但说明方向对）

---

## 🎯 2 个简历项目详细设计

### 项目 A：个人知识库助手

```
┌─────────────────────────────────────────────────────────┐
│                    React Frontend                       │
│                   (Streamlit 可替)                       │
└────────────────────────┬────────────────────────────────┘
                         │ WebSocket
┌────────────────────────┴────────────────────────────────┐
│                    FastAPI Backend                       │
│  ┌──────────────────────────────────────────────────┐  │
│  │          LangGraph Agent                          │  │
│  │  ┌────────┐  ┌──────────┐  ┌──────────────┐     │  │
│  │  │ Think  │→ │ Retrieve │→ │   Generate   │     │  │
│  │  └────────┘  └──────────┘  └──────────────┘     │  │
│  └──────────────────────────────────────────────────┘  │
│         │              │              │                  │
│         ▼              ▼              ▼                  │
│   ┌──────────┐   ┌──────────┐   ┌──────────────┐      │
│   │ Hybrid   │   │  Chroma  │   │   LangSmith  │      │
│   │Retrieval │   │  Vector  │   │    Trace     │      │
│   └──────────┘   └──────────┘   └──────────────┘      │
│                          │                               │
│                          ▼                               │
│                  ┌──────────────┐                       │
│                  │ MCP Servers  │                       │
│                  │ (Filesystem, │                       │
│                  │  GitHub)     │                       │
│                  └──────────────┘                       │
└─────────────────────────────────────────────────────────┘
```

**关键指标**：
- 检索 P99 < 500ms
- RAGAS faithfulness > 0.85
- 30+ eval case 通过率 > 80%
- Docker Compose 一键启动

### 项目 B：自动化研究 Agent

```
┌─────────────────────────────────────────────────────────┐
│                   用户输入: "对比 LangGraph 和 CrewAI"  │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────┴────────────────────────────────┐
│              Supervisor Agent（决策下一步）              │
└────────────────────────┬────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Planner    │ │  Researcher  │ │    Reviewer   │
│  (拆任务)    │ │ (搜索+抓取)  │ │  (审稿修改)   │
└──────────────┘ └──────────────┘ └──────────────┘
        │                │                │
        ▼                ▼                ▼
┌──────────────────────────────────────────────────────┐
│  Tools: Tavily / Jina Reader / Write File / HITL     │
└──────────────────────────────────────────────────────┘
```

**关键指标**：
- 完成一份 3000 字报告 < 5 分钟
- 引用准确率 ≥ 90%
- HITL 触发率 < 20%
- LangSmith trace 覆盖 100%

---

## 💼 面试准备清单

### 高频技术题（精选 30 题）

| 类别 | 题 |
|---|---|
| **Agent 基础** | 1. ReAct 是什么？2. Agent vs Workflow 区别？3. Context Engineering 怎么做？4. Tool Calling 原理？5. Function Calling schema 设计原则？ |
| **RAG** | 6. Naive RAG 流程？7. 切片策略有哪些？8. 混合检索如何融合 BM25 + 向量？9. Reranker 作用？10. RAGAS 指标含义？ |
| **框架** | 11. LangGraph 核心概念？12. State vs Memory 区别？14. 为什么 checkpoint？15. HITL 怎么实现？ |
| **MCP** | 16. MCP 三大原语？17. MCP vs Function Calling？18. MCP 客户端实现？ |
| **工程** | 19. Agent 死循环怎么防？20. Prompt Injection 怎么防？21. Token 成本怎么降？22. 如何评估 Agent？ |
| **LLM** | 23. Transformer 自注意力机制？24. LLM 训练三阶段？25. RLHF 是什么？26. 什么是 Prompt Tuning？ |
| **算法** | 27. 两数之和（Hot 100 #1）28. 二分查找 29. 岛屿数量 30. LRU 缓存 |

### STAR 法则准备（讲项目用）

每个项目准备 4-5 段故事：
- **情境**：什么场景，什么挑战
- **任务**：你的目标是什么
- **行动**：你具体做了什么（技术细节）
- **结果**：量化指标（成功率、延迟、成本）

### 反问面试官清单

1. 团队目前 Agent 的应用场景是什么？
2. 用 LangGraph 还是自研框架？
3. 有没有用户反馈 Agent 失败的真实案例？
4. 工程团队对 Agent 评估的成熟度如何？

---

## 📊 15 周进度追踪表

> 复制到自己的笔记里，每周更新。

```
阶段        周      关键产出                状态  完成日期
─────────────────────────────────────────────────────────
阶段 0      W1     概念笔记 + 环境就绪      ⬜    ___
阶段 1      W2     6 个练习 + chatbot      ⬜    ___
阶段 1      W3     weather-llm 项目       ⬜    ___
阶段 2      W4     最小 Agent + 20 eval    ⬜    ___
阶段 3      W6     Naive RAG 跑通          ⬜    ___
阶段 3      W7     RAG 部署 + RAGAS       ⬜    ___
阶段 4      W8     LangGraph Agent         ⬜    ___
阶段 4      W9     Pydantic AI + LangSmith ⬜    ___
阶段 5      W10     多 Agent + MCP server  ⬜    ___
阶段 5      W11    部署上线 demo           ⬜    ___
阶段 6      W12    项目 1 上线             ⬜    ___
阶段 6      W13    项目 2 上线 + 简历     ⬜    ___
阶段 7      W14    投递 30+                ⬜    ___
阶段 7      W15    模拟面试 + Offer        ⬜    ___
```

---

## 🆘 风险预案

### 场景 1：Python 学不下去**
**信号**：W3 结束时读 LangChain 源码仍吃力
**对策**：
- 多花 1 周补 Python（4-6 周都可）
- 优先读《Python编程：从入门到实践》后半本（项目导向）
- 找 1v1 答疑（编程教练 / 朋友）

### 场景 2：某个阶段超时**
**信号**：某阶段 1 周完不成
**对策**：
- 砍掉"锦上添花"内容（如可视化、Web UI）
- 保核心产出（Agent 能跑、RAG 能查）
- 求职优先级：1 个能讲清的项目 > 2 个浅的项目

### 场景 3：Agent 跑不通**
**信号**：阶段 2 Sprint 卡住
**对策**：
- 先用 MockModel 跑通，不纠结真实 LLM
- 看 trace 找到死循环点
- 简化：先把工具减到 1 个

### 场景 4：求职不顺**
**信号**：W14 投递 30+ 全部已读不回
**对策**：
- 简历优化（让 Agent 朋友帮你看）
- 内推（GitHub 项目 star 多 → 主动找内推）
- 扩大范围：远程岗位、海外岗位、外包岗位
- 备选：先做 AI 应用外包（积累作品）

### 场景 5：某个框架学不会**
**对策**：
- **核心只学 LangGraph**（其他能跑 Demo 就行）
- 1 个框架深 > 4 个框架浅

---

## 📌 6 个关键原则（贯穿全程）

1. **做出什么 > 学过什么** — 每个阶段必须有可演示的产出
2. **Trace + Eval 是 Agent 的第一公民** — 没评估 = 没产出
3. **从工作流开始，再加 Agent loop** — 不要一上来 LLM 自主决策
4. **核心只学 LangGraph** — 其他框架能跑 Demo 即可
5. **简历只写 2 个项目** — 5 个浅项目 < 2 个深项目
6. **每天 30% 看，70% 写** — 只看文档不写代码 = 没学

---

## 🎯 成功的 3 个关键指标

> 14 周结束时自检：

- [ ] **能讲 2 个项目**：用 5 分钟讲清架构 + 量化指标
- [ ] **能答 30 道高频题**：不看书不查文档
- [ ] **GitHub 有 2 个 star-worthy 仓库**：README 完整 + 能 clone 跑通

---

## 🚀 下一步行动（**今天就做**）

1. **现在**：把 W1 Day 1 的 4 个任务做掉（2h）
2. **今天结束前**：GitHub 建仓 `agent-learning`，写第一行 README
3. **本周结束**：完成阶段 0 全部验收
4. **14 周后**：拿 Offer 🎉

---

**最后一条**：这份路线偏紧。如果某周压力大，砍掉的是"锦上添花"（可视化、UI 优化），不是"核心产出"（Agent 能跑、RAG 能查）。保持每周有 commit，14 周后回头看，你会感谢自己开始。