"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_http_is_async():
    assert ex.best_tool("http") == "async"


def test_sleep_is_async():
    assert ex.best_tool("sleep") == "async"


def test_disk_is_async():
    assert ex.best_tool("disk_read") == "async"


def test_hash_is_threads():
    assert ex.best_tool("hash_4gb") == "threads"


def test_matrix_is_threads():
    assert ex.best_tool("matrix_mul") == "threads"


def test_in_memory_is_neither():
    assert ex.best_tool("in_memory") == "neither"
