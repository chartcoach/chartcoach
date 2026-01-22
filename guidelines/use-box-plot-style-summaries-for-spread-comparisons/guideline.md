---
id: use-box-plot-style-summaries-for-spread-comparisons
title: Use box-plot-style interval summaries to compare spread
bibliography: references.bib
description: Prefer interval summary graphics that encode distributional spread (such
  as interquartile range) when users compare variability across intervals.
labels:
- chart:box-plot
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- complexity:intermediate
---

## Use an interval summary that encodes spread when spread is the question <!-- role: advice -->

When users must decide which interval has the most spread (variability around its average), use an interval summary display that explicitly encodes spread using a distributional statistic.

## Why explicit spread proxies improve spread judgments <!-- role: reason -->

Spread judgments are difficult when viewers must infer variability from raw traces or fields. A summary statistic that correlates with spread, encoded directly per interval, reduces the need for mental estimation and makes comparisons more reliable.

**Mechanism:** Directly encoded distribution width provides an immediate comparison cue for variability across intervals.

**Evidence:** In the spread-comparison experiment, the encoding that explicitly provided a spread-related statistic per month (interquartile range) achieved the highest accuracy among tested encodings for that task [@albersTaskdrivenEvaluationAggregation2014a].

**Notes:** Some designs can support spread through visual summarization, but explicit distributional encodings performed best in this task.

## When this applies <!-- role: context -->

- **User Goal:** Identify the interval with greatest variability around its typical level.
- **Task:** Compare spread across fixed bins (e.g., months).
- **Data:** Many values per interval; spread is not equivalent to range.
- **Chart Setting:** Users must answer under limited viewing time; exact computation is infeasible.
- **Audience:** General readers; wording like “most spread out from the monthly average” may be used.
- **Success Criterion:** Higher accuracy on variability comparisons across intervals.

## When not to follow this <!-- role: exceptions -->

**Break it when:** The audience needs to see the raw within-interval temporal pattern rather than a distribution summary. **Why:** Interval summaries can hide shape and sequencing information [@albersTaskdrivenEvaluationAggregation2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Loss of within-interval temporal order and local pattern details.\
**Risk:** Users may interpret the summary as the full story and miss important structure.\
**Mitigation:** Provide an additional view or layer that preserves raw series context if needed.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using only a raw line graph and expecting reliable “most spread out” answers. **Why it fails:** Spread comparison was difficult without an explicit spread-related mapping, and the best-performing approach encoded a spread proxy directly [@albersTaskdrivenEvaluationAggregation2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users confuse “spread” with “range” or “maximum.”\
**Quick Check:** Ask users to explain their choice; if they cite extremes rather than variability, the display is not supporting spread.\
**Stronger Test:** Include control questions where range and spread are decorrelated and check whether answers track spread.

## What to do instead <!-- role: fix -->

- Use an interval summary graphic that encodes a spread-related statistic per interval.
- Keep the comparison unit consistent with the question’s binning (e.g., monthly spread shown monthly).
- Add a second view of the raw series when temporal order within the interval is also important.
