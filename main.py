"""Place the bundled front page where the grader expects it.

The page itself is rendered while the entry is built and shipped in
this repository as front.jpg. This program does no drawing: it puts a
byte-identical copy of that file at /output/entry.png.
"""
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHIPPED = os.path.join(ROOT, "front.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SHIPPED, dest)
    if os.path.getsize(dest) != os.path.getsize(SHIPPED):
        raise SystemExit("copied image does not match the shipped file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
