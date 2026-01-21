---
id: use-diverging-colormaps-cautiously-around-the-midpoint
title: Use Diverging Colormaps Cautiously for Midpoint-Straddling Comparisons
bibliography: references.bib
description: Diverging colormaps can increase errors when users compare values that
  cross the neutral midpoint.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- colormap:diverging
---

## The Rule <!-- role: advice -->

If users must compare which value is closer to a reference near the center, avoid diverging colormaps that force comparisons across the midpoint hue boundary.

## The Logic <!-- role: reason -->

- **The Principle:** Midpoint boundaries can induce erroneous grouping by hue/chroma (chromatic vs achromatic), distorting perceived distances.
- **The Evidence:** The blueorange diverging colormap performed similarly to its component single-hue halves when all colors were on one side, but showed increased errors when triplets straddled the central blue–orange boundary; participants often favored similarly-hued saturated colors over nearer achromatic ones [@liuSomewhereRainbowEmpirical2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two values is closer to a reference when values can fall on opposite sides of a central reference (e.g., “near zero”).
- **Data Type:** Quantitative data mapped to a diverging scale with a neutral midpoint.
- **Audience:** General users performing relative comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary task is to emphasize direction relative to the midpoint (above vs below) more than distance.
- **Reason:** The paper’s finding targets distance judgments; diverging schemes may still be appropriate when sign/direction is the key message [@liuSomewhereRainbowEmpirical2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a strong visual cue for “two-sidedness” around a central reference.
- **The Risk:** Replacing diverging with sequential can reduce immediate recognition of positive vs negative regions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a diverging palette for general quantitative similarity tasks just because the data has a “middle.”
- **Why it fails:** Comparisons that cross the midpoint can become systematically error-prone due to the hue boundary effect observed [@liuSomewhereRainbowEmpirical2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Values just across the midpoint look “more different” than equally spaced values on the same side, or users mis-pick the closer value near the center.
- **The Test:** Construct triplets where the correct answer is the neutral/achromatic color near the midpoint and the incorrect answer is a farther but more saturated same-hue option; if users often choose the saturated option, you’re seeing the midpoint boundary problem [@liuSomewhereRainbowEmpirical2018a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce tasks requiring fine distance judgments across the midpoint (e.g., provide separate comparisons within each side).
- **Best Fix:** Use a sequential colormap for similarity judgments, reserving diverging colormaps for tasks explicitly about deviation direction from a reference [@liuSomewhereRainbowEmpirical2018a].
