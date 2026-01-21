---
id: use-moderate-ensemble-member-count-to-reduce-collocation-bias
title: Plot a Moderate Number of Ensemble Tracks to Reduce Overweighting of Any One
  Track
bibliography: references.bib
description: Increase plotted ensemble members enough to reduce the collocation effect,
  but avoid very dense displays that can create new misunderstandings.
labels:
- chart:ensemble
- task:assess-risk
- visual:density
- impact:reduce-bias
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## The Rule <!-- role: advice -->

When using ensemble hurricane tracks, plot more than a small handful of paths; prefer a moderate count (on the order of a few dozen) rather than very few.

## The Logic <!-- role: reason -->

- **The Principle:** When few tracks are shown, viewers implicitly assign more meaning to each individual line, so an intersecting line disproportionately increases judged damage (“collocation effect”).
- **The Evidence:** Increasing the number of plotted tracks reduced the collocation effect relative to a 9-track display, with the strongest reduction observed around the ~33-track condition; the effect was reduced but not eliminated [@padillaPowerfulInfluenceMarks2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Making comparative judgments about which of two specific locations is at greater risk/damage.
- **Data Type:** Static ensemble track display (multiple lines representing possible paths).
- **Audience:** Novices relying on the visualization as a primary decision input.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The display becomes too dense to visually parse (tracks visually merge, clutter obscures structure).
- **Reason:** Extremely dense displays can introduce other misconceptions and reduce perceivability [@padillaPowerfulInfluenceMarks2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** More lines increase clutter and may reduce readability of the distribution’s shape.
- **The Risk:** Too many lines can prompt users to think the visualization shows *all possible paths*, which can worsen interpretations in some cases [@padillaPowerfulInfluenceMarks2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Pushing to the maximum possible track count (e.g., very dense plots) assuming “more is always better.”
- **Why it fails:** In the 65-track condition, participants were more likely to believe the plot showed all possible paths, and those beliefs were associated with a larger collocation effect than in the 17- and 33-track conditions [@padillaPowerfulInfluenceMarks2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users report (in surveys or interviews) that the display “shows all possible paths.”
- **The Test:** Ask a comprehension question like “Does this show all possible paths?”; if many say yes, your track density may be too high for the intended interpretation [@padillaPowerfulInfluenceMarks2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of displayed members from very high counts until users no longer interpret the display as exhaustive.
- **Best Fix:** Tune the member count to a moderate, readable level and pair with brief messaging that the shown tracks are only a subset of many model runs [@padillaPowerfulInfluenceMarks2020].
