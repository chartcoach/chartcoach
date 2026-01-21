---
id: avoid-prior-study-scatterplot-preset-for-speed-in-cluster-related-tasks
title: Avoid Prior-Study Scatterplot Presets When Speed Matters for Class-Separation
  Tasks
bibliography: references.bib
description: For class-separation (cluster-like) tasks in scatterplots, avoid the
  tested prior-study preset because it was significantly slower than other designs.
labels:
- chart:scatter
- task:cluster
- visual:position
- impact:speed
- data:quantitative
- audience:novice
- source:literature-collation
- complexity:basic
---

## The Rule <!-- role: advice -->

For class-separation/cluster-like tasks in scatterplots, do not use the tested prior-study scatterplot preset when completion time matters; use other tested presets instead.

## The Logic <!-- role: reason -->

Some scatterplot presets impose measurable time penalties even when accuracy is unchanged.

- **The Principle:** Preset design choices can affect efficiency (time) independently of correctness.
- **The Evidence:** For the *cluster* task time metric, the prior-study scatterplot design (E-4) was ranked fastest (best), with E-1 (algorithm) and E-2 (MATLAB) slower, and the differences between E-4 and E-1/E-2 reported as significant [@micallefPerceptualOptimizationVisual2017]. This task/metric distinction is retained in the structured collation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly performing a cluster/class-separation judgment using a scatterplot.
- **Data Type:** Two quantitative axes (positionX/positionY scatterplot).
- **Audience:** Users working under time constraints or interactive exploration workflows.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary goal is accuracy (not speed) for cluster/class separation.
- **Reason:** For *cluster* accuracy, all tested methods were ranked together with no significant differences [@micallefPerceptualOptimizationVisual2017], as collated in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may constrain your choice of presets to those already available in your environment.
- **The Risk:** If the “prior-study” preset is not available, you may need engineering effort to reproduce it.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Selecting a scatterplot preset based on tradition or provenance (“used in a study”) instead of task-time performance.
- **Why it fails:** The cited comparison shows significant time differences for the *cluster* task across presets, despite equivalent accuracy [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users spend longer than expected to make a class-separation judgment even though the plot is a standard scatterplot.
- **The Test:** Time users on cluster/class-separation judgments across presets; if a particular preset is consistently slower, replace it (the study found significant differences in time) [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from the slow preset to another tested preset (e.g., algorithm-generated or MATLAB-like) for the cluster task.
- **Best Fix:** Add task-aware preset routing in your visualization system: if task=cluster, avoid presets that are empirically slower per the collated evidence [@zengReviewCollationGraphical2023] based on [@micallefPerceptualOptimizationVisual2017].
