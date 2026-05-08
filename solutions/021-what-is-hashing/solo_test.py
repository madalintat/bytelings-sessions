"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_len():
    s = ex.TinySet()
    assert len(s) == 0


def test_add_and_contains():
    s = ex.TinySet()
    s.add("a")
    assert "a" in s
    assert "b" not in s


def test_add_idempotent():
    s = ex.TinySet()
    s.add("a")
    s.add("a")
    assert len(s) == 1


def test_discard_present():
    s = ex.TinySet()
    s.add(1)
    s.discard(1)
    assert 1 not in s
    assert len(s) == 0


def test_discard_absent_no_error():
    s = ex.TinySet()
    s.discard("nope")  # must not raise
    assert len(s) == 0


def test_collision_bucket():
    s = ex.TinySet(n_buckets=1)  # forces all collisions
    for i in range(100):
        s.add(i)
    for i in range(100):
        assert i in s
    assert len(s) == 100
    s.discard(50)
    assert 50 not in s
    assert len(s) == 99


def test_no_builtin_set_used():
    """We're rolling our own — don't cheat with Python's set/dict for storage."""
    import inspect
    src = inspect.getsource(ex.TinySet)
    # Heuristic: ban set( and dict( and {} as storage backbones.
    # (still allowed: hash(...), tuples, lists.)
    assert "set(" not in src, "Don't use Python's built-in set for storage"
