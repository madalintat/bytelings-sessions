"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def double_n(d: dict) -> dict:
    return {**d, "n": d.get("n", 0) * 2}


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: apply.py <input.jsonl> <output.jsonl>")
        return
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    n = _solo.transform_jsonl(src, dst, double_n)
    print(f"wrote {n} records to {dst}")


if __name__ == "__main__":
    main()
