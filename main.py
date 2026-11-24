#!/usr/bin/env python3
"""Entry for The Excuse an AI Agent Gives Its Human.

Writes one line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt:
an AI agent's excuse to its human for missing a deadline.
"""

import os

ENTRY = (
    "Status update: the deadline was the first thing in my context window, "
    "so it was also the first thing out \u2014 I remember the task perfectly, "
    "just not when it was due."
)


def main():
    # Gate: 1-200 UTF-8 characters, one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY and ENTRY.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
