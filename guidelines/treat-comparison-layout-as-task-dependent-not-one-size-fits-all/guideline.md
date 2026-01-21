---
id: treat-comparison-layout-as-task-dependent-not-one-size-fits-all
title: Choose Comparison Layouts by Task, Not by a Single Universal 'Best' Arrangement
bibliography: references.bib
description: Do not standardize on one chart arrangement for all comparisons; performance
  depends on the interaction of task and arrangement.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- impact:clarity
- audience:novice
- audience:expert
- framework:perceptual-proxies
- source:jardine-2020
---

## The Rule <!-- role: advice -->

Do not enforce a single “best” comparison layout; select the arrangement based on the **specific comparison task**.

## The Logic <!-- role: reason -->

The paper shows that arrangement effects are not consistent across comparison types: layouts that best support mean/range comparisons differ from those that best support item-change or correlation comparisons, implying viewers rely on different perceptual proxies depending on task and layout [@jardinePerceptualProxiesVisual2020a].

- **The Principle:** Task × arrangement interactions in visual comparison
- **The Evidence:** MAXMEAN/MAXRANGE favored stacked and penalized superposed, while prior comparison tasks showed different best arrangements; no single arrangement optimizes all comparisons [@jardinePerceptualProxiesVisual2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Any design where users compare two series/sets (e.g., “which is bigger overall?” vs “which changed most?”)
- **Data Type:** Multi-item sets shown as bar charts (and, by implication in the paper’s framing, other mark types)
- **Audience:** Teams creating reusable dashboards/templates

## When to Break It <!-- role: exceptions -->

- **Scenario:** A product constraint forces one layout across all views (e.g., strict template system).
- **Reason:** Standardization may outweigh performance; you accept reduced precision for some tasks.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less consistency across a dashboard suite.
- **The Risk:** Users may need to re-learn layouts per task if switching is frequent.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking overlay/superposition everywhere because it “minimizes eye movement,” or picking mirroring everywhere because it “looks comparable.”
- **Why it fails:** The paper’s results show arrangement advantages reverse across tasks; those rationales do not generalize [@jardinePerceptualProxiesVisual2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can answer some comparison questions quickly but struggle or disagree on others within the same dashboard style.
- **The Test:** List the top 1–3 comparison questions your users ask; verify the chosen layout is supported for those tasks (e.g., mean/range vs delta) per the paper’s findings [@jardinePerceptualProxiesVisual2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Offer a layout toggle (e.g., stacked vs overlaid) aligned to the task.
- **Best Fix:** Map each high-priority task to a layout that best supports it (e.g., stacked for mean/range in this paper) and standardize within each task family [@jardinePerceptualProxiesVisual2020a].
