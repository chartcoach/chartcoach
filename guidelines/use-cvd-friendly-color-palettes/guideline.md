---
id: use-cvd-friendly-color-palettes
title: "Use Color Vision Deficiency\u2013Friendly Color Palettes"
bibliography: references.bib
description: Choose and validate chart color palettes so categories remain distinguishable
  under common color vision deficiencies.
labels:
- chart:bar
- chart:line
- chart:scatter
- task:distinguish
- task:categorize
- visual:color
- impact:accessibility
- impact:clarity
- data:categorical
- audience:general
- source:chartability
---

## The Rule <!-- role: advice -->

Choose a colorblind-safe palette and validate it with a CVD simulation tool (Viz Palette or Chroma). Do not ship a palette that triggers major warnings in either tool.

## The Logic <!-- role: reason -->

Color vision deficiencies can make different colors appear similar, collapsing color-encoded distinctions and preventing users from reliably telling categories or series apart [@datawrapper_how_your]. Chartability treats this as a perceivability requirement and recommends explicit CVD simulation/testing rather than assuming that other design choices will always resolve CVD issues [@elavskyHowAccessibleMy2022]. Heuristic evaluation work for charts for people with low vision and CVD similarly supports checking and designing to preserve distinguishability in statistical graphics [@alcaraz_martinez_methodology_for_2022].

- **The Principle:** Preserve categorical/series discriminability under altered color perception
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@alcaraz_martinez_methodology_for_2022] [@datawrapper_how_your]

## Where to Apply <!-- role: context -->

This advice is designed for charts where color carries meaning.

- **User Goal:** Distinguish groups, series, or categories encoded by color
- **Data Type:** Categorical series (including multiple series/lines or grouped marks)
- **Audience:** General audiences, including people with color vision deficiencies

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The chart does not use color to encode information (color is purely decorative and no distinctions depend on it).
- **Reason:** If color is not used for meaning, CVD distinguishability is not a functional dependency of the chart’s interpretation [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Fewer palette options and reduced freedom to use brand or aesthetic colors.
- **The Risk:** You may need to revise established color schemes when tools surface major warnings, which can affect visual consistency across a product [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Assuming a palette is “colorblind safe” without running a CVD simulation check.
- **Why it fails:** CVD can make intended distinct colors look similar; simulation/testing is required to verify distinguishability [@datawrapper_how_your] [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Testing in only one tool (or only one CVD mode) and stopping after a quick glance.
- **Why it fails:** Chartability’s heuristic explicitly requires using tools like Viz Palette or Chroma and avoiding major warnings; incomplete checks can miss problematic pairings [@susielu_viz_palette] [@vis4_chromajs_colour] [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Two or more categories/series become hard to tell apart when colors are viewed under CVD simulations.
- **The Test:** Load the palette into Viz Palette or the Chroma.js palette helper and review the CVD simulation output; the palette must not produce major warnings in either tool [@susielu_viz_palette] [@vis4_chromajs_colour] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace problematic colors with alternatives until Viz Palette or Chroma no longer issues major warnings for the palette [@susielu_viz_palette] [@vis4_chromajs_colour].
- **Best Fix:** Redesign the chart’s palette in Viz Palette or Chroma using iterative CVD simulation checks, then re-apply the validated palette consistently across the visualization [@susielu_viz_palette] [@vis4_chromajs_colour] [@elavskyHowAccessibleMy2022].
