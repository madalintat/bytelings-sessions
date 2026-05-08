"""Solved: fluency — fixed registry (dict of lists).

Fix 1: _REGISTRY values are lists, not sets.
Fix 2: register_for appends to the existing list instead of overwriting.
"""
from __future__ import annotations

# Fix 1: value type is list, not set.
_REGISTRY: dict[str, list] = {}


def register_for(key: str):
    """Decorator: register a function under *key* in _REGISTRY."""
    def decorator(fn):
        # Fix 2: create-if-absent then append, never overwrite.
        _REGISTRY.setdefault(key, []).append(fn)
        return fn
    return decorator


@register_for("greet")
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


@register_for("greet")
def say_hey(name: str) -> str:
    return f"Hey, {name}!"


def dispatch(key: str, *args):
    """Call every handler registered under *key* and return the results."""
    return [fn(*args) for fn in _REGISTRY.get(key, [])]
