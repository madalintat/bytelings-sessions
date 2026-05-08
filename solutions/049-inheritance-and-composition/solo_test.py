"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_memorystore_save_load():
    s = ex.MemoryStore()
    s.save("k", "v")
    assert s.load("k") == "v"


def test_memorystore_missing_key():
    s = ex.MemoryStore()
    with pytest.raises(KeyError):
        s.load("missing")


def test_logger_with_real_store():
    s = ex.MemoryStore()
    log = ex.Logger(s)
    log.info("hello")
    log.info("world")
    assert s.load("info-0") == "hello"
    assert s.load("info-1") == "world"


def test_logger_count():
    log = ex.Logger(ex.MemoryStore())
    assert log.count == 0
    log.info("a")
    log.info("b")
    log.info("c")
    assert log.count == 3


def test_count_is_property():
    log = ex.Logger(ex.MemoryStore())
    # Property access — no parens.
    assert log.count == 0
    assert not callable(log.count)


def test_logger_with_fake_store():
    """The point of composition: a fake store with the same .save/.load works."""
    class FakeStore:
        def __init__(self):
            self.saved = []
        def save(self, key, value):
            self.saved.append((key, value))
        def load(self, key):
            for k, v in self.saved:
                if k == key:
                    return v
            raise KeyError(key)

    fake = FakeStore()
    log = ex.Logger(fake)
    log.info("hi")
    assert fake.saved == [("info-0", "hi")]
