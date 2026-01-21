---
id: reduce-bar-area-salience-to-support-mean-reading
title: Reduce Bar Area Salience When Viewers Must Infer Means
bibliography: references.bib
description: Lowering the salience of bar area (e.g., using outlines) can help viewers
  focus less on summed extent and more on value-relevant cues.
labels:
- chart:bar
- task:compare
- visual:area
- impact:accuracy
- data:categorical
- audience:general
- statistic:mean
- design:mark-style
- source:paper-yuan-haroz-franconeri
---

## The Rule <!-- role: advice -->

When using bars for average judgments, reduce the salience of filled area (e.g., by using outline-style marks) to discourage summed-area reading.

## The Logic <!-- role: reason -->

The paper reports follow-up experiments (in supplemental materials) where reducing area salience (switching shapes to outlines; or equating “ink” across conditions) improved performance for bars to match dots, suggesting that high-salience filled area can pull attention toward summed-extent proxies instead of bar-top values.

- **The Principle:** Attention is drawn to whole-object extent; lowering area salience can shift attention toward value cues
- **The Evidence:** [@yuanPerceptualProxiesExtracting2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare group averages from multiple values when a bar-like form is required
- **Data Type:** Grouped observations displayed as multiple bars per group
- **Audience:** Settings where viewers will “eyeball” means quickly and are vulnerable to area-based proxies

## When to Break It <!-- role: exceptions -->

- **Scenario:** Filled area is intentionally encoding something meaningful (e.g., you want sum/total to pop out)
- **Reason:** Reducing area salience undermines the very cue you are choosing to emphasize [@yuanPerceptualProxiesExtracting2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Outlines can be harder to see at small sizes or on low-contrast displays
- **The Risk:** Thin outlines may reduce legibility or aesthetic acceptance in some products

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping filled bars but merely telling users “look at the tops”
- **Why it fails:** The paper suggests the pull of extent/area is difficult to inhibit during multivalue judgments; the visual system tends to select whole bars as units [@yuanPerceptualProxiesExtracting2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Mean judgments correlate suspiciously with which group has more total filled area
- **The Test:** Create two versions—filled vs outline bars—keeping data constant; if outline improves mean judgments, your filled areas were likely driving summed-extent proxies [@yuanPerceptualProxiesExtracting2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from filled bars to outline-only bars for the observation marks
- **Best Fix:** Use a position-only encoding (dot plot) for mean comparisons; if bars must remain, reduce fill salience so area is less dominant [@yuanPerceptualProxiesExtracting2019].
