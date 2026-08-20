# W4 D4 周四 · 2h — LangChain 源码阅读

- **阶段**：1 Python 强化 | **周次**：W4 | **状态**：⬜
- **主题**：读真实项目源码，提升工程能力

---

## 🎯 今日目标（3 项）

- [ ] 读懂 LangChain 1 个核心文件
- [ ] 写阅读笔记（架构 + 设计模式）
- [ ] 用 5 层 context builder 的视角理解

---

## ✅ 任务清单（2h）

### 📂 选 1 个核心文件（10min）

- [ ] **[10min]** 推荐选这个：
  
  [langchain_core/runnables/base.py](https://github.com/langchain-ai/langchain/blob/main/libs/core/langchain_core/runnables/base.py)
  
  其他可选：
  - `libs/core/langchain_core/runnables/branch.py`（分支）
  - `libs/core/langchain_core/prompts/prompt.py`（prompt）
  - `libs/community/langchain_community/vectorstores/chroma.py`（向量库）

### 📖 精读（90min）

- [ ] **[90min]** 通读选中的文件，重点关注：

  | 看什么 | 怎么记 |
  |---|---|
  | **类继承关系** | 画 UML 类图 |
  | **关键方法签名** | 列方法表（参数 + 返回） |
  | **类型提示** | 哪些地方用 Pydantic |
  | **装饰器** | `@override`、`@classmethod` 等 |
  | **核心算法** | 哪些方法实现了关键逻辑 |

  - 不需要读懂每一行
  - 看 80% 即可（剩下 20% 是边角）
  - 用 `notes/week4/day4-langchain-source.md` 记录

### 📝 写笔记（20min）

- [ ] **[20min]** 笔记结构：

  ```markdown
  # LangChain runnables/base.py 阅读笔记
  
  ## 文件作用
  Runnable 是 LangChain 的核心抽象，所有组件都实现这个接口。
  
  ## 类图
  ```
  Runnable
  ├── RunnableSequence
  ├── RunnableParallel
  ├── RunnableBranch
  ├── RunnablePassthrough
  └── RunnableLambda
  ```
  
  ## 关键方法
  | 方法 | 作用 |
  |---|---|
  | invoke() | 同步调用 |
  | ainvoke() | 异步调用 |
  | stream() | 流式输出 |
  | batch() | 批量调用 |
  
  ## 学到的设计模式
  1. **统一接口**：所有组件用 invoke/ainvoke
  2. **链式组合**：用 `|` 操作符连接
  3. **Pydantic 校验**：输入输出都验证
  
  ## 我的 Agent 该怎么用
  - 用 RunnableSequence 串起 retrieve → prompt → LLM
  - 用 RunnableBranch 做条件分支
  ```

---

## 📚 读源码的 3 个原则

1. **带着问题读**：不是从头读到尾，而是"我要找 X 怎么实现"
2. **画图辅助**：类图、时序图比文字清楚
3. **对照文档**：先看官方文档说什么，再去代码里验证

---

## ✅ 当日验收

- [ ] 读完 1 个核心文件
- [ ] 笔记含类图 + 关键方法 + 设计模式
- [ ] 能在 5 分钟内讲清文件架构

---

## 💡 明日预告

**W4 D5 周五**：综合 Python CLI 工具（不是 Agent）