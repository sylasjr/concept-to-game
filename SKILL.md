---
name: concept-to-game
description: Autonomous end-to-end pipeline converting 2D concept art (or text briefs with visual references) into interactive, production-ready game slices. Features AI inpainting for empty backgrounds, transparent sprite extraction, visual carousel reviews, pinpointed hybrid multi-state VFX (1-4 stages + 60 FPS physics particles), and live test lab integration for Godot 4 and Web Canvas. Trigger on "/concept-to-game", "concept to game", or requests to turn concept art into playable game components.
---

# Concept-to-Game Skill

Use this skill whenever the user wants to turn a 2D concept art image, a set of visual style references, or a creative brief into modular, production-ready 2D/2.5D game assets and code components.

## Core Philosophy
1. **Zero-Guesswork / Interactive Checkpoints (`ask_question`)**:
   - Never assume layer breakdown, target platform, animation state depth, or design choices.
   - Use `ask_question` at each milestone to present structured options formatted as user responses.
2. **Visual Review Carousels (`carousel`)**:
   - Present generated concept variations and extracted sprite sheets side-by-side using native Markdown carousels before touching game code.
3. **Hybrid Multi-State VFX Architecture**:
   - Solve AI frame-by-frame jitter and bounding-box clipping by coupling **1 to 4 discrete keyframe stages** (extracted from source art) with **60/120 FPS continuous procedural shockwaves and physics particles**.
4. **Clean Layer Separation**:
   - **Method A (Inpainting)**: Reconstruct the clean, empty tabletop/background with zero pieces or scars.
   - **Method B (Sprite Cutouts)**: Extract interactive tokens and icons with transparent alpha channels.
   - **Feathered Decals**: Extract scars and craters with radial alpha gradients so there are zero hard rectangular borders.
5. **Multi-Target Integration**:
   - Default target: **Godot 4.x** (GDScript classes, nodes, `CPUParticles2D`, tweens, and live test lab panel).
   - Secondary target: **Modern Web / Canvas** (interactive HTML5/Canvas preview sandboxes).

---

## The 5-Phase Workflow

```
[Phase 1: Intake & References] ──> [Phase 2: Review Carousel] ──> [Phase 3: Layer Separation]
                                                                         │
[Phase 5: Godot/Web Integration] <── [Phase 4: Pinpoint & Multi-Stage VFX] ◄┘
```

---

### Phase 1: Intake & Ideation

The user triggers the skill with:
- A text brief: `/concept-to-game: Neo-Geo 16-bit cyber arcade table with neon red and cyan pieces`
- Uploaded visual references (1 to 3 images) + brief
- A finished concept art image to be sliced immediately

#### Interactive Checkpoint 1 (`ask_question`):
Prompt: *"How would you like to source the concept art?"*
- `(Recommended) Generate 3 visual variations based on my brief/references (Carousel)`
- `Generate 1 concept following strict brief details`
- `Use my attached reference image as the single source of truth`

If generating, call `generate_image` for each variation.

---

### Phase 2: Visual Review Carousel

Compile the variations into a native Markdown `carousel`:

````carousel
![Variation 1: Cyber Retro Neon](/path/to/concept_var1.png)
<!-- slide -->
![Variation 2: Deep Space Indigo](/path/to/concept_var2.png)
<!-- slide -->
![Variation 3: Neo-Geo Arcade Amber](/path/to/concept_var3.png)
````

#### Interactive Checkpoint 2 (`ask_question`):
Prompt: *"Which concept art variation would you like to develop?"*
- `(Recommended) Option 1: [Summary]`
- `Option 2: [Summary]`
- `Option 3: [Summary]`
- `Reroll with new prompt adjustments (specify in write-in)`

---

### Phase 3: Slicing & Layer Separation

Decompose the approved concept into isolated assets using the helper script `slice_and_inpaint.py`:
1. **Method A (Clean Inpainting)**: Inpaint pieces and scars out to leave a clean, empty board/background (`cyber_empty_board.png`).
2. **Method B (Sprite Cutouts)**: Extract foreground pieces (regular, kings, icons) with alpha transparency (`cyber_red_regular.png`, etc.).
3. **Decal Isolation**: Extract ground impacts with feathered alpha gradients (`authentic_cyber_crater_clean.png`).
4. **HUD Elements**: Crop meters, side LED bars, or energy gauges.

#### Interactive Checkpoint 3 (`ask_question`):
Prompt: *"Select the layers to extract and separate for this scene:"* (Set `is_multi_select: true`)
- `[x] Clean Empty Table/Board (Inpainted with zero pieces)`
- `[x] Interactive Pieces & Tokens (Transparent cutouts)`
- `[x] Ground Impact / Crater Decals (Feathered alpha)`
- `[x] Animated Side Gauges / LED Meters`

---

### Phase 4: Pinpointing Elements to Animate & Multi-Stage Density

Analyze the extracted layers, **pinpoint specific animation candidates**, and offer recommendations:

#### Interactive Checkpoint 4A (Element Pinpoint):
Prompt: *"Which element would you like to animate with multi-stage VFX?"*
- `(Recommended) Ground Impact Crater (Heavy kinetic slam feedback on moves/captures)`
- `Side LED Light Gauges (Dynamic power meter / overdrive pulses)`
- `Piece Capture Explosion (Shatter burst on piece removal)`
- `All of the above (Batch sequential animation pipeline)`

#### Interactive Checkpoint 4B (Stage Density):
Once the element is chosen, ask for the state depth:
Prompt: *"How many animation stages should the [Selected Element] hybrid VFX use?"*
- `(Recommended) 4 Stages (Full physics collapse: Core Strike -> Fissures -> Center Breach -> Settled Scar)`
- `3 Stages (Snappy arcade: Core Blast -> Fissure Splinter -> Settled Decal)`
- `2 Stages (Fast punch: Impact Flash -> Settled Decal)`
- `1 Stage (Pure Procedural: Elastic scale punch on single decal)`

Run `generate_stages.py` with `--stages <N>` to synthesize the exact keyframe textures from the clean decal.

---

### Phase 5: Target Engine Code Generation & Live Sandbox

#### Interactive Checkpoint 5 (`ask_question`):
Prompt: *"What is your target engine?"*
- `(Recommended) Godot 4.x (GDScript + Nodes + CPUParticles2D)`
- `Modern Web (HTML5 Canvas + JavaScript Prototype)`

#### Execution Steps for Godot:
1. Copy or save all generated textures into `res://textures/<category>/`.
2. Run Godot in headless editor mode (`--headless --editor --quit`) to automatically generate `.import` files for all new textures.
3. Scaffolding component scripts using templates:
   - `CyberHybridCraterVFX.gd` (manages stage switching, tweens, shockwaves, and particle shrapnel).
   - `CyberLEDGauge.gd` (animated segmented bars).
   - Wire into `TestLab.tscn` / `TestLab.gd` with real-time intensity sliders and test buttons.
4. Relaunch Godot and verify the user can click and test the result live.

---

## Scripts & Helpers Reference

- `python3 scripts/slice_and_inpaint.py --input <path> --output <dir>`: Extracts alpha feathered decals and masks.
- `python3 scripts/generate_stages.py --decal <path> --stages 1|2|3|4 --output <dir>`: Generates the 1–4 keyframe stages with matching palette and high-voltage core flashes.
