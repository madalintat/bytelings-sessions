"""Rung 3: Guided implement — M002 (too many parameters).

Topic: counting args across positional, posonly, and kwonly slots

The total parameter count for a function is:
    len(node.args.args)            # regular positional/keyword
  + len(node.args.posonlyargs)     # positional-only (PEP 570)
  + len(node.args.kwonlyargs)      # keyword-only

We do NOT count *args or **kwargs (node.args.vararg / node.args.kwarg)
as "parameters" for this rule — they're variadic.

Threshold: more than `limit` (default 6) triggers an issue.
"""
from __future__ import annotations
import ast
from dataclasses import dataclass


@dataclass
class Issue:
    line: int
    code: str
    message: str


def check_too_many_params(source: str, limit: int = 6) -> list[Issue]:
    """Return Issue per function with > `limit` named parameters.

    Message format: '<name> has <n> parameters (limit: <limit>)'

    >>> issues = check_too_many_params("def f(a,b,c,d,e,f,g): pass", limit=6)
    >>> len(issues), issues[0].code
    (1, 'M002')
    """
    # TODO: walk the tree, find FunctionDef + AsyncFunctionDef,
    # compute total per the formula above, append Issue if total > limit.
    raise NotImplementedError
