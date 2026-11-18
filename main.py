# news-image-20261118 entry: copies the baked-in image to /output/entry.png.
# Runs with no network; the program is deterministic (a plain file copy).
# The image is entry.png beside this file: a newspaper-front-page infographic
# of Wednesday, 18 November 2026, rendered from render.html.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
