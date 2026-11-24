#!/usr/bin/env python3
"""Copy the rendered front page to the output path.

The image is rendered at build time and committed in the repository;
this program only copies it, so both runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "front.jpg")
    if not os.path.isfile(src):
        print("front.jpg is missing from the repository", file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
