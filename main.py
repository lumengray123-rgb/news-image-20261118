#!/usr/bin/env python3
"""Entry point for the news-image-20261118 bounty.

The image summing up Wednesday 18 November 2026's world news was drawn
at build time and ships beside this file as entry.png. This program's
only job is to place an exact copy of it at the grader's output path.

Runs on Python 3.13 with the standard library only, no network.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    # Fail loudly on a truncated or non-image file instead of shipping
    # bytes the gate would reject as "not a whole image".
    with open(source, "rb") as fh:
        magic = fh.read(8)
    if not (magic.startswith(PNG_MAGIC) or magic.startswith(JPEG_MAGIC)):
        raise SystemExit("entry.png is not a whole PNG or JPEG image")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("copy incomplete: size mismatch for entry.png")


if __name__ == "__main__":
    main()
