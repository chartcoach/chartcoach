---
id: classify-ensemble-tasks-into-four-perceptual-categories
title: Classify Ensemble Tasks Into Four Perceptual Categories
bibliography: references.bib
description: Organize ensemble-based visualization tasks into identification, summarization,
  segmentation, and structure estimation to drive encoding choices.
labels:
- task:identify
- task:summarize
- task:cluster
- task:correlate
- impact:clarity
- audience:designer
- complexity:foundational
---

## The Rule <!-- role: advice -->

Classify ensemble-reliant questions into **identification**, **summarization**, **segmentation**, or **structure estimation** before choosing encodings.

## The Logic <!-- role: reason -->

This works because different user questions rely on different perceptual operations over sets (e.g., isolating items vs. averaging vs. grouping vs. pattern extraction), and treating them as the same “read values” task risks choosing encodings that are mismatched to how viewers compute ensemble information.

- **The Principle:** Task–Perception Alignment for Ensemble Coding
- **The Evidence:** [@szafirFourTypesEnsemble2016] as collated for recommendation use cases in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Any goal that involves reasoning about *collections* (not single marks), such as finding outliers, estimating means/variance, clustering, or perceiving trends/correlation.
- **Data Type:** Quantitative values shown as distributions (e.g., scatterplots, time series, dense fields).
- **Audience:** Visualization designers or recommendation systems deciding encodings for common analytic tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s question is truly a single-item lookup (e.g., “What is the value of this one point?”).
- **Reason:** The four-category framework targets tasks that may require ensemble coding over many items, not isolated value reading [@szafirFourTypesEnsemble2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Adds an explicit step to your design/recommendation workflow.
- **The Risk:** If you misclassify the task category, you may optimize for the wrong perceptual operation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “find anomalies,” “compare averages,” and “detect correlation” as interchangeable “comparison” tasks.
- **Why it fails:** These rely on different ensemble operations (identification vs summarization vs structure estimation), so a single encoding strategy is unlikely to support all equally well [@szafirFourTypesEnsemble2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can describe individual marks but struggle to answer the “set-level” question (e.g., average, cluster, trend).
- **The Test:** Ask: “Is the user selecting items, summarizing them, grouping them, or extracting a pattern?” If you can’t answer, you haven’t categorized the task.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rephrase the user question using one of the four verbs: identify / summarize / segment / estimate structure.
- **Best Fix:** In a recommender, explicitly store a task label from these four categories as part of the recommendation context and generate candidates accordingly [@zengReviewCollationGraphical2023].
