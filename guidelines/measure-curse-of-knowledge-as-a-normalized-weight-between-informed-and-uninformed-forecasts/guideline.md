---
id: measure-curse-of-knowledge-as-a-normalized-weight-between-informed-and-uninformed-forecasts
title: Quantify curse-of-knowledge bias as a normalized weight between uninformed
  and informed benchmarks
bibliography: references.bib
description: Measure how much an informed forecast of others is pulled toward the
  informed value using a unitless bias index.
labels:
- chart:none
- task:measure
- visual:none
- impact:diagnosis
- data:uncertainty
- audience:expert
- domain:behavioral-economics
- complexity:advanced
---

## Quantify bias as a weight between two benchmarks <!-- role: advice -->

Compute a curse-of-knowledge bias index by scaling the informed person’s estimate of the uninformed forecast between the uninformed benchmark and the informed benchmark. Use the resulting unitless value to compare bias across items with different numeric ranges.

## Normalization isolates the “pull” toward privileged information <!-- role: reason -->

Raw forecast errors are not comparable when items differ in scale; normalizing by the gap between what uninformed people would forecast and the informed value expresses bias as a fraction of the maximum possible “knowledge contamination.”

**Mechanism:** The index treats the uninformed forecast as 0% bias and the informed value as 100% bias, so movement toward the informed value directly reflects failure to ignore private information.

**Evidence:** Experiments operationalized curse-of-knowledge bias using an index equal to the difference between the informed subjects’ estimate of the uninformed mean forecast and the uninformed mean forecast, divided by the difference between the informed value (actual outcome) and the uninformed mean forecast; this index was used to compare individual vs. market bias and showed markets cut bias roughly in half [@camererCurseKnowledgeEconomic1989].

**Notes:** Index values can fall below 0 or above 1 in principle, indicating overshooting past either benchmark, though such cases were rare in the reported setting [@camererCurseKnowledgeEconomic1989].

## Contexts where you have informed and uninformed reference points <!-- role: context -->

- **User Goal:** Compare curse-of-knowledge magnitude across domains, items, or experimental conditions.
- **Task:** Convert estimates into a comparable bias metric.
- **Data:** For each item, you can observe (or estimate) an uninformed forecast, an informed value (e.g., true outcome known to informed subjects), and an informed subject’s estimate of the uninformed forecast.
- **Chart Setting:** Not a chart requirement; applies to analysis and reporting of judgment elicitation results.
- **Audience:** Researchers and practitioners diagnosing bias in pricing, forecasting-of-forecasts, or asymmetric-information judgments.
- **Success Criterion:** A stable, interpretable metric that supports cross-item aggregation and condition comparisons.

## Exceptions where the index is unstable or undefined <!-- role: exceptions -->

**Break it when:** The informed and uninformed benchmarks are equal or nearly equal. **Why:** The denominator becomes zero (or near zero), making the normalized index undefined or numerically unstable [@camererCurseKnowledgeEconomic1989].

## Costs of normalization <!-- role: costs -->

**Sacrifice:** You lose direct interpretability in original units (e.g., dollars per share). **Risk:** When denominators are small, the index can exaggerate small absolute deviations. **Mitigation:** Report denominators alongside the index so readers can see when scaling may be noisy.

## Mistakes in computing or interpreting the bias index <!-- role: mistakes -->

**Mistake:** Using the informed value alone as the “correct” target for the estimate of others’ beliefs. **Why it fails:** The task is to estimate the uninformed belief, and equating correctness with the informed value confounds accuracy with bias [@camererCurseKnowledgeEconomic1989].

**Mistake:** Comparing raw deviations across items with different scales instead of normalizing. **Why it fails:** Scale differences can dominate, masking whether estimates are proportionally pulled toward informed information [@camererCurseKnowledgeEconomic1989].

## Check whether the index is interpretable in your dataset <!-- role: check -->

**Failure Sign:** Many index values are extremely large in magnitude or flip sign due to tiny denominators. **Quick Check:** Inspect the benchmark gap (informed minus uninformed) for each item and flag near-zero gaps. **Stronger Test:** Recompute summaries excluding near-zero-gap items and verify conclusions are robust.

## Fixes when the benchmark gap is too small <!-- role: fix -->

- Exclude items with near-zero gaps between informed and uninformed benchmarks from normalized-bias comparisons.
- Group items by benchmark-gap magnitude and report bias separately by group.
- Use absolute-unit errors for small-gap items and normalized indices for large-gap items, keeping analyses separate.
- Redesign stimuli so the informed value differs meaningfully from the uninformed forecast, making bias measurable.
