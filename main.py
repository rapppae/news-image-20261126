#!/usr/bin/env python3
"""Ship the pre-rendered 26 November 2026 news poster.

The grader runs with the standard library only and no Pillow, so this
entrypoint does not draw anything: it copies the poster PNG that ships
in this repository to the output folder, then checks the copy on disk
with the standard library alone — PNG signature, exactly 1024 by 1024
(read from the IHDR chunk), and under one mebibyte. Anything off fails
loudly instead of silently shipping a broken image.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSTER = HERE / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EDGE = 1024
MAX_BYTES = 1024 * 1024


def target_path():
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.png"


def check_png(path):
    data = path.read_bytes()
    if data[:8] != PNG_MAGIC:
        raise SystemExit("not a PNG file")
    if data[12:16] != b"IHDR":
        raise SystemExit("no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EDGE, EDGE):
        raise SystemExit(f"wrong size: {width}x{height}")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"too big: {len(data)} bytes")
    return data, width, height


def main():
    dest = target_path()
    shutil.copyfile(POSTER, dest)
    data, width, height = check_png(dest)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {dest} ({width}x{height}, {len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
