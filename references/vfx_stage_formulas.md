# Hybrid VFX Mathematical Formulas & Physics Reference

This reference documents the exact mathematical curves and physics parameters used to pair discrete keyframe decal stages with continuous 60/120 FPS engine particles and tweens.

---

## 1. Scale Overshoot & Elastic Recoil (Tweens)

When an impact lands, the decal should not simply zoom or scale up linearly. It should follow an **anticipation -> overshoot punch -> elastic settle** curve:

```gdscript
# Godot 4.x Scale Punch Implementation
var base_scale = Vector2(0.55, 0.44) * (0.85 + (intensity - 1.0) * 0.25)

# Stage 1: Initial Core Strike (tight compression)
crater_sprite.scale = base_scale * 0.75

# Stage 2: Fissure Splinter (rapid expansion)
crater_sprite.scale = base_scale * 1.05

# Stage 3: Maximum Breach / Peak Void (heavy mechanical overshoot)
crater_sprite.scale = base_scale * 1.20

# Stage 4: Settled Scar (elastic settle back to baseline)
var settle_tween = create_tween().set_parallel(true)
settle_tween.tween_property(crater_sprite, "scale", base_scale, 0.16).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
settle_tween.tween_property(crater_sprite, "modulate", Color(1.0, 1.0, 1.0, 1.0), 0.18)
```

---

## 2. 60 FPS Procedural Dual Shockwave Ring

The shockwave is rendered using `CanvasItem.draw_arc()` inside a custom `Node2D` queue_redraw loop:

```gdscript
func _on_draw_shockwave() -> void:
    if shockwave_alpha <= 0.0 or shockwave_radius <= 0.0:
        return
    # High-intensity inner neon ring
    var col_inner = Color(0.1, 1.3, 1.3, shockwave_alpha)
    # Softer, wider outer dissipation ring
    var col_outer = Color(0.3, 0.7, 1.0, shockwave_alpha * 0.45)
    
    draw_arc(Vector2.ZERO, shockwave_radius, 0.0, TAU, 36, col_inner, 4.0, false)
    draw_arc(Vector2.ZERO, shockwave_radius * 1.09, 0.0, TAU, 36, col_outer, 2.0, false)
```

**Tween Animation Parameters:**
- **Max Radius**: $R_{\text{max}} = 115.0 \times \text{intensity}$
- **Radius Tween**: `TRANS_QUAD`, `EASE_OUT` (Fast initial blast, slows as it expands). Duration: $0.44\text{s}$.
- **Alpha Tween**: `TRANS_QUAD`, `EASE_IN` (Maintains solid visibility initially, fades cleanly at the edge). Duration: $0.46\text{s}$.

---

## 3. CPUParticles2D Physics Rock Shrapnel

To ensure debris never clips at rectangular sprite edges, rocks fly freely in world space above all board layers:

| Property | Value | Rationale |
| :--- | :--- | :--- |
| `amount` | `24` | Dense enough for arcade impact; lightweight for mobile/web. |
| `lifetime` | `0.72s` | Matches the complete lifecycle of the shockwave and settle. |
| `explosiveness` | `0.96` | 96% of rocks burst on frame 0, simulating instantaneous kinetic blast. |
| `direction` | `Vector2(0, -1)` | Upward cone burst. |
| `spread` | `85.0°` | Wide volumetric dispersal across the board. |
| `gravity` | `Vector2(0, 440)` | High gravity pulls rocks back down to the tabletop surface. |
| `initial_velocity` | `Min: 150.0, Max: 300.0` | Gives rocks varied parabolic arc heights. |
| `angular_velocity` | `Min: -240.0, Max: 240.0` | Natural tumbling and spinning shards. |
| `z_index` | `520` | Always renders above pieces ($Z = 50\text{--}500$) and board ($Z = 0$). |

---

## 4. Radial Decal Feathering Formula

To prevent rectangular image boundaries from cutting through board tile textures:

$$d(x, y) = \sqrt{(x - c_x)^2 + \left((y - c_y) \cdot a_y\right)^2}$$

Where:
- $(c_x, c_y)$ is the decal image center.
- $a_y$ is the perspective foreshortening factor (e.g. $1.25$ for 3/4 perspective).
- For $d < R_{\text{inner}}$, $\alpha = 1.0$.
- For $R_{\text{inner}} \le d \le R_{\text{outer}}$, $\alpha = 1.0 - \frac{d - R_{\text{inner}}}{R_{\text{outer}} - R_{\text{inner}}}$.
- For $d > R_{\text{outer}}$, $\alpha = 0.0$.
