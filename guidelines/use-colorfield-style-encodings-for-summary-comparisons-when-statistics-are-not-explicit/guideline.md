---
id: use-colorfield-style-encodings-for-summary-comparisons-when-statistics-are-not-explicit
title: Use color encodings that support visual summarization for summary comparisons
  (when statistics are not explicitly encoded)
bibliography: references.bib
description: Prefer color-based fields when viewers must compare aggregate properties
  without explicit computed summaries.
labels:
- chart:time-series
- task:compare
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- complexity:intermediate
---

## Choose color-based summarization when you cannot precompute the needed statistic <!-- role: advice -->

When you cannot or do not want to explicitly compute the needed summary statistic, use a color-based encoding that lets viewers visually summarize values within each interval.

## Why color-based summarization can beat line traces for summaries <!-- role: reason -->

Some summary judgments can be supported by preattentive or ensemble-style perception over a field of marks, where viewers form an overall impression of a region’s values. A line trace emphasizes precise point reading and shape, which can be less effective for extracting certain summaries without explicit computation.

**Mechanism:** Dense color encodings create a “field” that viewers can summarize over an interval, supporting ensemble judgments.

**Evidence:** For average comparison, a standard colorfield encoding outperformed a line graph encoding under the evaluated conditions, indicating better support for summary comparison without explicit mean encoding in the line graph [@albersTaskdrivenEvaluationAggregation2014a].

**Notes:** Not all summary tasks benefit equally; some summaries are better supported by explicit computed statistics.

## When this applies <!-- role: context -->

- **User Goal:** Compare interval-level summaries without requiring exact numbers.
- **Task:** Summary comparison (e.g., highest average) where explicit statistics may not be shown.
- **Data:** Many observations per interval; value distribution matters more than individual points.
- **Chart Setting:** Static overview where quick interval summarization is important.
- **Audience:** Readers who benefit from perceptual summarization rather than calculation.
- **Success Criterion:** Higher accuracy on summary comparisons without adding explicit statistics.

## When not to follow this <!-- role: exceptions -->

**Break it when:** Users must identify exact individual extrema or specific point values. **Why:** Color-based encodings underperformed position-based encodings for point comparison tasks like maxima/minima and range [@albersTaskdrivenEvaluationAggregation2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Precision for identifying specific individual values.\
**Risk:** Users may struggle to extract exact point-level facts from color alone.\
**Mitigation:** Pair with positional encodings or explicit statistics when point tasks are expected.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a colorfield and expecting accurate identification of the single maximum or minimum day. **Why it fails:** Color encodings were generally less accurate for those point-extrema tasks than position encodings [@albersTaskdrivenEvaluationAggregation2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users can describe “overall high vs low” intervals but fail at exact-point questions.\
**Quick Check:** Ask users to answer both an average question and an extrema question; if extrema accuracy collapses, the design is summary-oriented.\
**Stronger Test:** Run separate pilots for point and summary tasks to confirm the intended strength matches your task mix.

## What to do instead <!-- role: fix -->

- Add explicit per-interval statistics (such as mean) when summary comparisons must be accurate and unambiguous.
- Use a position-based encoding when point-level extraction is required.
- Use a composite view that preserves a positional trace while still supporting summary perception.
