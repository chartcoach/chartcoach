---
id: prefer-treemaps-or-other-non-scrolling-designs-for-fast-two-item-comparisons-in-ranked-lists
title: Avoid scrolled bar charts for fast two-item comparisons in ranked lists
bibliography: references.bib
description: Two-item comparisons are much slower with scrolled bar charts than with
  non-scrolling ranked-list designs.
labels:
- chart:bar
- task:compare
- impact:speed
- data:quantitative
- audience:novice
- domain:ranked-list
---

## Avoid scrolled bar charts for fast two-item comparisons in ranked lists <!-- role: advice -->

When the task is to compare two highlighted items in a ranked list and respond quickly, avoid scrolled bar charts. Prefer a non-scrolling ranked-list design such as treemaps, wrapped bars, packed bars, piled bars, or Zvinca plots.

## Why scrolled bar charts slow two-item comparisons <!-- role: reason -->

Comparing two specific items can require locating both items, potentially far apart in the list. If the list does not fit in view, scrolling introduces interaction cost and disrupts side-by-side comparison, increasing completion time.

**Mechanism:** Needing to navigate to find and re-find two targets increases search time and working memory load compared to layouts where both items can be accessed within a stable view.

**Evidence:** For the two-item comparison task time result (“sort-2”), scrolled bar charts were ranked slowest, while several non-scrolling alternatives were faster, with multiple significant pairwise differences reported [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline does not assert which alternative is most accurate for comparison; it is time-focused.

## When this applies <!-- role: context -->

- **User Goal:** Decide which of two items is larger (and/or by how much) quickly.
- **Task:** Two-item comparison within a ranked list.
- **Data:** Long list where items may be far apart in rank.
- **Chart Setting:** Interfaces where scrolling is required to reach items.
- **Audience:** General audiences or mixed experience.
- **Success Criterion:** Lower completion time.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** The list reliably fits in a single view without scrolling. **Why:** The interaction cost driving this result is reduced when scrolling is not needed.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Non-scrolling alternatives may trade away some aspects of bar-chart familiarity or a single global baseline. **Risk:** Some compact layouts can reduce discriminability for small differences. **Mitigation:** Measure both time and accuracy for your expected item counts and value distributions.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a scrolled bar chart for comparisons simply because it is the “standard” ranked-list view. **Why it fails:** The need to scroll can dominate comparison time.

## Quick tests <!-- role: check -->

**Failure Sign:** Users pause to scroll and lose track of one of the two items during comparison. **Quick Check:** Observe whether users must scroll to see both targets; if yes, test a non-scrolling layout. **Stronger Test:** A/B test scrolled bars vs a non-scrolling layout on comparison completion time.

## What to do instead <!-- role: fix -->

- Use a non-scrolling ranked-list design when comparisons are common and time-sensitive.
- Provide a comparison mode that brings both highlighted items into the same viewport without manual scrolling.
- Add search-and-focus interactions that jump directly to items to minimize navigation time.
- If you must keep scrolling, design the workflow so one item stays visually anchored while navigating to the other.
