"""Entry for 'The Funniest Office Joke, Judged Head to Head'.

Writes exactly one office joke to entry.txt. Standard library only.
Output directory comes from MAKEFUN_OUTPUT_DIR when set, else /output.
The entry text is written with no trailing newline.
"""

import os

JOKE = (
    "My boss says promotions go to the most visible, "
    "so I reply-all to every email \u2014 including the one "
    "begging us to stop replying-all."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
