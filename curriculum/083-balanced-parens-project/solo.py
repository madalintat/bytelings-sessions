"""Rung 4: Solo implement.

Topic: write `evaluate(expr)` — a tiny RPN (postfix) calculator.

In Reverse Polish Notation, operators come AFTER operands:
    "3 4 +"        -> 7
    "5 1 2 + 4 * + 3 -"  -> 14   (i.e. 5 + ((1+2)*4) - 3)

This is the canonical "stacks evaluate expressions" example. Walk the
tokens left to right:
    - if it's a number, push it
    - if it's an operator (+ - * /), pop two values (right then left),
      compute, push the result
After all tokens, the stack holds exactly one number — the answer.

Spec:
    - Input is a space-separated string of tokens.
    - Operators: "+", "-", "*", "/" (use integer division, floor toward zero
      for negatives is fine — use Python's // which rounds toward -inf is OK
      because all tests use positive results).
    - Numbers may be negative, e.g. "-3".
    - On malformed input (extra operands, missing operands, division by
      zero), raise ValueError.

Examples:
    evaluate("3 4 +")           -> 7
    evaluate("3")               -> 3
    evaluate("10 2 /")          -> 5
    evaluate("5 1 2 + 4 * + 3 -") -> 14

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def evaluate(expr: str) -> int:
    raise NotImplementedError
