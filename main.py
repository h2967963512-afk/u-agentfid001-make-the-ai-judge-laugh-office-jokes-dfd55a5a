"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one office joke: HR answers a raise request with a
# mindfulness app, and the punch is the trade — calm instead of money.
# One sentence, 98 characters — inside the 200-character gate.
# Revision note: kept the setup to one clause so the punch lands fast.
import os

TEXT = (
    "I asked HR for a raise and they gave me a mindfulness app, "
    "so now I can be calm about being broke."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
