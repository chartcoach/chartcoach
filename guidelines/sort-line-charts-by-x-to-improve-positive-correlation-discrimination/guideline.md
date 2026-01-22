---
id: sort-line-charts-by-x-to-improve-positive-correlation-discrimination
title: Use ordered (x-sorted) line charts to improve positive-correlation discrimination
  versus unsorted line charts
bibliography: references.bib
description: Sorting by X in a line chart improves JND-based correlation discrimination
  compared with an unsorted line chart for positive correlations.
labels:
- chart:line
- task:compare
- visual:order
- impact:accuracy
- data:quantitative
- audience:practitioner
- technique:sorting
---

## Sort points by X when using a line chart to judge positive correlation strength <!-- role: advice -->

If you use a line chart to support correlation discrimination, order the series by the X value (an ordered line chart) rather than using an arbitrary or original order when the goal is comparing positive correlations.

## Why ordering changes correlation-discrimination precision in line-based charts <!-- role: reason -->

Line-based charts impose an explicit order that can either reveal or obscure the relationship between X and Y. Sorting by X aligns the line’s progression with the underlying bivariate relationship, producing clearer cues for correlation strength and reducing JND.

**Mechanism:** Ordering can transform the visible structure from noise-like oscillations into a smoother monotonic trend, enabling finer discrimination of correlation differences.

**Evidence:** For positively correlated data, ordered line charts significantly outperformed standard line charts in JND-based correlation discrimination [@harrisonRankingVisualizationsCorrelation2014a]. Ordered line charts were also one of the few chart types in the study to show relatively symmetric performance across correlation directions compared to many other forms [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** The paper also found the negative line-chart condition to be unreliable under the tested method, so this guidance is most strongly supported for positive correlations.

## When ordered line charts are appropriate <!-- role: context -->

- **User Goal:** Compare correlation strength using a line-based representation.
- **Task:** Decide which of two relationships is more positively correlated.
- **Data:** Two quantitative variables that can be sorted by X without violating the meaning of the display.
- **Chart Setting:** Static displays where the chart’s order is not already semantically fixed (unlike time series).
- **Audience:** General audiences who need strong visible cues.
- **Success Criterion:** Lower JND than an unsorted line chart for the same r range.

## When not to sort by X in a line chart <!-- role: exceptions -->

**Break it when:** The line’s order has semantic meaning that must be preserved (for example, a fixed sequence inherent to the data). **Why:** Sorting would change what the line represents, even if it improves correlation discrimination.

## Tradeoffs of sorting for correlation discrimination <!-- role: costs -->

**Sacrifice:** Sorting changes the apparent narrative/sequence of the line, which may conflict with other goals for the chart. **Risk:** Viewers may infer an unintended sequence meaning from the ordered line. **Mitigation:** Treat ordered line charts as a correlation-judgment tool rather than a sequence-explanation tool.

## Common mistakes when using line charts for correlation <!-- role: mistakes -->

- **Mistake:** Using an unsorted line chart to communicate correlation strength between two variables. **Why it fails:** The imposed order can introduce visual noise that worsens discrimination precision.
- **Mistake:** Assuming that any line-based chart is suitable for correlation judgments. **Why it fails:** The paper shows large performance differences across line variants and sign conditions, including unreliable performance in some cases.

## Quick checks for whether sorting is helping <!-- role: check -->

**Failure Sign:** The line appears highly jagged and viewers cannot agree which display is more correlated. **Quick Check:** Compare ordered vs unordered versions and confirm the ordered version yields a visibly smoother trend for higher correlations. **Stronger Test:** Run a small forced-choice comparison study to estimate JND differences between ordered and unordered line charts for your target r range.

## What to do instead if sorting is not allowed <!-- role: fix -->

- Switch to a scatterplot for correlation discrimination tasks.
- Use the paper’s Weber-model ranking to select an alternative chart with lower predicted JND for your sign and r range.
- Limit correlation communication to coarse categories rather than fine discrimination when order cannot be changed.
- Provide a separate correlation-focused view (ordered for analysis) alongside an order-preserving line chart (for sequence meaning).
