"""Rung 5: Apply.

Tiny CLI: simulate a transactional update over a small in-memory store.

Try it:
    uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    store = {"users": 100, "credits": 50}
    print(f"before: {store}")

    # A successful transaction.
    with _solo.Transaction(store):
        store["users"] += 1
    print(f"after success: {store}")

    # A failing transaction — should roll back.
    try:
        with _solo.Transaction(store):
            store["users"] += 10
            raise RuntimeError("oops, something went wrong")
    except RuntimeError as e:
        print(f"caught {e}")
    print(f"after failure: {store}")


if __name__ == "__main__":
    main()
