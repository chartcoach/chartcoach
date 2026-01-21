---
id: choose-interpolation-as-a-tradeoff-between-truthfulness-and-usefulness
title: Choose Interpolation to Match Your Message
bibliography: references.bib
description: "Select an interpolation that fits what you want readers to notice\u2014\
  outliers vs. geographic patterns\u2014while acknowledging the truthfulness\u2013\
  usefulness tradeoff."
labels:
- chart:choropleth
- task:communicate
- visual:color
- impact:integrity
- data:quantitative
- audience:general
- complexity:advanced
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Pick the interpolation that best supports your intended takeaway (outliers vs. broad regional patterns), and do not choose a more dramatic interpolation solely to increase contrast. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Different interpolations change how color contrast maps to numeric differences; more “diversifying” interpolations can make moderate differences look big and extreme differences look small, altering what feels important to the reader. [@muth_interpolation_2022]

- **The Principle:** Perceptual emphasis shifts with nonlinear mapping
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Communicating a clear, honest visual argument with a choropleth (or similar color-mapped chart)
- **Data Type:** Quantitative data where distribution shape influences interpretability (especially skew and outliers)
- **Audience:** General audiences susceptible to interpreting “darker = much worse” without reading numeric detail [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your objective is explicitly rank-based (e.g., “top 20% vs. rest”) rather than magnitude-based.
- **Reason:** In rank-framing, a quantile-style interpolation aligns with the question being asked. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may accept a less visually dramatic map to avoid overstating differences.
- **The Risk:** If you optimize too far for “truthfulness” (e.g., strict linear), you may hide patterns readers need to see for the article’s purpose. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always using the interpolation with the most cuts (e.g., deciles) because it “looks better.”
- **Why it fails:** It can mislead by inflating contrast in dense ranges and compressing contrast among high outliers. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Very different numeric values appear nearly the same color at the high end, while modest differences near the center look dramatically different.
- **The Test:** Pick three regions: a true outlier, a high-but-not-outlier, and a typical value; compare numeric differences vs. perceived color differences to see whether the interpolation matches your narrative emphasis. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** If outliers look too similar, reduce quantile intensity (e.g., deciles → quintiles/quartiles) or revert to linear. [@muth_interpolation_2022]
- **Best Fix:** Create two candidate maps (one linear, one distribution-aware), decide which better matches the article’s point, and ensure the legend/annotation makes the intended reading unambiguous. [@muth_interpolation_2022]
