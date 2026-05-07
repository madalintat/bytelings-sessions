"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: composition with a swappable collaborator

Build:

1. Class `MemoryStore`:
   - `__init__()`: initializes an empty dict.
   - `save(self, key: str, value)`: stores the value under key.
   - `load(self, key: str)`: returns the value, or raises KeyError.

2. Class `Logger`:
   - `__init__(self, store)`: takes any object with .save/.load (could
     be a MemoryStore, could be a fake test double).
   - `info(self, msg: str)`: stores msg under f"info-{n}" where n
     starts at 0 and increments on each call.
   - Property `count` (read-only): returns how many messages have been
     logged so far.

The test will inject both a real MemoryStore and a fake double.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class MemoryStore:
    def __init__(self) -> None:
        raise NotImplementedError


class Logger:
    def __init__(self, store) -> None:
        raise NotImplementedError
