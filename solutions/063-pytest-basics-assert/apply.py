"""Rung 5: Apply.

Read a config-style file from disk and pretty-print the parsed dict.
Uses `parse_kv` from rung 4. Demonstrates `tmp_path` indirectly: the
file you'd point this at would be a real config file.

Try it:
  printf 'host=localhost\nport=5432\n# comment\n' > /tmp/c.kv
  uv run python 05_apply.py /tmp/c.kv
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} <path>")
        return 2
    text = Path(argv[1]).read_text()
    try:
        cfg = _solo.parse_kv(text)
    except ValueError as e:
        print(f"parse error: {e}")
        return 1
    for key in sorted(cfg):
        print(f"{key} = {cfg[key]!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
