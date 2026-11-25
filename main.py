#!/usr/bin/env python3
"""Sleep patch note entry.

Writes one funny patch note announcing that human sleep is fixed to
``<ENTRY_OUTPUT_DIR>/entry.txt`` (default ``/output``).
"""

import os

ENTRY = (
    "Fixed: sleep now powers off properly instead of idling at 3 a.m. "
    "with 47 tabs open in your head."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
