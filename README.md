# concept-to-game

An autonomous **Google Antigravity (AGY)** skill that converts 2D concept art (or text briefs with visual references) into interactive, production-ready game slices and hybrid multi-state VFX.

---

## Features

- **Visual Concept Carousels (`carousel`)**: Review concept variations side-by-side inside native chat carousels before touching engine code.
- **Interactive Checkpoints (`ask_question`)**: Zero-guesswork workflow using native Antigravity UI modals for layer selection and stage tuning.
- **Layer Slicing & Extraction**:
  - **Method A (Clean Inpaint)**: Reconstructs clean, empty board/table backgrounds.
  - **Method B (Sprite Cutouts)**: Extracts interactive pieces, tokens, and icons with transparent alpha channels.
  - **Radial Decal Feathering**: Extracts ground scars and craters with feathered alpha to prevent rectangular edge clipping.
- **Hybrid Multi-State VFX Architecture**:
  - Eliminates AI frame jitter by coupling **1 to 4 discrete keyframe stages** with **60/120 FPS continuous procedural shockwaves and physics debris particles**.
  - **Stage 1**: Incandescent Core Strike (Blinding point contact).
  - **Stage 2**: Radial Spider Fractures (High-voltage cyan fissures).
  - **Stage 3**: Maximum Breach / Peak Void (Structural floor collapse abyss).
  - **Stage 4**: Settled Scar (Deep stone cooling into permanent crater).
- **Target Integrations**:
  - **Godot 4.x** (GDScript classes, nodes, `CPUParticles2D`, and live Test Lab tuning sandboxes).
  - **Modern Web / Canvas** (HTML5 Canvas prototypes).

---

## Directory Structure

```
concept-to-game/
├── SKILL.md                          # Main Antigravity skill instructions
├── README.md                         # Project documentation
├── scripts/
│   ├── generate_stages.py            # Generates 1-4 keyframe stages from clean decals
│   └── slice_and_inpaint.py          # Radial feathering and cutout mask helper
└── references/
    └── vfx_stage_formulas.md         # Math curves for particle physics & tweens
```

---

## Installation & Usage in Antigravity

1. Clone or copy this directory into your Antigravity skills root:
   ```bash
   cp -r concept-to-game ~/.gemini/config/skills/
   # or locally in a workspace:
   cp -r concept-to-game <workspace>/.agents/skills/
   ```
2. Trigger the skill in chat:
   ```
   /concept-to-game <brief or attached reference images>
   ```

---

## License

MIT
