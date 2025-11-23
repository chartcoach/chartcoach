---
id: pictographs-for-memory-load
title: Use Pictographs for Demanding Memory Tasks
bibliography: references.bib
description: Employ pictographs when the user must retain data in working memory while
  performing other tasks.
labels:
- chart:isotype
- task:memory
- impact:recall
- visual:icons
- complexity:high
---

## The Rule <!-- role: advice -->
Use thematic pictographs (representing the data subject) within the chart elements when users need to remember the data while looking at other things or performing intervening tasks.

## The Logic <!-- role: reason -->
Pictographs provide "richer encoding cues" than abstract shapes. When working memory is not crowded, this doesn't matter much. However, when memory is under load (crowded), these extra visual hooks help preserve the information. [@haroz_isotype_2015] suggests images provide a broader set of associations (shape, identity) that separate them from verbal codes or simple shapes in memory.

*   **The Principle:** Dual Coding / Rich Encoding
*   **The Evidence:** Experiment 3 in [@haroz_isotype_2015] (using a 1-back memory task) found that pictographs led to less error than simple shapes when memory was loaded with intervening visualizations.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing data across different screens or remembering values while reading text.
*   **Data Type:** Categorical data with thematic potential (e.g., cars, animals, food).
*   **Audience:** Users in multitasking environments.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Rapid perception tasks where speed is the only metric.
*   **Reason:** Experiment 4 suggested no speed advantage for pictographs; the advantage is specifically in memory retention under load.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity.
*   **The Risk:** Choosing icons that are visually complex might introduce clutter that offsets the memory benefit if not carefully designed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using abstract shapes (circles/squares) for "cleanliness" in a complex dashboard.
*   **Why it fails:** In high-load scenarios, abstract shapes are harder to "hold" in memory than recognizable objects [@haroz_isotype_2015].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using generic bars or dots for distinct categories like "Cats" vs "Dogs"?
*   **The Test:** Show the user the chart, then show them a different chart, then ask them about the first chart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace generic points in a scatterplot or unit chart with simple icons representing the category.
*   **Best Fix:** Integrate the icon into the data representation (e.g., a stack of cars for car production) to maximize encoding hooks.
