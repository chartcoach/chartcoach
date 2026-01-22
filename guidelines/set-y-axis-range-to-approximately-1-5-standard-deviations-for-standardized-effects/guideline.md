---
id: set-y-axis-range-to-approximately-1-5-standard-deviations-for-standardized-effects
title: Set the y-axis range to about 1.5 standard deviations when readers must judge
  standardized effect size
bibliography: references.bib
description: "Use a y-axis span of roughly 1\u20132 SDs (about 1.5 SD) so the visual\
  \ size of an effect matches its standardized magnitude."
labels:
- chart:bar
- chart:line
- task:estimate
- visual:position
- impact:clarity
- impact:trust
- data:quantitative
- audience:novice
- custom:effect-size
---

## Use a ~1.5 SD y-axis span for standardized effect-size judgments <!-- role: advice -->

Set the y-axis range so it spans about 1.5 standard deviations (SDs) of the dependent variable when you want viewers to judge standardized effect size from the graph. Aim for a range in the neighborhood of 1–2 SDs rather than the minimum-possible range or the full possible scale.

## Visual-conceptual congruence from SD-scaled axes improves calibration <!-- role: reason -->

When the y-axis span is tied to the standard deviation, the plotted visual difference corresponds more closely to standardized effect size, so viewers can map “looks bigger” to “is bigger” without mentally rescaling from an arbitrary axis range.

**Mechanism:** A standardized axis reduces distortion from zooming (making small effects look large) and from overly wide axes (making meaningful effects look negligible), improving sensitivity to differences in effect magnitude while reducing systematic over- or underestimation.

**Evidence:** Across five experiments where participants categorized effects (none/small/medium/big), sensitivity to effect size was higher and bias was lower when the y-axis range was set to an SD-based span (roughly 1–2 SD total) compared with axes showing the full 0–100 range or the minimal range that just fit the data [@wittGraphConstruction2019]. Standardized ranges around ~1.5 SD produced much less “everything is small” bias than full-range axes and much less “everything is big” bias than minimal-range axes [@wittGraphConstruction2019].

**Notes:** The exact SD span varied across experiments (about 1.0–2.0 SD total), with the core benefit coming from using an SD-scaled range rather than a specific single number [@wittGraphConstruction2019].

## When effect-size comprehension from the graphic is the goal <!-- role: context -->

- **User Goal:** Judge how large an effect is (e.g., none/small/medium/large) from the visual impression.
- **Task:** Calibrate perceived magnitude to standardized effect size (such as Cohen’s d conventions).
- **Data:** Quantitative outcomes where standard deviation is meaningful for interpreting differences.
- **Chart Setting:** Static bar charts or line charts showing group means (with or without error bars).
- **Audience:** Readers who may not be expert graph interpreters (e.g., students, general scientific readers).
- **Success Criterion:** Higher sensitivity to differences in effect size and lower systematic bias in magnitude judgments.

## When not to treat ~1.5 SD as the default choice <!-- role: exceptions -->

- **Break it when:** Standard deviation is unknown, irrelevant, or not used to interpret effect size in your field. **Why:** An SD-based axis no longer aligns visual magnitude with the conceptual magnitude viewers are expected to use [@wittGraphConstruction2019].
- **Break it when:** A fixed SD-based span would exclude important uncertainty information (e.g., error bars) or require nonsensical values (such as negative values for a bounded performance measure). **Why:** The display would hide key information or imply impossible measurement values [@wittGraphConstruction2019].
- **Break it when:** Your primary need is consistent scaling across multiple figures for across-figure comparison and the SD-based range would vary too much from panel to panel. **Why:** Comparability across panels can be reduced if each panel uses a different SD-scaled span [@wittGraphConstruction2019].

## Tradeoffs of SD-based y-axis ranges <!-- role: costs -->

**Sacrifice:** You give up either maximal zoom (minimal-range axes) or maximal global context (full-range axes). **Risk:** Readers may misinterpret the graph if they assume the axis reflects the full feasible scale rather than an SD-scaled window around the mean. **Mitigation:** Indicate the SD-based span (in SD units) in the caption when the range is not self-evident [@wittGraphConstruction2019].

## Common ways SD-based scaling fails in practice <!-- role: mistakes -->

- **Mistake:** Using the software default “fit to data” (minimal range) for mean plots when the goal is to communicate effect magnitude. **Why it fails:** It biases viewers toward seeing effects as larger than they are and reduces calibrated magnitude judgments [@wittGraphConstruction2019].
- **Mistake:** Forcing a full 0–100 y-axis range for all plots of bounded outcomes when the goal is magnitude discrimination. **Why it fails:** It biases viewers toward judging most effects as null or small and reduces sensitivity to magnitude differences [@wittGraphConstruction2019].

## Quick checks for axis-range distortion <!-- role: check -->

**Failure Sign:** Most effects are judged “small” under a full-range axis, or “big” under a minimal-range axis, despite identical underlying data. **Quick Check:** Compare your current y-axis span to the dependent variable’s SD; if it is far larger than ~2 SD or far smaller than ~1 SD, expect magnitude distortion. **Stronger Test:** Pilot-test with representative readers using magnitude judgments (e.g., none/small/medium/big) on alternative axis ranges and compare sensitivity and bias [@wittGraphConstruction2019].

## Practical alternatives when ~1.5 SD cannot be used <!-- role: fix -->

- Center the y-axis on the grand mean and extend the range to fully include the uncertainty display (such as error bars), even if that requires going beyond ~1.5 SD [@wittGraphConstruction2019].
- Extend the SD-based range for unusually large effects so the full effect remains visible without clipping [@wittGraphConstruction2019].
- Add a caption note reporting the y-axis span in SD units when the plot omits error bars or when the scaling choice is not obvious from the axis alone [@wittGraphConstruction2019].
- Use a consistent SD-based scale across a set of related figures when cross-figure comparisons are a primary task, adjusting only enough to keep all key elements visible [@wittGraphConstruction2019].
