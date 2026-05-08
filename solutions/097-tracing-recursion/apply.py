"""Rung 5: Apply — print a "trace" of recursive calls.

Demonstrates how recursive calls stack and unwind by printing
indented trace messages on the way down and on the way up.

Try it: uv run python apply.py

Patterns: P-16 (yield-from-passthrough), P-28 (memoize-recursive).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def traced_reverse(s: str, depth: int = 0) -> str:
    pad = "  " * depth
    print(f"{pad}-> reverse({s!r})")
    if len(s) <= 1:
        result = s
    else:
        result = traced_reverse(s[1:], depth + 1) + s[0]
    print(f"{pad}<- {result!r}")
    return result


def main() -> None:
    word = "stack"
    print(f"Tracing reverse({word!r}):\n")
    traced_reverse(word)
    print(f"\n(Sanity check) solo reverse: {_solo.reverse(word)}")


if __name__ == "__main__":
    main()
