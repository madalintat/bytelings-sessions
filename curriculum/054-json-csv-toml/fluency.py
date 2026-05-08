"""Rung 2: Fluency drill — clean up JSON read/write.

Topic: json + pathlib

`load_config(path)` should return the parsed JSON object as a dict.
`save_config(path, data)` should write the dict as JSON, indented 2.

Both currently work the wrong way. Fix them.
"""
import json
from pathlib import Path


def load_config(path: Path) -> dict:
    """Read JSON from `path` and return a dict."""
    # TODO: don't use eval()! Use json.loads(path.read_text()).
    text = path.read_text()
    return eval(text)  # noqa


def save_config(path: Path, data: dict) -> None:
    """Write `data` as JSON, indented 2."""
    # TODO: json.dumps without indent gives a single-line blob — pass indent=2.
    path.write_text(json.dumps(data))
