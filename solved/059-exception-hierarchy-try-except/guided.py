"""Rung 3: Guided — solved version.

`try/except FileNotFoundError/finally` demonstrates all four clauses:
- `try`: the risky operation (file open + JSON parse).
- `except FileNotFoundError`: graceful fallback for a missing file.
- `finally`: always runs — the metrics increment side-effect belongs
  here so it fires regardless of success, missing-file, or JSON error.

We do NOT catch `json.JSONDecodeError` — a corrupted config is an
operator error that must surface.
"""
import json
from pathlib import Path

DEFAULT_CONFIG = {"debug": False, "workers": 1}


def read_config_or_default(path: Path, counter: list[int]) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        return json.loads(text)
    except FileNotFoundError:
        return DEFAULT_CONFIG
    finally:
        counter.append(1)
