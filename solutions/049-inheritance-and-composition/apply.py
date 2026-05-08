"""Rung 5: Apply.

Tiny CLI: log a few messages and dump the store.

Try it:
    uv run python apply.py hello world goodbye

Patterns: P-02 (in-place-vs-returning), P-21 (protocol-as-interface), P-23 (dispatch-by-type).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    store = _solo.MemoryStore()
    log = _solo.Logger(store)
    for msg in sys.argv[1:] or ["hello", "world"]:
        log.info(msg)
    print(f"logged {log.count} messages:")
    for i in range(log.count):
        print(f"  info-{i}: {store.load(f'info-{i}')}")


if __name__ == "__main__":
    main()
