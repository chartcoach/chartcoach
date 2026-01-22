---
id: expect-higher-relative-error-when-estimating-a-middle-slice-than-the-largest-slice
title: Expect higher relative error when estimating a middle slice than the largest
  slice in part-to-whole judgments
bibliography: references.bib
description: Part-to-whole percentage estimates are less accurate when users must
  judge a middle-sized slice rather than the largest slice.
labels:
- chart:part-to-whole
- task:sort
- visual:area
- visual:angle
- impact:accuracy
- data:quantitative
- data:categorical
- audience:general
- custom:slice-of-interest
---

## Plan for lower accuracy when the question targets a middle slice <!-- role: advice -->

Assume part-to-whole judgments will be less accurate when users must estimate a middle-sized slice rather than the largest slice. If your workflow routinely asks about non-largest slices, treat additional error as a baseline expectation.

## Slice-of-interest changes error in part-to-whole estimation <!-- role: reason -->

Even with the same chart type and number of parts, which slice is being queried changes the difficulty of estimating its share, and that difficulty shows up as higher relative error.

**Mechanism:** Middle slices are smaller and closer in magnitude to neighboring slices than the largest slice, which increases ambiguity during percent estimation and leads to larger relative errors.

**Evidence:** Relative absolute error was significantly higher for questions targeting the middle slice than for questions targeting the largest slice in part-to-whole percentage judgments across the tested charts (with the circular slice chart being an exception noted in the results visualization) [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about expected accuracy differences by slice queried, not about which chart type is best.

## Context: When slice-of-interest affects expected error <!-- role: context -->

- **User Goal:** Estimate the percent share of a specified category.
- **Task:** Part-to-whole percentage judgment, especially when the queried category is not the largest.
- **Data:** Categorical parts summing to a whole, with at least one middle-sized category of interest.
- **Chart Setting:** Static part-to-whole display where a single slice is highlighted by color.
- **Audience:** General audiences.
- **Success Criterion:** Predictable error bounds and reliable interpretation.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Your use case always queries the largest slice (or only asks which slice is largest). **Why:** The observed error increase is tied to querying a middle slice instead of the largest.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Accepting this expectation may require additional validation or tolerance bands in downstream decisions. **Risk:** Overgeneralizing can lead you to assume poor accuracy even when a particular chart design mitigates it. **Mitigation:** Validate with a small task-matched check for the specific slice positions your users care about.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Treating all part-to-whole questions as equally easy regardless of which slice is asked about. **Why it fails:** Relative error differs systematically between “largest slice” and “middle slice” questions in the evaluated setting.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users are consistent on “largest slice” questions but inconsistent on “middle slice” percent estimates. **Quick Check:** Compare absolute percent errors for largest-slice versus middle-slice prompts on the same dataset. **Stronger Test:** Stratify evaluation by slice rank (largest vs middle) and compare relative absolute error distributions.

## Fix: What to do instead <!-- role: fix -->

- Separate evaluation (or acceptance thresholds) for largest-slice versus middle-slice questions.
- If middle slices are decision-critical, run a targeted accuracy check that only uses the slice ranks your users will be asked about.
- Reframe the task so users answer about the largest slice when that is compatible with the decision.
- Add process safeguards (like requiring a second check) when decisions depend on a middle-slice percent estimate.
