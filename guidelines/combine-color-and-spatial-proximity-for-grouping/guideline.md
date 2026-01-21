---
id: combine-color-and-spatial-proximity-for-grouping
title: Reinforce Groups with Both Color and Spatial Proximity
bibliography: references.bib
description: "Use redundant cues\u2014place related words near each other and give\
  \ them the same color\u2014to approach the performance of whitespace-separated layouts."
labels:
- chart:word-cloud
- task:summarize
- task:categorize
- visual:color
- visual:position
- impact:comprehension
- data:categorical
- audience:general
- source:hearst-2020
---

## The Rule <!-- role: advice -->

Place each semantic group’s words close together and color them consistently, even if you can’t create large whitespace gaps.

## The Logic <!-- role: reason -->

Redundant cues make group structure easier to perceive. In Experiment 3, a semantically grouped layout that used both spatial clustering and group color (BSC) scored higher than a semantically colored-but-not-grouped Wordle, and performed similarly to columns (difference not statistically distinguishable), suggesting proximity+color can nearly substitute for whitespace partitions [@hearstEvaluationSemanticallyGrouped2020].

- **The Principle:** Redundant encoding for grouping robustness.
- **The Evidence:** BSC (color + spatial grouping) outperformed color-only Wordle and was close to column performance [@hearstEvaluationSemanticallyGrouped2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly infer multiple topics from one cloud while maintaining a “word cloud” feel.
- **Data Type:** Multiple semantic groups with clear membership.
- **Audience:** Analytic viewers; especially when you want a cloud-like layout rather than strict columns.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You can cleanly separate groups with whitespace and your priority is maximum readability/informativeness.
- **Reason:** In subjective ratings, designs with clearer separation (e.g., column/radial) tended to rate higher for readability/informativeness than a tighter semantic-cloud variant [@hearstEvaluationSemanticallyGrouped2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** More layout complexity than simple columns; potential for uneven density.
- **The Risk:** If font sizes vary strongly, the layout can become harder to read or feel chaotic (noted as a likely drawback in preferences) [@hearstEvaluationSemanticallyGrouped2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Only color-code groups but leave words spatially intermingled.
- **Why it fails:** The paper shows color-only Wordles improved over monochrome but still lagged behind spatially grouped designs [@hearstEvaluationSemanticallyGrouped2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Same-colored words are scattered across the display rather than forming local clusters.
- **The Test:** For each color, see if you can draw a simple contour around most of its words without enclosing many other colors; if not, spatial proximity is not reinforcing grouping [@hearstEvaluationSemanticallyGrouped2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Nudge words so same-group terms become locally adjacent.
- **Best Fix:** Use a layout method that explicitly clusters semantically related words while preserving a cloud-like overall form, and apply per-group color consistently [@hearstEvaluationSemanticallyGrouped2020].
