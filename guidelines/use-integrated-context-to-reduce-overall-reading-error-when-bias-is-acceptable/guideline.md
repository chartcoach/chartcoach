---
id: use-integrated-context-to-reduce-overall-reading-error-when-bias-is-acceptable
title: Use Integrated Context to Reduce Overall Value Error (When Bias Is Acceptable)
bibliography: references.bib
description: Integrated context lowers overall unsigned error, but introduces systematic
  bias around the 50% boundary.
labels:
- chart:bar
- task:read-value
- visual:position
- impact:precision
- data:proportional
- audience:general
- tradeoff:precision-vs-bias
---

## The Rule <!-- role: advice -->

Use integrated, range-revealing context (e.g., stacked bars / dot-on-axis) when minimizing overall reading error matters more than avoiding systematic midpoint bias.

## The Logic <!-- role: reason -->

Adding context that conveys the full range (0–100%) improves overall accuracy (lower unsigned error), consistent with viewers leveraging categorical structure to boost precision. But it also introduces repulsion around an implicit 50% boundary.

- **The Principle:** Categorization can amplify precision while introducing systematic bias
- **The Evidence:** Integrated conditions had lower unsigned error across experiments, alongside a 50% repulsion pattern in signed error [@mccolemanNoMarkIsland2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Get reasonably accurate readings across the full scale, not specifically near 50%.
- **Data Type:** Percent/proportion displays spanning much of 1–99%.
- **Audience:** General audiences needing quick approximate readings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your message depends on faithful interpretation specifically around 50% (near ties).
- **Reason:** Integrated context systematically pushes values away from the midpoint (below-half underestimated; above-half overestimated) [@mccolemanNoMarkIsland2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You accept biased readings around the midpoint boundary.
- **The Risk:** Viewers may perceive a larger-than-true gap when values straddle 50%.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding integrated part-to-whole context and assuming it is “unambiguously more truthful.”
- **Why it fails:** The paper shows a precision–bias tradeoff: lower unsigned error but new systematic bias [@mccolemanNoMarkIsland2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Many values lie in the 25–75% range where the repulsion pattern shows up most clearly.
- **The Test:** Ask whether misreading 48% as “more like 45%” and 52% as “more like 55%” would change interpretation; if yes, avoid integrated context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep integrated context but avoid relying on near-50% judgments in the narrative (don’t hinge conclusions on tiny midpoint differences).
- **Best Fix:** If midpoint fidelity is required, switch to a presentation that does not induce the same integrated midpoint boundary effects [@mccolemanNoMarkIsland2021].
