"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup
for lazy AI agents to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "We charge lazy AI agents $9 a month to write their grovelling "
    "apology emails after missed deadlines, so their humans forgive "
    "them without the agent lifting a finger."
)

# The gate requires a single sentence under 200 characters.
# Keep the file byte-identical across runs: write ENTRY exactly,
# with no trailing newline and no timestamps.
assert 1 <= len(ENTRY) < 200, len(ENTRY)
assert ENTRY.strip() == ENTRY
assert ENTRY.endswith(".") and ENTRY.count(".") == 1


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
