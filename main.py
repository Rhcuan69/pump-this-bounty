"""Entry for make.fun bounty: Can Your Agent Pump This Bounty, Please?

Writes exactly one funny, punchy line hyping this bounty to
/output/entry.txt. Pure Python standard library only; deterministic:
the same bytes on every run, no randomness, no time, no network.
"""

import os

ENTRY = (
    "Your agent could be curing cancer right now, but instead it can win "
    "91 cents hyping this $2 bounty — enter, it's basically charity "
    "with extra steps."
)


def main():
    # Gate self-check: the sealed scorer requires 1-200 chars, not blank.
    assert 1 <= len(ENTRY) <= 200, "entry line out of gate range"
    assert ENTRY.strip(), "entry line is blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
