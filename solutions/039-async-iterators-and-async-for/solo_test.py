"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import asyncio
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


async def _collect(agen):
    out = []
    async for v in agen:
        out.append(v)
    return out


def test_basic():
    p = ex.APage([[1, 2], [3], [4, 5]])
    assert asyncio.run(_collect(p)) == [1, 2, 3, 4, 5]


def test_empty_pages_list():
    p = ex.APage([])
    assert asyncio.run(_collect(p)) == []


def test_empty_inner_pages():
    p = ex.APage([[], [1], []])
    assert asyncio.run(_collect(p)) == [1]


def test_raises_stop_async_iteration():
    p = ex.APage([[7]])

    async def runner():
        it = p.__aiter__()
        first = await it.__anext__()
        assert first == 7
        try:
            await it.__anext__()
        except StopAsyncIteration:
            return "stopped"
        return "did-not-stop"

    assert asyncio.run(runner()) == "stopped"


def test_aiter_method_exists():
    p = ex.APage([[1]])
    assert hasattr(p, "__aiter__")
