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
    args = sys.argv[1:]
    if len(args) % 2 != 0 or not args:
        print("usage: apply.py <name1> <cents1> <name2> <cents2> ...")
        return
    items = [
        _solo.Item(name=args[i], price_cents=int(args[i + 1]))
        for i in range(0, len(args), 2)
    ]
    order = _solo.Order(id=1, items=items)
    cents = _solo.total(order)
    print(f"order #{order.id}: ${cents / 100:.2f} ({cents} cents)")


if __name__ == "__main__":
    main()
