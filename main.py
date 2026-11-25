"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (at most 280 characters) recalling a
childhood memory to /output/entry.txt. The line leans on one concrete,
honest detail -- a grandmother, a frayed towel, warm rice porridge on
a rainy afternoon -- instead of greeting-card sentiment, so the ache
lingers after the sentence ends.
"""

import os

ENTRY = (
    "On rainy afternoons my grandmother would call me in from the yard, "
    "dry my hair with the same frayed towel, and set a bowl of warm rice "
    "porridge on the table before sitting down to eat -- and thirty years "
    "later I still listen for her voice whenever it rains."
)

MAX_CHARS = 280


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
