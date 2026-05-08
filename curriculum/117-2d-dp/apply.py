"""Rung 5: Apply.

Tiny diff-similarity report: print LCS length and a similarity ratio
for a few string pairs. The same idea backs `git diff`.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    pairs = [
        ("ALGORITHM", "ALTRUISTIC"),
        ("README", "READ ME!"),
        ("python", "java"),
        ("kitten", "sitting"),
    ]
    for a, b in pairs:
        n = _solo.lcs_length(a, b)
        denom = max(len(a), len(b)) or 1
        print(f"  {a!r} vs {b!r}: LCS={n}, similarity={n/denom:.0%}")


if __name__ == "__main__":
    main()
