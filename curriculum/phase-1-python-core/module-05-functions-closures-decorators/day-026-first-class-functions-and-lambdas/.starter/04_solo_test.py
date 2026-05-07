"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    steps = [
        ("plus_one", lambda x: x + 1),
        ("times_two", lambda x: x * 2),
        ("to_str", str),
    ]
    run = ex.pipeline(steps)
    final, trace = run(3)
    assert final == "8"
    assert trace == [("plus_one", 4), ("times_two", 8), ("to_str", "8")]


def test_empty_steps():
    run = ex.pipeline([])
    final, trace = run(42)
    assert final == 42
    assert trace == []


def test_single_step():
    run = ex.pipeline([("double", lambda x: x * 2)])
    final, trace = run(5)
    assert final == 10
    assert trace == [("double", 10)]


def test_value_is_passed_through():
    run = ex.pipeline([("identity", lambda x: x)])
    final, trace = run("hello")
    assert final == "hello"
    assert trace == [("identity", "hello")]


def test_pipeline_reusable():
    """Calling run() twice should not interfere — fresh trace each time."""
    run = ex.pipeline([("plus_one", lambda x: x + 1)])
    f1, t1 = run(0)
    f2, t2 = run(10)
    assert f1 == 1
    assert f2 == 11
    assert t1 == [("plus_one", 1)]
    assert t2 == [("plus_one", 11)]
