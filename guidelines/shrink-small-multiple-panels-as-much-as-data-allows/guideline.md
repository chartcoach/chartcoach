---
id: shrink-small-multiple-panels-as-much-as-data-allows
title: Shrink Small Multiple Panels Aggressively
bibliography: references.bib
description: Make small-multiple panels as small as readability allows, especially
  when there are few data points.
labels:
- chart:line
- task:overview
- visual:layout
- impact:clarity
- data:temporal
- audience:general
- chart:small-multiples
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Make small multiple line-chart panels as narrow and short as you can without losing readability; use smaller panels when there are fewer data points.

## The Logic <!-- role: reason -->

Small multiples are meant to be compact; readers can efficiently perceive variation in position and pattern even at small sizes, so shrinking panels can increase scannability and reduce scrolling [@muth_small_multiple_line_charts_2024].

- **The Principle:** Compact display supports quick pattern scanning
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan many category trends quickly
- **Data Type:** Time series per category, especially with few time points
- **Audience:** General readers, including mobile users

## When to Break It <!-- role: exceptions -->

- **Scenario:** Each panel needs detailed reading (dense time points, many annotations, or subtle changes).
- **Reason:** Over-shrinking can make lines and labels illegible, undermining comprehension [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less room for labels and annotations inside each panel.
- **The Risk:** Panels become too small to read comfortably, especially if you keep too much text [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping panels large by default without testing smaller sizes.
- **Why it fails:** The chart becomes tall and scroll-heavy, making it harder to scan across many categories [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The small multiple chart feels like a long page of repeated large charts.
- **The Test:** Gradually reduce panel height/width; stop only when labels/lines become meaningfully harder to read [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce panel height and/or width and simplify in-panel text.
- **Best Fix:** Re-size panels based on data-point count (fewer points → smaller panels) and re-check readability on mobile [@muth_small_multiple_line_charts_2024].
