---
id: do-not-use-area-charts-to-compare-shares-use-lines
title: Do Not Use Area Charts to Compare Shares; Use Line Charts
bibliography: references.bib
description: Use line charts instead of area charts when the key point is comparing
  one share against another (e.g., which overtakes which).
labels:
- chart:area
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Don’t use an area chart if your main goal is to compare the size of different shares with each other (e.g., to show one overtaking another); use a line chart instead.

## The Logic <!-- role: reason -->

In stacked areas, only the bottom series shares a common baseline; other series are harder to compare precisely against each other. Lines allow direct comparison of series without the stacking baseline problem and let you omit irrelevant shares [@muth_area_charts_2018].

- **The Principle:** Enable like-with-like comparison by giving series comparable reference frames
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Determine which share is larger and when one surpasses another
- **Data Type:** Share/percentage time series, especially when many categories exist
- **Audience:** Readers who need a clear “crossing” or ranking-over-time message

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary message is the combined total plus overall composition, not share-vs-share comparison.
- **Reason:** Area charts are intended to show totals and their shares developing over time; if that’s the message, stacking may be appropriate [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Switching to lines deemphasizes the feeling of “parts of a whole.”
- **The Risk:** If you show only a subset of shares, readers may ask what happened to the omitted categories unless you clarify scope [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the area chart and adding callouts to claim one share overtook another.
- **Why it fails:** The underlying stacked geometry still makes the comparison harder; annotations can’t fully compensate [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must trace wavy boundaries in the middle of the stack to compare shares.
- **The Test:** Try to answer “Which is bigger at year X?” for two non-bottom layers; if it’s slow or uncertain, use lines [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a line chart [@muth_area_charts_2018].
- **Best Fix:** Show only the shares needed to make the comparison (e.g., the two groups involved in the overtake) using lines [@muth_area_charts_2018].
