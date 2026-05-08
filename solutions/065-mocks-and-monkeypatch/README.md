---
day: day-065-mocks-and-monkeypatch
phase: phase-3-quality-production
module: module-12-testing-with-pytest
style: pain
---
# Day 65 — When tests hit the network and the suite turns flaky

You wrote a function that fetches the weather and returns a tidy dict.
You wrote a test. The test passed. You shipped.

A week later, half the team is staring at a CI failure:

```text
FAILED tests/test_weather.py::test_today
ConnectionError: HTTPSConnectionPool(host='api.weather.example')
```

The provider had a hiccup. Your *function* is fine. Your *test* is
broken — it depends on a service you don't control. Welcome to flake
hell.

## The pain, distilled

Real units of code talk to:

- Networks (HTTP APIs)
- Filesystems
- The clock (`time.time()`, `datetime.now()`)
- Environment variables, config files
- Random number generators

Anything in that list is **non-deterministic** in tests. If your test
exercises any of it, your test will eventually fail for reasons that
have nothing to do with your code. Worse: it'll fail *intermittently*,
which is the worst kind of failure — you'll learn to ignore it, and
then ignore real failures by reflex.

## The fix: replace the dependency at test time

`monkeypatch` is pytest's built-in fixture for this. It lets you
swap a module-level attribute or env var **for the duration of one
test**, then put it back automatically.

```python
def fetch_weather(city: str) -> dict:
    response = httpx.get(f"https://api.weather/{city}")
    return {"temp": response.json()["temp_c"]}

def test_fetch_weather(monkeypatch):
    class FakeResp:
        def json(self):
            return {"temp_c": 21.5}
    monkeypatch.setattr("httpx.get", lambda url: FakeResp())
    assert fetch_weather("paris") == {"temp": 21.5}
```

No network. Deterministic. Runs in 2 ms. Survives the provider's
outage tomorrow.

## What `monkeypatch` can do

| Method | Use |
|---|---|
| `monkeypatch.setattr(target, value)` | Replace an attribute (string path or object). |
| `monkeypatch.setenv("KEY", "v")` | Set an env var, restored after the test. |
| `monkeypatch.delenv("KEY", raising=False)` | Remove an env var. |
| `monkeypatch.setitem(d, k, v)` | Mutate a dict, undo on teardown. |
| `monkeypatch.chdir(path)` | Change cwd, restore after. |

Each one auto-undoes when the test exits — you never have to clean up.

## `unittest.mock.MagicMock` for richer fakes

When the dependency is a *whole object* (a client with several
methods you'll inspect), reach for `MagicMock`:

```python
from unittest.mock import MagicMock

def test_send_email(monkeypatch):
    mailer = MagicMock()
    monkeypatch.setattr("myapp.email.client", mailer)
    send_welcome_email("ada@example.com")
    mailer.send.assert_called_once_with(to="ada@example.com")
```

`MagicMock` records calls. `.assert_called_once_with(...)` is the
assertion. You're testing *that your code talked to the dependency
correctly*, not the dependency's actual behavior — which is exactly
the right line.

## The line you don't cross

Don't mock things you own. If you wrote a `parse_csv` function, do
NOT mock it in tests of code that calls it — let the real function
run. Mock only at the **boundaries** of your system: I/O, time,
randomness, third-party services. Inside the boundary, real code talks
to real code, and bugs surface where they live.

## Now: open `fluency.py`

A test hits the real clock. Make it deterministic.
