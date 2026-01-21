---
id: add-brief-explanations-that-ensemble-lines-are-a-sample-not-deterministic
title: Explain That Displayed Tracks Are a Small Sample, Not Deterministic Paths
bibliography: references.bib
description: Use minimal instruction to reduce deterministic interpretations of individual
  ensemble lines in hurricane track displays.
labels:
- chart:ensemble
- task:interpret-uncertainty
- visual:annotation
- impact:reduce-bias
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## The Rule <!-- role: advice -->

Explicitly state that the tracks shown are only a small subset of many model outputs and that any single track is not very meaningful on its own.

## The Logic <!-- role: reason -->

- **The Principle:** Viewers may commit a deterministic construal error—treating probabilistic outputs as deterministic—leading them to overweight one track [@padillaPowerfulInfluenceMarks2020].
- **The Evidence:** “Visualization instructions” describing how ensembles are generated significantly reduced the collocation effect versus no instructions, though it did not eliminate it [@padillaPowerfulInfluenceMarks2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting what an ensemble track display means and making decisions based on it.
- **Data Type:** Uncertainty shown via multiple hurricane paths in a static image (common in print or brief broadcast contexts).
- **Audience:** General audiences with limited meteorological modeling knowledge.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your visualization already includes a mechanism that makes sampling vs. determinism unambiguous, and adding more text would overwhelm critical content.
- **Reason:** Additional explanation may add clutter without improving understanding in that specific design.

## The Price <!-- role: costs -->

- **The Sacrifice:** Takes time/space (or airtime) and may reduce immediate “glanceability.”
- **The Risk:** Users may still show the bias despite the explanation; instructions alone are not sufficient [@padillaPowerfulInfluenceMarks2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Only providing the ensemble plot without explaining how it was made.
- **Why it fails:** People can still treat individual lines as meaningful and show higher damage judgments for line-location overlap [@padillaPowerfulInfluenceMarks2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users interpret a location “on a line” as categorically more likely to be hit than an equidistant “off-line” location.
- **The Test:** Include a comprehension check asking whether touching a track increases likelihood compared to equidistant non-touching locations; high agreement indicates the misunderstanding persists [@padillaPowerfulInfluenceMarks2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a one-sentence caption: the lines are a small subset of many model runs; any one line is not very meaningful.
- **Best Fix:** Pair the explanation with task-focused training/annotation that directly targets the collocation misunderstanding (see guideline on task-specific instruction) [@padillaPowerfulInfluenceMarks2020].
