"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: apply.py <input.toml> <output.json>")
        return
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    data = _solo.toml_to_json(src, dst)
    keys = list(data.keys())
    print(f"wrote {dst} with {len(keys)} top-level keys: {keys}")


if __name__ == "__main__":
    main()
