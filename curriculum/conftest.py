"""Curriculum-tree pytest configuration.

Pytest auto-loads conftest.py files from rootdir down to the test path.
When the watcher invokes `pytest curriculum/<slug>/<rung>_test.py`,
this file gets loaded and adds the curriculum directory to sys.path
so test files can `from _byte import diagnose` cleanly.

This is the in-tree shim that makes the diagnose helper usable without
requiring `bytelings` to be installed in the learner's .venv. The
helper itself lives at `curriculum/_byte.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

_CURRICULUM = Path(__file__).resolve().parent
if str(_CURRICULUM) not in sys.path:
    sys.path.insert(0, str(_CURRICULUM))
