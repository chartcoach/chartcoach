---
id: use-appropriate-white-space-and-padding-for-interval-charts
title: Balance white space and mark spacing on interval charts to avoid overly thin
  marks or oversized gaps
bibliography: references.bib
description: Use padded, structured spacing so marks and groups are neither crowded
  nor excessively separated, preserving readability and interpretation.
labels:
- chart:bar
- task:compare
- visual:space
- impact:accessibility
- data:categorical
- audience:novice
- source:chartability
- category:perceivable
---

## Use balanced white space on interval charts <!-- role: advice -->

Balance white space and mark spacing on charts with intervals so bars (or other interval marks) are not extremely thin with large gaps, and not extremely thick with cramped gaps. Keep spacing structured so labels and groups remain easy to visually parse.

## Why spacing balance improves perceivability and understanding <!-- role: reason -->

When spacing is balanced, viewers can more easily separate groups, follow label-to-mark associations, and scan the plot without losing track of what is connected or comparable. When spacing is extreme (too sparse or too dense), the chart can become harder to perceive and interpret because the visual structure no longer supports how the information is chunked.

**Mechanism:** Balanced whitespace acts as visual punctuation that supports grouping and separation, improving readability and reducing interpretive effort.

**Evidence:** Whitespace is a critical design element that improves readability and clarity when balanced appropriately in data visualization layouts [@towardsdatascience_data_visualisation]. Whitespace guides the viewer’s eye, creates balance, and groups related items, improving readability rather than wasting space [@calliaweb_whitespace_not]. A synthesized accessibility heuristic set for data visualization includes “Spacing is inappropriate” as a Perceivable concern for charts with intervals because extreme gaps or cramped marks can create perceivable and understandable issues [@elavskyHowAccessibleMy2022].

**Notes:** This guidance targets spacing choices that alter how clearly marks, labels, and groups can be visually identified, rather than decorative whitespace.

## When to apply spacing checks in practice <!-- role: context -->

- **User Goal:** Identify categories, compare magnitudes, and understand groupings without misreading which labels belong to which marks.
- **Task:** Compare and scan across categories (and optionally across grouped/stacked series).
- **Data:** Categorical or binned/interval data with multiple marks arranged along an axis; can be moderate to high cardinality.
- **Chart Setting:** Static or interactive charts where layout and padding decisions affect the perceived structure, especially in dashboards or constrained containers.
- **Audience:** Mixed audiences, including readers who benefit from clear visual grouping and reduced cognitive load.
- **Success Criterion:** Marks and labels are easy to distinguish and associate; group structure is visually obvious; the chart is readable at intended display size.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The design intentionally prioritizes showing a very dense distribution of many intervals in a fixed-width container where separation cannot be increased. **Why:** Increasing whitespace would reduce the amount of information that can be shown within the available space.

## Tradeoffs of adding or reducing whitespace <!-- role: costs -->

**Sacrifice:** Balanced spacing may require more space or reduce the number of categories visible at once. **Risk:** Over-correcting spacing can either waste space (hurting overview) or compress information (hurting legibility). **Mitigation:** Treat spacing as a controllable layout parameter and validate it at the final rendering size used by the audience.

## Common spacing-related failure modes <!-- role: mistakes -->

- **Mistake:** Using very thin bars with large gaps for interval charts. **Why it fails:** Marks become hard to visually identify and compare, and the structure can look disconnected.
- **Mistake:** Packing bars so tightly that gaps and label associations become ambiguous. **Why it fails:** Crowding reduces readability and makes grouping and scanning harder.

## Quick tests for spacing problems <!-- role: check -->

**Failure Sign:** The chart feels either “spindly” (tiny marks separated by large empty space) or “cramped” (marks touch or nearly touch and labels look jammed). **Quick Check:** At the intended viewing size, see if you can quickly match several labels to their marks without pausing to trace or zoom. **Stronger Test:** Ask a colleague to do a fast comparison task (e.g., “which category is larger?”) and note whether they hesitate due to spacing/association confusion.

## Practical fixes for inappropriate spacing <!-- role: fix -->

- Adjust bar/interval width and inner padding so marks are clearly visible while still visually separated.
- Add or refine structural spacing (group padding, section breaks, or aligned label columns) so related items cluster and unrelated items separate.
- Reduce the number of categories shown at once (filter, aggregate, or paginate) if adequate spacing cannot be achieved in the available container.
- Provide an alternative representation (such as a readable table alongside the chart) when layout constraints prevent a clear, spaced visual structure.
