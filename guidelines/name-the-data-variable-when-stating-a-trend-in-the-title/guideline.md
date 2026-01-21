---
id: name-the-data-variable-when-stating-a-trend-in-the-title
title: Name the Data Variable When Stating a Trend in the Title
bibliography: references.bib
description: When a title describes an increase/decrease, explicitly specify which
  variable the trend refers to.
labels:
- chart:line
- task:interpret-trend
- visual:text
- impact:accuracy
- data:multivariate
- audience:general-public
- rhetoric:framing
---

## The Rule <!-- role: advice -->

If your title states a trend (e.g., “increasing,” “decreasing”), explicitly name the variable/metric the trend is about.

## The Logic <!-- role: reason -->

Trend-only titles can cause readers to infer the wrong metric when multiple metrics coexist; titles steer which part of the visualization becomes the “main message.”

- **The Principle:** Title-driven metric selection (statistical framing)
- **The Evidence:** The paper notes trend titles can be misleading if they omit the variable (e.g., readers may think dollars are decreasing when only %GDP is decreasing), and shows title slant significantly changes perceived message [@kongFramesSlantsTitles2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand what is increasing/decreasing without misattributing the trend
- **Data Type:** Charts with multiple measures (e.g., dollars vs percent of GDP) where measures support different narratives
- **Audience:** Readers who may rely heavily on titles for interpretation [@kongFramesSlantsTitles2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Single-metric charts where no alternative variable could plausibly be inferred
- **Reason:** Variable naming is redundant when there is no risk of metric confusion [@kongFramesSlantsTitles2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Longer titles.
- **The Risk:** Reduced punchiness compared to a short, provocative headline [@kongFramesSlantsTitles2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Writing “Budget is decreasing” over a chart that contains both “budget in dollars” and “budget as % of GDP.”
- **Why it fails:** Readers may map the trend claim onto the wrong series or assume it applies to all series [@kongFramesSlantsTitles2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A directional word (increase/decrease) appears without a metric noun.
- **The Test:** Ask a reviewer: “Which variable is this trend about?” If they answer inconsistently, the title is under-specified [@kongFramesSlantsTitles2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Append the variable name (e.g., “as a percentage of GDP”).
- **Best Fix:** Rewrite as “<Metric> <direction> <timeframe>” and ensure the chart visibly supports that exact metric framing [@kongFramesSlantsTitles2018].
