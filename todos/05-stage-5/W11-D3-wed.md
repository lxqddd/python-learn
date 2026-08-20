# W11 D3 周三 · 2h — 监控与日志

- **阶段**：5 多 Agent + MCP | **周次**：W11 | **状态**：⬜
- **主题**：结构化日志 + 链路追踪

---

## 🎯 今日目标（3 项）

- [ ] 学 structlog 结构化日志
- [ ] 接 OpenTelemetry / LangSmith trace
- [ ] 记录关键指标

---

## ✅ 任务清单（2h）

### 💻 结构化日志（60min）

- [ ] **[60min]** 创建 `monitoring/logger.py`：

  ```python
  import structlog
  import logging
  import time
  from functools import wraps
  
  logging.basicConfig(level=logging.INFO)
  structlog.configure(
      processors=[
          structlog.processors.TimeStamper(fmt="iso"),
          structlog.processors.JSONRenderer(),
      ],
  )
  
  log = structlog.get_logger()
  
  def trace_calls(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          t0 = time.time()
          log.info("function_called", func=func.__name__)
          try:
              result = func(*args, **kwargs)
              log.info("function_completed", func=func.__name__, elapsed_ms=round((time.time()-t0)*1000, 2))
              return result
          except Exception as e:
              log.error("function_failed", func=func.__name__, error=str(e))
              raise
      return wrapper
  ```

  - 安装：`uv pip install structlog`
  - 跑通看 JSON 输出

### 📊 指标收集（40min）

- [ ] **[40min]** 创建 `monitoring/metrics.py`：用 dataclass 收集成功/失败/延迟/token

### 🔗 接 LangSmith trace（20min）

- [ ] **[20min]** 验证 LangSmith 上能看到 trace

### 📝 笔记（20min）

- [ ] **[20min]** 写 `notes/week11/day3-monitoring.md`

---

## ✅ 当日验收

- [ ] structlog 输出 JSON
- [ ] 指标收集能记录成功/失败
- [ ] LangSmith 上能看到 trace

---

## 💡 明日预告

**W11 D4 周四**：Railway 部署