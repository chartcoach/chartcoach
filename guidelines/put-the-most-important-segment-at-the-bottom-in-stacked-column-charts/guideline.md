---
id: put-the-most-important-segment-at-the-bottom-in-stacked-column-charts
title: Put the most important segment at the bottom of a stacked column chart
bibliography: references.bib
description: Place the key segment on a shared baseline to make it easy to compare
  across columns, and use color to emphasize it.
labels:
- chart:stacked-column
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Place the key segment at the bottom and emphasize it with color <!-- role: advice -->

Put the most important segment at the bottom of each stacked column and use color to make it visually prominent.

## Why bottom placement improves comparison <!-- role: reason -->

Only the bottom segment in a stacked column chart consistently starts from the same baseline across categories, so it supports more accurate comparisons than segments placed higher in the stack.

**Mechanism:** A shared baseline allows direct visual comparison of segment lengths; color emphasis guides attention to the intended segment.

**Evidence:** Readers can compare values more easily when they share a baseline, so the most important segment should be placed at the bottom and highlighted with color [@muth_stacked_columns_2018].

**Notes:** Emphasis should support the intended reading order, not compete with it.

## When this applies <!-- role: context -->

- **User Goal:** Compare one segment across multiple totals.
- **Task:** Identify which categories have more or less of the key component.
- **Data:** Multiple totals with a designated “main” segment.
- **Chart Setting:** Any stacked column chart where one segment carries the message.
- **Audience:** Readers scanning quickly; color may be the primary attention cue.
- **Success Criterion:** The key segment is the easiest segment to compare across columns.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The most important segment is the second most important comparison and you are using a 100% stack with a deliberate second baseline at the top. **Why:** In that setup, the top baseline can also support strong comparisons for a specific segment [@muth_stacked_columns_2018].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Reordering segments can reduce consistency with other charts or domain conventions. **Risk:** Color emphasis can overpower other information if too saturated or too many hues are used. **Mitigation:** Keep the emphasis focused on the single segment that supports the main point.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Leaving the key segment in the middle or top of the stack. **Why it fails:** It loses the shared baseline, making comparisons unnecessarily hard [@muth_stacked_columns_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The segment you want compared is floating and readers must trace its start position in each column. **Quick Check:** Ask “Which segment do I want compared?” and confirm it touches the baseline. **Stronger Test:** Have someone compare that segment between two columns without using tooltips; if they struggle, reposition it [@muth_stacked_columns_2018].

## What to do instead <!-- role: fix -->

- Reorder the stack so the key segment is the bottom segment across all columns.
- Use color to highlight only the key segment and mute the others.
- If multiple segments must be compared, switch to split bars or small multiples.
- Add direct labels for the key segment to reduce reliance on legend lookups.
