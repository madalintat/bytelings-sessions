"""Rung 3: Guided implement — read_config_or_default.

Topic: try / except / else / finally working together.

Real-world framing: a service starts up and tries to read its config
from disk. If the file is missing, fall back to a default. If the
file is corrupted (bad JSON), raise — that's an operator error.
Always increment a counter so we know how many startup reads happen.
"""
import json
from pathlib import Path

DEFAULT_CONFIG = {"debug": False, "workers": 1}


def read_config_or_default(path: Path, counter: list[int]) -> dict:
    """Return parsed JSON from `path`, or DEFAULT_CONFIG if missing.

    Behavior contract:
      - File missing -> return DEFAULT_CONFIG (no exception).
      - File present but invalid JSON -> let json.JSONDecodeError propagate.
      - Always append 1 to `counter` (the metrics-increment side-effect),
        regardless of which branch ran.

    Implementation hints:
      - Use try / except FileNotFoundError / finally.
      - The `finally` clause is where the counter increment goes.
    """
    # TODO: implement the try / except FileNotFoundError / finally pattern.
    raise NotImplementedError
