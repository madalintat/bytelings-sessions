"""Rung 4: Solo implement — solved version.

Reads os.environ lazily on each call so monkeypatch can change it
between tests. Empty string is treated the same as unset.
"""
import os


def current_user_greeting() -> str:
    name = os.environ.get("USER_NAME", "").strip()
    if name:
        return f"Hello, {name}!"
    return "Hello, stranger!"
