---
id: avoid-3d-text-at-low-resolution-or-small-sizes
title: Avoid Small 3D Text on Low-Resolution Displays
bibliography: references.bib
description: Do not rely on small 3D fonts for labeling on low-resolution displays
  where 3D antialiasing produces muddy letterforms.
labels:
- task:label
- visual:text
- impact:accessibility
- data:any
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Do not use small 3D-rendered text (e.g., ~12pt equivalents) as a primary label mechanism on low-resolution displays.

## The Logic <!-- role: reason -->

At historically common screen resolutions (72–96 ppi), small 3D text becomes muddy because 3D antialiasing lacks the specialized subpixel optimizations used by 2D font rendering, reducing legibility and harming labeling effectiveness [@brath3DInfoVisHere2014].

- **The Principle:** Legibility depends on rendering quality and resolution; 3D font rendering can degrade small text.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Read labels and annotations in a 3D scene.
- **Data Type:** Any chart requiring text labels in 3D space.
- **Audience:** General users, especially on typical desktop/projector setups [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** High-resolution displays (e.g., much higher ppi) where 3D text detail is sufficiently rendered.
- **Reason:** Higher resolution improves the visibility of fine typographic detail and can make 3D text more viable [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less direct labeling inside the 3D scene.
- **The Risk:** If you avoid 3D labels, you may need alternative labeling strategies that require more coordination [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping 3D labels small and hoping antialiasing will “clean it up.”
- **Why it fails:** The letterforms remain low-contrast/muddy at low ppi and become hard to read [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Serifs and counters fill in; strokes look uneven; words blur at normal viewing size.
- **The Test:** View the scene at intended display resolution and distance; if labels require zooming to read, they’re too small/low-quality [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase text size or move labels to a 2D overlay plane.
- **Best Fix:** Use labeling approaches that avoid fragile 3D text readability (e.g., coordinated views/devices for text, or design the scene to minimize in-3D text reliance) [@brath3DInfoVisHere2014].
