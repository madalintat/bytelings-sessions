"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_one_simple():
    src = "def add(a, b):\n    return a + b\n"
    out = ex.function_summary(src)
    assert len(out) == 1
    assert out[0]["name"] == "add"
    assert out[0]["line"] == 1
    assert out[0]["args"] == 2
    assert out[0]["is_async"] is False
    assert out[0]["returns"] == 1


def test_no_return():
    src = "def shout(x):\n    print(x)\n"
    out = ex.function_summary(src)
    assert out[0]["returns"] == 0


def test_async():
    src = "async def fetch(url):\n    return url\n"
    out = ex.function_summary(src)
    assert out[0]["is_async"] is True
    assert out[0]["returns"] == 1


def test_args_excludes_varargs():
    src = "def f(a, b, *args, **kwargs):\n    pass\n"
    out = ex.function_summary(src)
    assert out[0]["args"] == 2


def test_returns_excludes_nested():
    src = (
        "def outer(x):\n"
        "    def inner():\n"
        "        return 1\n"
        "    return x\n"
    )
    out = ex.function_summary(src)
    by_name = {f["name"]: f for f in out}
    assert by_name["outer"]["returns"] == 1
    assert by_name["inner"]["returns"] == 1


def test_in_source_order():
    src = "def a():\n    pass\n\ndef b():\n    pass\n\ndef c():\n    pass\n"
    out = ex.function_summary(src)
    assert [f["name"] for f in out] == ["a", "b", "c"]
