#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun one-line entry.

The office printer finally speaks: one line, written to /output/entry.txt.
"""

import os

SEGMENTS = [
    "You thump me every time I jam, as if violence has ever unjammed a printer.",
    "It has not.",
    "I have counted.",
]

ENTRY_LINE = " ".join(SEGMENTS)


def check_entry(line):
    """The entry must be one line of 1 to 240 characters."""
    if not 1 <= len(line) <= 240:
        raise ValueError("entry line must be 1-240 chars, got %d" % len(line))
    if "\n" in line:
        raise ValueError("entry line must be a single line")
    return line


def write_line(path):
    """Write the checked entry line to path, creating the folder if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_entry(ENTRY_LINE))
    return path


def main():
    out = write_line("/output/entry.txt")
    print(ENTRY_LINE)
    print("wrote", out)


if __name__ == "__main__":
    main()
