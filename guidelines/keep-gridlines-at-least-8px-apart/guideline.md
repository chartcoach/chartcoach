---
id: keep-gridlines-at-least-8px-apart
title: Keep gridlines at least 8 px apart to avoid interference
bibliography: references.bib
description: Dense gridlines increased error sharply at small chart heights; spacing
  of at least ~8 pixels avoided the worst interference.
labels:
- chart:line
- task:compare
- visual:luminance
- impact:accuracy
- data:quantitative
- audience:general
- custom:component-gridlines
---

## Space gridlines so adjacent lines are at least 8 pixels apart <!-- role: advice -->

When adding gridlines, avoid packing them so closely that adjacent gridlines are less than about 8 pixels apart. If the chart is short, reduce the number of gridlines rather than keeping fine spacing.

## Why overly dense gridlines can hurt reading accuracy <!-- role: reason -->

When gridlines are too dense relative to chart height, they create visual clutter and make it harder to trace data marks to their referenced values, increasing comparison error.

**Mechanism:** High-frequency reference patterns compete with data marks and hinder accurate alignment.

**Evidence:** In crowdsourced comparison tasks, error increased steeply in the condition with a 40-pixel chart height and 10-unit gridline spacing, and results suggested gridlines should be separated by at least 8 pixels to avoid interference [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** Moderate gridline additions improved accuracy overall, but excessively dense gridlines at small sizes were harmful.

## When this applies <!-- role: context -->

- **User Goal:** Compare values using gridlines as reading aids.
- **Task:** Estimate differences between marked values.
- **Data:** Quantitative values on a fixed scale.
- **Chart Setting:** Small charts or dashboards where gridlines are optional.
- **Audience:** General audiences.
- **Success Criterion:** Improved comparison accuracy without clutter.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Gridlines are the primary carrier of information (e.g., a ruled background used for a specific measurement task). **Why:** You may accept clutter to meet that specialized requirement.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Fewer gridlines reduce the number of reference anchors. **Risk:** Too sparse gridlines can make interpolation harder for some users. **Mitigation:** Use a small number of well-chosen gridlines plus clear axis ticks.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding many gridlines to “increase precision” in a very short chart. **Why it fails:** Dense gridlines can impede tracing and increase error.

## Quick tests <!-- role: check -->

**Failure Sign:** The grid visually dominates or creates a striped background. **Quick Check:** Measure pixel distance between adjacent gridlines; if it is under ~8 pixels, reduce the count. **Stronger Test:** Compare user error with dense vs sparse gridlines at your deployed chart height.

## What to do instead <!-- role: fix -->

- Use fewer gridlines (larger spacing) while keeping key reference values.
- Increase chart height if dense gridlines are truly necessary.
- Emphasize axis ticks/labels and de-emphasize gridlines.
- Provide interactive readouts for exact values instead of relying on dense gridlines.
