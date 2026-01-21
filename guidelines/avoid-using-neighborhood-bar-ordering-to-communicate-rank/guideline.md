---
id: avoid-using-neighborhood-bar-ordering-to-communicate-rank
title: "Do Not Rely on Neighbor Bar Heights to Communicate a Bar\u2019s Rank"
bibliography: references.bib
description: Neighboring bar heights can systematically bias perceived rank in bar
  charts, but the effect is small and should not be used as a deliberate rank-communication
  device.
labels:
- chart:bar
- task:rank
- task:sort
- visual:length
- visual:position
- impact:accuracy
- impact:bias
- data:categorical
- data:quantitative
- audience:general
- effect-size:small
---

## The Rule <!-- role: advice -->

Do not use (or “tune”) the heights of neighboring bars as a mechanism to communicate, emphasize, or manipulate a target bar’s perceived rank.

## The Logic <!-- role: reason -->

People judge a bar’s standing partly relative to nearby bars: the same target bar is perceived as *lower rank* when surrounded by *high* neighbors, and *higher rank* when surrounded by *low* neighbors. This neighborhood-driven bias exists but is small compared to other influences on rank judgments, so it is not a dependable design lever. This guideline is distilled from the collation in [@zengReviewCollationGraphical2023] based on experimental evidence in [@zhaoNeighborhoodPerceptionBar2019].

- **The Principle:** Context-dependent (neighbor-based) bias in rank estimation
- **The Evidence:** [@zhaoNeighborhoodPerceptionBar2019; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating where a highlighted bar falls within the full set (rank/percentile-style judgments).
- **Data Type:** Univariate bar charts with a quantitative value per categorical item (length encoding with categorical x-position).
- **Audience:** General audiences doing quick judgments (the study uses brief exposure), where rank impressions matter. Grounded via [@zhaoNeighborhoodPerceptionBar2019] and collated in [@zengReviewCollationGraphical2023].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your communication goal is *not* rank (e.g., you only care about reading exact labeled values).
- **Reason:** This guideline targets rank-estimation bias; if rank is irrelevant, neighbor-driven rank bias is not the key failure mode. Evidence basis remains [@zhaoNeighborhoodPerceptionBar2019] as summarized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up a potential “micro-optimization” of perceived rank via local reordering.
- **The Risk:** If you ignore the rule and try to shape rank perception via neighborhoods, the resulting effect may be inconsistent and dominated by other factors, making your intent unreliable (as reported in [@zhaoNeighborhoodPerceptionBar2019] and collated by [@zengReviewCollationGraphical2023]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reordering a few bars around a target to try to make it “feel” higher/lower ranked.
- **Why it fails:** Neighborhood effects exist but are small; the same bar can shift only slightly in perceived rank between high- vs low-neighbor contexts, so the change may not meaningfully control perception ([@zhaoNeighborhoodPerceptionBar2019], summarized in [@zengReviewCollationGraphical2023]).

## How to Check <!-- role: check -->

- **Visual Sign:** A highlighted bar appears to “change standing” primarily because nearby bars are extreme (very high or very low), even though its value is unchanged.
- **The Test:** Keep the target bar fixed and swap its immediate neighbors between “mostly high” and “mostly low” bars; if perceived rank changes, you are in the neighborhood-bias regime described by [@zhaoNeighborhoodPerceptionBar2019] (as collated in [@zengReviewCollationGraphical2023]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Avoid local neighborhood manipulations meant to influence rank; keep a consistent ordering strategy rather than “curating” neighbors around a target.
- **Best Fix:** If rank communication is critical, use explicit rank cues rather than relying on neighborhood context (e.g., directly presenting rank as text/annotation), since neighborhood effects are not a dependable channel per [@zhaoNeighborhoodPerceptionBar2019] and its collation in [@zengReviewCollationGraphical2023].
