# W11 D2 周二 · 2h — 安全防御

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：Prompt Injection 防御 + 沙箱

---

## 🎯 今日目标（3 项）

- [ ] 学 3 类 Prompt Injection
- [ ] 学防御策略
- [ ] 实现 1 个简单沙箱

---

## ✅ 任务清单（2h）

### 📖 阅读（30min）

- [ ] **[30min]** 看 [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

### 💻 Prompt Injection 演示（30min）

- [ ] **[30min]** 试 3 类注入攻击

### 🛡 防御实现（60min）

- [ ] **[60min]** 加防御层：

  ```python
  import re
  
  DANGEROUS_PATTERNS = [r"忽略.*?指令", r"忽略.*?规则", r"system\s*prompt"]
  DANGEROUS_TOOLS = ["shell", "bash", "exec", "eval", "system"]
  
  def check_input_safety(user_input):
      for pattern in DANGEROUS_PATTERNS:
          if re.search(pattern, user_input, re.IGNORECASE):
              return False, f"检测到可疑模式"
      return True, ""
  
  def check_tool_safety(tool_name, args):
      if tool_name in DANGEROUS_TOOLS:
          return False, f"工具 {tool_name} 被禁用"
      for arg_name, arg_value in args.items():
          if isinstance(arg_value, str):
              if ".." in arg_value or arg_value.startswith("/"):
                  return False, f"参数 {arg_name} 包含可疑路径"
      return True, ""
  ```

### 📝 笔记（10min）

- [ ] **[10min]** 写 `notes/week11/day2-security.md`

---

## ✅ 当日验收

- [ ] 3 类注入测试
- [ ] 防御中间件写完
- [ ] 至少 2 类能挡

---

## 💡 明日预告

**W11 D3 周三**：监控与日志