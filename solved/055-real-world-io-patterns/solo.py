"""Rung 4: Solo — solved version.

We stream `src_path` line-by-line (no full load), skip invalid JSON
silently, apply the transform, and write to a `.tmp` sibling. After
all records are written we use `os.replace` for an atomic swap. Both
files use explicit utf-8 encoding.
"""
import json
import os
from pathlib import Path


def transform_jsonl(src_path: Path, dst_path: Path, transform) -> int:
    tmp = dst_path.with_suffix(dst_path.suffix + ".tmp")
    count = 0
    with (
        open(src_path, encoding="utf-8") as src,
        open(tmp, "w", encoding="utf-8") as dst,
    ):
        for line in src:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            dst.write(json.dumps(transform(record)) + "\n")
            count += 1
    os.replace(tmp, dst_path)
    return count
