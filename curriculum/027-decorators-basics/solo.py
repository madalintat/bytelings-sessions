"""Rung 4: Solo implement.

Topic: a `retry` decorator

Implement `retry(fn)`:

- Wrap fn so that if fn raises an exception, it's retried up to 2
  more times (3 total attempts).
- If all attempts fail, re-raise the LAST exception.
- Record successful attempts in wrapped.successes (count, int).
- Record failed attempts in wrapped.failures (count, int).
- functools.wraps must preserve the function's __name__.

Examples:
    @retry
    def f():
        return "ok"
    f()                # 'ok'; successes=1, failures=0

    @retry
    def flaky(_n=[0]):
        _n[0] += 1
        if _n[0] < 3:
            raise RuntimeError("nope")
        return "good"
    flaky()            # 'good'; successes=1, failures=2

    @retry
    def always_bad():
        raise ValueError("boom")
    always_bad()       # raises ValueError; successes=0, failures=3

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-18 (decorator-as-wrapper).
"""
import functools


def retry(fn):
    raise NotImplementedError
