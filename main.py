#!/usr/bin/env python3
"""Write the office reply-all joke to /output/entry.txt.

The joke is a one-liner about accidentally becoming the very thing
you tried to stop: replying all to complain about reply-all.
It runs with only the Python standard library, no extra setup,
and it always writes the same single line to the output file.
"""

import os

LINE = "I hit reply-all to tell everyone to stop replying all, and now I'm the reason there's a 47-email thread about replying all."
OUTPUT_PATH = "/output/entry.txt"


def main():
    """Create the output folder and write the joke plus a newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
