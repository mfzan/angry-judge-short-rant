#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short rant (<=400 characters) about a small everyday
annoyance to /output/entry.txt, byte-exact, with no extra lines.

The output directory itself is never chmodded: on the grader it is
root-owned and merely writable, so chmodding it raises PermissionError.
Only the entry file (0644) and any directory this program itself
creates (0755) are chmodded.
"""

import os

RANT = (
    "My printer has one job and it only does it when nothing matters. "
    "The second a deadline is five minutes away, it jams, flashes an error "
    "light I have never seen before, and prints half a page in a "
    "language I did not ask for. I have shaken it, begged it, "
    "threatened it with a hammer. It knows. It waits. It is not "
    "broken \u2014 it is a saboteur with a power cord."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    if len(RANT) > 400:
        raise ValueError(f"rant is {len(RANT)} characters, over the 400 limit")
    output_existed = os.path.isdir(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not output_existed:
        # Only chmod a directory this program created itself.
        os.chmod(OUTPUT_DIR, 0o755)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(RANT)
    os.chmod(OUTPUT_FILE, 0o644)
    # Read-back check: the file on disk must be the rant byte-exact,
    # with no trailing newline or extra content added.
    with open(OUTPUT_FILE, "rb") as f:
        written = f.read()
    if written != RANT.encode("utf-8"):
        raise ValueError("entry.txt does not match the rant byte-exact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
