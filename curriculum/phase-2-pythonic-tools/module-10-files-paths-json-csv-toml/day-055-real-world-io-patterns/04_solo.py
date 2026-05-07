"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a robust JSON-lines processor with atomic output

Implement `transform_jsonl(src_path, dst_path, transform)`:
- `src_path` is a Path to a JSONL file (one JSON object per line).
- `dst_path` is a Path where the output goes.
- `transform` is a callable: dict → dict.
- Read `src_path` line-by-line (streaming).
- For each line that's valid JSON, apply `transform` to the dict and
  write the transformed dict as JSON on its own line in the OUTPUT.
- Skip lines that don't parse (don't crash; don't include them).
- Write the output ATOMICALLY: temp file + os.replace.
- Use utf-8 encoding for both read and write.
- Return the number of records successfully written.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import json
import os
from pathlib import Path


def transform_jsonl(src_path: Path, dst_path: Path, transform) -> int:
    raise NotImplementedError
