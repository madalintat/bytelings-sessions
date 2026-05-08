"""Rung 5: Apply.

Run `bottleneck` on a fake "request handler" that calls several
helpers, only one of which is slow. Watch it find the slow one.

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def parse_request(payload: dict) -> dict:
    return {k.lower(): v for k, v in payload.items()}


def authorize(user: str) -> bool:
    return len(user) > 0


def render_response(data: dict) -> str:
    return ",".join(f"{k}={v}" for k, v in data.items())


def expensive_template_render(data: dict) -> str:
    # The actual hotspot — quadratic on size.
    out = ""
    items = list(data.items())
    for _ in range(200):
        for k, v in items:
            out = out + f"{k}={v};"
    return out


def handle_request(payload: dict, user: str) -> str:
    parsed = parse_request(payload)
    authorize(user)
    quick = render_response(parsed)
    slow = expensive_template_render(parsed)
    return quick + "|" + slow[:50]


def main() -> None:
    payload = {f"k{i}": i for i in range(20)}
    report = _solo.bottleneck(handle_request, payload, "ada")
    print("bottleneck report:")
    print(" ", report)


if __name__ == "__main__":
    main()
