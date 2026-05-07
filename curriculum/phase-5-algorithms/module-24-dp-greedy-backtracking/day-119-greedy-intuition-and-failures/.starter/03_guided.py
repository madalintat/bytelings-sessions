"""Rung 3: Guided — fractional knapsack (greedy WORKS here).

Topic: greedy by ratio.

You have items, each (weight, value). You can take fractions. Given
a capacity, return the maximum total value you can fit.

>>> fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50)
240.0
    # take all of items 1 and 2 (10+20 = 30 weight, 60+100 = 160 val),
    # then 20/30 of item 3 (worth 80). Total 240.

>>> fractional_knapsack([], 10)
0.0
>>> fractional_knapsack([(10, 100)], 5)
50.0     # half of one item

Hints:
- Sort items by value/weight ratio, descending.
- Walk through; take as much of each as fits. When an item doesn't
  fully fit, take a fraction = (remaining capacity / item.weight).
- Watch zero-weight items (skip or treat carefully).
"""


def fractional_knapsack(items: list[tuple[int, int]], capacity: int) -> float:
    raise NotImplementedError
