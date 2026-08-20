# 🎬 演示脚本（Demo Script）

> 用于面试展示、博客录屏、向朋友介绍
> 建议每个 demo 时长控制在 30-60 秒

---

## Demo 1：基本搜索（30 秒）

```bash
cd projects/01-minimal-agent
python agent.py "搜索 Python 异步笔记"
```

**预期输出**：
1. Agent 决定调用 `search_notes(query="搜索 Python 异步笔记")`
2. 工具返回 1 条命中（python-async）
3. Agent 给出最终答案

**讲解词**：
> "这是一个 200 行的最小 Agent。它接收任务、调用工具、读结果、然后回答。
> 注意每次决策都有 `reason_summary` 记录原因——这是审计的关键。"

---

## Demo 2：搜索 + 写文件（45 秒）

```bash
python agent.py "总结 React Hooks 内容并保存"
```

**预期输出**：
1. Agent 先 `search_notes`
2. 看到 "总结" 关键词，再调用 `write_summary`
3. 看到 `⚠️ [HITL]` 警告（human-in-the-loop 触发）
4. 文件写入 `output/summary.md`

**讲解词**：
> "注意 `write_summary` 工具触发了 HITL 警告——这是因为它是写操作，生产环境必须人工确认。
> 我们用结构化错误代替抛异常，所以 Agent 知道下一步该怎么做，不会崩。"

---

## Demo 3：边界场景——空查询（20 秒）

```bash
echo "" | xargs -I {} python agent.py "{}"
# 或者直接修改 agent.py 接受 stdin
```

**预期输出**：
1. Agent 立即 `final_answer`，不调用工具
2. 状态 completed

**讲解词**：
> "用户输入空字符串时，Agent 不应该调用工具。我们用 prompt engineering 教会模型识别这种情况。"

---

## Demo 4：边界场景——未知工具（30 秒）

修改 `mock_model.py` 让它输出一个不存在的工具名：

```python
return Action(type="tool_call", tool_name="delete_everything", args={})
```

**预期输出**：
1. Agent 收到模型决策：`delete_everything`
2. 检查白名单 → 不在 → 返回 `unknown_tool` 错误
3. 把错误喂回 context，让模型有机会纠正

**讲解词**：
> "看，模型想调用 `delete_everything`——但 Agent 不让它。
> 工具白名单是安全的第一道防线。即使模型被 prompt injection 攻击，它也只能从我们定义的工具里选。"

---

## Demo 5：路径穿越攻击（30 秒）

修改 `mock_model.py` 让它输出：

```python
return Action(type="tool_call", tool_name="write_summary",
              args={"text": "hacked", "filename": "../../../etc/passwd"})
```

**预期输出**：
1. `write_summary` 返回 `{"ok": false, "error": "invalid_filename"}`
2. 没有创建任何文件

**讲解词**：
> "文件名里有 `../` 想去写 `/etc/passwd`——但被工具自己拦下了。
> 这就是 'Defense in depth'：不要相信模型，要让工具自己验证参数。"

---

## 🎙 面试场景模拟

### 提问 1：「ReAct 是什么？」

**回答要点**：
- Reasoning + Acting 交替
- 不是让模型自由思考，而是结构化循环
- 我的实现里，模型输出 JSON，里面只有 `reason_summary`（不是完整 CoT）

### 提问 2：「Context Engineering 怎么做？」

**回答要点**：
- 5 层：system / task / memory / retrieved / recent_trace
- 关键是**控制每层的大小和更新频率**
- memory 层长期缓存，retrieved 层每次更新，trace 层只保留最近 N 步

### 提问 3：「怎么评估 Agent 好不好？」

**回答要点**：
- 20 条 eval case（正常/边界/安全）
- 评分维度：成功率、平均步数、工具调用准确率、违规率
- 失败归因：工具失败 vs 检索失败 vs 模型误判 vs 上下文污染
- 高级方法：LLM-as-judge、LangSmith trace 重放

### 提问 4：「为什么不上 LangChain / LangGraph？」

**回答要点**：
- 第一阶段**故意不用框架**，理解原理
- 手写过 200 行循环后，再看框架代码不会觉得魔法
- 现在的实现是 L2（Workflow），下一步升级到 L3 用 LangGraph