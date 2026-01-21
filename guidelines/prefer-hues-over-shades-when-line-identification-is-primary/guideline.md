---
id: prefer-hues-over-shades-when-line-identification-is-primary
title: Use Hues to Separate Entangled Lines
bibliography: references.bib
description: When the main task is tracking many overlapping lines, prefer distinct
  hues over sequential shades to keep lines distinguishable.
labels:
- chart:line
- task:track
- visual:color
- impact:readability
- data:temporal
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

In dense line charts where line identification is the priority, use distinct hues to keep lines visually separable—even if you could encode an order with shades.

## The Logic <!-- role: reason -->

In “entangled” line charts, shades are harder to tell apart and viewers don’t naturally expect hue-encoded categories to also carry an order. Distinct hues can improve line-tracking and reduce confusion when many lines overlap, trading off emphasis of ranking for the ability to follow individual series [@muth_quantitative_vs_qualitative_2021].

- **The Principle:** Optimize color for object tracking when series compete for attention
- **The Evidence:** [@muth_quantitative_vs_qualitative_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Follow specific lines across time (identify “Belgium vs UK” style series)
- **Data Type:** Many time series with crossings/overlap; “spaghetti” line charts
- **Audience:** General readers who need quick line-following rather than careful legend decoding

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary message is rank/order (e.g., highest-to-lowest) and that order is stable and can be made visually consistent.
- **Reason:** Shades can reinforce a stable ranking when the lines are ordered consistently, making the ordering easier to see [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You weaken cues about ordering (readers don’t expect ordered meaning from hues).
- **The Risk:** If hues are reused across facets/groups without clear labeling, viewers may mis-associate series or miss the intended ranking story [@muth_quantitative_vs_qualitative_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a sequential shade ramp to encode rank but expecting readers to notice the double-encoding in a tangled line chart.
- **Why it fails:** It’s hard to spot quickly that shades encode rank when lines overlap and readers are busy tracking shapes [@muth_quantitative_vs_qualitative_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers lose the line they’re following; multiple lines look interchangeable.
- **The Test:** Pick a series and trace it end-to-end in under 3 seconds. If you can’t, the colors aren’t distinct enough for tracking [@muth_quantitative_vs_qualitative_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace close lightness steps with more separated hues for the lines most likely to be compared.
- **Best Fix:** Reduce the number of lines shown or restructure (e.g., small multiples) so identification doesn’t depend on fine color differences [@muth_quantitative_vs_qualitative_2021].
