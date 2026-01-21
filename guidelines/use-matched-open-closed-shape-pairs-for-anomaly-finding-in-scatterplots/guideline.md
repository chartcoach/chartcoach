---
id: use-matched-open-closed-shape-pairs-for-anomaly-finding-in-scatterplots
title: Use Matched Open/Closed Shape Pairs for Anomaly Finding in Scatterplots
bibliography: references.bib
description: For anomaly-finding tasks in scatterplots, prefer the higher-ranked shape
  pairings (triangle+cross or square+cross) and avoid the lowest-ranked pairing (asterisk+cross).
labels:
- chart:scatter
- task:find-anomalies
- visual:shape
- visual:position
- impact:accuracy
- impact:speed
- data:categorical
- data:quantitative
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

When a scatterplot’s primary task is finding anomalies, prefer the top-ranked shape pairings and avoid the bottom-ranked pairing:

- Prefer triangle+cross and square+cross
- Avoid asterisk+cross

## The Logic <!-- role: reason -->

- **The Principle:** Shape pairing choices change how much perceptual interference users experience while separating categories during anomaly judgments.
- **The Evidence:** The extracted experimental results collated in [@zengReviewCollationGraphical2023] from [@burlinsonOpenVsClosed2018] rank anomaly-finding accuracy with (triangle+cross) and (square+cross) at the top tier, and (asterisk+cross) as worst; the significance set includes E-6 > E-1 and multiple top-tier > lower-tier comparisons for accuracy.

## Where to Apply <!-- role: context -->

- **User Goal:** Find anomalies/outliers while distinguishing two categories by shape in the same scatterplot.
- **Data Type:** Two quantitative axes (positionX/positionY) and a nominal category encoded with shape.
- **Audience:** General users; especially where errors (missed anomalies) are costly.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The anomaly task is not present (the chart is for correlation, ranking, or another goal).
- **Reason:** The ranking and pairwise significance are reported for the find-anomalies task specifically in the structured results from [@burlinsonOpenVsClosed2018], as collated by [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced freedom in symbol choice if you want to stay near the best-performing pairings.
- **The Risk:** Using a poor pairing (notably asterisk+cross) can push you toward the worst-performing condition for anomaly accuracy.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using asterisk+cross because both are “sharp” and appear visually prominent.
- **Why it fails:** In the extracted rankings, asterisk+cross is the lowest-ranked design for anomaly accuracy (and also low for time), despite seeming salient [@burlinsonOpenVsClosed2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** One category is an asterisk and the other is a cross in a two-class scatterplot intended for anomaly finding.
- **The Test:** Swap asterisk to square or triangle and re-evaluate whether the chart now uses one of the top-ranked pairings for anomaly accuracy from the extracted results [@burlinsonOpenVsClosed2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace asterisk with square or triangle while keeping the other symbol unchanged.
- **Best Fix:** In a visualization recommender, add a task-conditioned shape preference list for anomaly finding (prioritizing triangle+cross and square+cross; deprioritizing asterisk+cross) based on the collated evidence [@zengReviewCollationGraphical2023; @burlinsonOpenVsClosed2018].
