"""Rung 5: Apply.

Tiny CLI: read a .env-style blob from stdin, print KEY=VALUE pairs
sorted by key.

Reuses parse_env from rung 4.

Try it: printf "B=2\nA=1\n# comment\nC=hello world\n" | uv run python apply.py

Patterns: P-01 (sentinel-loop).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    env = _solo.parse_env(sys.stdin.read())
    for key in sorted(env):
        print(f"{key}={env[key]}")


if __name__ == "__main__":
    main()
