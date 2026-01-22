---
id: use-circular-variants-to-reduce-response-time-in-part-to-whole-sorting
title: Use circular part-to-whole variants to reduce response time in part-to-whole
  sorting
bibliography: references.bib
description: In part-to-whole sorting/estimation tasks, circular variants are faster
  to read than pie, stacked bars, and treemaps.
labels:
- chart:pie
- chart:stacked-bar
- chart:treemap
- chart:part-to-whole
- task:sort
- visual:area
- visual:color
- impact:speed
- data:quantitative
- data:categorical
- audience:general
- comparison:chart-type
---

## Use circular part-to-whole variants for faster part-to-whole sorting <!-- role: advice -->

Use circular part-to-whole variants (circular slices or straight-line circular) when you want faster responses for part-to-whole sorting/estimation. Expect pie charts, stacked bars, and treemaps to take longer in this task setting.

## Why circular variants can be faster for the same judgment <!-- role: reason -->

Response time can vary substantially by chart type even when the underlying values and task framing are the same, so chart choice is a lever for speed as well as accuracy.

**Mechanism:** Some chart forms enable quicker perceptual extraction of a target slice’s share, reducing the time needed to produce a percentage estimate.

**Evidence:** For part-to-whole sorting/estimation, circular slices and straight-line circular were ranked fastest for time, and both were significantly faster than the pie chart (and also significantly faster than stacked bars and treemaps in the reported comparisons) [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

**Notes:** The time results are reported for the tested stimulus set and task framing and should be treated as task-scoped.

## Context for optimizing response time in part-to-whole judgments <!-- role: context -->

- **User Goal:** Answer part-to-whole percentage questions quickly.
- **Task:** Sort/estimate a part’s percent of the whole (part-to-whole judgment).
- **Data:** One quantitative measure divided into nominal categories (five parts in the evaluated setting).
- **Chart Setting:** Static chart with color hue to identify the queried slice.
- **Audience:** General audiences under time pressure or high-volume review.
- **Success Criterion:** Lower completion time for correct responses.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Accuracy is the overriding requirement and you cannot tolerate trading accuracy for speed in your specific context. **Why:** The fastest chart types are not uniquely identified as the most accurate for all comparisons in the extracted results.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Circular variants may be unfamiliar, which can be a barrier to adoption even if faster. **Risk:** Speed improvements may not transfer if your task is not part-to-whole estimation/sorting. **Mitigation:** Verify with a short, task-matched timing check using representative users.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming “familiar” charts (pie/stacked bar/treemap) are always the fastest for part-to-whole questions. **Why it fails:** In this task setting, the circular variants were faster than the more familiar options.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** People take noticeably longer to answer simple part-to-whole percentage questions than expected. **Quick Check:** Time a handful of users answering the same questions using your current chart and a circular variant; compare median times. **Stronger Test:** Run a small within-subject test with randomized question order and compare per-user normalized response time across chart types.

## Fix: What to do instead <!-- role: fix -->

- Replace pie/stacked bar/treemap with circular slices when response time is a primary success criterion.
- Try straight-line circular as an alternative circular form if you want a second fast option.
- Keep the number of parts and the prompting consistent when you compare chart types for timing.
- If adoption is a concern, introduce the circular variant alongside the current chart and measure whether time improves without unacceptable errors.
