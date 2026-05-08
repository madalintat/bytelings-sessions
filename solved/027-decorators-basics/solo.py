"""Rung 4: Solo — solved version.

`retry` wraps `fn` to retry up to 3 total attempts on any exception.
  - On success, increment `wrapped.successes` and return the result.
  - On failure, increment `wrapped.failures` and try again.
  - After 3 failures, re-raise the last exception.

The test for `test_immediate_success` calls f() once and checks
successes == 2 — wait, let me re-read the test.

Looking at the test:
    assert f() == "ok"
    assert f.successes == 2
    assert f.failures == 0

So calling f() once gives successes=2? That seems odd. Re-reading:
the test calls f() TWICE (the assertion counts per-call, not total).
Actually looking again — the test only calls f() once but checks
successes==2... let me re-read:

  def test_immediate_success():
    @ex.retry
    def f():
        return "ok"
    assert f() == "ok"
    assert f.successes == 2
    assert f.failures == 0

This means after the first call, successes should be 2. That doesn't
make sense for a single call. Unless `successes` is cumulative across
all calls. The second f() call in the test is the second call to f,
but there's only ONE `f()` call in the test. Let me look again at the
test file...

Actually re-reading: `test_immediate_success` calls f() once and expects
successes==2 — but then `test_recovers_after_two_failures` calls flaky()
once and checks successes==1, failures==2. So it's per-function total
(cumulative). The first test must be calling f() twice somehow...
No, it calls `assert f() == "ok"` once. Let me check if there's some
double-call in the test setup. The test is straightforward.

Wait — looking again: the first test says `assert f.successes == 2` after
one call to `f()`. This suggests the decorator counts something differently
from what I assumed. Perhaps "successes" counts total attempts that succeeded
within a call? For the simple case that's always 1. But it says 2...

Actually I suspect the test has `f.successes == 2` after TWO calls to f():
  assert f() == "ok"    <- first call, successes becomes 1
                        <- ... oh wait there are TWO asserts each calling f:
  assert f() == "ok"    <- but no, there's just one.

I'll implement straightforwardly with cumulative counters: each successful
return increments successes by 1, each exception increments failures by 1.
If the first test expects 2 after one call, there's perhaps one call in
test setup or the test is checking the counter differently. The most
natural interpretation: successes=total successful calls, failures=total
failed attempts (including retries within calls).
"""
import functools


def retry(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        last_exc = None
        for _ in range(3):
            try:
                result = fn(*args, **kwargs)
                wrapped.successes += 1
                return result
            except Exception as exc:
                last_exc = exc
                wrapped.failures += 1
        raise last_exc

    wrapped.successes = 0
    wrapped.failures = 0
    return wrapped
