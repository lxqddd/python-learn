# W3 D4 周四 · 2h — dotenv + 模块化

- **阶段**：1 Python 突击 | **周次**：W3 | **状态**：⬜
- **主题**：环境变量 / 配置管理 / 项目结构

---

## 🎯 今日目标（3 项）

- [ ] 学 python-dotenv
- [ ] 学项目结构组织
- [ ] 写练习 10（settings.py）

---

## ✅ 任务清单（2h）

### 📖 阅读（40min）

- [ ] **[40min]** 学 [python-dotenv](https://pypi.org/project/python-dotenv/)
  - 创建 `.env` 文件存敏感信息
  - `load_dotenv()` 加载
  - `os.getenv("KEY")` 读取
  - `.env` 必须加到 `.gitignore`

### 💻 练习 10：settings.py（40min）

- [ ] **[40min]** 创建项目级配置：

  **1. 在 `sandbox/tiny-projects/` 下建 `.env`：**
  ```bash
  # sandbox/tiny-projects/.env
  DEEPSEEK_API_KEY=sk-你的key
  DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
  MODEL_NAME=deepseek-chat
  AGENT_MAX_STEPS=5
  ```

  **2. 在 `sandbox/tiny-projects/` 下建 `settings.py`：**
  ```python
  """统一配置管理"""
  import os
  from pathlib import Path
  from dotenv import load_dotenv
  from pydantic import BaseModel
  
  # 加载 .env
  load_dotenv()
  
  class Settings(BaseModel):
      """应用配置"""
      deepseek_api_key: str
      deepseek_base_url: str = "https://api.deepseek.com/v1"
      model_name: str = "deepseek-chat"
      agent_max_steps: int = 5
      
      @classmethod
      def load(cls) -> "Settings":
          return cls(
              deepseek_api_key=os.getenv("DEEPSEEK_API_KEY", ""),
              deepseek_base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"),
              model_name=os.getenv("MODEL_NAME", "deepseek-chat"),
              agent_max_steps=int(os.getenv("AGENT_MAX_STEPS", "5")),
          )
  
  # 单例
  settings = Settings.load()
  ```

  **3. 确认 `.env` 不被 git 追踪：**
  ```bash
  echo ".env" >> ../../.gitignore
  ```

- 跑通 settings.py，确认 API Key 读到了

### 📚 项目结构（40min）

- [ ] **[40min]** 整理 W2-W3 的代码为合理结构：

  ```
  sandbox/
  ├── README.md
  ├── week2-basics/      # 练习 1-5
  ├── week3-advanced/    # 练习 7-10（建新目录，移动练习）
  └── tiny-projects/
      ├── 01-chatbot/
      └── 02-config-demo/
          ├── .env
          ├── settings.py
          └── main.py
  ```

  - 把 `ex07-ex10` 移到 `week3-advanced/`
  - 写 `sandbox/README.md` 列出所有练习位置

---

## 📚 关键概念

| 概念 | 用途 |
|---|---|
| `.env` | 存敏感配置（不进 git） |
| `load_dotenv()` | 加载 .env 到环境变量 |
| `pydantic.BaseModel` | 类型安全的配置 |
| 单例模式 | 全局只一个 settings 实例 |

---

## ✅ 当日验收

- [ ] settings.py 跑通，能读 .env
- [ ] `.env` 在 `.gitignore` 里
- [ ] sandbox 目录结构整理好

---

## ⚠️ 关键提醒

**`.env` 绝对不能 commit 到 git**！如果不小心提交了：
1. 立刻去 DeepSeek 重置 API Key
2. 用 `git rm --cached .env` 从 git 移除
3. 改 `.gitignore`

---

## 💡 明日预告

**W3 D5 周五**：综合项目 `weather-llm`