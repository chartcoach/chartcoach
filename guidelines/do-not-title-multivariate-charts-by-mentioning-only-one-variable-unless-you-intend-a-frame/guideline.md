---
id: do-not-title-multivariate-charts-by-mentioning-only-one-variable-unless-you-intend-a-frame
title: Do Not Title Multivariate Charts by Mentioning Only One Variable Unless You
  Intend a Frame
bibliography: references.bib
description: Avoid single-variable titles for charts with multiple key variables,
  because it subtly frames interpretation.
labels:
- chart:generic
- task:interpret
- visual:text
- impact:bias-awareness
- data:multivariate
- audience:general-public
- rhetoric:framing
---

## The Rule <!-- role: advice -->

For visualizations that contain two (or more) variables that can support different conclusions, do not title the chart by mentioning only one variable unless you deliberately want to frame the takeaway.

## The Logic <!-- role: reason -->

A “statistics frame” can look neutral while still steering attention to one variable, and title slant shifts the perceived main message. This makes variable-only titles a subtle but powerful framing device.

- **The Principle:** Subtle framing via variable selection in titles
- **The Evidence:** The paper identifies “statistics frames” (variable/trend/value) and argues that mentioning only one variable can appear neutral yet cue viewers toward a side; experimentally, title slant significantly influenced perceived message [@kongFramesSlantsTitles2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Form an interpretation that considers the full visualization rather than one favored metric
- **Data Type:** Multi-variable charts used in debates (e.g., absolute counts vs per-capita; dollars vs %GDP)
- **Audience:** Viewers likely to treat data/graphs as inherently neutral [@kongFramesSlantsTitles2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is explicitly designed to focus the reader on one variable while de-emphasizing others
- **Reason:** Single-variable titling can be appropriate when the chart’s purpose is intentionally scoped to that metric [@kongFramesSlantsTitles2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less concise titles.
- **The Risk:** Readers may perceive the title as “dry” compared to a single striking statistic [@kongFramesSlantsTitles2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a variable-only title to claim neutrality (“just the facts”) while the chart includes another variable implying the opposite conclusion.
- **Why it fails:** The variable-only title is itself a framing choice that can shift the message people take away [@kongFramesSlantsTitles2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart clearly shows multiple metrics, but the title names only one.
- **The Test:** Ask: “If I swapped the title to the other metric, would the ‘main message’ flip?” If yes, the title is framing [@kongFramesSlantsTitles2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Mention both variables in the title.
- **Best Fix:** Use a balanced statistics title that explicitly contrasts both measures (or state the topic and let the chart carry the comparison) [@kongFramesSlantsTitles2018].
