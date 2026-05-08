"""Rung 5: Apply.

Tiny CLI: read a JSONL file, double every numeric "n", write atomically.

Try it:
    printf '{"n":1}\\n{"n":2}\\n' > /tmp/in.jsonl
    uv run python 05_apply.py /tmp/in.jsonl /tmp/out.jsonl
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def double_n(d: dict) -> dict:
    return {**d, "n": d.get("n", 0) * 2}


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: 05_apply.py <input.jsonl> <output.jsonl>")
        return
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    n = _solo.transform_jsonl(src, dst, double_n)
    print(f"wrote {n} records to {dst}")


if __name__ == "__main__":
    main()
