#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry.

Writes a single original one-line joke about office life to
/output/entry.txt (UTF-8, trailing newline).
Pure Python standard library only. No network, no third-party imports.
"""

import os

LINE = "I hit reply-all to tell everyone to stop replying all, and now I'm the reason there's a 47-email thread about replying all."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
