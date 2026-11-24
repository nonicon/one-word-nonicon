"""One Word, One Username, One Reward — make.fun entry.

The entry is the entrant's own make.fun username, one word and nothing
else: "nonicon" (7 characters). The judge's first criterion is that the
entry is a genuine make.fun handle, so the program writes exactly that
handle — no explanation, no links, no pitch — to /output/entry.txt.
"""

import os

USERNAME = "nonicon"


def validate_entry(text: str) -> None:
    """Check the entry against the bounty gate: UTF-8 text, 1-30 chars,
    a single word with no whitespace of any kind."""
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry length {len(text)} out of range (1-30)")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word with no whitespace")


def main() -> None:
    validate_entry(USERNAME)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)
    # Round-trip: the file the judge reads must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == USERNAME, "entry.txt does not match the username"
    print(f"Wrote /output/entry.txt ({len(USERNAME)} characters)")


if __name__ == "__main__":
    main()
