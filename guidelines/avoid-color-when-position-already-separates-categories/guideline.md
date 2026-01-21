---
id: avoid-color-when-position-already-separates-categories
title: Remove Category Colors When Another Encoding Already Separates Marks
bibliography: references.bib
description: Use fewer colors by relying on position/spacing (and similar channels)
  to distinguish categories instead of coloring each category.
labels:
- chart:bar
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Do not assign different colors to categories when they are already clearly separated by another visual variable (especially position and spacing). Use one shared color instead.

## The Logic <!-- role: reason -->

Explain categories once—don’t encode the same distinction twice. If position (and gaps) already makes categories separable, adding many hues creates unnecessary visual noise and can make the chart harder to decipher, including for colorblind readers, as described by Muth in her “use fewer colors” checklist ([@muth_fewer_colors_2022]).

- **The Principle:** Avoid redundant encoding; reduce color noise.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying categories by where they are (not by color); reading values without hunting a legend.
- **Data Type:** Categorical marks already separated (e.g., basic bar charts with gaps).
- **Audience:** General audiences, including colorblind readers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to emphasize one or a few categories as the key message.
- **Reason:** In that case, color has a job (highlighting) rather than duplicating position ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose an immediate “color-coded category” cue.
- **The Risk:** If categories are not well-separated by layout (tight spacing, overlapping marks), a single color can make them harder to tell apart ([@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping many category colors “just in case” even though the marks are already separated by position.
- **Why it fails:** It produces a confetti-like chart that is harder to decipher and can reduce accessibility ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** The chart looks like a confetti party even though categories are already separated by layout.
- **The Test:** Temporarily set all category colors to the same color; if the chart remains easy to understand for a first-time reader, the extra colors are unnecessary ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Set all marks (bars/symbols/lines) to one color and keep category separation via position/spacing.
- **Best Fix:** If you still need to call attention to something, keep the base single color and apply a highlight color only to the most important category ([@muth_fewer_colors_2022]).
