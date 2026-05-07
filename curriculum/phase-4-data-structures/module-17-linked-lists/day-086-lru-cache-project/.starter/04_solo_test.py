"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_caching():
    calls = []

    def slow(n):
        calls.append(n)
        return n * 2

    f = ex.memoize_lru(slow, capacity=2)
    assert f(1) == 2
    assert f(2) == 4
    assert f(1) == 2
    assert calls == [1, 2]


def test_hit_miss_counters():
    f = ex.memoize_lru(lambda x: x, capacity=2)
    f(1); f(2); f(1)
    assert f.misses == 2
    assert f.hits == 1


def test_eviction_on_capacity():
    calls = []

    def slow(n):
        calls.append(n)
        return n

    f = ex.memoize_lru(slow, capacity=2)
    f(1); f(2); f(3)   # 3 evicts 1
    f(1)               # miss again, since 1 was evicted
    assert calls == [1, 2, 3, 1]


def test_recent_access_protects_from_eviction():
    calls = []

    def slow(n):
        calls.append(n)
        return n

    f = ex.memoize_lru(slow, capacity=2)
    f(1); f(2); f(1); f(3)   # f(1) before f(3) means 2 is LRU; 3 evicts 2
    f(2)                     # miss, since 2 was evicted
    f(1)                     # hit
    assert calls == [1, 2, 3, 2]


def test_cache_clear():
    f = ex.memoize_lru(lambda x: x, capacity=2)
    f(1); f(1)
    assert f.hits == 1
    f.cache_clear()
    assert f.hits == 0
    assert f.misses == 0
    f(1)
    assert f.misses == 1


def test_multi_arg_keys():
    f = ex.memoize_lru(lambda a, b: a + b, capacity=4)
    assert f(1, 2) == 3
    assert f(1, 2) == 3
    assert f.hits == 1
    assert f(2, 1) == 3
    assert f.misses == 2  # (1,2) and (2,1) are different keys
