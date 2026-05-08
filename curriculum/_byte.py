"""In-tree copy of bytelings.testing.diagnose for curriculum tests.

Shipped alongside the curriculum so test files can import the helper
via a plain `from _byte import diagnose` (curriculum/conftest.py adds
this directory to sys.path on test collection). Mirrors
bytelings/testing.py exactly — keep them in sync if the API ever
evolves.

The pattern bytelings steals from Kaggle's `learntools`: when a test
fails, don't just print a generic AssertionError. Map each anticipated
wrong answer to a teaching message.
"""
from __future__ import annotations

import importlib.util
import sys
from collections.abc import Callable
from pathlib import Path
from typing import TypeAlias

__all__ = ["diagnose", "Check", "load_rung"]

Check: TypeAlias = tuple[Callable[[], bool], str]


_LOADED_RUNGS: dict[str, object] = {}


def load_rung(file_path: Path | str, name: str):
    """Load a rung's source file via spec_from_file_location AND register
    it in sys.modules.

    The default `module_from_spec` + `exec_module` pattern leaves the
    module out of sys.modules, which silently breaks any code that pickles
    helper functions across processes (ProcessPoolExecutor) — pickle uses
    the function's __module__ to import it back in the worker, and
    importlib.import_module(name) requires the entry to exist.

    Memoizes by absolute file path so that the same .py loaded from
    multiple sites (e.g. a test file AND a sibling rung file) gets a
    single module object. Without this, ProcessPoolExecutor fails with
    "not the same object as <module>.<func>" because the two loads
    produce two different function instances under the same alias.

    Use this in test files for days that call ProcessPoolExecutor::

        ex = load_rung(_HERE / "fluency.py", _NAME)
    """
    key = str(Path(file_path).resolve())
    if key in _LOADED_RUNGS:
        return _LOADED_RUNGS[key]
    spec = importlib.util.spec_from_file_location(name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    _LOADED_RUNGS[key] = module
    return module


def diagnose(passed: bool, fallback_msg: str, *checks: Check) -> None:
    """Assert with a per-wrong-answer diagnostic.

    Args:
        passed: the main pass/fail signal (typically ``actual == expected``).
        fallback_msg: shown when the test fails AND no targeted check fired.
            Always orient the learner — point at the spec, the docstring,
            or the literal expected value.
        *checks: zero or more ``(predicate, message)`` pairs evaluated in
            order. The first predicate that returns truthy wins; its
            message is raised.

    A predicate that itself raises is treated as "not matching" — we
    swallow and continue. That keeps a flaky predicate from masking a
    real failure.
    """
    if passed:
        return
    for predicate, message in checks:
        try:
            if predicate():
                raise AssertionError(message)
        except AssertionError:
            raise
        except Exception:
            continue
    raise AssertionError(fallback_msg)
