"""Rung 4: Solo implement — solved version.

Reverse Polish Notation evaluator. Push numbers; on operator pop two
values (right operand first, then left), compute, push result.
After all tokens the stack should hold exactly one value.
"""


def evaluate(expr: str) -> int:
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),  # truncate toward zero
    }
    stack: list[int] = []
    for tok in expr.split():
        if tok in ops:
            if len(stack) < 2:
                raise ValueError(f"not enough operands for {tok!r}")
            right = stack.pop()
            left = stack.pop()
            if tok == "/" and right == 0:
                raise ValueError("division by zero")
            stack.append(ops[tok](left, right))
        else:
            try:
                stack.append(int(tok))
            except ValueError:
                raise ValueError(f"invalid token: {tok!r}")
    if len(stack) != 1:
        raise ValueError(f"expression left {len(stack)} values on stack")
    return stack[0]
