"""Rung 3: Guided implement — a function that uses an HTTP client,
paired with tests that monkeypatch the client.

Topic: testing at the boundary using monkeypatch.setattr.

Real-world framing: a service-status checker.
"""
from typing import Any


# In real life, you'd `import httpx` here and call httpx.get.
# We use a tiny stand-in to keep the curriculum dependency-free —
# the testing pattern is identical.
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
    """Return True iff GET <url> returns 200 and JSON {"status": "ok"}.

    Network errors should propagate (the caller decides retry policy).
    """
    # TODO: call client.get(url), check status_code == 200 and
    # response.json() == {"status": "ok"}.
    raise NotImplementedError
