# W11 D1 周一 · 2h — AutoGen 多 Agent

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：3 Agent 协作

---

## 🎯 今日目标（3 项）

- [ ] 学 AutoGen GroupChat
- [ ] 实现 3 Agent 协作
- [ ] 对比单 Agent vs 多 Agent

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [AutoGen GroupChat](https://microsoft.github.io/autogen/docs/tutorial/group-chat)

### 💻 研究报告小组（90min）

- [ ] **[90min]** 在 `projects/04-portfolio/multi-agent/autogen_team.py` 创建：

  ```python
  """AutoGen：研究报告 3 人组"""
  from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
  
  llm_config = {
      "config_list": [{
          "model": "deepseek-chat",
          "base_url": "https://api.deepseek.com/v1",
          "api_key": "sk-xxx",
      }],
      "temperature": 0.3,
  }
  
  researcher = AssistantAgent(
      name="Researcher",
      system_message="""你是研究员。
      职责：查找资料，输出 3-5 条关键发现。""",
      llm_config=llm_config,
  )
  
  writer = AssistantAgent(
      name="Writer",
      system_message="""你是写手。
      职责：根据研究员发现写一份 300 字报告。""",
      llm_config=llm_config,
  )
  
  reviewer = AssistantAgent(
      name="Reviewer",
      system_message="""你是审稿人。
      职责：审阅报告，给出 3 条具体改进建议。
      如果报告已经足够好，回复'通过'。""",
      llm_config=llm_config,
  )
  
  user = UserProxyAgent(
      name="User",
      human_input_mode="NEVER",
      max_consecutive_auto_reply=15,
      code_execution_config=False,
  )
  
  groupchat = GroupChat(
      agents=[user, researcher, writer, reviewer],
      messages=[],
      max_round=8,
      speaker_selection_method="auto",
  )
  manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)
  
  if __name__ == "__main__":
      user.initiate_chat(
          manager,
          message="调研一下 Python asyncio 的核心机制，输出 300 字报告",
      )
  ```

  - 安装：`uv pip install pyautogen`
  - 跑通

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week10/day1-autogen.md`

---

## ✅ 当日验收

- [ ] AutoGen 3 Agent 跑通
- [ ] 报告 ≥ 300 字

---

## 💡 明日预告

**W11 D2 周二**：CrewAI 多 Agent