---
id: minimize-required-visual-comparisons
title: Reduce the Number of Comparisons the Viewer Must Make
bibliography: references.bib
description: Design charts so the viewer does not need many sequential pairwise comparisons
  to answer key questions.
labels:
- chart:bar
- task:compare
- visual:attention
- impact:speed
- data:multivariate
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Design the graphic so the key takeaway is visible with few comparisons; avoid forcing viewers to perform many pairwise comparisons.

## The Logic <!-- role: reason -->

- **The Principle:** Comparison is often serial and slow—people effectively do one comparison at a time.
- **The Evidence:** The paper explains that while some summary statistics are fast, repeated comparisons across many elements quickly become time-consuming and error-prone [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Finding “which is decreasing,” “which pair differs,” or other relational judgments across many elements.
- **Data Type:** Charts with many marks (e.g., 20 bars) and many possible pairwise relations.
- **Audience:** Any audience, especially under time pressure.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Exploratory analysis where the point is to allow open-ended comparison among many combinations.
- **Reason:** The goal may require broad comparison affordances, accepting slower reading [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Completeness or flexibility; you may show fewer relationships at once.
- **The Risk:** Over-simplification could hide secondary but important patterns.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more marks or more categories “for completeness,” increasing comparison load.
- **Why it fails:** It multiplies the number of potential comparisons and slows reading [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Answering a simple relational question requires scanning back and forth repeatedly.
- **The Test:** List the top 3 questions the viewer must answer; if each requires multiple sequential comparisons, the chart is over-demanding.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce elements (filter to most relevant) or pre-sort to make the key comparison adjacent.
- **Best Fix:** Re-encode the relationship directly (e.g., plot differences as objects) so the viewer reads the answer rather than computes it [@zacksDesigningGraphsDecisionMakers2020].
