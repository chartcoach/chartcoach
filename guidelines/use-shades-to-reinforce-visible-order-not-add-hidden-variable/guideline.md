---
id: use-shades-to-reinforce-visible-order-not-add-hidden-variable
title: Use Shades to Reinforce Visible Order
bibliography: references.bib
description: Use sequential/diverging shades to emphasize an order that is already
  visible in the chart, and avoid using color as the only encoding for a new variable.
labels:
- chart:general
- task:rank
- visual:color
- impact:clarity
- data:ordered
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use sequential or diverging shades to emphasize an order that is already visible without color; avoid using shades as the only way to introduce an additional (new) variable.

## The Logic <!-- role: reason -->

Viewers can reliably interpret shades as “more/less” when the chart already shows the same ordering via another channel (position, size, or consistent ordering), making the color a reinforcing cue. When color alone encodes a new variable, the reader must decode the legend and mentally map color to value, which makes most charts slow and error-prone to read [@muth_quantitative_vs_qualitative_2021].

- **The Principle:** Prefer color as redundant (double) encoding for fast comprehension
- **The Evidence:** [@muth_quantitative_vs_qualitative_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** See ranking/ordering quickly (e.g., biggest to smallest, worst to best)
- **Data Type:** Ordered quantitative values; or categories with a meaningful underlying order you’re already showing
- **Audience:** Readers skimming; “quick to read” charts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Scatter plots where readers are accustomed to colored points and you provide strong “color keys” elsewhere (e.g., companion plots/legends that teach the colors).
- **Reason:** In some scatter plots, coloring by an additional variable can still work if it’s easy to spot what the shades encode and the visualization supports decoding [@muth_quantitative_vs_qualitative_2021].
- **Scenario:** You can double-encode the new variable elsewhere (not only by color).
- **Reason:** The blog notes a chart becomes easier when the meaning is reinforced (e.g., position plus shades) [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may give up the opportunity to encode an extra variable with color.
- **The Risk:** If ordering is inconsistent (e.g., line ranks change but shades stay assigned), readers can get confused about what the shades mean [@muth_quantitative_vs_qualitative_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning shades to categories while also expecting the same colors to serve as a category key.
- **Why it fails:** Readers don’t expect the same colors to do “two jobs” (identify category and encode an underlying ranking) [@muth_quantitative_vs_qualitative_2021].
- **The Wrong Fix:** Encoding annual performance or another summary only in color without any other cue.
- **Why it fails:** Color-only encoding makes the insight easy to miss, especially in already demanding chart types [@muth_quantitative_vs_qualitative_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** If you removed color (made everything gray), the intended ordering/variable disappears.
- **The Test:** Temporarily disable color. If the “message” collapses instead of being merely less prominent, you’re relying on color as the only encoding [@muth_quantitative_vs_qualitative_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Sort elements (bars/boxes/lines) so the ordered story is visible, then apply a matching shade ramp.
- **Best Fix:** If you truly need two variables, redesign to show the second variable with another channel or supporting chart (so color is not doing all the work) [@muth_quantitative_vs_qualitative_2021].
