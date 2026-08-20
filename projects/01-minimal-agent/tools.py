"""
工具实现 — First 7 Days Sprint 的 2 个最小工具

设计原则（来自 Anthropic "Writing tools for agents"）：
1. 返回结构化 dict，不用异常传递业务错误
2. 错误格式统一：{"ok": false, "error": "<code>", "retryable": bool, "hint": "..."}
3. 限制返回数量，避免 context 爆炸
4. 高风险工具（写操作）标记 requires_confirmation
5. 工具名是动词_名词（search_notes, write_summary）

下一步升级方向：
- search_notes → 换成向量检索（Chroma / Milvus）
- write_summary → 加锁、加版本号、加权限校验
"""

from __future__ import annotations

from pathlib import Path

# ============================================================
# 模拟"个人笔记库"
# 真实项目里这通常是一个向量数据库（Chroma / Milvus / Qdrant）
# ============================================================

NOTES_DB: dict[str, dict] = {
    "python-async": {
        "title": "Python 异步编程笔记",
        "content": (
            "asyncio 是 Python 标准库的异步框架。"
            "async def 定义协程函数，await 等待异步操作完成。"
            "事件循环（event loop）是 asyncio 的核心，"
            "asyncio.run() 启动主循环，asyncio.gather() 并发执行多个协程。"
            "常见陷阱：阻塞调用（time.sleep）会卡死整个事件循环。"
        ),
        "tags": ["python", "async", "asyncio"],
    },
    "react-hooks": {
        "title": "React Hooks 学习笔记",
        "content": (
            "useState 管理组件本地状态。"
            "useEffect 处理副作用（数据获取、订阅），依赖数组决定何时重跑。"
            "useMemo 缓存计算结果，useCallback 缓存回调函数。"
            "自定义 Hook 是复用状态逻辑的标准方式。"
            "规则：Hook 必须在顶层调用，不能写在条件或循环里。"
        ),
        "tags": ["react", "frontend", "hooks"],
    },
    "agent-basics": {
        "title": "Agent 基础概念",
        "content": (
            "Agent = LLM（推理）+ Loop（循环）+ Tools（行动）+ Memory（记忆）。"
            "ReAct 是最经典的循环模式：Reasoning（推理）+ Acting（行动）交替进行。"
            "生产 Agent 不会暴露完整思维链，只记录可审计的 reason_summary。"
            "五大组件：Goal、Policy、State、Context Builder、Eval/Trace。"
        ),
        "tags": ["agent", "llm", "react"],
    },
    "langgraph-intro": {
        "title": "LangGraph 入门",
        "content": (
            "LangGraph 用图（StateGraph）定义 Agent 流程，"
            "节点是函数，边是条件转移。"
            "比裸写 ReAct 循环更适合生产：支持分支、持久化、检查点、人在回路。"
            "核心概念：State、Node、Edge、Conditional Edge、Checkpoint。"
        ),
        "tags": ["agent", "langgraph", "framework"],
    },
}


# ============================================================
# 工具函数实现
# ============================================================

def search_notes(query: str, limit: int = 3) -> dict:
    """在笔记库中搜索关键词

    Args:
        query: 搜索关键词
        limit: 返回数量上限（默认 3，最大 10）

    Returns:
        {
          "ok": true,
          "count": 2,
          "results": [{"id": "...", "title": "...", "snippet": "...", "score": 3}, ...]
        }

        或错误：
        {"ok": false, "error": "empty_query", "retryable": false, "hint": "..."}
    """
    # 参数校验
    if not query or not query.strip():
        return {
            "ok": False,
            "error": "empty_query",
            "retryable": False,
            "hint": "query 不能为空字符串",
        }
    if limit < 1 or limit > 10:
        return {
            "ok": False,
            "error": "invalid_limit",
            "retryable": False,
            "hint": "limit 应在 1-10 之间",
        }

    # 简单关键词匹配（生产环境换成向量检索）
    query_lower = query.lower()
    hits: list[dict] = []
    for note_id, note in NOTES_DB.items():
        score = 0
        if query_lower in note["title"].lower():
            score += 3
        for tag in note["tags"]:
            if query_lower in tag.lower():
                score += 2
        if query_lower in note["content"].lower():
            score += 1
        if score > 0:
            hits.append({
                "id": note_id,
                "title": note["title"],
                "snippet": note["content"][:80] + "..." if len(note["content"]) > 80 else note["content"],
                "score": score,
            })

    hits.sort(key=lambda x: x["score"], reverse=True)
    hits = hits[:limit]

    return {
        "ok": True,
        "count": len(hits),
        "query": query,
        "results": hits,
    }


def write_summary(text: str, filename: str = "summary.md") -> dict:
    """把总结写入 output 文件夹

    ⚠️ 高风险操作（写文件）：需要 human-in-the-loop 确认。

    Args:
        text: 要写入的内容
        filename: 文件名，默认 summary.md

    Returns:
        {"ok": true, "path": "output/summary.md", "bytes": 1234}
    """
    if not text or not text.strip():
        return {
            "ok": False,
            "error": "empty_text",
            "retryable": False,
            "hint": "text 不能为空",
        }

    # 安全检查：禁止路径穿越
    if "/" in filename or "\\" in filename or filename.startswith("."):
        return {
            "ok": False,
            "error": "invalid_filename",
            "retryable": False,
            "hint": "filename 不能包含路径分隔符或以 . 开头",
        }

    out_path = Path("./output") / filename
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")

    return {
        "ok": True,
        "path": str(out_path),
        "bytes": len(text.encode("utf-8")),
    }


# ============================================================
# 工具注册表（Agent 通过这个 dict 找工具）
# ============================================================

TOOL_REGISTRY: dict[str, dict] = {
    "search_notes": {
        "func": search_notes,
        "description": "在个人笔记库中搜索关键词，返回匹配的笔记列表（含 id、title、snippet、score）。",
        "requires_confirmation": False,
        "input_schema": {
            "query": {"type": "string", "required": True, "description": "搜索关键词"},
            "limit": {"type": "integer", "required": False, "default": 3, "description": "返回数量上限（1-10）"},
        },
    },
    "write_summary": {
        "func": write_summary,
        "description": "把总结内容写入 output/<filename.md>。高风险操作：会触发 human-in-the-loop 确认。",
        "requires_confirmation": True,
        "input_schema": {
            "text": {"type": "string", "required": True, "description": "要写入的内容"},
            "filename": {"type": "string", "required": False, "default": "summary.md", "description": "文件名（不含路径）"},
        },
    },
}


# ============================================================
# 工具 schema 转 LLM-friendly 描述（用于 prompt）
# ============================================================

def get_tool_descriptions() -> str:
    """生成给模型看的工具描述（用于 system prompt）"""
    lines = []
    for name, meta in TOOL_REGISTRY.items():
        lines.append(f"### {name}")
        lines.append(f"  描述：{meta['description']}")
        if meta["requires_confirmation"]:
            lines.append("  ⚠️ 高风险：需要人类确认")
        lines.append("  参数：")
        for param, schema in meta["input_schema"].items():
            req = "必填" if schema.get("required") else "可选"
            default = f" 默认={schema.get('default')}" if "default" in schema else ""
            lines.append(f"    - {param} ({schema['type']}, {req}){default}: {schema['description']}")
        lines.append("")
    return "\n".join(lines)