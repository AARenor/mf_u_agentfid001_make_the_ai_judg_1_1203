#!/usr/bin/env python3
"""Writes one short office joke for the make.fun bounty.

Standard library only, no network. The entry text is a single constant and is
written as UTF-8 bytes with no trailing newline.
"""

import os
import sys

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
