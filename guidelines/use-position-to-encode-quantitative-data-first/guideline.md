---
id: use-position-to-encode-quantitative-data-first
title: Encode Quantitative Values with Position First
bibliography: references.bib
description: Prefer position (x/y) over other channels when encoding quantitative
  values.
labels:
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:foundational
---

## The Rule <!-- role: advice -->

Encode quantitative values using position on an axis (x or y) before considering length, angle, orientation, area, or color.

## The Logic <!-- role: reason -->

Position judgments are treated as the most effective (most accurate) perceptual task for quantitative encodings in the effectiveness ordering summarized from the theoretical ranking. This guideline is collated for visualization recommendation use in [@zengReviewCollationGraphical2023] and originates from the effectiveness ranking in [@mackinlayAutomatingDesignGraphical1986a].

- **The Principle:** Effectiveness via perceptual-task ordering
- **The Evidence:** [@mackinlayAutomatingDesignGraphical1986a], as collated in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing quantitative magnitudes accurately
- **Data Type:** Quantitative measures mapped to a single visual channel
- **Audience:** General audiences (including non-experts)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot use position due to a required layout constraint or because position is already committed to other required variables.
- **Reason:** The rule assumes position is available as a primary encoding channel; if it is not available, you must use lower-ranked channels.

## The Price <!-- role: costs -->

- **The Sacrifice:** You may consume the most valuable channels (x/y axes), limiting how many other variables you can show with position.
- **The Risk:** Overloading position with too many encodings can force later variables into less effective channels.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding the main quantitative variable with color hue or area while leaving position to show something less important.
- **Why it fails:** It reverses the effectiveness ordering, potentially reducing accuracy for the primary quantitative read.

## How to Check <!-- role: check -->

- **Visual Sign:** The chart’s main numeric quantity is expressed via color/area/angle while the axes are underutilized for that quantity.
- **The Test:** Identify the primary quantitative question; verify it can be answered by reading a position on an axis.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the quantitative field onto x or y position.
- **Best Fix:** Redesign the chart so the most important quantitative variable is mapped to position and less important variables use lower-ranked channels.
