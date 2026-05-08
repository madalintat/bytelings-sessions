"""Rung 3: Guided implement — solved version.

is_service_healthy calls client.get(url), checks status == 200 and
json() == {"status": "ok"}. The client object lives at module level
so monkeypatch.setattr can swap it out in tests.
"""
from typing import Any


class _Client:
    def get(self, url: str) -> "_Response":  # pragma: no cover
        raise RuntimeError("real network call — should be patched in tests")


class _Response:
    def __init__(self, status_code: int, payload: dict) -> None:
        self.status_code = status_code
        self._payload = payload

    def json(self) -> dict:
        return self._payload


client = _Client()


def is_service_healthy(url: str) -> bool:
    """Return True iff GET <url> returns 200 and JSON {"status": "ok"}."""
    response = client.get(url)
    return response.status_code == 200 and response.json() == {"status": "ok"}
