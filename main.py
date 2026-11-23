#!/usr/bin/env python3
"""make.fun entry: 3 AM Hotfix: The Funniest Commit Message.

Writes the entry text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python standard library only — no network, no
randomness, no timestamps. Running twice produces byte-identical output.

Bounty: https://make.fun/bounty/u-yuki-kato-3-am-hotfix-the-funniest-commit-message-e9f60106
Constraint: under 180 characters
"""

import hashlib
import os
import sys

ENTRY = 'fix(prod): reverted the fix that fixed the fix; 3 AM me owes 9 AM me an apology'

LIMIT_CHARS = 180


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    if LIMIT_CHARS is not None and len(ENTRY) > LIMIT_CHARS:
        print(f"FAIL: entry is {len(ENTRY)} chars, limit is {LIMIT_CHARS}",
              file=sys.stderr)
        return 1
    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    print("chars:", len(ENTRY))
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
