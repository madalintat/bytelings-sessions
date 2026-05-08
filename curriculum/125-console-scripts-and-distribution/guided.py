"""Rung 3: Guided implement — generate a console-script shim.

Topic: write the file that `pip install` would write for you.

Given an entry-point spec, return the source code of the shim file
that calls it. The shape:

    #!/usr/bin/env python
    import sys
    from <module> import <attr>
    sys.exit(<attr>())

The shebang must be on line 1. The exit() call passes through the
return value of the entry-point function (which conventionally is an
int — 0 for success, non-zero for failure).
"""
from __future__ import annotations


def make_shim(spec: str) -> str:
    """Return the shim source code for entry-point spec 'module:attr'.

    >>> print(make_shim("habit_cli.cli:main"))
    #!/usr/bin/env python
    import sys
    from habit_cli.cli import main
    sys.exit(main())
    <BLANKLINE>

    The output ends with a single trailing newline.

    Raises ValueError if `spec` is malformed (no ':', empty side, etc.).
    """
    # TODO: split on ':', validate, build the four-line string with a
    # trailing newline. Use textwrap.dedent or an f-string template.
    raise NotImplementedError
