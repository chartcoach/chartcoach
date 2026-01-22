---
id: do-not-use-color-alone-to-encode-meaning-in-charts
title: Encode categories with a redundant non-color channel whenever color carries
  meaning
bibliography: references.bib
description: If color encodes meaning in a chart, add at least one other visual channel
  so the information remains interpretable without color.
labels:
- chart:scatter
- task:identify
- visual:color
- impact:accessibility
- data:categorical
- audience:novice
- standard:wcag
---

## Use redundant encodings when color carries meaning <!-- role: advice -->

When color conveys meaningful or essential information in a chart, also encode that same information with a non-color channel so the message does not depend on color perception. For categorical color schemes, use textures, shapes, size (for filled marks), or dash patterns (for lines and paths) in addition to color [@elavskyHowAccessibleMy2022].

## Redundant channels preserve meaning without color perception <!-- role: reason -->

Encoding meaning in color alone makes the chart’s semantics inaccessible when viewers cannot reliably perceive color differences, so they lose the ability to interpret categories, status, or prompts. Adding a redundant channel preserves the mapping between data and marks even when color cues are unavailable or ambiguous.

**Mechanism:** A second, independent visual cue (pattern/shape/size/dash) provides an alternate route to discriminate categories or states when hue differences are not perceivable, preventing loss of information.

**Evidence:** Information must not be conveyed by color alone; additional cues such as patterns, shapes, or text must be provided so the content remains understandable without color perception [@w3c_understanding_use]. Adding patterns or shapes alongside color can preserve categorical distinctions in charts when color differences are insufficient, illustrated with chart examples using redundant encodings [@observablehq_no_use; @elavskyHowAccessibleMy2022].

**Notes:** This guideline targets meaning and essential distinctions (e.g., categories or states), not purely decorative color.

## When color is part of the data encoding <!-- role: context -->

- **User Goal:** Identify or distinguish which category, group, or state a mark belongs to.
- **Task:** Match legend entries to marks, compare categories, or notice a changed/selected/alert state.
- **Data:** Categorical groups encoded by color (or any essential status/meaning signaled by color).
- **Chart Setting:** Any static or interactive chart where the legend or state cues rely on color.
- **Audience:** Mixed audiences, including people who cannot perceive color differences reliably.
- **Success Criterion:** The same categories/states can be correctly identified without relying on color.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Color is not encoding any meaningful or essential information (it is purely decorative). **Why:** There is no semantic loss if color cannot be perceived [@elavskyHowAccessibleMy2022].

## Tradeoffs of redundant non-color encodings <!-- role: costs -->

**Sacrifice:** Additional encodings can increase visual complexity and reduce aesthetic simplicity. **Risk:** Overuse of textures/shapes can clutter dense plots and make patterns hard to parse. **Mitigation:** Keep the redundant channel consistent and limited to the elements where color carries meaning [@elavskyHowAccessibleMy2022].

## Common ways this fails in charts <!-- role: mistakes -->

- **Mistake:** Using only a color legend to distinguish categories with no other cues. **Why it fails:** Category identity becomes unavailable when color differences cannot be perceived [@w3c_understanding_use; @elavskyHowAccessibleMy2022].
- **Mistake:** Indicating interactive state or status (e.g., selected/alert) only by changing color. **Why it fails:** The state change may be invisible without reliable color perception, so users miss essential feedback [@w3c_understanding_use; @elavskyHowAccessibleMy2022].

## Quick ways to detect color-only meaning <!-- role: check -->

**Failure Sign:** If you remove or ignore color, categories or states become indistinguishable. **Quick Check:** Temporarily view the chart without relying on color cues and see whether categories/states can still be identified via patterns, shapes, size, or dashes [@elavskyHowAccessibleMy2022]. **Stronger Test:** Verify that every meaning conveyed by color is also conveyed by at least one other channel across all categories and relevant states [@w3c_understanding_use; @elavskyHowAccessibleMy2022].

## Practical alternatives to color-only encoding <!-- role: fix -->

- Add textures/pattern fills to categorical areas or bars so each category remains distinguishable without color [@observablehq_no_use; @elavskyHowAccessibleMy2022].
- Add shape variation for categorical points (e.g., different marker shapes) alongside color [@observablehq_no_use; @elavskyHowAccessibleMy2022].
- Use dash patterns for categorical lines or paths alongside color [@elavskyHowAccessibleMy2022].
- Add direct text labels for categories or states when patterns/shapes would be too dense to interpret [@w3c_understanding_use; @elavskyHowAccessibleMy2022].
