---
id: avoid-stacked-bars-for-near-half-splits-when-estimation-must-be-unbiased
title: Avoid stacked bar charts for near-50/50 splits when unbiased value estimation
  matters
bibliography: references.bib
description: Stacked bars reduce overall error but systematically push remembered
  values away from the 50% midpoint.
labels:
- chart:bar
- task:estimate
- visual:length
- visual:position
- impact:accuracy
- data:proportional
- audience:general
- bias:categorical-repulsion
---

## Avoid midpoint-sensitive stacked bars for near-half estimates <!-- role: advice -->

Avoid using stacked bar charts when the key comparisons involve values near a 50/50 split and you need unbiased value readout. Use a display that does not visually integrate the value into a full 0–100% whole in a way that highlights an implicit midpoint.

## Categorical repulsion around implicit midpoints <!-- role: reason -->

Adding context that makes a value feel like “a proportion of a whole” encourages observers to encode it categorically (e.g., “below half” vs “above half”). That categorical boundary can bias memory and reproduction away from the midpoint, producing systematic underestimation just below 50% and overestimation just above 50%.

**Mechanism:** An implicit midpoint acts like a category boundary, and remembered values are repulsed away from that boundary during reproduction.

**Evidence:** In reproduction tasks, integrated (stacked) bars produced a repulsion pattern around the implicit 50% mark: values in 25–49% were reproduced lower (underestimated) while values in 51–75% were reproduced higher (overestimated) across multiple experiments. [@mccolemanNoMarkIsland2021]

**Notes:** This bias can coexist with reduced overall unsigned error in the integrated condition.

## When midpoint bias is consequential <!-- role: context -->

- **User Goal:** Read and communicate proportions without systematic bias.
- **Task:** Estimate a single value or judge whether it is slightly above vs slightly below half.
- **Data:** Percentages or part-to-whole values where many items fall near 50%.
- **Chart Setting:** Static reports/dashboards where viewers must read values quickly and may rely on memory.
- **Audience:** Any audience where “near half” distinctions can change decisions.
- **Success Criterion:** Estimates are not systematically shifted to exaggerate differences across the 50% boundary.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary goal is minimizing typical absolute error and the decision does not hinge on being unbiased around 50%. **Why:** Integrated context can improve overall accuracy even while introducing midpoint repulsion.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose some of the overall error reduction that comes from integrated part-to-whole context. **Risk:** Avoiding stacked bars can reduce the salience of “part of a whole” framing that some messages need. **Mitigation:** Ensure the alternative still communicates the intended whole without creating a strong midpoint boundary.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing a stacked bar specifically to help viewers “see the whole” for close-to-half values. **Why it fails:** The implicit midpoint can systematically push remembered estimates away from 50%, biasing near-half judgments.

## Quick tests <!-- role: check -->

**Failure Sign:** Values just under 50% tend to be interpreted as smaller than they are, while values just over 50% feel larger than they are. **Quick Check:** If your key story is “49% vs 51%” (or similar), treat stacked bars as high-risk. **Stronger Test:** Run a small reproduction pilot where viewers redraw or re-enter the value after a brief delay and check for opposite-signed bias on either side of 50%.

## What to do instead <!-- role: fix -->

- Use a non-integrated bar presentation for each value so it is not visually embedded as a part of a full stack.
- Separate the components so the viewer does not rely on an implicit midpoint boundary of a single integrated whole.
- Reduce reliance on memory by keeping the value visible during interaction or by adding explicit numeric readouts.
- If a part-to-whole framing is required, validate that your specific value range does not cluster near 50% before committing to a stacked design.
