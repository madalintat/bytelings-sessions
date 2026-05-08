"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. This copy is unchanged from
the starter (it already delegates to tag_index from solo.py).
"""
import json
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    posts = [json.loads(line) for line in sys.stdin if line.strip()]
    if not posts:
        print("(no input)")
        return
    index = _solo.tag_index(posts)
    for tag in sorted(index):
        ids = ", ".join(str(i) for i in index[tag])
        print(f"{tag}: {ids}")


if __name__ == "__main__":
    main()
