# 🏆 Project 04 · 简历级项目（第 11-12 周）

> 这是求职前最关键的产出。**至少完成 2 个**写进简历。

---

## 🎯 选择组合

| 组合 | 适合 |
|---|---|
| **A. 通用组合** | 任何 Agent 岗位 |
| **B. 算法岗组合** | 求职 RAG/搜索/算法岗 |
| **C. 应用岗组合** | 求职产品/全栈/Agent 开发岗 |

---

## 组合 A：通用组合（推荐入门）

### 项目 1：个人知识库助手

```
RAG + MCP + FastAPI + Web UI
```

技术栈：
- FastAPI + Uvicorn
- LangGraph
- Chroma 向量库
- MCP server（filesystem、GitHub）
- React / Next.js 前端

学到：
- 完整 RAG pipeline
- MCP 协议实践
- 前后端分离
- Docker 部署

### 项目 2：自动化研究 Agent

```
LangGraph + 多工具 + LangSmith + Web Search
```

技术栈：
- LangGraph + LangSmith
- Tavily / SerpAPI（搜索）
- Jina Reader（网页抓取）
- OpenAI / Claude（LLM）

学到：
- 多工具编排
- 网络搜索 + 内容提取
- 长任务的状态管理
- 评估与监控

---

## 组合 B：算法岗组合

### 项目 1：多模态 RAG 系统

支持图片、PDF、表格的 RAG。

### 项目 2：Agent Eval Harness

设计自动化评估框架，支持自定义场景。

---

## 组合 C：应用岗组合

### 项目 1：客户支持 Agent

```
RAG + 工作流 + 工单系统集成
```

### 项目 2：内容创作 Agent

```
多 Agent + 发布到多平台
```

---

## 🗂 项目 1 推荐结构

```
personal-kb-assistant/
├── README.md              ← 项目介绍、架构图、demo gif
├── docs/
│   ├── architecture.md    ← 系统设计文档
│   ├── eval_report.md     ← 评估报告
│   └── demo.md            ← 演示步骤
├── backend/
│   ├── app.py             ← FastAPI 主入口
│   ├── agent.py           ← LangGraph Agent
│   ├── rag.py             ← RAG pipeline
│   ├── tools.py           ← MCP 工具
│   └── tests/
├── frontend/
│   ├── package.json
│   └── src/
├── docker-compose.yml     ← 一键启动
├── .env.example
└── eval/
    └── cases.jsonl        ← 30+ 条 eval
```

---

## 📅 第 11 周

- [ ] 确定项目组合
- [ ] 完成项目 1 的 MVP
- [ ] 写架构图（draw.io / excalidraw）
- [ ] 录 demo 视频（3 分钟内）

---

## 📅 第 12 周

- [ ] 项目 2 的 MVP
- [ ] 两个项目的 README 完整化
- [ ] 录两个 demo
- [ ] 写技术博客（CSDN / 掘金 / Medium）
- [ ] 准备简历 bullet 和面试故事
- [ ] 上传代码到 GitHub（profile repo）

---

## 🎯 完成标准（每个项目）

### 功能
- [ ] 能解决真实场景问题（不是 demo toy）
- [ ] 有清晰的输入/输出
- [ ] 有 Web UI 或 CLI 演示

### 工程
- [ ] README 完整（架构图、demo、限制）
- [ ] Docker 一键启动
- [ ] 至少 20 条 eval case
- [ ] LangSmith / 自建 trace

### 简历表达（量化）
- [ ] 数字：成功率 % / QPS / 延迟 ms / 成本下降 %
- [ ] 架构：用了什么核心组件
- [ ] 业务：解决了什么用户问题

---

## 📚 推荐资源

- [Hello-Agents（Datawhale）](https://datawhalechina.github.io/hello-agents/)
- [awesome-langgraph](https://github.com/awesome-langgraph)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [OpenAI Cookbook](https://cookbook.openai.com/)

---

## 🎯 简历模板

### 项目 1 标题（个人知识库助手）

> 构建个人知识库 RAG + Agent 系统，支持多格式文档检索与对话式问答。技术栈：FastAPI + LangGraph + Chroma + MCP + React。系统支持 100+ 文档秒级检索，混合检索（向量+BM25）+ Reranker，P99 延迟 < 500ms；设计 30 条 eval case，faithfulness 评分 0.87，已部署到 Railway。

### 项目 2 标题（自动化研究 Agent）

> 基于 LangGraph 构建自动化研究 Agent，能根据主题自动搜索、抓取、阅读、总结。技术栈：LangGraph + LangSmith + Tavily + Jina Reader。支持人机协作中断恢复，平均完成一份研究报告从 2 小时缩短到 15 分钟，已应用于 X 个真实项目。