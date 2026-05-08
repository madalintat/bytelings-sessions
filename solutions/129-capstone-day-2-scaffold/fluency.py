"""Rung 2: Fluency drill — fix the broken toy registry.

Topic: @rule_for(node_type) registry pattern

The registry below has two bugs. Find and fix them.
"""
from __future__ import annotations

# BUG 1: The registry should map a string key to a LIST of handlers
# so multiple functions can be registered for the same key.
# Right now it maps to a set — which can't preserve order and
# doesn't accumulate callables the way we need.
_REGISTRY: dict[str, set] = {}   # TODO: change `set` to `list`


def register_for(key: str):
    """Decorator: register a function under *key* in _REGISTRY."""
    def decorator(fn):
        # BUG 2: This creates a NEW list each time instead of appending.
        # A handler registered second silently replaces the first.
        _REGISTRY[key] = [fn]    # TODO: append to existing list instead
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
