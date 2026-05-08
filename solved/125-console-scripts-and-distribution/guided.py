"""Rung 3: Guided implement — solved version.

Strategy: split on ':', validate both sides are non-empty, then
build the four-line shim string with a single trailing newline.

The shim format mirrors what pip/uv write when installing a
console-script entry point — it's a real executable Python file.

ValueError is raised for any malformed spec so callers get a clear
error instead of a confusing AttributeError or IndexError.
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
    if ":" not in spec:
        raise ValueError(f"entry-point spec must contain ':': {spec!r}")
    module, attr = spec.split(":", 1)
    module = module.strip()
    attr = attr.strip()
    if not module or not attr:
        raise ValueError(f"both sides of ':' must be non-empty: {spec!r}")
    return (
        "#!/usr/bin/env python\n"
        "import sys\n"
        f"from {module} import {attr}\n"
        f"sys.exit({attr}())\n"
    )
