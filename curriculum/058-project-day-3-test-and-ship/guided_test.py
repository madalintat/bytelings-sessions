"""Tests for rung 3."""
import asyncio
import importlib.util
from pathlib import Path

import httpx
import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _make_factory(values):
    """Each call returns a fresh coroutine that yields the next item.
    If the item is an exception class, raise it; otherwise return it."""
    iterator = iter(values)

    def factory():
        async def coro():
            v = next(iterator)
            if isinstance(v, BaseException):
                raise v
            return v
        return coro()
    return factory


def test_succeeds_first_try():
    factory = _make_factory(["ok"])
    assert asyncio.run(ex.with_retries(factory, attempts=3)) == "ok"


def test_succeeds_after_retries():
    factory = _make_factory([
        ConnectionError("flaky"),
        ConnectionError("flaky"),
        "finally ok",
    ])
    assert asyncio.run(ex.with_retries(factory, attempts=5)) == "finally ok"


def test_all_attempts_fail():
    factory = _make_factory([RuntimeError("x"), RuntimeError("x"), RuntimeError("x")])
    with pytest.raises(RuntimeError):
        asyncio.run(ex.with_retries(factory, attempts=3))


def test_does_not_retry_4xx():
    """A 4xx HTTPStatusError must NOT be retried — re-raise immediately."""
    request = httpx.Request("GET", "http://x")
    response = httpx.Response(404, request=request)
    err = httpx.HTTPStatusError("404", request=request, response=response)

    state = {"calls": 0}

    def factory():
        async def coro():
            state["calls"] += 1
            raise err
        return coro()

    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(ex.with_retries(factory, attempts=5))
    assert state["calls"] == 1, "4xx must not be retried"
