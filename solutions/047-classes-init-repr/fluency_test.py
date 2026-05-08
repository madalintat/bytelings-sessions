"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_init():
    c = ex.Counter("cards")
    assert c.name == "cards"
    assert c.value == 0


def test_init_with_start():
    c = ex.Counter("cards", 10)
    assert c.value == 10


def test_increment():
    c = ex.Counter("x")
    c.increment()
    c.increment()
    assert c.value == 2


def test_repr_quotes_the_name():
    c = ex.Counter("cards", 3)
    assert repr(c) == "Counter(name='cards', value=3)"


def test_repr_for_default_start():
    c = ex.Counter("zeros")
    assert repr(c) == "Counter(name='zeros', value=0)"
