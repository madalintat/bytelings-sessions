"""Tests for rung 2 — correctness + perf bound."""
import importlib.util
import inspect
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


URLS = [f"https://x/{i}" for i in range(10)]


def test_correctness():
    out = ex.fetch_all(URLS)
    assert out == [len(u) for u in URLS]


def test_uses_thread_pool():
    src = inspect.getsource(ex.fetch_all)
    assert "ThreadPoolExecutor" in src or "concurrent.futures" in src, (
        "use a ThreadPoolExecutor"
    )


def test_perf_bound():
    """10 calls of 100ms each, parallel, should be << 0.5s."""
    start = time.perf_counter()
    ex.fetch_all(URLS)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.5, (
        f"too slow ({elapsed:.2f}s) — switch to ThreadPoolExecutor.map"
    )
