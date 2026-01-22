---
id: expect-faster-responses-with-long-tail-than-fat-tail-in-part-to-whole-middle-slice-judgments
title: Expect faster responses with long-tail than fat-tail distributions in middle-slice
  part-to-whole judgments
bibliography: references.bib
description: For middle-slice part-to-whole judgments, long-tail distributions produce
  faster response times than fat-tail distributions.
labels:
- chart:part-to-whole
- task:sort
- impact:speed
- data:quantitative
- data:categorical
- custom:distribution-shape
- custom:long-tail
- custom:fat-tail
- audience:general
---

## Anticipate faster middle-slice judgments with long-tail value distributions <!-- role: advice -->

When users estimate a middle slice in part-to-whole charts, expect faster responses when the category values follow a long-tail distribution rather than a fat-tail (flatter) distribution. Use this expectation when setting timing benchmarks for user workflows.

## Distribution shape affects response time for the same part-to-whole task <!-- role: reason -->

How values are distributed across slices can change how quickly viewers can estimate a particular slice’s share, even if accuracy differences are not detectable.

**Mechanism:** Larger separations between slice sizes reduce the time needed to distinguish the target slice from its neighbors during estimation.

**Evidence:** For middle-slice part-to-whole estimation, response time differed significantly by distribution shape: long-tail distributions yielded faster mean response times than fat-tail distributions in the evaluated task [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

**Notes:** This is about timing, not accuracy; the extracted results did not show a significant accuracy difference between tail types for the middle-slice case.

## Context: When distribution shape matters for timing <!-- role: context -->

- **User Goal:** Answer part-to-whole percentage questions efficiently.
- **Task:** Estimate the percent share of a middle-ranked slice (not the largest).
- **Data:** Five-part breakdown where distributions can be long-tailed (uneven) or fat-tailed (flatter).
- **Chart Setting:** Static part-to-whole displays with a highlighted target category.
- **Audience:** General audiences completing many similar judgments.
- **Success Criterion:** Predictable response time / throughput.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Your task does not involve a middle-slice estimate (for example, you only ask about the largest slice and do not vary tail type). **Why:** The tail-type timing effect was tested in the middle-slice condition.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You cannot usually control real-world distribution shapes, so this is more useful for setting expectations than for designing the data. **Risk:** Using timing expectations as a proxy for correctness can be misleading because accuracy may not change with tail type in this setting. **Mitigation:** Track both time and error when evaluating a workflow.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming distribution shape will strongly change accuracy for middle-slice part-to-whole estimates. **Why it fails:** The extracted results did not show a significant difference in absolute or signed error between fat-tail and long-tail conditions.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users slow down noticeably on flatter distributions even though the chart style is unchanged. **Quick Check:** Compare median completion times on long-tail versus fat-tail examples for the same middle-slice prompt. **Stronger Test:** Collect per-user normalized response times and test whether long-tail cases remain faster for your audience and interface.

## Fix: What to do instead <!-- role: fix -->

- Set different time expectations (or service-level targets) for long-tail versus fat-tail datasets in part-to-whole middle-slice workflows.
- If throughput is critical on fat-tail cases, consider changing the workflow to reduce reliance on precise middle-slice estimation.
- Evaluate chart choices separately within each distribution regime rather than pooling timing results across all distributions.
- When reporting results, stratify performance by distribution shape so slower cases are not hidden in overall averages.
