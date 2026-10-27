"""
练习 7 · ChatHistory 类（W3 D1）
================================

目标：用类封装"对话历史管理"——这是后面聊天机器人、Agent 项目都会复用的组件。

验收标准（全部满足才算完成）：
1. ChatHistory("你是助手") 创建实例；system_prompt 为空字符串时抛 ValueError
2. add(role, content) 追加一条消息（role 不用校验）
3. message_count 是只读属性，返回消息条数（不含 system prompt）
4. to_payload() 返回可直接喂给 LLM API 的列表，system 固定在最前：
   [{"role": "system", ...}, {"role": "user", ...}, ...]
5. to_dict() 返回完整状态，且能通过 json.dumps() 序列化
6. from_dict() 是 @classmethod，内部用 cls(...) 构造（体会和 staticmethod 的区别）
7. 运行 `python ex07_chat_history.py`，全部断言通过并打印 "✅ 全部断言通过"

实现提示：
- 内部字段命名用 _system_prompt / _messages（下划线 = 约定俗成的"内部"）
- to_payload() 不要把内部列表直接交出去（想想调用方 append 之后会发生什么）；
  也别把 system prompt 塞进 _messages —— system 不是历史消息
- from_dict 里调用 cls(...)，不要写死 ChatHistory(...) —— 想想子类继承时会发生什么
- 查语法、查文档都行；不要直接搜"ChatHistory 题解"

进阶挑战（选做，review 时讲一下你的取舍）：
- 用 @property + setter 给 system_prompt 加校验（空值不允许）
- 加 save(path) / load(path) classmethod，用 pathlib + json 存到文件
- 加 __repr__，让 print(h) 输出可读内容
- 加 trim(max_messages) 方法，只保留最近 N 条 —— 这是"上下文压缩"的雏形

不要修改文件末尾的验收测试。
"""

import json


class ChatHistory:
    """管理一次对话的消息历史。"""

    def __init__(self, system_prompt: str) -> None:
        if not system_prompt:
            raise ValueError('system prompt can not be empty')
        self.system_prompt = system_prompt
        self._messages: list[dict] = []

    def add(self, role: str, content: str) -> None:
        """追加一条消息。role 常见取值为 'user' / 'assistant'。"""
        self._messages.append({"role": role, "content": content})

    @property
    def message_count(self) -> int:
        """消息条数（不含 system prompt）。"""
        return len(self._messages)

    def to_payload(self) -> list[dict]:
        """返回可直接传给 LLM API 的消息列表，system prompt 固定在最前。"""
        return [{'role': 'system', 'content': self.system_prompt}, *self._messages]

    def to_dict(self) -> dict:
        """返回可 JSON 序列化的完整状态。"""
        return {
            'system_prompt': self.system_prompt,
            'messages': list(self._messages)
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ChatHistory":
        """从 to_dict() 的结果重建实例。"""
        chat_history = cls(data["system_prompt"])
        for msg in data['messages']:
            chat_history.add(msg['role'], msg['content'])
        return chat_history


# ════════════════════════════════════════════════════════════
# 验收测试：以下代码不要修改。你的实现必须让全部断言通过。
# ════════════════════════════════════════════════════════════
def run_tests() -> None:
    h = ChatHistory("你是助手")
    assert h.message_count == 0, "初始消息数应为 0"

    h.add("user", "你好")
    h.add("assistant", "你好，有什么可以帮你？")
    assert h.message_count == 2, "添加两条消息后 message_count 应为 2"

    payload = h.to_payload()
    assert payload[0] == {"role": "system", "content": "你是助手"}, "system 必须在最前"
    assert payload[1] == {"role": "user", "content": "你好"}
    assert len(payload) == 3, "payload 应包含 system + 两条消息"

    data = h.to_dict()
    json.dumps(data, ensure_ascii=False)  # 必须能序列化，否则抛 TypeError

    h2 = ChatHistory.from_dict(data)
    assert h2 is not h, "from_dict 必须返回新实例"
    assert h2.to_payload() == h.to_payload(), "重建后的内容必须一致"

    # 独立性检查：h 后续变化不能影响 h2（说明内部列表没有被共享）
    h.add("user", "第三条")
    assert h2.message_count == 2, "h2 不应受 h 后续变化影响"

    try:
        ChatHistory("")
    except ValueError:
        pass
    else:
        raise AssertionError("空 system_prompt 应该抛 ValueError")

    print("✅ 全部断言通过")


if __name__ == "__main__":
    run_tests()
