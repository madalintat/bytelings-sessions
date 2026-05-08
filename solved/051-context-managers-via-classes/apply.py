"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    store = {"users": 100, "credits": 50}
    print(f"before: {store}")

    with _solo.Transaction(store):
        store["users"] += 1
    print(f"after success: {store}")

    try:
        with _solo.Transaction(store):
            store["users"] += 10
            raise RuntimeError("oops, something went wrong")
    except RuntimeError as e:
        print(f"caught {e}")
    print(f"after failure: {store}")


if __name__ == "__main__":
    main()
