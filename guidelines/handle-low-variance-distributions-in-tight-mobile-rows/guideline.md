---
id: handle-low-variance-distributions-in-tight-mobile-rows
title: Cap or Adapt Very Tall Distributions in Small Rows
bibliography: references.bib
description: Prevent low-variance predictions from producing overly tall density/dot
  displays that break compact mobile layouts.
labels:
- chart:density
- task:scan
- visual:height
- impact:readability
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

When displaying many predictive distributions in short mobile rows, prevent low-variance predictions from becoming disproportionately tall by capping height (or adjusting mark spacing for dense dotplots).

## The Logic <!-- role: reason -->

On small screens, tight (low-variance) distributions can become very tall (especially density-based encodings), exceeding row height and breaking the compact list layout; the paper adopts scaling down max height only when it would exceed the row height (and reduces dot spacing for dense dotplots) to keep the visualization usable in a multi-row mobile list [@kayWhenIshMy2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Scan a list of ~10 upcoming buses quickly.
- **Data Type:** Predictive PDFs that can become extremely peaked near arrival time.
- **Audience:** Mobile users in time- and space-constrained contexts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You show a single distribution at large size (no need to fit within a fixed row height).
- **Reason:** The “too tall” failure mode is driven by space constraints in dense lists [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Distorts peak height, reducing fine-grained density comparability for the most certain predictions.
- **The Risk:** Users may misread capped peaks as lower certainty if the cap is not visually indicated [@kayWhenIshMy2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Normalize every distribution to the same maximum height.
- **Why it fails:** Normalization makes cross-row comparison of uncertainty harder because height no longer reflects variance consistently [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Some rows overflow, clip, or dominate vertical space when predictions are very certain.
- **The Test:** Inspect the UI at times when a bus is 1–2 minutes away; if the plot spikes beyond the row, you need height handling.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply a max-height cap only when the peak would exceed row height.
- **Best Fix:** Prefer encodings that remain consistent under tight variance (the paper notes low-count dotplots and stripeplots do not require the same height hack), while still meeting your estimation goals [@kayWhenIshMy2016].
