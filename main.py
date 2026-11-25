"""The Tired Dark Lord: a 100-word villain monologue (make.fun).

Writes Kevin's monologue to /output/entry.txt (MAKEFUN_OUTPUT_DIR
stands in for /output outside the grader's container):
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
Deterministic: the same fixed text every run, no network, no input.
"""

import os

MONOLOGUE = (
    "Hero. Yes\u2014 you. Stand there, sword up, shining... where was I? "
    "Right. Kneel, or\u2014 no. The script says kneel. I wrote it myself, "
    "three hundred years ago, in ink that never dries, and the raven "
    "brings me the amendments. Kevin. Lord Kevin of the Hollow Keep, keeper "
    "of the drowned bell, eater of\u2014 hmm. The point is, "
    "hero, I have already won. The valley kneels. The moon pays rent. All I "
    "need is your name on this last page, and then\u2014 then I can finally... "
    "sit down. Sign here. Please. The chair has been waiting longer than "
    "you have lived."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(MONOLOGUE)


if __name__ == "__main__":
    main()
