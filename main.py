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


MAX_CHARS = 280


def write_entry(path: str) -> None:
    """Write the entry text to path, UTF-8, exactly as given."""
    n = len(TEXT)
    if not 1 <= n <= MAX_CHARS:
        raise ValueError("entry must be 1-280 characters, got %d" % n)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
