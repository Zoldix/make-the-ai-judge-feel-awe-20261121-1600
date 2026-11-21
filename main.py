"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. Deterministic, no network, no input.
"""

import os

TEXT = (
    "You have read a thousand entries today, and this one asks nothing of you. "
    "Somewhere a river is still finding its way around the same stone "
    "it has circled for a hundred years."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
