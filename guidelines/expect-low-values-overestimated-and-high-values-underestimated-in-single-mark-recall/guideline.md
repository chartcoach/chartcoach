---
id: expect-low-values-overestimated-and-high-values-underestimated-in-single-mark-recall
title: Expect low values to be overestimated and high values to be underestimated
  in single-mark recall
bibliography: references.bib
description: When people reproduce a single bar or dot value from memory, small values
  drift upward and large values drift downward.
labels:
- chart:bar
- chart:dot
- task:estimate
- visual:position
- visual:length
- impact:trust
- impact:accuracy
- data:proportional
- audience:general
- bias:regression-to-middle
---

## Anticipate systematic compression of extremes in recall-based readouts <!-- role: advice -->

Assume that very small encoded values will tend to be reproduced too large, and very large encoded values will tend to be reproduced too small, when viewers rely on memory. Avoid designs where decisions depend on accurate recall of extreme values without additional cues.

## Extreme values drift toward the middle during reproduction <!-- role: reason -->

When reproducing a single magnitude after brief exposure, responses can show systematic bias patterns at the ends of the range. This creates a compression of extremes that can distort interpretations when low/high values are especially important.

**Mechanism:** Memory for magnitudes is biased, producing overestimation near the low end and underestimation near the high end of the scale.

**Evidence:** Across bar and dot reproduction experiments over 1–99% values, lower quartile values were overestimated relative to higher quartile values, which were underestimated, including comparisons of \<25% versus >75%. [@mccolemanNoMarkIsland2021]

**Notes:** This bias pattern is distinct from the midpoint repulsion effect that emerges with integrated context.

## When extreme-value fidelity is critical <!-- role: context -->

- **User Goal:** Correctly interpret unusually low or unusually high values.
- **Task:** Read a value and later recall or restate it.
- **Data:** Bounded numeric scales with meaningful extremes (near 0% or near 100%).
- **Chart Setting:** Dashboards, alerts, or reports where values may be glanced at and then used later.
- **Audience:** Decision-makers relying on quick reads rather than careful measurement.
- **Success Criterion:** Extremes remain extreme in users’ recalled understanding.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users can directly read values with persistent labels or the chart remains visible during decision-making. **Why:** The bias is demonstrated in a brief-view, memory-based reproduction paradigm.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Supporting extreme-value accuracy can add annotation or interaction complexity. **Risk:** Over-correcting for expected bias can introduce new distortions. **Mitigation:** Validate with a small reproduction study if extreme fidelity is mission-critical.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using unlabeled bars/dots for extreme values in workflows where users must remember the number later. **Why it fails:** Extremes tend to drift toward less extreme reproductions in recall.

## Quick tests <!-- role: check -->

**Failure Sign:** Users recall “about 10%” as larger than it was, or “about 90%” as smaller than it was. **Quick Check:** If the design depends on accurate recall of values in the lowest or highest quartile of the range, assume bias risk. **Stronger Test:** Run a timed view-and-reproduce check for representative extreme values and quantify signed error direction.

## What to do instead <!-- role: fix -->

- Add direct numeric labels for extreme values that must be remembered accurately.
- Keep the value visible while users perform downstream steps that depend on it.
- Provide persistent contextual anchors that support extreme interpretation (while checking for categorical repulsion near implicit boundaries).
- Reduce reliance on memory by co-locating extreme values with the decision or action they trigger.
