---
id: exclude-dark-yellow-green
title: Exclude Dark Yellow-Green Colors
bibliography: references.bib
description: Remove dark yellow-green hues to improve average palette preference.
labels:
- visual:color
- impact:aesthetics
- impact:preference
- data:categorical
---

## The Rule <!-- role: advice -->
Filter out the dark yellowish-green region of color space when generating or selecting categorical palettes.

## The Logic <!-- role: reason -->
There is a specific region of color space (defined as $L \in [35,75]$ and $H \in [85^{\circ},114^{\circ}]$ in CIE LCh) that creates strongly disliked colors across many cultures. When algorithms maximize discriminability against preferred "cool" colors (blues), they mathematically tend to select opposite hues (yellows/browns) in this disliked region. Removing this specific slice of color space significantly increases average aesthetic ratings without critically harming discriminability [@gramazio_colorgorical_2017].

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating aesthetically pleasing visualizations that general audiences find "preferable."
*   **Data Type:** Any categorical visualization.
*   **Audience:** General public (based on average observer preferences).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Specific semantic mapping.
*   **Reason:** If the data represents something that naturally requires this color (e.g., "Forestry," "Military Camouflage," or "Decay"), the semantic meaning overrides general aesthetic preference.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Total available color volume.
*   **The Risk:** You lose a chunk of "discriminable" space, which may make it harder to find distinct colors for palettes with very high cardinality (e.g., 10+ categories).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using purely mathematical complementary colors.
*   **Why it fails:** The mathematical complement to a nice dark blue is often a muddy, dark orange-yellow that users find unappealing [@gramazio_colorgorical_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the palette contain "pukey" greens or muddy mustard yellows?
*   **The Test:** Check if any color falls within the perceptual range of dark yellow-green (approximate Hue 85-114 degrees).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Shift the hue toward a cleaner Green or a distinct Orange, or increase the lightness significantly.
*   **Best Fix:** Apply a hard filter to the color generation process to exclude the hue range $85^{\circ}-114^{\circ}$ at low-to-mid lightness levels.
