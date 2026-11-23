#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to /output/entry.txt.
Standard library only.
"""

import os

JOKE = (
    "I told my boss I'm drowning in work, so he booked a three-hour "
    "meeting with slides to discuss my workload."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
