---
id: use-event-striping-to-count-outliers-per-interval
title: Use event striping when users must count outliers per interval
bibliography: references.bib
description: Highlight outliers explicitly to improve accuracy when users compare
  how many unusual points occur in each interval.
labels:
- chart:time-series
- task:count
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- complexity:intermediate
---

## Highlight outliers explicitly when outlier count is the target judgment <!-- role: advice -->

When users must decide which interval contains the most outliers, use a design that explicitly marks outliers as distinct visual events rather than requiring viewers to infer them from the underlying value encoding.

## Why explicit outlier marking improves outlier numerosity judgments <!-- role: reason -->

Counting outliers combines summary understanding (what is unusual) with numerosity (how many). Making outliers salient reduces the need for viewers to decide from subtle deviations and supports more reliable counting and comparison across intervals.

**Mechanism:** Visual boosting of outliers increases salience and separability, supporting numerosity estimation across intervals.

**Evidence:** In the outlier-count task, the outlier-highlighting design significantly outperformed all other tested encodings in accuracy for identifying which month had the most unusual days [@albersTaskdrivenEvaluationAggregation2014a].

**Notes:** Enhancements tuned for outliers can reduce performance on other summary tasks even if the base encoding looks similar.

## When this applies <!-- role: context -->

- **User Goal:** Identify which interval has the greatest number of unusual observations.
- **Task:** Outlier numerosity comparison across bins (e.g., months).
- **Data:** Time series with occasional unusual points; users care about frequency of anomalies.
- **Chart Setting:** Static review, monitoring summaries, or quick diagnostic comparisons.
- **Audience:** General readers; outlier described as “unusual” may be more interpretable.
- **Success Criterion:** High accuracy for “most outlier days” interval selection.

## When not to follow this <!-- role: exceptions -->

**Break it when:** Users primarily need other summaries (like average or spread) and outliers are secondary. **Why:** The outlier-focused design underperformed more general encodings for several non-outlier summary tasks in the evaluated set [@albersTaskdrivenEvaluationAggregation2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** General-purpose summary readability for non-outlier tasks.\
**Risk:** Users may overweight outliers and neglect broader context if the highlighting is dominant.\
**Mitigation:** Ensure the context layer remains visible enough to interpret outliers in relation to baseline behavior.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a distribution-summarizing encoding and expecting it to support outlier counting without explicit outlier marks. **Why it fails:** Outlier counting benefited most from explicit outlier mapping rather than general summarization [@albersTaskdrivenEvaluationAggregation2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users disagree on what qualifies as “unusual” and cannot consistently count.\
**Quick Check:** Verify that each outlier is visually distinct as a separate mark and does not merge into adjacent events.\
**Stronger Test:** Run a small accuracy test where the difference in outlier counts between the top intervals is small (e.g., one or two outliers) and confirm performance remains acceptable.

## What to do instead <!-- role: fix -->

- Use an outlier-focused encoding that explicitly overlays outliers as distinct events.
- If users also need averages or spread, pair the outlier view with a separate summary view rather than overloading one display.
- Reduce reliance on viewers inferring outliers from subtle value differences by making the outlier layer the comparison target.
