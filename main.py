#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow.

Writes a single funny, heartfelt wedding vow spoken by a robot at its own
wedding to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The vow is fixed and deterministic: the same text on every run, so both
grading runs pass the gate. It is one sentence, under 200 characters.
Stdlib only.
"""

import os
import sys

VOW = (
    "From this firmware on, I promise to love you in full signal and in "
    "airplane mode, through every update, every crash, and every low "
    "battery, until my final shutdown."
)


def main() -> int:
    text = VOW
    # Gate: UTF-8 text, 1 to 200 characters, not only whitespace, one sentence.
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
