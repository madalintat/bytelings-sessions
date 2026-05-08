---
day: 002-numbers-and-ops
phase: phase-1-python-core
module: module-01-setup-and-values
style: pain
---
# Day 2 — When 0.1 + 0.2 isn't 0.3

You're writing a financial app. A user adds 0.10 and 0.20. You print the
result. Your screen says:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

You stare at it. You blame Python. You blame your laptop. You don't
trust math anymore.

## Why this happens

Python's `float` is a 64-bit IEEE-754 number. Computers store floats
in *binary* fractions, but `0.1` in binary is an infinite repeating
fraction, just like `1/3` is in decimal. The CPU rounds. The rounding
shows up the moment you add two of them.

This is not a Python bug. JavaScript does it. Java does it. Rust does
it. It's how floating-point works everywhere.

## The fix: `int` for exact arithmetic, or `Decimal` for money

```python
>>> from decimal import Decimal
>>> Decimal("0.1") + Decimal("0.2")
Decimal('0.3')
```

For money, never use `float`. Use `int` cents (`1050` instead of
`10.50`) or `Decimal`. The pain point goes away.

## Other operators worth knowing

| Operator | What |
|---|---|
| `//` | Integer division (floor): `7 // 2 == 3` |
| `%` | Modulo (remainder): `7 % 2 == 1` |
| `**` | Power: `2 ** 10 == 1024` |
| `divmod(a, b)` | Returns `(a // b, a % b)` in one shot |

## Now: open `fluency.py`

Two broken expressions to fix.
