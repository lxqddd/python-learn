# W5 周末 · Day 6 + Day 7 · 4h — 复盘与简历

- **阶段**：2 First 7 Days Sprint | **周次**：W5 | **状态**：⬜
- **主题**：项目打包 + 简历表达

---

## 🎯 今日目标（4 项）

- [ ] 写项目 README（让陌生人能 clone-and-run）
- [ ] 写 eval_report（手动补充观察）
- [ ] 写 demo_script（面试展示用）
- [ ] 产出简历 bullet

---

## ✅ 任务清单（4h）

### 📝 Day 6（2h）：项目打包

- [ ] **[60min]** 写 `projects/01-minimal-agent/README.md`：
  - 项目目标（个人笔记搜索助手）
  - 架构图（手绘或 Mermaid）
  - 安装步骤（`uv venv` + `uv pip install`）
  - 运行命令（`python agent.py "..."`）
  - 测试命令（`python eval_runner.py`）
  - 已知限制（MockModel 不读搜索结果）

- [ ] **[30min]** 写 `projects/01-minimal-agent/eval_report.md`：
  - 跑分汇总表（手动填 Day 5 数据）
  - 失败归因分析
  - 改进计划（短期 / 中期 / 长期）
  - 简历表达模板

- [ ] **[30min]** 写 `projects/01-minimal-agent/demo_script.md`：
  - 5 个 demo 场景（基本搜索 / 搜索+写 / 空查询 / 未知工具 / 路径穿越）
  - 每个 demo 的预期输出 + 讲解词
  - 面试常见问题 + 答案要点

### 📝 Day 7（2h）：复盘 + 简历

- [ ] **[30min]** 复盘整个 sprint：
  - 写 `notes/week4/sprint-retrospective.md`
  - 3 件做对的、3 件做错的、3 件下次改进

- [ ] **[60min]** 用模板产出**简历 bullet**：
  
  > 构建面向「个人笔记搜索」场景的 Agent 系统，采用 ReAct loop + 工具注册表 + 分层 context builder，接入 2 个外部工具并对高风险动作设置 human-in-the-loop；设计 20 条端到端 eval case（10 正常 + 5 边界 + 5 安全），任务成功率达到 __%，平均步数 __，通过工具结果截断将平均成本降低 __%。
  
  - 填上具体数字（从 eval_results.json 拿）
  - 改到自己语言风格
  - 存到 `notes/week4/resume-bullet.md`

- [ ] **[30min]** Git commit + push：
  ```bash
  cd projects/01-minimal-agent
  git add .
  git commit -m "feat: complete First 7 Days Sprint"
  git tag v1.0-sprint
  git push origin main --tags
  ```

---

## 📚 Day 6-7 的意义

**为什么要项目打包？**
- 别人（包括未来的面试官）clone 后能跑
- README 是项目的"门面"

**为什么要写简历 bullet？**
- 现在不写，3 个月后会忘细节
- 量化指标（成功率、步数）是**最有说服力的**

**模板为什么重要？**
- 你不需要从 0 写简历，直接套模板
- STAR 法则（情境/任务/行动/结果）让简历专业 10 倍

---

## 📊 进度

```
W5 D6-D7: [░░░░░░░░░░] 0/4
W5 整体:  [░░░░░░░░░░] 0/21
阶段 2:   [░░░░░░░░░░] 0/21
```

---

## ✅ 阶段 2 验收（必须全部 ✅）

- [ ] 200 行最小 Agent 能跑
- [ ] 2 个 tool card 完整
- [ ] 5 层 context builder 已实现
- [ ] 20 条 eval 跑过，分数记录
- [ ] README + eval_report + demo_script 齐全
- [ ] 简历 bullet 已写好
- [ ] GitHub commit + tag

---

## 🎉 阶段 2 毕业 = 整个路线的关键里程碑

完成这 7 天后，你已经：
- ✅ **真正理解**了 Agent（不是"看过文档"）
- ✅ 有一个**可写进简历**的项目
- ✅ 掌握了"做出什么 > 学过什么"的节奏
- ✅ 接下来 10 周可以放心学框架

---

## 💡 下周预览

**W5 阶段 3 RAG 入门**：
- FastAPI 基础
- 文档加载 + 切片
- 向量化 + 向量库
- 端到端 Naive RAG

明天打开 [`../03-stage-3/W5-D1-mon.md`](../03-stage-3/W5-D1-mon.md)。