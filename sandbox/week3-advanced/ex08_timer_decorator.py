"""
练习 8 · 计时装饰器（W3 D2）
============================

目标：写一个装饰器 @timer，记录被装饰函数的执行耗时。
这是你以后写 Agent 时"观测每一步耗时"的最小原型。

验收标准（全部满足才算完成）：
1. @timer 装饰的函数：参数原样透传（位置参数和关键字参数都要支持），返回值原样返回
2. 每次调用都产生一条记录，形如：
   {"name": "函数名", "duration_ms": 12.3, "ok": True}
   （ok 表示函数是否成功返回；抛异常时为 False）
3. get_records() 返回记录列表；返回的必须是副本，调用方改动不影响内部记录
4. clear_records() 清空记录（测试会用它隔离用例）
5. 装饰后元信息保留：被装饰函数的 __name__、__doc__ 不变（functools.wraps）
6. 函数抛异常时：异常继续抛给调用方，但**耗时记录依然要产生**（ok=False）
7. 运行 `python ex08_timer_decorator.py`，全部断言通过并打印 "✅ 全部断言通过"

实现提示：
- 装饰器的本质：接收一个函数，返回一个新函数
- 计时用 time.perf_counter()（高精度、单调），不要用 time.time()
- 新函数用 *args, **kwargs 接收任意参数并原样转发
- functools.wraps(func) 放到 wrapper 上，元信息就保住了
- "异常时也要记录"——想想 try/except/finally 各自在什么时候执行（finally 一定会执行）
- 不要在 get_records 里把内部列表直接交出去（上一课刚学过的）

进阶挑战（选做）：
- 让装饰器能带参数：@timer(label="search")——需要"装饰器工厂"（三层函数）
- 记录参数摘要（截断长参数），想想隐私敏感参数要不要记录
- 写成类装饰器（__call__），体会和函数装饰器的区别

不要修改文件末尾的验收测试。
"""

import functools
import time

# 记录存放在这里；测试通过 get_records()/clear_records() 访问
_records: list[dict] = []


def timer(func):
    """装饰器：记录 func 的执行耗时，用法 @timer。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ok = True
        try:
            return func(*args, **kwargs)
        except Exception:
            ok = False
            raise
        finally:
            _records.append({"name": func.__name__, "duration_ms": (time.perf_counter() - start) * 1000, "ok": ok})
    return wrapper

def get_records() -> list[dict]:
    return list(_records)


def clear_records() -> None:
    _records.clear()


# ════════════════════════════════════════════════════════════
# 验收测试：以下代码不要修改。
# ════════════════════════════════════════════════════════════
def run_tests() -> None:
    clear_records()

    @timer
    def add(a, b=0):
        """两数相加"""
        return a + b

    assert add(1, 2) == 3, "返回值必须原样透传"
    assert add(1, b=5) == 6, "关键字参数必须透传"

    records = get_records()
    assert len(records) == 2, f"应有 2 条记录，实际 {len(records)}"
    last = records[-1]
    assert last["name"] == "add", f"记录 name 不对: {last!r}"
    assert last["ok"] is True, "成功调用 ok 应为 True"
    assert isinstance(last["duration_ms"], float), "duration_ms 应是 float"
    assert last["duration_ms"] >= 0

    # 元信息保留（functools.wraps）
    assert add.__name__ == "add", f"__name__ 应保留，实际 {add.__name__!r}"
    assert add.__doc__ == "两数相加", "__doc__ 应保留"

    # 独立副本：改返回值不影响内部记录
    rec = get_records()
    rec.append({"name": "fake", "duration_ms": 0.0, "ok": True})
    assert len(get_records()) == 2, "get_records 必须返回副本，不能交出内部列表"

    # 耗时测量合理
    @timer
    def slow():
        time.sleep(0.03)

    slow()
    assert get_records()[-1]["duration_ms"] >= 20, "30ms 的 sleep 应记录到至少 20ms"

    # 异常：继续抛出 + 依然记录
    @timer
    def boom():
        raise RuntimeError("boom")

    try:
        boom()
    except RuntimeError:
        pass
    else:
        raise AssertionError("异常必须继续抛给调用方")
    assert get_records()[-1]["ok"] is False, "异常调用 ok 应为 False"

    print("✅ 全部断言通过")


if __name__ == "__main__":
    run_tests()
