"""
练习 9 · 生成器版文本处理（W3 D2）
==================================

难度递进（从简单到复杂，建议按顺序做）：
  ① take()               — 消费任意迭代器，取前 n 个
  ② read_nonempty_lines() — 文件 → 逐行生成器
  ③ chunk_text()          — 字符串 → 定长片段
  ④ chunk_lines()         — 行流 → 定长片段（需要缓冲区，支持无限输入）
  ⑤ chunk_document()      — 组合 ② + ④，一条完整的文档处理流水线

验收标准（全部满足才算完成）：
1. take(iterable, n)：返回前 n 个元素组成的 list；元素不足时返回全部；
   必须惰性消费——不能先把整个 iterable 变成 list 再取（测试会检测）
2. read_nonempty_lines(path)：返回生成器；逐行去掉首尾空白、跳过空行
3. chunk_text(text, size)：返回生成器；每段最多 size 个字符；
   空文本不产出任何片段；size <= 0 时抛 ValueError
4. chunk_lines(lines, size)：返回生成器；把一组"不含换行符"的行用 "\n"
   重新连接后流式切块，每块最多 size 个字符；必须支持无限输入（惰性）
5. chunk_document(path, size)：返回生成器；复用 read_nonempty_lines 和
   chunk_lines 组合出"读文件 → 过滤空行 → 切块"的流水线
6. 运行 `python ex09_generators.py`，全部断言通过并打印 "✅ 全部断言通过"

实现提示：
- take：for 循环 + 计数器 + break；不需要 itertools 也可以
- read_nonempty_lines：`with open(...) as f:`，`for line in f`，`line.strip()`，
  空行（strip 后为空字符串）跳过
- chunk_text：可以用 `range(0, len(text), size)` 配合切片
- chunk_lines：维护一个缓冲区字符串 `buf`；每读一行先接进 buf（行之间补 "\n"），
  只要 buf 长度 >= size 就 yield 一段并切掉前 size 个字符；循环结束后如果 buf 非空，
  再 yield 一次
- chunk_document：把前两个生成器"串"起来——生成器可以作为另一个生成器的输入，
  不需要中间列表

调试提示：测试是按顺序断言的，当前失败的那一行就是你要解决的下一题。
不要修改文件末尾的验收测试。
"""

import os
import tempfile


def take(iterable, n: int) -> list:
    """取 iterable 的前 n 个元素；必须惰性消费（支持无限迭代器）。"""
    while n > 0:
        yield iterable[n - 1]
        n -= 1


def read_nonempty_lines(path: str):
    """逐行读取文件：去掉首尾空白、跳过空行，yield 每一行。"""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() not in ("\n", "\t"):
                continue
            yield line



def chunk_text(text: str, size: int):
    """把 text 切成每段最多 size 个字符的片段；size <= 0 抛 ValueError。"""
    index = 0
    if size <= 0:
        raise ValueError('size can not be <= 0')
    for i in text:
        s = text.split(i, size)
        index += size
        yield s

def chunk_lines(lines, size: int):
    """把一组行（不含换行符）用 "\\n" 连接后流式切块，每块最多 size 个字符。"""



def chunk_document(path: str, size: int):
    """组合 read_nonempty_lines + chunk_lines：读文件 → 过滤空行 → 切块。"""
    raise NotImplementedError("实现 chunk_document")


# ════════════════════════════════════════════════════════════
# 验收测试：以下代码不要修改。
# ════════════════════════════════════════════════════════════
def run_tests() -> None:
    # ── 1. take ──────────────────────────────────────────
    assert take([1, 2, 3, 4], 2) == [1, 2]
    assert take([], 5) == []
    assert take([1, 2], 10) == [1, 2]

    def cautious_source(limit: int):
        """如果被消费超过 limit 个元素就报错——用来检测是否惰性。"""
        for i in range(100):
            if i >= limit:
                raise AssertionError("take 消费了超过 n 个元素，说明没有惰性")
            yield i

    assert take(cautious_source(5), 3) == [0, 1, 2], "take 必须惰性消费"

    # ── 2. read_nonempty_lines 与 5. chunk_document ──────
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write("  first line  \n\nsecond line\n   \nthird\n")
    try:
        it = read_nonempty_lines(path)
        assert hasattr(it, "__next__"), "read_nonempty_lines 必须返回生成器/迭代器"
        assert list(it) == ["first line", "second line", "third"]

        doc = chunk_document(path, 7)
        assert hasattr(doc, "__next__"), "chunk_document 必须返回生成器"
        chunks = list(doc)
        assert "".join(chunks) == "first line\nsecond line\nthird"
        assert all(len(c) <= 7 for c in chunks), "每块长度不能超过 size"
    finally:
        os.unlink(path)

    # ── 3. chunk_text ────────────────────────────────────
    assert list(chunk_text("abcdefg", 3)) == ["abc", "def", "g"]
    assert "".join(chunk_text("abcdefg", 3)) == "abcdefg"
    assert list(chunk_text("", 5)) == []
    try:
        list(chunk_text("abc", 0))
    except ValueError:
        pass
    else:
        raise AssertionError("size <= 0 应抛 ValueError")

    # ── 4. chunk_lines ───────────────────────────────────
    assert list(chunk_lines([], 5)) == []
    joined = list(chunk_lines(["ab", "cd", "ef"], 4))
    assert "".join(joined) == "ab\ncd\nef"
    assert all(len(c) <= 4 for c in joined), "每块长度不能超过 size"

    def long_source():
        for i in range(100_000):
            yield f"line{i}"
        raise AssertionError("chunk_lines 把整个输入读完了，说明没有惰性")

    chunks = take(chunk_lines(long_source(), 30), 3)
    assert len(chunks) == 3, "应能从前 3 块后立即停止"
    assert all(len(c) <= 30 for c in chunks)

    print("✅ 全部断言通过")


if __name__ == "__main__":
    run_tests()
