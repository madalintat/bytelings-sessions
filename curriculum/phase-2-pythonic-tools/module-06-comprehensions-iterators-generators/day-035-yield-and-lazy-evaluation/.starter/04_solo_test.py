"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from itertools import islice
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_naturals_first_five():
    assert list(islice(ex.naturals(), 5)) == [1, 2, 3, 4, 5]


def test_naturals_returns_generator():
    import types
    assert isinstance(ex.naturals(), types.GeneratorType)


def test_take_while_basic():
    assert list(ex.take_while(lambda n: n < 5, ex.naturals())) == [1, 2, 3, 4]


def test_take_while_immediately_false():
    assert list(ex.take_while(lambda n: n > 100, ex.naturals())) == []


def test_take_while_on_finite_source():
    assert list(ex.take_while(lambda x: x < 3, [1, 2, 3, 4, 1])) == [1, 2]


def test_take_while_does_not_consume_past_failure():
    """After predicate fails on item X, the source must not be drained further."""
    source = iter([1, 2, 99, 3, 4])
    out = list(ex.take_while(lambda n: n < 50, source))
    assert out == [1, 2]
    # The 99 was consumed (had to test it), but 3 and 4 must still be there.
    assert list(source) == [3, 4]
