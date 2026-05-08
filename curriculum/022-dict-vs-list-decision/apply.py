"""Rung 5: Apply.

Tiny CLI: read two CSV-like files (id,name lines) and print the
merged roster, secondary winning on name collisions.

Reuses merge_rosters from rung 4.

Try it:
  echo "1,Alice" > /tmp/p.csv
  echo "2,Bob"  >> /tmp/p.csv
  echo "1,Alicia" > /tmp/s.csv
  echo "3,Carol" >> /tmp/s.csv
  uv run python apply.py /tmp/p.csv /tmp/s.csv
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def load(path: str) -> list[dict]:
    out = []
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        id_str, _, name = line.partition(",")
        out.append({"id": int(id_str), "name": name.strip()})
    return out


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: apply.py <primary.csv> <secondary.csv>", file=sys.stderr)
        sys.exit(2)
    merged = _solo.merge_rosters(load(sys.argv[1]), load(sys.argv[2]))
    for c in merged:
        print(f"{c['id']},{c['name']}")


if __name__ == "__main__":
    main()
