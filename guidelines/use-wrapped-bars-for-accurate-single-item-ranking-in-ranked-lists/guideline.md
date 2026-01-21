---
id: use-wrapped-bars-for-accurate-single-item-ranking-in-ranked-lists
title: Use Wrapped Bars for Accurate Single-Item Ranking in Ranked Lists
bibliography: references.bib
description: For ranking a highlighted item in a ranked list, wrapped bars yield higher
  accuracy than scrolled barcharts, treemaps, and other dense ranked-list layouts.
labels:
- chart:bar
- chart:treemap
- task:rank
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- domain:ranked-list
---

## The Rule <!-- role: advice -->

Use wrapped bars when users must accurately determine the rank (position) of a single highlighted item in a long ranked list.

## The Logic <!-- role: reason -->

Wrapped bars performed best for accuracy on the paper’s first “sort” condition (single-item rank task), outperforming treemap and scrolled barchart, and also outperforming packed, piled, and Zvinca designs in the same condition.

- **The Principle:** Reduce perceptual difficulty when locating and decoding a specific item’s relative position in a ranked arrangement.
- **The Evidence:** The extracted rankings show wrapped bars (E-3) as most accurate for sort-1, with significant pairwise advantages over all other tested designs [@mylavarapuRankedListVisualizationGraphical2019]. This paper’s results are collated for recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine the rank of a single selected item (“what place is this?”).
- **Data Type:** A single quantitative value per item (ranked list) with item identity as nominal.
- **Audience:** General audiences (crowdsourced participants).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users primarily need the fastest possible responses for ranking, not the most accurate.
- **Reason:** In the time ranking for the corresponding sort-1 condition, wrapped bars are grouped with slower designs (with scrolled barchart), while several other techniques are grouped as faster [@mylavarapuRankedListVisualizationGraphical2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potentially slower completion time for the rank task compared to other non-scrolling alternatives.
- **The Risk:** Users may still face cross-column scanning costs in wrapped layouts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to packed/piled/Zvinca designs to “fit everything on one screen” for rank lookups.
- **Why it fails:** In the accuracy ranking for sort-1, packed (E-4), piled (E-5), and Zvinca (E-6) are all in the worst-performing group relative to wrapped bars [@mylavarapuRankedListVisualizationGraphical2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently misreport the selected item’s place (systematic rank error).
- **The Test:** Run a quick internal test: highlight random items and ask users to report rank; compare error rates across candidate chart types.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace treemap/packed/piled/Zvinca ranked-list views with wrapped bars for the rank-lookup view.
- **Best Fix:** Offer wrapped bars as the default for rank lookup, and provide other views only when optimizing for time or other tasks [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].
