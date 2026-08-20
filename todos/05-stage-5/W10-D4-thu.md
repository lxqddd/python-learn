# W11 D4 周四 · 2h — MCP 协议入门

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：Model Context Protocol 三大原语

---

## 🎯 今日目标（3 项）

- [ ] 学 MCP 架构（client / server）
- [ ] 学三大原语（tools / resources / prompts）
- [ ] 装 MCP Python SDK

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 看 [MCP 官方文档](https://modelcontextprotocol.io/)：
  - 架构：Host / Client / Server
  - 三大原语：Tools / Resources / Prompts

### 📖 看示例（20min）

- [ ] **[20min]** 浏览 [MCP Servers 仓库](https://github.com/modelcontextprotocol/servers)

### 🛠 装 SDK（10min）

- [ ] **[10min]** 安装：
  ```bash
  uv pip install mcp
  ```

### 📝 笔记（50min）

- [ ] **[50min]** 写 `notes/week10/day4-mcp-intro.md`：
  - MCP 架构图
  - 三大原语对比
  - MCP vs Function Calling

---

## 📚 关键概念

| 概念 | 说明 |
|---|---|
| **MCP** | Model Context Protocol |
| **Host** | Claude Desktop / Cursor |
| **Client** | MCP 协议客户端 |
| **Server** | 暴露工具/资源的服务 |
| **Tools** | LLM 可调用的函数 |
| **Resources** | 只读的上下文 |
| **Prompts** | 模板化的提示词 |

---

## ✅ 当日验收

- [ ] MCP SDK 装好
- [ ] 理解 client / server / 三大原语

---

## 💡 明日预告

**W11 D5 周五**：自建 MCP Server