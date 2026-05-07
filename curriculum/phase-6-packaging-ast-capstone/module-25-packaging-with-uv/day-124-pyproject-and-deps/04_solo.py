"""Rung 4: Solo implement.

Topic: build a small dependency report from a parsed pyproject

Implement `summarize_project(toml_text)` that returns a dict:

    {
        "name": str,
        "version": str,
        "python": str,           # value of requires-python (or "" if missing)
        "deps": list[str],       # names only, no specifiers
        "dev_deps": list[str],   # names only; merge optional-deps['dev']
                                  # AND tool.uv.dev-dependencies (deduped, sorted)
    }

Use tomllib. Use the split-style approach from rung 3 to drop specifiers.
Hidden tests cover missing keys, both dev sources, and dedup.
"""
from __future__ import annotations


def summarize_project(toml_text: str) -> dict:
    raise NotImplementedError
