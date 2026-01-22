---
id: use-area-charts-only-for-temporal-change-in-totals-and-shares
title: Use area charts only to show how a total and its parts change over time
bibliography: references.bib
description: Use area charts for temporal trends where the overall total and the composition
  (shares) both matter.
labels:
- chart:area
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:foundational
---

## Use area charts only to show temporal development of totals and shares <!-- role: advice -->

Use an area chart only when you need to show how values develop over time and you also care about how the total and its component shares change.

## Area charts encode both composition and total height at once <!-- role: reason -->

Stacked areas communicate two messages simultaneously: the full stack height (the total) and the thickness of each band (each share), which can be appropriate when both are intended to be read together.

**Mechanism:** The cumulative stack creates a salient “total” silhouette while the internal bands show how contributions evolve across time.

**Evidence:** Area charts are presented as most suitable when the goal is to show how a total and its shares develop over time, and as a weaker choice for non-temporal category comparisons [@muth_area_charts_2018].

**Notes:** If the total is not intended to be read, the stacked structure adds decoding work without adding meaning.

## When this area-chart rule applies <!-- role: context -->

- **User Goal:** Understand how a whole changes over time and how components contribute to that whole.
- **Task:** Track trends in both overall total and composition.
- **Data:** Time series with multiple components per time point (often summing to a meaningful total, sometimes 100%).
- **Chart Setting:** Static or lightly annotated explanatory charts where the reader scans for overall pattern more than exact values.
- **Audience:** General audiences who benefit from an intuitive “part-to-whole over time” display.
- **Success Criterion:** Readers can correctly describe both the overall trend and the changing mix of components.

## When not to follow this <!-- role: exceptions -->

**Break it when:** You want to compare category sizes across non-time categories (or mainly compare categories with each other). **Why:** Area charts are recommended specifically for change over time; other chart types support categorical comparison more directly [@muth_area_charts_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Precise comparisons between interior bands become harder than in simpler encodings. **Risk:** Readers may focus on the overall shape and miss the intended comparison between components. **Mitigation:** Keep the message centered on “total + composition over time,” not fine-grained cross-series comparisons [@muth_area_charts_2018].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using an area chart to show how values differ across categories that are not time. **Why it fails:** The chart type is tuned to temporal interpretation, and categorical differences are more directly readable with bar/column variants [@muth_area_charts_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers ask “why is this stacked?” or try to compare categories instead of reading change over time. **Quick Check:** Remove the time axis—if the chart’s purpose collapses, it likely belongs to a different chart family. **Stronger Test:** Ask a colleague to summarize the main takeaway in one sentence; if they describe category ranking rather than temporal change, reconsider the chart type [@muth_area_charts_2018].

## What to do instead <!-- role: fix -->

- Use a (stacked) bar or column chart when the goal is to compare sizes across categories rather than show change over time [@muth_area_charts_2018].
- Use split bars if you need a clearer part-to-whole comparison at a small number of category positions [@muth_area_charts_2018].
- Use a line chart when the focus is on trends over time but the total stack is not meaningful [@muth_area_charts_2018].
