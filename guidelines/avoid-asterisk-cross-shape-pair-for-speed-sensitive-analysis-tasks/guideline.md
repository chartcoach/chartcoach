---
id: avoid-asterisk-cross-shape-pair-for-speed-sensitive-analysis-tasks
title: Avoid Asterisk+Cross Shape Pair for Speed-Sensitive Analysis Tasks
bibliography: references.bib
description: Avoid using asterisk+cross as the two-category shape pair in scatterplots
  when task speed matters for correlation or anomaly finding.
labels:
- chart:scatter
- task:correlate
- task:find-anomalies
- visual:shape
- visual:position
- impact:speed
- data:categorical
- data:quantitative
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

If completion time is important in correlation judgments or anomaly finding with shape-encoded categories, do not use the asterisk+cross shape pairing.

## The Logic <!-- role: reason -->

- **The Principle:** Some shape combinations induce more perceptual interference, slowing task completion even when positional encodings are unchanged.
- **The Evidence:** In the collated results referenced by [@zengReviewCollationGraphical2023] from [@burlinsonOpenVsClosed2018], asterisk+cross is ranked slowest for the correlate time metric, with a significant best-vs-worst difference reported (E-6 faster than E-1). For find-anomalies time, asterisk+cross is also placed at the bottom of the ranking list.

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly judge correlation or quickly identify anomalies while distinguishing two categories by shape.
- **Data Type:** Two quantitative axes in a scatterplot with a nominal grouping encoded by shape.
- **Audience:** Any; especially workflows where time-to-insight is important.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is not time-sensitive (e.g., a static explanatory graphic where users can spend longer).
- **Reason:** This guideline is specifically about the time metric rankings extracted from [@burlinsonOpenVsClosed2018] as collated by [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to change an established “brand” shape choice or library default.
- **The Risk:** If your plotting library defaults to asterisk and cross for categories, you may systematically slow users on these tasks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming any two distinct symbols will be equally fast because position encodes the quantitative values.
- **Why it fails:** The structured evidence shows time rankings differ substantially across shape pairings even though position encodings are constant [@burlinsonOpenVsClosed2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend shows categories mapped to asterisk and cross.
- **The Test:** Swap one of the shapes to a closed shape (square/triangle) and compare whether the new pairing aligns with faster-ranked designs for the same task in the extracted results [@burlinsonOpenVsClosed2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace asterisk with square or triangle, keeping cross (or replace cross with square/triangle).
- **Best Fix:** Add a recommender constraint/heuristic: for correlate and find-anomalies tasks, assign shape pairs from the higher-ranked set and explicitly blacklist asterisk+cross based on collated evidence [@zengReviewCollationGraphical2023; @burlinsonOpenVsClosed2018].
