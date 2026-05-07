"""Shared fixtures for the day 6 refactor test suite.

We don't import the package by name (because it isn't installed into
the swe-skills env). We load the modules via importlib and expose them
as fixtures.
"""
import importlib.util
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).parent.parent
_PKG = _HERE / "src" / "habit"


def _load(name: str, file: str, extra_replace: dict | None = None):
    src = (_PKG / file).read_text(encoding="utf-8")
    if extra_replace:
        for old, new in extra_replace.items():
            src = src.replace(old, new)
    spec = importlib.util.spec_from_file_location(name, _PKG / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    if extra_replace:
        # exec the rewritten source in the module's namespace
        exec(compile(src, str(_PKG / file), "exec"), mod.__dict__)
    else:
        spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def core_mod():
    return _load("_d134_core", "core.py")


@pytest.fixture(scope="session")
def storage_mod(core_mod):
    # storage.py uses `from .core import ...`; rewrite to use our loaded core.
    return _load(
        "_d134_storage",
        "storage.py",
        extra_replace={"from .core import": "from _d134_core import"},
    )


@pytest.fixture
def data_path(tmp_path: Path, monkeypatch):
    """A scratch data path that overrides HABIT_DATA for the test."""
    p = tmp_path / "data.json"
    monkeypatch.setenv("HABIT_DATA", str(p))
    return p
