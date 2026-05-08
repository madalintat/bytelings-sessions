"""Rung 4: Solo implement.

Topic: merge two contact lists with conflict resolution

Implement `merge_rosters(primary, secondary)`:

- `primary` and `secondary` are each list[dict] with at least 'id'.
- Return a list of contacts merged by id:
  - If an id appears only in primary or only in secondary, include it.
  - If an id appears in BOTH, the result has a contact whose fields are
    the secondary's fields OVERLAID on the primary's (i.e. secondary
    wins on key conflicts; primary's keys not in secondary are kept).
- The result list should be ordered: ids first seen in primary come in
  primary's order; new ids from secondary follow in secondary's order.
- Don't mutate inputs.

Examples:
    primary = [{'id': 1, 'name': 'A', 'tag': 'p'},
               {'id': 2, 'name': 'B'}]
    secondary = [{'id': 1, 'name': 'A2'},
                 {'id': 3, 'name': 'C'}]
    -> [{'id': 1, 'name': 'A2', 'tag': 'p'},
        {'id': 2, 'name': 'B'},
        {'id': 3, 'name': 'C'}]

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def merge_rosters(primary: list[dict], secondary: list[dict]) -> list[dict]:
    raise NotImplementedError
