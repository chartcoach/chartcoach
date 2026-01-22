---
id: prefer-continuous-scales-when-neighbor-comparison-needs-nuance
title: Use a continuous choropleth color scale when comparing neighboring regions
  requires nuance
bibliography: references.bib
description: Continuous scales preserve small differences that discrete class breaks
  can hide, while tooltips can provide exact values.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:precision
- data:quantitative
- audience:general
- interaction:tooltip
---

## Choose a continuous color scale when discrete bins would hide important variation <!-- role: advice -->

Use a continuous choropleth color scale when you want readers to see fine differences between nearby regions that might fall into the same discrete class. If readers need exact numbers, provide tooltips rather than adding more bins.

## Continuous encoding preserves gradient information <!-- role: reason -->

Discrete steps compress a range of values into a small set of categories, which improves quick bin recognition but removes within-bin differences. Continuous scales keep those differences visible, supporting comparisons between adjacent regions while still allowing exact values through interaction.

**Mechanism:** Continuous scales maintain a one-to-one mapping between value changes and color changes, avoiding artificial boundaries created by bins.

**Evidence:** Discrete steps help readers see which range a value falls into, but they “sacrifice nuance,” while continuous scales let readers compare neighboring regions even if discrete steps would assign them the same shade; tooltips can provide exact values anyway [@muth_choroplethmaps_2018].

**Notes:** Continuous scales are most effective when the palette has a clear lightness progression.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Compare regions that are close in value, especially neighbors.
- **Task:** Detect smooth gradients or subtle local contrasts.
- **Data:** Quantitative values with meaningful small differences.
- **Chart Setting:** Interactive maps where tooltips can reveal exact values.
- **Audience:** Readers who will explore locally rather than only scan for broad bins.
- **Success Criterion:** Neighboring regions with different values look different without needing many legend categories.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary need is quick identification of which predefined range each region belongs to. **Why:** Discrete steps make ranges immediately legible in the legend [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Continuous legends can be less immediately “categorical” for range lookup. **Risk:** Small color differences may still be hard to see if the palette has weak lightness contrast. **Mitigation:** Ensure strong lightness progression and offer tooltips for certainty.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using discrete bins for data where within-bin differences matter (e.g., neighbors are close but not equal). **Why it fails:** It hides nuance and can make distinct regions appear identical [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Adjacent regions with different values appear the same color in important areas. **Quick Check:** Sample several neighboring pairs and see whether value differences are visually detectable. **Stronger Test:** Ask a reader to identify which of two neighboring regions is higher without using the tooltip; if they frequently can’t, continuous or improved contrast is needed.

## What to do instead <!-- role: fix -->

- Switch from discrete steps to a continuous color scale for the choropleth.
- Strengthen the palette’s lightness progression so small differences are visible.
- Enable tooltips to provide exact values without forcing many discrete classes.
- Use a non-map chart if precise ranking across many regions is the primary task.
