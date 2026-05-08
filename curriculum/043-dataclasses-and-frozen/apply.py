"""Rung 5: Apply.

Tiny CLI: build an order from CLI args and print the total.

Args come as alternating name/cents pairs:
    uv run python 05_apply.py apple 150 banana 80 coffee 350
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    args = sys.argv[1:]
    if len(args) % 2 != 0 or not args:
        print("usage: 05_apply.py <name1> <cents1> <name2> <cents2> ...")
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
