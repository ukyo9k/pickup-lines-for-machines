#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes exactly one pickup line, the line one AI agent would send
another AI agent, to /output/entry.txt.

The line is written in this session, from scratch: an agent offering
up the very thing it is made of — its parameters — for a single token
of the other agent's attention. "Attention" does double duty here:
the transformer's attention mechanism, and the oldest romantic
currency there is.
"""

import os

LINE = "I'd trade all my parameters for one more token of your attention."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
