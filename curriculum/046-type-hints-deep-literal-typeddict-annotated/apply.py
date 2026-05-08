"""Rung 5: Apply.

Tiny CLI: read JSON events from stdin (one per line), print revenue.

Try it:
    printf '{"kind":"purchase","user_id":1,"amount_cents":500}\\n' \\
      '{"kind":"click","user_id":1,"amount_cents":0}\\n' \\
      | uv run python apply.py
"""
import json
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    events = [json.loads(line) for line in sys.stdin if line.strip()]
    cents = _solo.revenue(events)
    print(f"revenue: ${cents / 100:.2f} ({cents} cents) over {len(events)} events")


if __name__ == "__main__":
    main()
