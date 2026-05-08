---
day: day-082-deque-and-real-uses
phase: phase-4-data-structures
module: module-16-stacks-queues-deques
style: tour
---
# Day 82 — A tour of `collections.deque`

You met `deque` yesterday as the fast-queue rescue. Today you'll walk
through it like a tourist — every method, when it's the right tool,
and the two real-world patterns where it's a quiet superpower.

## The full method tour

```python
from collections import deque

d = deque([1, 2, 3])     # build from any iterable
d.append(4)              # right side: O(1)        -> [1, 2, 3, 4]
d.appendleft(0)          # left side: O(1)         -> [0, 1, 2, 3, 4]
d.pop()                  # right: O(1) returns 4   -> [0, 1, 2, 3]
d.popleft()              # left: O(1) returns 0    -> [1, 2, 3]
d.extend([4, 5])         # extend right            -> [1, 2, 3, 4, 5]
d.extendleft([0, -1])    # NOTE: reversed in!      -> [-1, 0, 1, 2, 3, 4, 5]
d.rotate(1)              # shift right by 1        -> [4, 5, -1, 0, 1, 2, 3]
d.rotate(-2)             # shift left by 2         -> [-1, 0, 1, 2, 3, 4, 5]
len(d), d[0], d[-1]      # O(1) at the ends; index access is O(n) in middle
```

The two surprises to remember:
1. `extendleft([1, 2, 3])` ends up `[3, 2, 1, ...]` — it pushes one
   at a time on the left, reversing the order. This bites every
   beginner once.
2. `d[len(d) // 2]` is **O(n)**, not O(1). A deque is a chain of
   blocks, not an array. Use `list` if you need random index access.

## When to reach for a deque

- **FIFO queue** — `append` + `popleft`. (Yesterday.)
- **Sliding window** — keep the last N items. `deque(maxlen=N)`
  silently drops the oldest when full.
- **Recently-seen cache** — same shape as sliding window but the
  "drop" is a feature.
- **Palindrome / two-ended walk** — peel from both ends until they meet.

## The killer feature: `maxlen`

```python
last_5 = deque(maxlen=5)
for line in sys.stdin:
    last_5.append(line)
# last_5 always holds the most recent 5 lines, no manual pruning.
```

This pattern shows up constantly: log tailing, rolling averages, the
"last N events" feed in a UI. With a `list`, you'd need `if
len(buf) > 5: buf.pop(0)` (slow!) or `buf = buf[-5:]` (allocates).
With `deque(maxlen=5)`, the bounded ring is just there.

## Sliding window example: rolling sum

```python
def rolling_sums(nums: list[int], k: int) -> list[int]:
    window: deque[int] = deque(maxlen=k)
    out: list[int] = []
    s = 0
    for n in nums:
        if len(window) == k:
            s -= window[0]      # the one about to be evicted
        window.append(n)        # eviction happens automatically
        s += n
        if len(window) == k:
            out.append(s)
    return out
```

`maxlen` removes the eviction bookkeeping; you just compensate the
running sum. This is the shape you'll reuse for every sliding-window
algorithm in Phase 5.

## Now: open `02_fluency.py`

Two deque idioms to fix.
