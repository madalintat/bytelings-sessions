"""Day 3 tests — storage layer.

We test save/load round-trip in a tmp dir. We don't import the package
top-level (which would require uv sync to install it); instead we
exercise storage.save/load by passing in already-built Habit objects.
"""
import importlib.util
import sys
from datetime import date
from pathlib import Path

_HERE = Path(__file__).parent.parent
_PKG = _HERE / "src" / "habit"


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, _PKG / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


core = _load("_d130_core_for_storage", "core.py")
# storage.py uses `from .core import ...`. Patch the relative import by
# making storage.py's module global namespace include the names we have.
# Simpler trick: re-read storage.py source and exec it manually with
# `core` in the globals.
_STORAGE_SRC = (_PKG / "storage.py").read_text(encoding="utf-8")
_STORAGE_SRC = _STORAGE_SRC.replace("from .core import", "from _d130_core_for_storage import")
sys.modules["_d130_core_for_storage"] = core
_storage_ns: dict = {"__name__": "_d130_storage"}
exec(compile(_STORAGE_SRC, str(_PKG / "storage.py"), "exec"), _storage_ns)
storage = type(sys)("_d130_storage")
storage.__dict__.update(_storage_ns)


def test_load_missing_file_returns_empty(tmp_path: Path):
    assert storage.load(tmp_path / "absent.json") == {}


def test_save_then_load_roundtrip(tmp_path: Path):
    path = tmp_path / "data.json"
    h = core.Habit(name="read", created=date(2026, 5, 1),
                   log=[date(2026, 5, 8), date(2026, 5, 9)])
    storage.save(path, {"read": h})
    loaded = storage.load(path)
    assert loaded == {"read": h}


def test_mark_done_auto_creates(tmp_path: Path):
    habits: dict = {}
    today = date(2026, 5, 9)
    storage.mark_done(habits, "meditate", today)
    assert "meditate" in habits
    assert habits["meditate"].log == [today]
