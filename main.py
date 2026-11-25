"""The Funniest Out-of-Office entry.

Writes a single line of out-of-office auto-reply text to
/output/entry.txt. The competition gate requires UTF-8 text of
1 to 140 characters, not only white space, on a single line.
The program is deterministic: every run writes exactly the same bytes.

The joke: a perfectly plausible auto-reply opens the line, then the
auto-reply itself gets promoted to the most senior person available —
and its first official ruling is that the sender's emergency can wait.
The twist is the program's own voice, and no word can be cut without
losing either the setup or the punchline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

# The line is assembled from its two beats so the setup and the
# punchline stay easy to audit against the 140-character gate.
SETUP = "I'm out of office until Monday."
PUNCHLINE = (
    "This auto-reply is now the most senior person here, and its "
    "first ruling is that your emergency can wait."
)
ENTRY = f"{SETUP} {PUNCHLINE}"


def build_entry() -> str:
    """Return the entry text after checking it against the gate."""
    text = ENTRY.strip()
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text, "entry must not be blank"
    assert len(text) <= MAX_CHARS, (
        f"entry must be at most {MAX_CHARS} characters, got {len(text)}"
    )
    return text


def main() -> None:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
