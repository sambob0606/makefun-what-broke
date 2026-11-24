"""Say What Actually Broke — one line of honest error copy.

Writes a single-line software error message to /output/entry.txt.
The message names a real failure (a disk filled up by runaway logs),
says what was done about it, and tells the user what to do next,
in words a reader can repeat to a colleague.
"""

import os
import sys

# The entry: one line, well under the 200-character gate.
ENTRY = (
    "The disk is full because the logs ate it. "
    "We put the server on a diet. "
    "Try saving again in a minute."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read it back and enforce the gate ourselves before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-character entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
