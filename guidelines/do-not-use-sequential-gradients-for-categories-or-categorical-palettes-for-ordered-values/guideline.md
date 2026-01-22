---
id: do-not-use-sequential-gradients-for-categories-or-categorical-palettes-for-ordered-values
title: Do not use sequential gradients for categories, and do not use categorical
  palettes for ordered values
bibliography: references.bib
description: Match palette type to data type to avoid implying false order or hiding
  true order.
labels:
- chart:multi
- task:encode
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:basic
---

## Match palette type to whether the data are ordered or not <!-- role: advice -->

Use distinct hues for unordered categories, and use ordered lightness gradients for numeric or ranked values rather than assigning arbitrary categorical colors.

## Why palette–data mismatches mislead <!-- role: reason -->

Sequential shades imply ordering and magnitude, while categorical palettes imply distinct groups without order; using the wrong type causes readers to infer structure that is not present or miss structure that is.

**Mechanism:** Viewers interpret lightness changes as “more/less,” so shaded single-hue category palettes can create an unintended ranking signal.

**Evidence:** Using shades of one hue for categories implies ranking because dark is associated with more/high and bright with less/low, so categories should use different hues; conversely, gradient palettes are meant for ordered values rather than categories [@muth_colors_2018].

**Notes:** If some categories are intentionally emphasized via lightness or saturation, the chart should explain why they stand out.

## When this applies to palette selection <!-- role: context -->

- **User Goal:** Correctly interpret whether the variable is ordered or unordered.
- **Task:** Decode category membership versus magnitude.
- **Data:** Categorical variables (unordered) and quantitative/ordered variables (ordered).
- **Chart Setting:** Any chart or map where color is the primary encoding.
- **Audience:** General readers likely to apply “dark means more” heuristics.
- **Success Criterion:** The palette does not imply a false ranking and does not obscure real order.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Categories truly have an inherent order you want to communicate. **Why:** In that case, a sequential ramp can legitimately encode the intended ordering [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Distinct-hue categorical palettes can feel more colorful. **Risk:** Too many hues can reintroduce legend overload. **Mitigation:** Reduce the number of categories shown at once.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding categories with a single-hue light-to-dark ramp to “keep it subtle.” **Why it fails:** Readers infer an ordering that may not exist [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers ask whether darker categories “mean more.” **Quick Check:** Look at the palette without labels and ask whether it suggests order. **Stronger Test:** Convert the chart to grayscale; if categories become an apparent ranked sequence, the palette is implying order.

## What to do instead <!-- role: fix -->

- Switch categorical encodings to distinct hues so groups read as different, not ordered.
- Use a sequential ramp with monotonic lightness only for ordered values.
- Reduce category count or split into multiple views if distinct hues become too many.
- Add explicit explanation when any category is intentionally highlighted via saturation or lightness.
