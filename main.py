#!/usr/bin/env python3
"""Copy the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png)."""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
