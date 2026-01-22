---
id: use-pie-charts-for-quarter-half-three-quarter-shares-not-fine-comparisons
title: Use pie charts for ~25/50/75% shares, not for fine comparisons
bibliography: references.bib
description: Prefer pie charts when the key values are near quarter, half, or three-quarter
  shares; otherwise choose bars for comparisons.
labels:
- chart:pie
- task:estimate
- task:compare
- visual:angle
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Use pie charts when key shares are around 25%, 50%, or 75% <!-- role: advice -->

Use a pie chart when the message hinges on recognizing approximate quarter, half, or three-quarter shares. If readers must compare similar shares or small differences, use a bar or column chart instead.

## Why pies help with quarters but hinder close comparisons <!-- role: reason -->

Pie charts make some benchmark proportions easy to spot, but they are a weak choice for judging small differences between categories.

**Mechanism:** Recognizable reference fractions (quarters/halves) can be visually inferred from the circle, while close values require more precise comparison than pie slices typically support.

**Evidence:** Values around 25%, 50%, or 75% are described as easier to spot in a pie chart than in stacked bars/columns, while pie charts are discouraged for comparing shares—especially when differences are small—where bars/columns are recommended instead [@muth_pie_charts_2018].

**Notes:** This is about the reader task (spotting benchmarks vs comparing close values), not about whether the data sums to 100%.

## When the reader needs to recognize benchmark proportions <!-- role: context -->

- **User Goal:** Quickly recognize whether a category is about a quarter, half, or three-quarters of the whole.
- **Task:** Estimate broad share sizes rather than discriminate between close values.
- **Data:** Part-to-whole data with a salient share near 25/50/75.
- **Chart Setting:** Editorial or explanatory contexts where a single key proportion is the takeaway.
- **Audience:** Broad audiences who benefit from quick, approximate judgments.
- **Success Criterion:** The reader can identify the “about half/quarter” story at a glance.

## When not to rely on pie slices for the job <!-- role: exceptions -->

**Break it when:** The reader’s goal is to compare category sizes (especially when differences are small). **Why:** Pie charts are not the best choice for comparing shares closely; bars/columns support that task better [@muth_pie_charts_2018].

## Tradeoffs of optimizing for benchmark recognition <!-- role: costs -->

**Sacrifice:** You may downplay precise ranking or small differences by choosing a pie. **Risk:** Readers may over-interpret tiny slice differences as meaningful. **Mitigation:** Use a comparison-friendly chart type when fine distinctions matter.

## Common comparison failures with pie charts <!-- role: mistakes -->

**Mistake:** Choosing a pie chart to help readers decide which of several similar shares is bigger. **Why it fails:** The chart type is poorly suited to comparing small differences between slices [@muth_pie_charts_2018].

## Quick checks for task-fit <!-- role: check -->

**Failure Sign:** The question you want readers to answer sounds like “Which category is larger?” or “How much larger is A than B?” **Quick Check:** If the main differences are small, treat that as a fail for pies. **Stronger Test:** Convert the same data to a bar chart and see if the intended comparison becomes immediately obvious.

## What to do instead when comparison is the goal <!-- role: fix -->

- Switch to a bar chart or column chart to support comparing shares directly.
- Use a stacked bar chart instead of a pie when you need the part-to-whole framing but also want easier comparisons.
- Emphasize the key value in text if the goal is primarily to communicate one number.
