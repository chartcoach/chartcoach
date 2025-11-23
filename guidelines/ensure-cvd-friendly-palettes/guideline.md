---
id: ensure-cvd-friendly-palettes
title: Verify Color Palettes with CVD Simulation
bibliography: references.bib
description: Ensure color choices are distinguishable to people with color vision
  deficiencies by testing against simulations.
labels:
- chart:any
- visual:color
- impact:accessibility
- impact:inclusivity
- method:heuristic
- audience:cvd
---

## The Rule <!-- role: advice -->
Select color palettes that are "colorblind safe" and verify that distinct data categories remain distinguishable under color vision deficiency (CVD) simulations.

## The Logic <!-- role: reason -->
This heuristic ensures that content falls under the "Perceivable" principle of accessibility. While high contrast and texture can help resolve interpretability issues, specific color combinations (such as red-green) remain difficult for a significant portion of the population to distinguish. Research indicates that approximately 8% of men of European descent have red-green deficiencies [@datawrapper_how_your]. Therefore, relying on assumptions about contrast is insufficient; explicit simulation is required to guarantee safety.
*   **The Principle:** Perceivable / CVD Safety
*   **The Evidence:** [@elavsky_how_2022], [@alcaraz_martinez_methodology_for_2022]

## Where to Apply <!-- role: context -->
This rule applies to any data visualization where color is used to encode information (categorical, sequential, or diverging).
*   **User Goal:** To differentiate between data groups or values based on hue or saturation.
*   **Data Type:** Categorical data (distinct hues) or continuous data (gradients).
*   **Audience:** General audiences, inclusive of the ~29% of the global population with visual impairments or blindness (including CVD) [@elavsky_how_2022].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When color is strictly decorative and carries no semantic meaning or data value.
*   **Reason:** If the inability to distinguish a color does not result in the loss of information or context, the strict adherence to a safe palette is less critical, though still recommended for aesthetic consistency.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Adhering to CVD-safe palettes restricts the design space, potentially excluding specific brand colors or widely used semantic associations (like standard Red/Green for bad/good) if they fail simulation tests.
*   **The Risk:** Palettes optimized solely for CVD safety may sometimes lack the vibrancy or cultural coding desired for specific narrative impacts.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying on high contrast alone to solve hue differentiation issues.
*   **Why it fails:** While contrast assists legibility, the source notes emphasize that even with high contrast, it is still important to test color schemes against CVD simulations to ensure hues do not blend together [@elavsky_how_2022].
*   **The Wrong Fix:** Using "Traffic Light" (Red/Green/Yellow) scales without modification.
*   **Why it fails:** These are frequently indistinguishable to those with Deuteranopia or Protanopia [@datawrapper_how_your].

## How to Check <!-- role: check -->
*   **Visual Sign:** In simulation mode, distinct data categories appear as the same shade of muddy brown or yellow, making them indistinguishable.
*   **The Test:** Input your chart's colors into tools like **Viz Palette** [@susielu_viz_palette] or **Chroma.js** [@vis4_chromajs_colour]. Ensure the palette does not return "major warnings" regarding distinguishability.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use the simulation tools to slightly adjust the lightness or brightness of the conflicting colors so they are distinct even if the hues appear similar.
*   **Best Fix:** Adopt a pre-tested, universally safe palette (e.g., Viridis or Cividis) or use tools like Chroma.js to mathematically generate a safe diverging or sequential scale [@vis4_chromajs_colour].
