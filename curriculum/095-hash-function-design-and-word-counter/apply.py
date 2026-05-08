"""Rung 5: Apply.

Tiny CLI: read text from stdin, print the top K most common words.

Try it:
    cat some-large-text-file.txt | uv run python 05_apply.py 10

Bonus diagnostic: also prints a quality score showing how well your
djb2 hash distributes those word keys across 256 buckets. A real
text corpus should land you very close to 1.0.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)

_spec_g = spec_from_file_location(
    "_guided", Path(__file__).parent / "03_guided.py"
)
_guided = module_from_spec(_spec_g)
_spec_g.loader.exec_module(_guided)

_spec_f = spec_from_file_location(
    "_fluency", Path(__file__).parent / "02_fluency.py"
)
_fluency = module_from_spec(_spec_f)
_spec_f.loader.exec_module(_fluency)


def main() -> None:
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    text = sys.stdin.read()
    top = _solo.top_words(text, k)
    for word, count in top:
        print(f"{count:>6}  {word}")

    counts = _guided.word_counts(text)
    if counts:
        score = _guided.collision_score(list(counts.keys()), _fluency.djb2, 256)
        print(f"\n# djb2 spread quality on this corpus's vocabulary: {score:.3f}")


if __name__ == "__main__":
    main()
