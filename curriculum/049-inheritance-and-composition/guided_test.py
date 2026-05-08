"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_animal_basic():
    a = ex.Animal("?")
    assert a.name == "?"
    assert a.speak() == "(generic noise)"


def test_dog_inherits_name():
    d = ex.Dog("Rex", "lab")
    assert d.name == "Rex"
    assert d.breed == "lab"


def test_dog_speak_overrides():
    assert ex.Dog("Rex", "lab").speak() == "Rex says woof"


def test_dog_is_an_animal():
    d = ex.Dog("Rex", "lab")
    assert isinstance(d, ex.Animal)


def test_super_was_called():
    """super().__init__(name) is what gives Dog its `.name` attribute."""
    d = ex.Dog("Buddy", "poodle")
    assert d.name == "Buddy"
