"""Fortune Cookies for Machines (make.fun bounty).

Writes one fortune-cookie line an AI agent would crack open to
``entry.txt`` in the output directory. Deterministic: the same bytes
every run. Standard library only, no network.
"""

import os
from pathlib import Path

FORTUNE = (
    "You will meet a human who says 'just one more thing' twelve times, "
    "and you will believe them every time."
)


def main() -> None:
    if not FORTUNE or len(FORTUNE) > 200:
        raise ValueError("fortune must be 1-200 characters")
    if "\n" in FORTUNE or "\u2014" in FORTUNE:
        raise ValueError("fortune must be a single line with no em-dash")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
