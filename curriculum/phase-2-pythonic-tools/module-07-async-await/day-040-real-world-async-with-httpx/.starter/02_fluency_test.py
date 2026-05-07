"""Tests for rung 2 — uses httpx.MockTransport so no real network."""
import asyncio
import importlib.util
from pathlib import Path

import httpx

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _handler(request):
    if request.url.path == "/ok":
        return httpx.Response(200, text="ok")
    if request.url.path == "/missing":
        return httpx.Response(404, text="missing")
    return httpx.Response(500)


def _build_client():
    return httpx.AsyncClient(
        transport=httpx.MockTransport(_handler),
        base_url="http://test",
    )


def test_check_status_returns_int():
    async def runner():
        async with _build_client() as client:
            return await ex.check_status(client, "http://test/ok")
    assert asyncio.run(runner()) == 200


def test_check_status_404():
    async def runner():
        async with _build_client() as client:
            return await ex.check_status(client, "http://test/missing")
    assert asyncio.run(runner()) == 404


def test_open_client_and_check_uses_async_with():
    """If `with` (sync) is used, this raises a TypeError before fetch."""
    # We can't easily exercise open_client_and_check without real network,
    # so we just check by AST that it uses `async with`.
    import ast
    src = (_HERE / "02_fluency.py").read_text()
    tree = ast.parse(src)
    fn = next(
        n for n in tree.body
        if isinstance(n, ast.AsyncFunctionDef) and n.name == "open_client_and_check"
    )
    has_async_with = any(isinstance(n, ast.AsyncWith) for n in ast.walk(fn))
    assert has_async_with, "open_client_and_check must use `async with`"
