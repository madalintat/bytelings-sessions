"""Rung 3: Guided — multi-pass stable sorting.

Topic: rely on Timsort's stability to compose sorts.

Implement `sort_events(events)`. Each event is a dict with keys
`user`, `priority` (lower number = more important), and `time`.
Sort the list so that:

  1) Lowest priority number first.
  2) Within the same priority, oldest time first.
  3) Within the same priority AND time, alphabetical user.

Implement this two ways internally — but the FUNCTION must produce
the correct result. Either:
  (a) one sort with a tuple key (priority, time, user), or
  (b) three sorts in reverse order: by user, then time, then priority,
      relying on stability.

Both should give the same answer.

>>> sort_events([{'user':'b','priority':1,'time':10},
...              {'user':'a','priority':2,'time':5}])
[{'user': 'b', 'priority': 1, 'time': 10}, {'user': 'a', 'priority': 2, 'time': 5}]
"""


def sort_events(events: list[dict]) -> list[dict]:
    raise NotImplementedError
