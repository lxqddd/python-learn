# W1 D4 周四 · 2h — 工具链完善

> **阶段**：0 定方向 | **周次**：W1 | **状态**：⬜ 未开始
> **主题**：VS Code + Git + 第一次 commit

---

## 🎯 今日目标（3 项）

- [ ] 配置好 VS Code（Python / 格式化扩展）
- [ ] 学 Git 基础，建 `agent-learning` 仓库
- [ ] 第一次 commit

---

## ✅ 任务清单（2h）

### 🔧 VS Code 配置（40min）

- [ ] **[40min]** 配置 VS Code：
  - 装扩展：**Python**（微软官方）、**Black Formatter**、**isort**、**GitLens**
  - 设置格式化：`settings.json` 加：
    ```json
    {
      "editor.formatOnSave": true,
      "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.codeActionsOnSave": {"source.fixAll.isort": "explicit"}
      }
    }
    ```
  - 产出：VS Code 截图存到 `notes/week1/vscode-config.png`

### 📚 Git 基础（40min）

- [ ] **[40min]** 学 Git 基础操作：
  - 看 [Git 简明指南](https://rogerdudler.github.io/git-guide/index.zh.html)（前 5 章够用）
  - 重点学：`init` / `add` / `commit` / `push` / `status` / `log`
  - 在 GitHub 建一个新仓库：`agent-learning`（公开，README 后面写）

### 📝 第一次 commit（40min）

- [ ] **[40min]** 本地初始化 + 推到 GitHub：
  ```bash
  cd ~/Desktop/test/python
  
  git init
  git add .
  git commit -m "feat: init learning workspace"
  git remote add origin https://github.com/<你的用户名>/agent-learning.git
  git push -u origin main
  ```
  - 在 README 里写 1 句话：我的目标是 14 周后拿到 Agent 开发 Offer
  - 产出：GitHub 链接 + commit 截图存到 `notes/week1/first-commit.png`

---

## 📚 关键概念（今日必须理解）

| 概念 | 一句话 |
|---|---|
| **Git** | 代码版本管理工具，保存每次修改 |
| **Commit** | 一次"存档"，附说明 |
| **Push** | 把本地存档传到 GitHub |
| **Repository** | 一个项目的文件夹 |
| **Branch** | 主线 / 试验线 / 修复线 |

**核心原则**：**每天都 commit**，哪怕只有一行。14 周后看 commit 历史，你会感谢自己。

---

## 🔗 资源链接

- [Git 简明指南](https://rogerdudler.github.io/git-guide/index.zh.html)
- [GitHub](https://github.com/)
- [VS Code Python 教程](https://code.visualstudio.com/docs/python/python-tutorial)

---

## 📊 进度

```
W1 D4:        [░░░░░░░░░░] 0/3
W1 整体:      [░░░░░░░░░░] 0/23
阶段 0:       [░░░░░░░░░░] 0/23
```

---

## ✅ 当日验收

- [ ] VS Code 装了 4 个扩展，格式化生效
- [ ] 能解释 `git add` / `commit` / `push` 区别
- [ ] GitHub 仓库有第一个 commit
- [ ] commit message 写规范（用 `feat:` / `fix:` / `docs:` 前缀）

---

## ⚠️ 常见问题

| 问题 | 解决 |
|---|---|
| `git: command not found` | 重新装 Git |
| push 失败 authentication | GitHub 现在不能用密码，要用 Personal Access Token |
| commit 乱码 | `git config --global core.quotepath false` |
| 提交了 API Key | 立刻去 DeepSeek 重置 + 删 commit |

---

## 💡 明日预告

**W1 D5 周五**：阶段总结 + 检验概念

---

**完成后**：把当日所有 `[ ]` 改成 `[x]`，明天打开 [`W1-D5-fri.md`](W1-D5-fri.md)