# W13 D4 周四 · 4h — 项目 1 · MCP 集成

- **阶段**：6 简历级项目 | **周次**：W13 | **状态**：⬜
- **主题**：MCP server + Agent 集成

---

## 🎯 今日目标（3 项）

- [ ] 自建 filesystem MCP server
- [ ] 自建 GitHub MCP server
- [ ] Agent 集成 MCP 工具

---

## ✅ 任务清单（4h）

### 🛠 Filesystem MCP Server（60min）

- [ ] **[60min]** `backend/mcp_servers/filesystem_server.py`：

  ```python
  """Filesystem MCP Server"""
  from mcp.server.fastmcp import FastMCP
  from pathlib import Path
  import os
  
  mcp = FastMCP("filesystem-kb")
  ALLOWED_DIR = Path(os.getenv("KB_DATA_DIR", "./data")).resolve()
  
  @mcp.tool()
  def read_file(path: str) -> str:
      """读取 KB 中的文件"""
      target = (ALLOWED_DIR / path).resolve()
      if not str(target).startswith(str(ALLOWED_DIR)):
          return f"❌ 禁止访问"
      if not target.exists():
          return f"❌ 不存在"
      return target.read_text(encoding="utf-8")
  
  @mcp.tool()
  def list_files(pattern: str = "*") -> str:
      """列出 KB 中的文件"""
      return "\n".join(f.name for f in ALLOWED_DIR.glob(pattern))
  
  if __name__ == "__main__":
      mcp.run()
  ```

### 🛠 GitHub MCP Server（60min）

- [ ] **[60min]** `backend/mcp_servers/github_server.py`：

  ```python
  """GitHub MCP Server"""
  from mcp.server.fastmcp import FastMCP
  import os
  import requests
  
  mcp = FastMCP("github")
  
  @mcp.tool()
  def search_repos(query: str, limit: int = 5) -> str:
      """搜索 GitHub 仓库"""
      resp = requests.get(
          "https://api.github.com/search/repositories",
          params={"q": query, "per_page": limit},
          timeout=10,
      )
      items = resp.json().get("items", [])
      return "\n\n".join([f"**{r['full_name']}** ⭐ {r['stargazers_count']}\n{r['description']}" for r in items]) or "未找到"
  
  @mcp.tool()
  def get_readme(repo: str) -> str:
      """获取 README"""
      resp = requests.get(
          f"https://api.github.com/repos/{repo}/readme",
          headers={"Accept": "application/vnd.github.v3.raw"},
          timeout=10,
      )
      if resp.status_code != 200:
          return f"❌ 错误"
      return resp.text[:5000]
  
  if __name__ == "__main__":
      mcp.run()
  ```

### 🔗 Agent 集成 MCP（90min）

- [ ] **[90min]** 改 `backend/agent.py`：

  ```python
  @tool
  def read_kb_file(path: str) -> str:
      """读取 KB 文件"""
      target = Path("./data") / path
      if ".." in path:
          return "❌ 非法路径"
      if not target.exists():
          return "❌ 不存在"
      return target.read_text(encoding="utf-8")
  
  @tool
  def search_github(query: str) -> str:
      """搜索 GitHub 仓库"""
      import requests
      resp = requests.get(
          "https://api.github.com/search/repositories",
          params={"q": query, "per_page": 5},
          timeout=10,
      )
      items = resp.json().get("items", [])
      return "\n\n".join([f"**{r['full_name']}** ⭐ {r['stargazers_count']}" for r in items]) or "未找到"
  ```

### 🧪 集成测试（30min）

- [ ] **[30min]** 测试 3 个工具都能调

---

## ✅ 当日验收

- [ ] 2 个 MCP server 跑通
- [ ] Agent 能调所有 MCP 工具

---

## 💡 明日预告

**W13 D5 周五 · 4h**：前端 + 评估 + demo 视频