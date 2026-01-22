---
id: test-color-palettes-with-cvd-simulations-and-remove-major-warnings
title: Test chart color palettes with color vision deficiency simulations and remove
  any major tool warnings
bibliography: references.bib
description: Ensure chart colors remain distinguishable under common color vision
  deficiencies by testing palettes in dedicated tools and addressing any major warnings.
labels:
- chart:generic
- task:decode
- visual:color
- impact:accessibility
- data:categorical
- audience:everyone
- disability:cvd
- process:palette-selection
---

## Verify palette distinguishability under color vision deficiency simulations <!-- role: advice -->

Test the chart’s color palette in a color vision deficiency simulation tool and change the palette until the tool shows no major warnings. Do this even if the chart also uses high contrast or textures.

## Why simulated color vision deficiency checks prevent color-only confusion <!-- role: reason -->

Color vision deficiency can make distinct hues appear similar, which turns color-coded categories or series into ambiguous marks even when the chart otherwise looks acceptable. Running a palette through simulation tools exposes these collisions before publishing and helps ensure categorical distinctions remain perceivable.

**Mechanism:** Simulations reveal when hue differences collapse into similar lightness and chroma under common color vision deficiencies, which is the primary way color-based encodings become indistinguishable.

**Evidence:** Color vision deficiencies can make certain color combinations hard to distinguish, so palette choices should be evaluated for how they appear to colorblind and colorweak readers [@datawrapper_how_your]. A synthesized heuristic evaluation methodology for charts includes color vision deficiency considerations alongside other accessibility checks [@alcaraz_martinez_methodology_for_2022]. Chartability includes this heuristic as part of making visualizations perceivable and audit-ready in practice [@elavskyHowAccessibleMy2022].

**Notes:** This guideline focuses on whether the chosen palette remains distinguishable under simulation, not on whether color is the only encoding.

## Where palette simulation checks apply <!-- role: context -->

- **User Goal:** Distinguish categories or series that are encoded by color.
- **Task:** Identify, compare, or track groups based on color-coded marks.
- **Data:** Categorical groupings or multiple series where color is a key discriminator.
- **Chart Setting:** Any chart that uses a color palette for marks, lines, fills, or legends.
- **Audience:** General audiences, including people with color vision deficiencies.
- **Success Criterion:** A color vision deficiency simulation tool reports no major warnings for the palette.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart contains no color encodings that distinguish values or categories. **Why:** A palette simulation is irrelevant if color is not used to communicate differences.

## Tradeoffs of palette constraints <!-- role: costs -->

**Sacrifice:** Some preferred brand or aesthetic palettes may need to be changed. **Risk:** Over-constraining the palette can reduce the number of visually distinct categories available. **Mitigation:** Treat the simulation output as a gate for “major warnings,” not as a demand for a single specific palette.

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Assuming high contrast or textures automatically resolve all color vision deficiency problems. **Why it fails:** Distinguishability can still break when hues collapse under color vision deficiency even if contrast or redundant cues exist [@elavskyHowAccessibleMy2022].
- **Mistake:** Skipping tool-based checks and relying on personal judgment. **Why it fails:** Designers without color vision deficiency may not notice collisions that simulations surface [@datawrapper_how_your].

## Fast checks for color vision deficiency friendliness <!-- role: check -->

**Failure Sign:** Two or more categories or series become difficult to tell apart when viewed under a color vision deficiency simulation. **Quick Check:** Load the palette into Viz Palette and ensure it does not show major warnings in its colorblind checks [@susielu_viz_palette]. **Stronger Test:** Use the Chroma.js palette helper’s color vision deficiency simulations and confirm there are no major warnings for the palette configuration you plan to use [@vis4_chromajs_colour].

## What to do if the palette fails the simulation <!-- role: fix -->

- Replace the palette with an alternative that passes the simulation tool without major warnings.
- Reduce the number of color-coded categories or series until the remaining colors stay distinguishable under simulation.
- Change the design so the intended distinctions do not depend on fine hue differences (for example, simplify the color grouping strategy).
- Re-run the simulation after any palette adjustment and stop only when major warnings are cleared in the chosen tool [@susielu_viz_palette; @vis4_chromajs_colour].
