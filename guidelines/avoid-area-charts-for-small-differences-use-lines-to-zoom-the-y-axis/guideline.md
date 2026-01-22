---
id: avoid-area-charts-for-small-differences-use-lines-to-zoom-the-y-axis
title: Avoid area charts for tiny differences; use a line chart so the y-axis can
  be zoomed
bibliography: references.bib
description: When differences are small, prefer a line chart that can use a non-zero
  y-axis to make variation readable.
labels:
- chart:area
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:foundational
---

## Use lines instead of areas when differences are small <!-- role: advice -->

Avoid area charts when the differences between values are very small, and use a line chart so the vertical scale can be set to make the differences visible.

## Area charts typically require a zero baseline that flattens subtle change <!-- role: reason -->

Area encodings rely on filled height, which is commonly anchored at zero, making small variations hard to see; lines can be shown with a tighter vertical range that makes subtle differences legible.

**Mechanism:** A compressed dynamic range reduces discriminability; increasing the effective slope/vertical resolution supports faster detection of change.

**Evidence:** Area charts are recommended for considerably large differences; for small differences, a line chart is recommended because its y-axis does not need to start at zero and can be stretched to show tiny differences [@muth_area_charts_2018].

**Notes:** This is about making variation readable, not about changing the underlying data.

## When this applies <!-- role: context -->

- **User Goal:** Notice small changes over time.
- **Task:** Detect subtle trend differences or small fluctuations.
- **Data:** Time series where series vary within a narrow band relative to their absolute level.
- **Chart Setting:** Editorial or analytical contexts where small changes are meaningful.
- **Audience:** Readers who need to see fine-grained variation without misreading a flat area.
- **Success Criterion:** Small but meaningful changes are visually apparent without exaggerating the story.

## When not to follow this <!-- role: exceptions -->

**Break it when:** Differences are large enough that the trend is clear even with a zero baseline and you also need to show a meaningful total plus shares. **Why:** In that case, the area encoding remains readable and aligned with the message [@muth_area_charts_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the “mass”/filled-area cue that some audiences find intuitive for totals. **Risk:** A tightened y-axis can be perceived as exaggerating change if not clearly labeled. **Mitigation:** Make axis labeling and context explicit so readers understand the scale choice [@muth_area_charts_2018].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a stacked area chart where all bands look nearly flat. **Why it fails:** The zero-baseline area encoding hides the small differences the reader is supposed to notice [@muth_area_charts_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The chart looks almost like a rectangle even though the text discusses variation. **Quick Check:** If you must squint to see change, the area chart is too insensitive for the effect size. **Stronger Test:** Replot as lines with a tighter y-axis range and confirm the intended differences become immediately visible [@muth_area_charts_2018].

## What to do instead <!-- role: fix -->

- Replace the area chart with a line chart and adjust the y-axis range to reveal small differences [@muth_area_charts_2018].
- Reduce the number of series shown to the few that matter most for the subtle comparison [@muth_area_charts_2018].
- Use annotations to point to the small changes you need readers to notice [@muth_area_charts_2018].
