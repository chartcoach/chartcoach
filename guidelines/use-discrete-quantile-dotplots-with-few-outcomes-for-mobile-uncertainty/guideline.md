---
id: use-discrete-quantile-dotplots-with-few-outcomes-for-mobile-uncertainty
title: Use low-count quantile dotplots to communicate predictive uncertainty on small
  screens
bibliography: references.bib
description: Improve the precision and confidence of probability judgments by showing
  a small number of evenly spaced quantile outcomes as dots.
labels:
- chart:dotplot
- task:estimate
- visual:position
- impact:accuracy
- data:uncertainty
- audience:novice
- platform:mobile
---

## Prefer low-count quantile dotplots for probability judgments <!-- role: advice -->

When you need users to estimate chances of arriving before/after a time on a mobile screen, show uncertainty as a quantile dotplot with a small number of dots (low outcome count). Use evenly spaced quantiles so the dotplot is stable and countable.

## Discrete outcomes support frequency-style reasoning without animation <!-- role: reason -->

A small set of discrete outcomes allows users to translate “probability” into “how many dots,” which supports interval estimation by counting and can be done quickly when stacks stay small.

**Mechanism:** Using quantiles creates a consistent discrete representation of a continuous predictive distribution, and a low number of dots keeps groups countable (especially in tails), supporting more self-consistent probability estimates.

**Evidence:** In a controlled experiment on realtime transit prediction scenarios, a low-count dotplot condition (dotplot-20) reduced variance in probability estimates by about 1.15× compared to density plots and also increased user confidence, while higher-count dotplots did not show the same advantage [@kayWhenIshMy2016].

**Notes:** The benefit depends on keeping the number of outcomes small; overly dense discrete marks can be read like continuous density/area instead of being counted.

## Glanceable, space-constrained uncertainty for arrival-time decisions <!-- role: context -->

- **User Goal:** Assess schedule risk/opportunity (e.g., “Will it arrive within 10 minutes?”) quickly.
- **Task:** Estimate cumulative probability for a threshold time, or probability of an interval.
- **Data:** Continuous predictive distributions (often skewed) for arrival times.
- **Chart Setting:** Mobile list views with many items; limited row height; static (non-animated) displays.
- **Audience:** Non-expert users making in-the-moment decisions.
- **Success Criterion:** Lower variance (more consistent probability estimates) and higher user confidence.

## When not to do this <!-- role: exceptions -->

**Break it when:** You require very fine-grained probability resolution across the full distribution in a single view. **Why:** Low-count dotplots trade distribution smoothness for countability and may under-resolve subtle shape differences.

## Tradeoffs of low-count dotplots <!-- role: costs -->

**Sacrifice:** Smooth depiction of density shape and some visual elegance. **Risk:** Some users may find dotplots less visually appealing than density-based encodings. **Mitigation:** Use dotplots where estimation consistency matters most, and consider offering an alternative view if aesthetics is a primary product constraint.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a very high dot count (e.g., ~100) and expecting users to count precisely. **Why it fails:** Users may stop counting and revert to area/density heuristics, removing the precision advantage.
- **Mistake:** Generating dots from random draws each time. **Why it fails:** Sampling noise changes the dot pattern across refreshes, making the representation inconsistent and harder to trust.

## Quick tests <!-- role: check -->

**Failure Sign:** Users describe the dotplot as “a density shape” and rarely reference counting dots for tail probabilities. **Quick Check:** Check typical vertical stacks; if stacks commonly exceed a small handful of dots, countability is likely degraded. **Stronger Test:** Run a probability-estimation task (threshold questions) and compare the variance of responses across encodings.

## What to do instead <!-- role: fix -->

- Use evenly spaced quantiles (inverse cumulative distribution) to place dots deterministically.
- Reduce the number of dots until vertical stacks remain small enough to count comfortably.
- If you must show a smoother shape, switch to a density plot and accept slightly higher variance in user probability estimates.
