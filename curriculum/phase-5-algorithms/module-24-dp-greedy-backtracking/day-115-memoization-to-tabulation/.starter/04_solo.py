"""Rung 4: Solo.

Topic: bottom-up min path sum on a triangle.

Given a triangle as a list of lists where row i has length i+1, find
the minimum path sum from top to bottom. At each step you may move
to an adjacent number on the row below.

Example triangle:
       2
      3 4
     6 5 7
    4 1 8 3

The path 2 -> 3 -> 5 -> 1 sums to 11, which is minimum.

>>> min_path([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
11

Hints (bottom-up is cleanest here):
- Start with the last row as your "best below" array.
- Walk rows in reverse; for each cell (r, c):
    best[c] = triangle[r][c] + min(best[c], best[c+1])
- After processing row 0, best[0] is the answer.

Tests in 04_solo_test.py are HIDDEN.
"""


def min_path(triangle: list[list[int]]) -> int:
    raise NotImplementedError
