---
id: use-stacked-columns-for-time-only-when-total-matters-and-intervals-are-uniform
title: Use Stacked Column Charts for Time Only with Uniform Intervals and a Crucial
  Total
bibliography: references.bib
description: Use stacked columns for time series only when showing the total of parts
  is essential and time points are evenly spaced.
labels:
- chart:stacked-column
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use stacked column charts for dates only if (1) the total of the parts is crucial and (2) your dates are equally spaced intervals.

## The Logic <!-- role: reason -->

Stacked columns imply discrete, evenly spaced categories; uneven time gaps are not represented faithfully. Also, if the total isn’t important, stacked columns add decoding effort compared with simpler time-focused charts [@muth_stacked_columns_2018].

- **The Principle:** Match chart scale to the structure of time
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** See how totals (and a key component) change at a few evenly spaced time points
- **Data Type:** Low-frequency time series (few dates) with part-to-whole composition per date
- **Audience:** Broad audiences reading quickly on screens [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Time points have irregular intervals.
- **Reason:** Use an area chart or line chart with a continuous x-axis to show the spacing correctly [@muth_stacked_columns_2018].
- **Scenario:** The total is not important.
- **Reason:** Use a line chart; it’s quicker for readers to decipher [@muth_stacked_columns_2018].
- **Scenario:** Your key message is one share overtaking another.
- **Reason:** A line chart communicates the crossover more clearly, even if it no longer emphasizes “parts of a total” [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to drop compositional detail (e.g., switch to lines) to better show time dynamics.
- **The Risk:** With stacked columns, readers may not intuitively read the story as “shares over time” when the goal is crossover or relative change [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using stacked columns on irregular dates (e.g., missing years) as if spacing were equal.
- **Why it fails:** The visual timing is misleading because all columns appear equally spaced [@muth_stacked_columns_2018].
- **The Wrong Fix:** Using stacked columns when only a single line would communicate the message.
- **Why it fails:** Adds unnecessary cognitive load [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Unequal time gaps appear identical; readers can’t tell where time “jumps.”
- **The Test:** List your dates and verify equal intervals; if not equal, don’t use stacked columns. Then ask: “Would a line chart answer the same question faster?” [@muth_stacked_columns_2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce to a few evenly spaced dates (if editorially valid) and keep the total prominent.
- **Best Fix:** Use a line chart when totals aren’t essential or when showing crossovers; use an area or line chart for irregular intervals [@muth_stacked_columns_2018].
