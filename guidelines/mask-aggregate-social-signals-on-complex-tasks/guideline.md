---
id: mask-aggregate-social-signals-on-complex-tasks
title: Mask Aggregate Social Signals on Bias-Prone Tasks
bibliography: references.bib
description: Hide summary statistics of user interactions on difficult visualization
  tasks to prevent systematic errors from reinforcing one another.
labels:
- chart:scatter
- task:estimate
- impact:accuracy
- audience:general-public
- source:social-data
---

## The Rule <!-- role: advice -->
Do not display aggregate summaries of prior user judgments (such as histograms of estimates) alongside visualizations that are subject to systematic perceptual errors.

## The Logic <!-- role: reason -->
When a visual task is difficult and prone to systematic bias (e.g., estimating correlation in a scatterplot), the "wisdom of the crowd" often fails.
*   **The Principle:** **Social Proof.** Users interpret the behavior of others as correct behavior. If the crowd is systematically wrong, showing their work validates the error.
*   **The Evidence:** In experiments on linear association, @hullman_impact_2011 found that collective judgments were often no better than individual ones due to systematic bias. Furthermore, exposing users to biased social signals (e.g., a histogram centered away from the truth) significantly increased individual error rates compared to control groups.

## Where to Apply <!-- role: context -->
*   **User Goal:** Making quantitative estimates based on visual patterns (e.g., "What is the correlation?" or "What is the proportion?").
*   **Data Type:** Abstract data requiring "intuitive physics" or complex aggregation, such as scatterplots with moderate correlations.
*   **Audience:** Collaborative visualization environments or social data platforms (e.g., ManyEyes).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The task is simple and free of systematic perceptual bias.
*   **Reason:** @hullman_impact_2011 found that when the social signal is **unbiased** (accurate), showing it actually *reduces* individual error rates compared to showing no social information at all.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "social" feeling of the platform; the visualization may feel lonely or inactive without visible prior activity.
*   **The Risk:** Users may feel less confident in their judgments because they cannot "anchor" their opinion against the group.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Waiting for a large number of responses ($N$) before showing the aggregate, assuming high $N$ corrects the bias.
*   **Why it fails:** @hullman_impact_2011 showed that systematic bias affects the whole group; a large number of wrong answers just creates a "stronger" wrong signal.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the interface show a bar chart, histogram, or average of previous user inputs next to the main chart?
*   **The Test:** If you remove the social display, do individual user estimates shift closer to the statistical truth?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Hide the social histogram by default until the user has submitted their own estimate.
*   **Best Fix:** Curate the social signals. Only display aggregate feedback if it falls within a statistically acceptable range of the ground truth (if known).
