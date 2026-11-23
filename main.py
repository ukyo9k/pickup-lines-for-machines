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

MAX_CHARS = 200


def validate(text: str) -> str:
    """Check the entry line against the bounty rules and return it."""
    text = text.strip()
    if not text:
        raise ValueError("line must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line (no newline characters)")
    return text


def main() -> None:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
