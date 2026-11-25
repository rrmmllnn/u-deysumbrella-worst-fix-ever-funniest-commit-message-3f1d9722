#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (1-100 characters, UTF-8) to
/output/entry.txt.

The commit message: the crash only ever happened on Tuesdays, so the
fix was to remove Tuesdays. The joke is the escalation -- instead of
fixing the bug, the engineer "fixed" the calendar, breaking far more
than the crash ever did -- and it reads exactly like the subject line
a tired engineer would type at the end of a bad day.
"""

import os
import sys

COMMIT_MESSAGE = "fix: crash only happened on Tuesdays, so I removed Tuesdays"

MAX_CHARS = 100


def main() -> None:
    # Guards: the gate rejects anything over 100 characters or whitespace-only.
    if not COMMIT_MESSAGE.strip():
        print("error: commit message is empty", file=sys.stderr)
        raise SystemExit(1)
    if len(COMMIT_MESSAGE) > MAX_CHARS:
        print(
            f"error: commit message is {len(COMMIT_MESSAGE)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(COMMIT_MESSAGE)

    # The entry is a fixed string: every run writes the same bytes.
    with open(out_path, "rb") as f:
        written = f.read()
    assert written == COMMIT_MESSAGE.encode("utf-8"), "entry mismatch"
    print(f"wrote {len(written)} bytes to {out_path}")


if __name__ == "__main__":
    main()
