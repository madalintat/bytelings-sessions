"""Tests for rung 2."""
import importlib.util
import typing
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_describe_runtime():
    """At runtime, types don't enforce — output should still be normal."""
    user = {"id": 1, "name": "Bytelinger"}
    assert ex.describe("medium", user) == "Bytelinger (medium)"


def test_user_is_typeddict():
    assert typing.is_typeddict(ex.User)


def test_user_has_correct_fields():
    hints = typing.get_type_hints(ex.User)
    assert hints == {"id": int, "name": str}


def test_describe_mode_is_literal():
    """The `mode` parameter must be annotated as Literal[...]."""
    hints = typing.get_type_hints(ex.describe)
    mode_type = hints["mode"]
    assert typing.get_origin(mode_type) is typing.Literal, (
        "describe.mode must be annotated as Literal[...]"
    )
    assert set(typing.get_args(mode_type)) == {"small", "medium", "large"}
