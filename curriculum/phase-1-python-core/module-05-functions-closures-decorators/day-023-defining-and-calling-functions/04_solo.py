"""Rung 4: Solo implement.

Topic: parse a CLI flag list into a config dict

Implement `parse_flags(args, *, allow_unknown=False)`:

- `args` is a list of strings like ['--verbose', '--out=file.txt', '--count', '3'].
- Recognized flags:
    --verbose            (bool: True if present, else False)
    --out=FILE  or --out FILE   (str)
    --count=N   or --count N    (int)
- Return a dict like {'verbose': bool, 'out': str|None, 'count': int|None}.
- If `allow_unknown=True`, ignore unknown --flags silently.
- If `allow_unknown=False` (default), raise ValueError on unknown --flags.
- `--out` and `--count` may or may not have values; if missing, raise ValueError.
- `--count` value must be int; raise ValueError on non-int.

Examples:
    parse_flags(['--verbose'])                  -> {'verbose': True, 'out': None, 'count': None}
    parse_flags(['--out=x.txt'])                -> {'verbose': False, 'out': 'x.txt', 'count': None}
    parse_flags(['--out', 'x.txt', '--count', '3'])
                                                -> {'verbose': False, 'out': 'x.txt', 'count': 3}
    parse_flags(['--bogus'])                    -> ValueError
    parse_flags(['--bogus'], allow_unknown=True) -> {'verbose': False, 'out': None, 'count': None}

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def parse_flags(args: list[str], allow_unknown: bool = False) -> dict:
    raise NotImplementedError
