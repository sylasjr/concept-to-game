#!/usr/bin/env python3
"""
generate_stages.py
Generates 1, 2, 3, or 4 discrete keyframe stages from a single authentic 2D decal,
preserving exact pixel art colors, stone textures, and perspective foreshortening
while eliminating AI frame-by-frame jitter and hard rectangular borders.
"""

import argparse
import math
import os
from PIL import Image

def generate_stages(decal_path: str, stages: int, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    img = Image.open(decal_path).convert("RGBA")
    w, h = img.size
    cx, cy = w / 2.0, h / 2.0

    print(f"Generating {stages} hybrid stage(s) from: {decal_path}")

    if stages == 1:
        # Stage 1 of 1: Single pristine decal
        out_path = os.path.join(output_dir, "hybrid_stage_1_settle.png")
        img.save(out_path)
        print(f"Saved: {out_path}")
        return

    if stages == 2:
        # Stage 1: Impact Core Flash
        img1 = img.copy()
        pix1 = img1.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix1[x, y]
                if a > 0:
                    d = math.sqrt((x - cx)**2 + ((y - cy) * 1.3)**2)
                    if d < 65:
                        pix1[x, y] = (255, 255, 255, 255)
                    elif d < 110:
                        factor = 1.0 - (d - 65) / 45.0
                        pix1[x, y] = (min(255, int(r * 1.8 + 60)), min(255, int(g * 2.0 + 80)), min(255, int(b * 2.0 + 80)), int(a * factor))
                    else:
                        pix1[x, y] = (0, 0, 0, 0)
        img1.save(os.path.join(output_dir, "hybrid2_stage_1_flash.png"))
        img.save(os.path.join(output_dir, "hybrid2_stage_2_settle.png"))
        print(f"Saved 2 stages to {output_dir}")
        return

    if stages == 3:
        # Stage 1: Epicenter Core Blast
        img1 = img.copy()
        pix1 = img1.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix1[x, y]
                if a > 0:
                    d = math.sqrt((x - cx)**2 + ((y - cy) * 1.35)**2)
                    if d < 55:
                        pix1[x, y] = (255, 255, 255, 255)
                    elif d < 90:
                        factor = 1.0 - (d - 55) / 35.0
                        pix1[x, y] = (min(255, int(r * 2.0 + 50)), min(255, int(g * 2.2 + 80)), min(255, int(b * 2.2 + 80)), int(a * factor))
                    else:
                        pix1[x, y] = (0, 0, 0, 0)

        # Stage 2: Spider Fractures
        img2 = img.copy()
        pix2 = img2.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix2[x, y]
                if a > 0:
                    d = math.sqrt((x - cx)**2 + ((y - cy) * 1.25)**2)
                    if d < 135:
                        pix2[x, y] = (min(255, int(r * 0.9)), min(255, int(g * 1.45 + 35)), min(255, int(b * 1.45 + 45)), a)
                    elif d < 185:
                        factor = 1.0 - (d - 135) / 50.0
                        pix2[x, y] = (r, g, b, int(a * factor))
                    else:
                        pix2[x, y] = (0, 0, 0, 0)

        img1.save(os.path.join(output_dir, "hybrid3_stage_1_flash.png"))
        img2.save(os.path.join(output_dir, "hybrid3_stage_2_splinter.png"))
        img.save(os.path.join(output_dir, "hybrid3_stage_3_settle.png"))
        print(f"Saved 3 stages to {output_dir}")
        return

    if stages >= 4:
        # Stage 1: Incandescent Core Strike
        img1 = img.copy()
        pix1 = img1.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix1[x, y]
                if a > 0:
                    d = math.sqrt((x - cx)**2 + ((y - cy) * 1.35)**2)
                    if d < 45:
                        pix1[x, y] = (255, 255, 255, 255)
                    elif d < 75:
                        factor = 1.0 - (d - 45) / 30.0
                        pix1[x, y] = (min(255, int(r * 2.2 + 80)), min(255, int(g * 2.4 + 100)), min(255, int(b * 2.4 + 100)), int(a * factor))
                    else:
                        pix1[x, y] = (0, 0, 0, 0)

        # Stage 2: Radial Spider Fractures
        img2 = img.copy()
        pix2 = img2.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix2[x, y]
                if a > 0:
                    d = math.sqrt((x - cx)**2 + ((y - cy) * 1.25)**2)
                    if d < 125:
                        pix2[x, y] = (min(255, int(r * 0.9)), min(255, int(g * 1.5 + 40)), min(255, int(b * 1.5 + 50)), a)
                    elif d < 170:
                        factor = 1.0 - (d - 125) / 45.0
                        pix2[x, y] = (r, g, b, int(a * factor))
                    else:
                        pix2[x, y] = (0, 0, 0, 0)

        # Stage 3: Maximum Breach / Peak Void (Structural collapse abyss)
        img3 = img.copy()
        pix3 = img3.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix3[x, y]
                if a > 0:
                    d = math.sqrt((x - cx)**2 + ((y - cy) * 1.22)**2)
                    if d < 55:
                        pix3[x, y] = (max(0, int(r * 0.25)), max(0, int(g * 0.25)), max(0, int(b * 0.35)), a)
                    elif d < 110:
                        pix3[x, y] = (min(255, int(r * 1.3 + 30)), min(255, int(g * 1.6 + 60)), min(255, int(b * 1.7 + 70)), a)
                    elif d < 220:
                        pix3[x, y] = (r, g, b, a)
                    else:
                        factor = 1.0 - (d - 220) / 35.0
                        pix3[x, y] = (r, g, b, int(a * max(0.0, factor)))

        img1.save(os.path.join(output_dir, "hybrid4_stage_1_strike.png"))
        img2.save(os.path.join(output_dir, "hybrid4_stage_2_fissures.png"))
        img3.save(os.path.join(output_dir, "hybrid4_stage_3_breach.png"))
        img.save(os.path.join(output_dir, "hybrid4_stage_4_settle.png"))
        print(f"Saved 4 stages to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 1-4 hybrid stages from a decal PNG")
    parser.add_argument("--decal", required=True, help="Path to clean decal PNG")
    parser.add_argument("--stages", type=int, default=4, choices=[1, 2, 3, 4], help="Number of stages to generate (1-4)")
    parser.add_argument("--output", required=True, help="Output directory")
    args = parser.parse_args()
    generate_stages(args.decal, args.stages, args.output)
