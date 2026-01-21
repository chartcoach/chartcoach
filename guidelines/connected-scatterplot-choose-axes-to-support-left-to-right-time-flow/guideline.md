---
id: connected-scatterplot-choose-axes-to-support-left-to-right-time-flow
title: Arrange Axes to Favor Left-to-Right Time Progression
bibliography: references.bib
description: Reduce directional confusion by selecting axis assignments that yield
  an overall left-to-right path.
labels:
- chart:scatter
- task:interpret
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- chart:connected-scatterplot
---

## The Rule <!-- role: advice -->

Choose which variable goes on x vs. y so the connected scatterplot’s overall trajectory progresses predominantly left to right across time.

## The Logic <!-- role: reason -->

A non-conventional global flow (e.g., prominent right-to-left stretches) is salient and can trigger “reverse chronological” interpretations; time-reversal errors were common when participants worked with connected scatterplots [@harozConnectedScatterplotPresenting2016].

- **The Principle:** Spatial-direction biases for reading sequences
- **The Evidence:** Participants noted surprise/confusion when time ran right-to-left in a connected scatterplot, and time reversals were the dominant qualitative error in tasks involving connected scatterplots [@harozConnectedScatterplotPresenting2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Follow the narrative of change over time.
- **Data Type:** Paired time series where axis assignment can change the path’s global direction.
- **Audience:** Readers accustomed to conventional left-to-right sequence representations.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The analytic or communicative goal depends on a specific axis assignment (e.g., you must place a specific variable on x for interpretability).
- **Reason:** Preserving the intended semantic mapping may outweigh the benefit of left-to-right flow [@harozConnectedScatterplotPresenting2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a more semantically “natural” axis assignment.
- **The Risk:** For some datasets, forcing left-to-right flow may not be feasible without other compromises.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a right-to-left global path and relying only on a caption to explain direction.
- **Why it fails:** Direction misunderstandings occurred even with exposure and in tasks that required careful reading [@harozConnectedScatterplotPresenting2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Large, prominent segments move right-to-left, or the path “backs up” across the x-axis repeatedly.
- **The Test:** Trace the path quickly with your finger; if you naturally start at the wrong end or reverse direction mid-way, reconsider axis assignment.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap x and y variables and see whether the global flow becomes predominantly left-to-right.
- **Best Fix:** If swapping is not acceptable, keep the mapping but strengthen direction cues and annotations to prevent reversed-time readings [@harozConnectedScatterplotPresenting2016].
