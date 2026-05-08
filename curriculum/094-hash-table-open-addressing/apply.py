"""Rung 5: Apply.

Tiny CLI: load key/value pairs, run a workload of inserts/deletes, then
print a histogram of cluster lengths. Lets you SEE clusters grow as
the load factor rises.

Usage:
    uv run python 05_apply.py     # uses a built-in synthetic workload
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "03_guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)

_spec_s = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec_s)
_spec_s.loader.exec_module(_solo)


def main() -> None:
    m = _guided.HashMapOA()
    # insert 80% of capacity at first
    for i in range(int(_guided.HashMapOA.INITIAL_CAPACITY * 0.7)):
        m.put(f"k-{i}", i)

    # NOTE: solo's EMPTY/TOMB sentinels are different objects than the
    # guided module's. We map slots through identity here so the
    # solo's cluster_lengths sees its own sentinels.
    def translate(slots):
        out = []
        for s in slots:
            if s is _guided.EMPTY:
                out.append(_solo.EMPTY)
            elif s is _guided.TOMB:
                out.append(_solo.TOMB)
            else:
                out.append(s)
        return out

    lengths = _solo.cluster_lengths(translate(m._slots))
    print(f"capacity={m._capacity()} live={len(m)}")
    print(f"clusters={sorted(lengths, reverse=True)}")


if __name__ == "__main__":
    main()
