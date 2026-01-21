---
id: turn-donut-small-multiples-into-equal-scale-bars-or-table
title: Unroll Donut Small Multiples into Equal-Scale Bars in a Table
bibliography: references.bib
description: Replace hard-to-compare donut small multiples with equal-scale mini bars
  in a table to enable clear within- and between-group comparisons.
labels:
- chart:table
- chart:bar
- task:compare
- task:part-to-whole
- visual:position
- impact:clarity
- data:categorical
- audience:general
- series:fix-my-chart
---

## The Rule <!-- role: advice -->

Convert donut small multiples showing percentages into equal 0–100% stacked bars placed in a table so readers can compare categories within and across groups.

## The Logic <!-- role: reason -->

Stacked bars on a common linear scale support faster, more accurate comparisons than repeated circular segments, and a table layout supports both row-wise (within one group) and column-wise (across groups) scanning, as described in Datawrapper’s “Turning donuts into bars” fix.

- **The Principle:** Prefer linear, common-scale encodings for comparison and enable two-direction scanning via tabular layout.
- **The Evidence:** Rose Mintzer-Sweeney’s redesign replaces state-by-state donuts with 0–100 mini bars in a table to make comparisons easier within and between states [@mintzer_donuts_into_bars_2025].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare composition (poor/fair/good shares) within a group and differences in shares across many groups.
- **Data Type:** Many categories (e.g., states) each with percentages that sum to 100%.
- **Audience:** Broad/public audiences who need quick lookups and straightforward comparisons [@mintzer_donuts_into_bars_2025].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need to show one or two groups, not many.
- **Reason:** The table+mini-bars structure is primarily justified by the need to compare across many groups; for very few groups, the added structure may be unnecessary [@mintzer_donuts_into_bars_2025].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loses the “donut” aesthetic and any compact circular motif.
- **The Risk:** A table format can feel more “dense” and may require scrolling/pagination when there are many groups [@mintzer_donuts_into_bars_2025].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep the donuts and just tweak colors or add more annotations to “make them interesting.”
- **Why it fails:** The core problem remains: “every one of these donuts looks the same,” and readers still can’t easily compare slices across many donuts [@mintzer_donuts_into_bars_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Many donuts look nearly identical at a glance, and it’s hard to tell which groups differ without careful reading.
- **The Test:** Try answering: “Which state has the highest fair share?” If you can’t do it quickly from the chart, you need a common-scale bar/table approach [@mintzer_donuts_into_bars_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the donut small multiples with 0–100% stacked bars (still one per group) so segments align on a common baseline.
- **Best Fix:** Put those 0–100 mini stacked bars into a table so readers can scan across rows and down columns for comparisons, matching the approach in [@mintzer_donuts_into_bars_2025].
