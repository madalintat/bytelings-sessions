"""Rung 5 — filter out the noise.

Read lines from stdin, print only the truthy ones (skip blanks).
"""
import sys


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line:
            print(line)


if __name__ == "__main__":
    main()
