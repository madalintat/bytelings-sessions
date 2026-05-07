"""Rung 4: Solo implement.

Topic: build a tiny "memo dict" wrapper

Implement `tally(*tags, **counts)`:

- `tags` is any number of strings; each string is one occurrence.
- `counts` is keyword args mapping tag-name -> int (extra adds).
- Return a dict {tag: total_count}. Sum tags + counts together.
- An empty call returns {}.

Examples:
    tally('a', 'b', 'a')                  -> {'a': 2, 'b': 1}
    tally('a', a=10)                       -> {'a': 11}
    tally('x', 'y', x=5, z=2)              -> {'x': 6, 'y': 1, 'z': 2}
    tally()                                -> {}

Bonus rule: a tag may not start with an underscore.
If any positional tag does, raise ValueError.
(Keyword args can't start with _ in Python anyway, no check needed there.)

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def tally(*tags: str, **counts: int) -> dict[str, int]:
    raise NotImplementedError
