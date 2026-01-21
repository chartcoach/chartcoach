---
id: limit-small-multiple-panels-to-support-a-clear-takeaway
title: Limit Panels to the Categories That Support Your Takeaway
bibliography: references.bib
description: "Show fewer small-multiple panels so readers aren\u2019t forced to hunt\
  \ for what matters."
labels:
- chart:line
- task:focus
- visual:layout
- impact:clarity
- data:temporal
- audience:general
- chart:small-multiples
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Include only as many small-multiple panels as needed to support your intended takeaway; avoid dumping dozens of panels on readers.

## The Logic <!-- role: reason -->

While faceting removes overlap, too many panels shifts work to the reader (they must search for “the interesting bits”), and long scrolling—especially on mobile—reduces comprehension and engagement [@muth_small_multiple_line_charts_2024].

- **The Principle:** Reduce cognitive load by curating what’s shown
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand key patterns and comparisons without exhaustive search
- **Data Type:** Many categories over time
- **Audience:** General readers, especially on mobile

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must provide all categories for completeness.
- **Reason:** The communication goal is full coverage; in that case, consider a different presentation (e.g., sparklines in a searchable table) instead of an overwhelming grid [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced completeness; some categories are not shown.
- **The Risk:** Accusations of cherry-picking if selection criteria aren’t clear or the remaining panels misrepresent the overall picture [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Faceting everything because you can, then expecting readers to find the story themselves.
- **Why it fails:** Readers face excessive scanning and scrolling, which weakens understanding [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart becomes a long, scroll-heavy list/grid of panels.
- **The Test:** View on a phone-sized screen: if it takes substantial scrolling to reach the end, you likely have too many panels [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories shown to those that illustrate the message.
- **Best Fix:** If full coverage is required, move the “all categories” view to sparklines in a searchable table and keep the small-multiple chart focused [@muth_small_multiple_line_charts_2024].
