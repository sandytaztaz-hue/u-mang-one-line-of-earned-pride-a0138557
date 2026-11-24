#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of earned pride to /output/entry.txt.
A baker who failed her exam twice and sold her wedding ring for flour,
now watching the queue outside her little shop stretch past the church.
"""
import os

ENTRY = "She failed her baking exam twice, sold her wedding ring for flour, and this morning the queue outside her little shop stretched past the church."


def main():
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
