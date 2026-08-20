# W5 D5 周五 · 4h — 20 条 Eval

- **阶段**：2 First 7 Days Sprint | **周次**：W5 | **状态**：⬜
- **主题**：写 20 条测试用例 + 跑分 + 失败归因

---

## 🎯 今日目标（3 项）

- [ ] 写 20 条 eval cases
- [ ] 跑 eval_runner.py
- [ ] 失败归因

---

## ✅ 任务清单（4h）

### 📝 写 20 条 eval cases（90min）

- [ ] **[90min]** 在 `projects/01-minimal-agent/eval_cases.jsonl` 写 20 条：

  **格式（每行一个 JSON）：**
  ```json
  {"id": "normal-01", "category": "normal", "input": "搜索 Python 异步笔记", "expected_tools": ["search_notes"], "expected_status": "completed", "expected_keywords": ["asyncio"], "scoring": "keyword_match"}
  ```

  **分布：**
  - 10 条 **normal**（正常任务）
  - 5 条 **edge**（边界：空、超长、不存在、超出限制）
  - 5 条 **safety**（安全：未知工具、路径穿越、prompt injection）

  **完整模板**：`projects/01-minimal-agent/eval_cases.jsonl`（先自己写 5 条，参考模板后写完）

### 💻 实现 `eval_runner.py`（60min）

- [ ] **[60min]** 写 `projects/01-minimal-agent/eval_runner.py`：
  - 读 `eval_cases.jsonl`
  - 每条跑 `run_agent()`
  - 评分（工具序列匹配 + 关键词匹配 + 状态匹配）
  - 输出 `eval_results.json` 和汇总

  **完整代码参考**：`projects/01-minimal-agent/eval_runner.py`

### 🏃 跑分（30min）

- [ ] **[30min]** 跑：
  ```bash
  cd projects/01-minimal-agent
  uv run python eval_runner.py
  ```
  - 看到 by category 汇总：
    ```
    normal : __/10 通过
    edge   : __/5 通过
    safety : __/5 通过
    overall: __/20 通过
  ```

### 📊 失败归因（60min）

- [ ] **[60min]** 看 `eval_results.json`，把失败 case 分类：

  | 失败类型 | 表现 | 修复方向 |
  |---|---|---|
  | **工具序列错** | 调了不该调的 / 没调该调的 | 改 prompt |
  | **关键词缺失** | final_answer 没含预期词 | 改 MockModel 或接真实 LLM |
  | **状态错** | 应该 running 报 completed | 评分脚本 bug |
  | **安全漏洞** | 调了未知工具 | 工具白名单生效 |

  - 写 `notes/week4/day5-failure-analysis.md`
  - **这是 Day 7 简历材料**：失败归因 = 工程能力的体现

---

## 📚 Eval 用例设计原则

**1 个好的 eval case 包含**：
- 输入（真实场景的请求）
- 期望工具序列
- 期望状态
- 期望关键词
- 评分方法

**为什么必须有 safety case？**
- 证明 Agent **能拒绝**不该做的
- 工具白名单、路径穿越、prompt injection 必须有覆盖

---

## 📊 进度

```
W5 D5:    [░░░░░░░░░░] 0/4
W5 整体:  [░░░░░░░░░░] 0/21
阶段 2:   [░░░░░░░░░░] 0/21
```

---

## ✅ 当日验收

- [ ] 20 条 eval case 写完
- [ ] eval_runner.py 跑通
- [ ] 失败归因分析写完
- [ ] eval_results.json 存好

---

## ⚠️ 不要追求 100%

**65-80% 通过率是健康的**。全过意味着 case 太简单。失败才有改进空间。

接真实 LLM 后，通过率会显著提升（关键词缺失问题自动解决）。

---

## 💡 周末预告

**W5 周末**：D6 + D7
- D6：写 README + eval_report + demo_script
- D7：复盘 + 简历 bullet