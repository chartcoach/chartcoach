---
id: dont-trust-labels-to-fix-perception
title: Prioritize Visual Scaling Over Axis Labels
bibliography: references.bib
description: Correctly reading axis values does not neutralize the feeling of exaggerated
  severity caused by truncation.
labels:
- chart:line
- chart:bar
- visual:scale
- task:estimation
- impact:bias
---

## The Rule <!-- role: advice -->
Do not assume that clear axis labels or the ability to accurately read data values will counteract the visual exaggeration caused by a truncated y-axis.

## The Logic <!-- role: reason -->
There is a dissociation between "reading values" (decoding) and "judging severity" (interpretation). Even when users are forced to attend to the numbers, the visual spatial arrangement dominates their emotional or qualitative assessment of the trend.
*   **The Evidence:** In Experiment 3, [@correll_truncating_2020] asked participants to estimate specific values before judging the chart. While estimation error was generally low (people read the numbers correctly), the perceived severity of the effect remained significantly exaggerated in truncated charts. "Accurate estimation of values does not seem to counteract the visual magnification of difference."

## Where to Apply <!-- role: context -->
*   **User Goal:** Ensuring the audience understands the *significance* (severity) of a change, not just the raw numbers.
*   **Data Type:** Any chart with a truncated axis.
*   **Audience:** Lay audiences and decision-makers who may rely on "gut checks" of visual data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Tables or precise readout displays.
*   **Reason:** If the visualization is secondary to a data table, the user may rely entirely on the numbers. But for standard charts, the visual dominates.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot defend a sensationalized chart by simply pointing to the numbers and saying "the data is right there."
*   **The Risk:** Users will correctly state that "Sales dropped 2%," but will emotionally react as if sales crashed 50%.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Truncating an axis to highlight a tiny change, then making the axis labels bold or large to ensure people "read the numbers."
*   **Why it fails:** The bias is visual, not mathematical. The visual exaggeration of the slope or height difference persists even when the user knows the numbers [@correll_truncating_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** A steep slope or large bar difference representing a trivial percentage change.
*   **The Test:** Ignore the numbers. Look only at the shape. Does the change look like a crisis? If yes, that is the message you are sending.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a zero-baseline reference line or a small "full scale" preview graphic.
*   **Best Fix:** Determine the "meaningful effect size." Scale the axis so that a trivial change *looks* trivial visually (e.g., a flat line), and a significant change *looks* significant.
