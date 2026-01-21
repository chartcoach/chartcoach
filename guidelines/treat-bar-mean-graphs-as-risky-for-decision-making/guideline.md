---
id: treat-bar-mean-graphs-as-risky-for-decision-making
title: Avoid Mean-Bar Graphs When Decisions Depend on Interpreting Plausible Values
bibliography: references.bib
description: Mean-as-bar displays can shift downstream decisions by making within-bar
  deviations feel more plausible than outside-bar deviations.
labels:
- chart:bar
- task:decide
- visual:area
- impact:decision-making
- data:summary
- audience:general
- domain:risk
- bias:within-the-bar
---

## The Rule <!-- role: advice -->

Do not use bar graphs of means in decision contexts where users must choose actions based on which side of a mean seems more plausible.

## The Logic <!-- role: reason -->

Because viewers over-weight values that lie “within” the bar, the display can push them toward choices consistent with the bar’s anchored direction rather than with the underlying (symmetric) information.

- **The Principle:** Perceptual interpretation of a bounded bar biases inferred likelihood, which then propagates into decisions.
- **The Evidence:** In a CEO decision scenario, rising vs. falling mean bars (with identical mean information) shifted participants toward increasing vs. decreasing the parameter relative to a no-graph control [@newmanBarGraphsDepicting2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Choosing an action (increase vs. decrease, accept vs. reject) based on interpretation of variability around a mean.
- **Data Type:** Summary statistics where the mean alone does not justify directional action.
- **Audience:** Decision-makers in applied settings (the demonstrated effect occurred in an applied, managerial framing) [@newmanBarGraphsDepicting2012].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The decision is truly about a one-sided quantity from a fixed baseline (so directionality of fill is meaningful and intended).
- **Reason:** The paper’s concern is that directionality is *not* warranted by mean information, yet the bar display induces it [@newmanBarGraphsDepicting2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need alternative displays or additional explanation rather than a familiar bar chart.
- **The Risk:** If stakeholders insist on bars, decisions may be biased by the graphical form rather than the underlying evidence [@newmanBarGraphsDepicting2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the mean bar and assuming “people won’t base real decisions on that subtle perception.”
- **Why it fails:** The paper demonstrates a measurable shift in downstream decision outputs caused by the bar’s directionality [@newmanBarGraphsDepicting2012].

## How to Check <!-- role: check -->

- **Visual Sign:** A mean is shown as an axis-anchored bar in a context where the viewer might interpret “safer” or “better” as moving up vs. down.
- **The Test:** Show two versions (rising vs. falling bar depicting the same mean) and see whether recommendations flip; if so, the display is driving the decision [@newmanBarGraphsDepicting2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the bar and show the mean as a point while keeping the same narrative and scale.
- **Best Fix:** Use a visualization that does not create a within-bar region that privileges one side of the mean, especially when decisions hinge on perceived plausibility above vs. below the mean [@newmanBarGraphsDepicting2012].
