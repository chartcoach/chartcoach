---
id: separate-adjacent-stacked-segments-to-reduce-part-of-whole-bias
title: Insert a gap between adjacent stacked segments when you want pure segment-to-segment
  comparisons
bibliography: references.bib
description: Separating adjacent stacked segments can reduce bias and error in segment
  height comparisons that otherwise trigger part-to-whole judgments.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- chart:stacked-bar
- bias:part-to-whole
---

## Add separation between adjacent stacked segments for height-ratio judgments <!-- role: advice -->

If viewers must compare two stacked segments as a pure height ratio, insert a gap (or an intervening segment) so the compared segments are not directly adjacent. Avoid placing the two compared segments immediately on top of each other when accuracy matters.

## Adjacency in a stack can trigger part-to-whole bias <!-- role: reason -->

When two compared segments are adjacent within a single stack, viewers may default to part-to-whole reasoning, producing biased estimates; separating the segments reduces this bias and improves accuracy.

**Mechanism:** Direct adjacency promotes interpreting the two segments as composing a whole, shifting judgments toward part-to-whole proportions rather than the intended segment-to-segment ratio.

**Evidence:** In divided/stacked bar comparisons, separating the compared bars by an intervening bar reduced absolute error, and the large negative bias seen for adjacent comparisons was substantially attenuated when the compared bars were not adjacent. [@talbotFourExperimentsPerception2014; @zengReviewCollationGraphical2023]

**Notes:** This guideline targets situations where the intended judgment is segment-to-segment, not composition.

## Context: When this applies <!-- role: context -->

- **User Goal:** Compare two stacked components as a ratio (A relative to B), not A relative to (A+B).
- **Task:** Percent-of-height estimation between two marked segments in a single divided/stacked bar.
- **Data:** Quantitative values encoded as stacked segment lengths.
- **Chart Setting:** Divided/stacked bars where two compared segments would otherwise be adjacent.
- **Audience:** General audiences prone to using quick heuristics.
- **Success Criterion:** Lower bias and lower absolute error in the ratio judgment.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The intended message is explicitly part-to-whole composition within a single stack. **Why:** Introducing gaps/intervening elements can undermine the gestalt of a single whole and confuse composition reading.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adding gaps or intervening segments can increase chart height/space or complicate stacking. **Risk:** Viewers may misread gaps as missing data or separate groups. **Mitigation:** Use clear labeling or consistent gap semantics across the chart.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Asking for a segment-to-segment ratio while placing the two target segments adjacent in the same stack. **Why it fails:** Adjacency increases bias consistent with part-to-whole interpretation.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** People answer closer to a part-to-whole proportion than the true segment-to-segment ratio when segments are adjacent. **Quick Check:** Compute both ratios (A/B and A/(A+B)) and see which one user answers resemble. **Stronger Test:** Compare adjacent vs. separated segment layouts with the same questions and measure bias.

## Fix: What to do instead <!-- role: fix -->

- Insert a visible gap or an intervening segment between the two compared segments.
- Move one of the compared values into a separate aligned comparison view.
- Reframe the task explicitly as part-to-whole if that is the true intent.
- Show the two compared segments as separate bars to eliminate adjacency-driven composition cues.
