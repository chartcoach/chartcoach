---
id: do-not-rely-on-error-bars-to-prevent-within-bar-bias
title: Do Not Assume Error Bars Eliminate Bar-Mean Misinterpretation
bibliography: references.bib
description: Error bars do not prevent viewers from treating the interior of a mean
  bar as more likely than equally distant values outside it.
labels:
- chart:bar
- task:communicate-uncertainty
- visual:error-bars
- impact:accuracy
- data:summary
- audience:general
- bias:within-the-bar
---

## The Rule <!-- role: advice -->

If you must show uncertainty, do not use error bars as a justification for keeping mean-as-bar encoding; change the mean encoding away from a filled bar.

## The Logic <!-- role: reason -->

The misinterpretation comes from the bar being perceived as a bounded visual object; adding error bars does not remove the “contained region” that draws attention and biases likelihood judgments toward values that lie within the filled rectangle.

- **The Principle:** Object boundaries drive attention and memory in a way that persists even when other statistical cues (like error bars) are present.
- **The Evidence:** The within-the-bar bias occurred for bar graphs both with and without error bars [@newmanBarGraphsDepicting2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding that values can plausibly occur on both sides of the mean.
- **Data Type:** Mean comparisons where uncertainty/variability is important enough to show error bars.
- **Audience:** Any audience making likelihood or risk inferences from the display [@newmanBarGraphsDepicting2012].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking viewers to reason about the likelihood of particular values around a mean (e.g., the only task is rough between-category ranking by central tendency).
- **Reason:** The documented failure mode is specifically about inferred likelihood/plausibility of values relative to the mean [@newmanBarGraphsDepicting2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** You increased design work because you must redesign the mean mark, not just “add error bars.”
- **The Risk:** If you keep bars and add more adornments, you may create a false sense of statistical correctness while leaving the perceptual bias intact [@newmanBarGraphsDepicting2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “We added symmetric error bars, so people will understand values above/below the mean equally.”
- **Why it fails:** Participants still favored within-bar values despite bidirectional error bars intended to emphasize symmetry [@newmanBarGraphsDepicting2012].

## How to Check <!-- role: check -->

- **Visual Sign:** A filled bar still defines a clear interior region up to the mean, even if whiskers extend above and below.
- **The Test:** Remove the error bars mentally—if the core mark is still a filled rectangle to the mean, the bias mechanism remains [@newmanBarGraphsDepicting2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep the uncertainty depiction but replace the filled bar mean with a point mean.
- **Best Fix:** Redesign so the mean is not a bounded filled object anchored to one axis, while uncertainty remains visible without implying “containment” [@newmanBarGraphsDepicting2012].
