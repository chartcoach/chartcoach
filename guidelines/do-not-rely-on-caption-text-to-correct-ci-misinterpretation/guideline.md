---
id: do-not-rely-on-caption-text-to-correct-ci-misinterpretation
title: Do Not Rely on Captions to Correct CI-Only Charts
bibliography: references.bib
description: "Adding explanatory text about PIs alongside CI plots does not eliminate\
  \ readers\u2019 overestimation of treatment effectiveness."
labels:
- chart:error-bar
- task:interpret
- visual:text
- impact:robustness
- data:distribution
- audience:novice
- uncertainty:annotation
---

## The Rule <!-- role: advice -->

If your figure visually encodes inferential uncertainty (CIs/SEs), do not expect caption text alone to prevent readers from overestimating treatment effectiveness—change the visual encoding.

## The Logic <!-- role: reason -->

Readers anchor on what the graphic makes perceptually salient; extra explanatory text does not reliably override the strong cue that narrow CI/SE bars imply strong, consistent effects.

- **The Principle:** Visual dominance over textual correction in quantitative judgment.
- **The Evidence:** In Experiment 1, the CI-vs-PI gap in willingness to pay persisted even when captions included extra information about both CIs and PIs; the CI visualization still led to higher perceived effectiveness [@hofmanHowVisualizingInferential2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Make a calibrated judgment of treatment value or likelihood of personal benefit.
- **Data Type:** Two-condition experimental summaries shown as means with intervals.
- **Audience:** General readers, especially those reading quickly (press, reports, slide decks).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your audience is guaranteed to be trained and required to perform a deliberate analytic read (e.g., graded coursework with explicit computation tasks).
- **Reason:** The paper’s evidence is about typical reader judgment; enforced analytic tasks may reduce reliance on the visual heuristic [@hofmanHowVisualizingInferential2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to redesign the figure (more space, different chart type) instead of “patching” with text.
- **The Risk:** Adding outcome-uncertainty visuals can make the mean difference feel less visually prominent [@hofmanHowVisualizingInferential2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep CI error bars and add a caption sentence like “individual outcomes vary widely.”
- **Why it fails:** Even with extra information, participants shown CI visuals still paid more and inferred higher superiority than those shown PI visuals [@hofmanHowVisualizingInferential2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The caption is long and definitional, but the graphic remains a mean-plus-narrow-interval plot.
- **The Test:** Remove the caption and see if the figure still supports correct individual-level judgments; if not, the encoding—not the text—is doing the wrong work [@hofmanHowVisualizingInferential2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap CI error bars for PI (or other outcome-uncertainty) intervals while keeping the overall layout.
- **Best Fix:** Add a visualization that directly conveys individual outcome variability (e.g., hypothetical outcome samples) rather than relying on prose [@hofmanHowVisualizingInferential2020].
