"""Tests for rung 3 — patching the http client."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def fake_get_factory(status: int, body: dict, recorder: list | None = None):
    def fake_get(url: str):
        if recorder is not None:
            recorder.append(url)
        return ex._Response(status, body)

    return fake_get


def test_healthy(monkeypatch):
    monkeypatch.setattr(ex.client, "get", fake_get_factory(200, {"status": "ok"}))
    assert ex.is_service_healthy("https://x") is True


def test_wrong_status(monkeypatch):
    monkeypatch.setattr(ex.client, "get", fake_get_factory(500, {"status": "ok"}))
    assert ex.is_service_healthy("https://x") is False


def test_wrong_body(monkeypatch):
    monkeypatch.setattr(ex.client, "get", fake_get_factory(200, {"status": "degraded"}))
    assert ex.is_service_healthy("https://x") is False


def test_calls_client_with_url(monkeypatch):
    seen: list[str] = []
    monkeypatch.setattr(ex.client, "get", fake_get_factory(200, {"status": "ok"}, seen))
    ex.is_service_healthy("https://api.example/health")
    assert seen == ["https://api.example/health"]


def test_network_error_propagates(monkeypatch):
    def boom(url):
        raise ConnectionError("no route to host")

    monkeypatch.setattr(ex.client, "get", boom)
    with pytest.raises(ConnectionError):
        ex.is_service_healthy("https://x")
