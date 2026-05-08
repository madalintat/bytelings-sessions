"""Tests for rung 2 — green after both registry bugs are fixed."""
import importlib.util
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)


def test_registry_is_a_dict_of_lists():
    diagnose(
        isinstance(ex._REGISTRY.get("greet"), list),
        f"_REGISTRY['greet'] is {type(ex._REGISTRY.get('greet')).__name__!r}, "
        "expected a list. Change the value type in _REGISTRY.",
        (lambda: isinstance(ex._REGISTRY.get("greet"), set),
         "_REGISTRY['greet'] is still a set — sets can't accumulate "
         "handlers in order. Change `set` to `list` in the type hint "
         "and the assignment."),
    )


def test_both_greet_handlers_registered():
    handlers = ex._REGISTRY.get("greet", [])
    diagnose(
        len(handlers) == 2,
        f"Expected 2 handlers for 'greet', found {len(handlers)}. "
        "The second @register_for('greet') is overwriting the first.",
        (lambda: len(handlers) == 1,
         "Only 1 handler survived. The decorator is doing "
         "`_REGISTRY[key] = [fn]` each time — that replaces instead of "
         "appending. Use .setdefault + .append, or check-and-append."),
        (lambda: len(handlers) == 0,
         "No handlers found at all — did you accidentally break the "
         "decorator body?"),
    )


def test_dispatch_calls_all_handlers():
    results = ex.dispatch("greet", "World")
    diagnose(
        len(results) == 2,
        f"dispatch('greet', 'World') returned {results!r}, "
        "expected two greetings.",
        (lambda: len(results) == 1,
         "Only one greeting came back — fix the registry first so both "
         "handlers are stored, then dispatch will call both."),
    )
    diagnose(
        "Hello, World!" in results,
        f"'Hello, World!' missing from dispatch results {results!r}.",
    )
    diagnose(
        "Hey, World!" in results,
        f"'Hey, World!' missing from dispatch results {results!r}.",
    )


def test_dispatch_unknown_key_returns_empty():
    diagnose(
        ex.dispatch("unknown") == [],
        f"dispatch('unknown') returned {ex.dispatch('unknown')!r}, expected [].",
    )
