# W1 D3 周三 · 2h — Python 第一次体验 + 调 LLM

> **阶段**：0 定方向 | **周次**：W1 | **状态**：⬜ 未开始
> **主题**：Python 入门 + 第一次用代码调 API

---

## 🎯 今日目标（2 项）

- [ ] 看 Python 入门视频（够用就行，不求精通）
- [ ] 写 `hello.py` 调 DeepSeek API，看到 AI 回复

---

## ✅ 任务清单（2h）

### 📖 视频学习（90min）

- [ ] **[90min]** 看 [莫烦 Python 入门](https://mofanpy.com/) 第 1-5 集
  - 重点看：变量、print、字符串、列表、字典、函数
  - 不需要看完所有细节，目标是"能看懂代码"
  - 产出：`notes/week1/day3-video-notes.md` 写下 5 个学到的语法点

### 💻 实战：调 API（30min）

- [ ] **[30min]** 写第一个 Python 脚本 `sandbox/hello.py`：

  ```python
  """第一次调 LLM API"""
  import os
  from openai import OpenAI
  
  # 从环境变量读 API Key
  client = OpenAI(
      api_key=os.getenv("DEEPSEEK_API_KEY"),
      base_url="https://api.deepseek.com/v1",
  )
  
  # 第一次对话
  response = client.chat.completions.create(
      model="deepseek-chat",
      messages=[
          {"role": "user", "content": "你好，请用一句话介绍你自己"},
      ],
  )
  print("AI:", response.choices[0].message.content)
  ```

  - 安装 openai 库：`uv pip install openai`
  - 设置环境变量：`export DEEPSEEK_API_KEY=sk-xxxxx`
  - 运行：`python sandbox/hello.py`
  - 看到 AI 回复 → 截图存到 `notes/week1/hello-api-success.png`

---

## 📚 关键概念（今日必须理解）

- **API**：别人写好的功能，你调一次拿结果（像点外卖）
- **环境变量**：把敏感信息（API Key）从代码里拿出来，放到外面
- **OpenAI 兼容**：DeepSeek 用同样的接口，可以无缝切换

---

## 🔗 资源链接

- [莫烦 Python](https://mofanpy.com/)
- [DeepSeek API 文档](https://platform.deepseek.com/docs)
- [openai-python SDK](https://github.com/openai/openai-python)

---

## 📊 进度

```
W1 D3:        [░░░░░░░░░░] 0/2
W1 整体:      [░░░░░░░░░░] 0/23
阶段 0:       [░░░░░░░░░░] 0/23
```

---

## ✅ 当日验收

- [ ] hello.py 能跑通，看到 AI 输出
- [ ] 理解什么是 API Key、什么是环境变量
- [ ] 知道为什么 DeepSeek 用 OpenAI 兼容接口

---

## ⚠️ 常见问题

| 问题 | 解决 |
|---|---|
| `ModuleNotFoundError: No module named 'openai'` | `uv pip install openai` |
| `AuthenticationError` | 检查 API Key 是否正确，是否充值过 |
| 网络超时 | 检查是否能 ping 通 `api.deepseek.com` |
| 中文乱码 | Python 3 默认 UTF-8，应该不会乱码；如果是，加 `# -*- coding: utf-8 -*-` |

---

## 💡 明日预告

**W1 D4 周四**：VS Code 配置 + Git 基础 + 第一次 commit

---

**完成后**：把当日所有 `[ ]` 改成 `[x]`，明天打开 [`W1-D4-thu.md`](W1-D4-thu.md)