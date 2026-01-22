---
id: focus-salience-on-task-relevant-features
title: Make task-critical features the most visually salient elements
bibliography: references.bib
description: Use visual salience to pull attention toward the information needed for
  the decision.
labels:
- chart:general
- task:decide
- visual:salience
- impact:accuracy
- data:general
- audience:novice
- complexity:foundational
---

## Use salience to prioritize the decision-relevant data <!-- role: advice -->

Make the marks that contain the decision-critical information the most visually salient elements in the display. Reduce salience for decorative or secondary elements so they do not compete for attention.

## Salience steers Type 1 attention before deliberation can help <!-- role: reason -->

Early visual processing pulls attention to salient features with little to no working memory involvement, shaping what gets encoded and used for a decision. When salience highlights irrelevant features, viewers may ignore less-salient but decision-relevant information and make systematically biased choices.

**Mechanism:** Bottom-up attention captures focus on high-salience features, shaping the visual description and downstream conceptual message before Type 2 corrections occur.

**Evidence:** Viewers overweight salient foregrounded features and miss crucial background/base-rate information, changing stated willingness-to-pay and risk judgments [@padillaDecisionMakingVisualizations2018]. Salient boundaries or prominent paths in geospatial uncertainty displays bias judgments toward those features even when they are not decision-relevant [@padillaDecisionMakingVisualizations2018].

**Notes:** Salience can help performance when it highlights the task-relevant variable, especially after viewers have been trained on what to look for.

## When to use salience as a decision aid <!-- role: context -->

- **User Goal:** Make a choice based on values, risks, or likelihoods shown in a visualization.
- **Task:** Identify the most likely region/outcome, compare risk across options, or judge where an event will occur.
- **Data:** Multivariate or uncertain data where multiple features could attract attention.
- **Chart Setting:** Static 2D graphics used for communication (reports, briefings, public communication).
- **Audience:** Mixed or non-expert audiences; viewers may not know what is task-relevant.
- **Success Criterion:** Higher decision accuracy and fewer attention-driven misinterpretations.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The task is to encourage open-ended exploration rather than a specific decision. **Why:** Forcing salience to a single feature can prematurely narrow attention and hide alternative patterns.

## Tradeoffs of salience-driven design <!-- role: costs -->

**Sacrifice:** Some aesthetic freedom and visual uniformity. **Risk:** Over-salience can look like advocacy and can crowd out secondary-but-important context. **Mitigation:** Balance salience with explicit annotation of what is being emphasized.

## Common salience failures <!-- role: mistakes -->

- **Mistake:** Making borders, frames, or containers the most prominent elements. **Why it fails:** Viewers may interpret boundaries as meaningful categories/containments and overweight them in judgments.
- **Mistake:** Highlighting an attention-grabbing but non-diagnostic feature (e.g., a single path/trace). **Why it fails:** Viewers substitute the salient feature for the underlying distribution and misjudge likelihood or impact.

## Quick tests for salience alignment <!-- role: check -->

**Failure Sign:** People explain their decision using a visually prominent feature that is not the intended evidence. **Quick Check:** Squint/blur the visualization and note which features still stand out; those will likely drive first impressions. **Stronger Test:** Run a brief timed (few-seconds) comprehension check to see whether first-glance decisions track the intended variable.

## What to do instead when salience is misaligned <!-- role: fix -->

- Reduce contrast, thickness, or edge prominence of non-critical containers, gridlines, and decorative frames.
- Increase relative salience (contrast, distinctiveness) of the marks that encode the decision variable.
- Add a short, direct annotation that names the decision variable viewers should attend to.
- Redesign the encoding so the key information is carried by the naturally most noticeable feature (e.g., the primary marks rather than a legend).
