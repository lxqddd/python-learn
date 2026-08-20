# W11 D5 周五 · 4h — 自建 MCP Server

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：filesystem MCP server

---

## 🎯 今日目标（3 项）

- [ ] 实现 filesystem MCP server
- [ ] 配置 Claude Desktop 连接
- [ ] 测试

---

## ✅ 任务清单（4h）

### 💻 写 MCP Server（90min）

- [ ] **[90min]** 创建 `filesystem_server.py`：

  ```python
  """filesystem MCP Server"""
  from mcp.server.fastmcp import FastMCP
  from pathlib import Path
  
  mcp = FastMCP("filesystem")
  
  @mcp.tool()
  def read_file(path: str) -> str:
      """读取文件内容"""
      base = Path("/Users/你的用户名/Desktop/test/python").resolve()
      target = (base / path).resolve()
      
      if not str(target).startswith(str(base)):
          return f"❌ 禁止访问 {path}"
      if not target.exists():
          return f"❌ 文件不存在"
      try:
          return target.read_text(encoding="utf-8")
      except Exception as e:
          return f"❌ 读取失败：{e}"
  
  @mcp.tool()
  def list_dir(path: str = ".") -> str:
      """列出目录内容"""
      base = Path("/Users/你的用户名/Desktop/test/python").resolve()
      target = (base / path).resolve()
      if not str(target).startswith(str(base)):
          return f"❌ 禁止访问"
      if not target.is_dir():
          return f"❌ 不是目录"
      items = [f"{'📁' if p.is_dir() else '📄'} {p.name}" for p in target.iterdir()]
      return "\n".join(items)
  
  @mcp.resource("config://app")
  def get_config() -> str:
      return "Python 学习项目根目录"
  
  @mcp.prompt()
  def study_helper(topic: str) -> str:
      return f"你是一个耐心的老师，帮我理解 {topic}"
  
  if __name__ == "__main__":
      mcp.run()
  ```

  - 改 `base` 路径
  - 用 `mcp dev filesystem_server.py` 启动调试

### 🔗 配置 Claude Desktop（60min）

- [ ] **[60min]** 编辑 `~/Library/Application Support/Claude/claude_desktop_config.json`：

  ```json
  {
    "mcpServers": {
      "filesystem": {
        "command": "uv",
        "args": [
          "--directory",
          "/Users/你的用户名/Desktop/test/python/projects/04-portfolio/mcp",
          "run",
          "filesystem_server.py"
        ]
      }
    }
  }
  ```

  - 重启 Claude Desktop

### 🧪 测试（30min）

- [ ] **[30min]** 在 Claude Desktop 测试

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week10/day5-mcp-server.md`

---

## ✅ 当日验收

- [ ] filesystem MCP server 跑通
- [ ] Claude Desktop 能连接
- [ ] 路径穿越被拦截

---

## 💡 周末预告

**W11 周日**：打开 [`W11-review.md`](W11-review.md) 做验收