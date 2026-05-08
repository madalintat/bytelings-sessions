"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def good_fetch(url: str) -> str:
    return f"ok:{url[-1]}"


def mixed_fetch(url: str) -> str:
    if url.endswith("3"):
        raise RuntimeError("boom")
    return f"ok:{url[-1]}"


def test_all_succeed():
    urls = ["https://x/1", "https://x/2"]
    out = ex.gather_results(urls, good_fetch)
    assert out == {"https://x/1": "ok:1", "https://x/2": "ok:2"}


def test_partial_failure_does_not_break_others():
    urls = ["https://x/1", "https://x/2", "https://x/3", "https://x/4"]
    out = ex.gather_results(urls, mixed_fetch)
    assert set(out) == set(urls)
    assert out["https://x/1"] == "ok:1"
    assert out["https://x/4"] == "ok:4"
    assert out["https://x/3"].startswith("error: ")
    assert "boom" in out["https://x/3"]


def test_empty_urls():
    assert ex.gather_results([], good_fetch) == {}
