"""Rung 4: Solo implement.

Topic: write a function PLUS the tests it deserves.

Build `parse_kv(text: str) -> dict[str, str]`:

  - Input is one or more lines of "key=value", separated by newlines.
  - Blank lines are ignored.
  - Lines starting with '#' are comments — ignored.
  - Whitespace around key and value is stripped.
  - Duplicate keys: LAST one wins.
  - Lines without '=' raise ValueError("malformed line: <line>").

Examples:
    parse_kv("a=1\nb=2") == {"a": "1", "b": "2"}
    parse_kv("# comment\n  x = hi  \n") == {"x": "hi"}
    parse_kv("a=1\na=2") == {"a": "2"}

Hidden tests in 04_solo_test.py.
"""


def parse_kv(text: str) -> dict[str, str]:
    raise NotImplementedError
