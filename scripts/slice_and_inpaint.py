#!/usr/bin/env python3
"""
slice_and_inpaint.py
Extracts foreground elements, crops UI gauges, and applies feathered alpha masks
to ground decals to eliminate hard rectangular bounding boxes.
"""

import argparse
import math
import os
from PIL import Image

def feather_decal(input_path: str, output_path: str, inner_radius: float = 180.0, outer_radius: float = 230.0, aspect: float = 1.25):
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    cx, cy = w / 2.0, h / 2.0
    pix = img.load()

    for y in range(h):
        for x in range(w):
            r, g, b, a = pix[x, y]
            if a > 0:
                d = math.sqrt((x - cx)**2 + ((y - cy) * aspect)**2)
                if d > outer_radius:
                    pix[x, y] = (0, 0, 0, 0)
                elif d > inner_radius:
                    factor = 1.0 - (d - inner_radius) / (outer_radius - inner_radius)
                    pix[x, y] = (r, g, b, int(a * factor))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"Feathered decal saved cleanly to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply radial feathering to eliminate decal bounding boxes")
    parser.add_argument("--input", required=True, help="Input raw decal PNG")
    parser.add_argument("--output", required=True, help="Output feathered PNG")
    parser.add_argument("--inner", type=float, default=180.0, help="Inner solid radius")
    parser.add_argument("--outer", type=float, default=235.0, help="Outer fade radius")
    parser.add_argument("--aspect", type=float, default=1.25, help="Perspective foreshortening Y scale factor")
    args = parser.parse_args()
    feather_decal(args.input, args.output, args.inner, args.outer, args.aspect)
