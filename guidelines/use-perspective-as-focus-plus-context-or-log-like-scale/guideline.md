---
id: use-perspective-as-focus-plus-context-or-log-like-scale
title: Use 3D Perspective to Provide Focus+Context in One View
bibliography: references.bib
description: Use perspective tilt to allocate more screen area to recent or small
  values while preserving long-range context in the same chart.
labels:
- chart:line
- chart:bar
- task:trend
- task:compare
- visual:perspective
- impact:efficiency
- data:temporal
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Tilt the chart in 3D perspective when you need a single-view focus+context effect (or a log-like emphasis on smaller values).

## The Logic <!-- role: reason -->

Perspective naturally expands foreground and compresses background, which can function like a log-like allocation of space or a focus+context view—giving more area to recent or small-scale variation while keeping long-term context in the same display, reducing the need to cross-reference separate views [@brath3DInfoVisHere2014].

- **The Principle:** Use perspective space allocation to combine detail and context in one view.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Inspect fine-grained recent variation while retaining historical context.
- **Data Type:** Time series with long history where recent detail matters; data with wide variation.
- **Audience:** Viewers who benefit from a single integrated view (analysis or presentation) [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Accurate, unbiased comparison across the full timeline is the primary requirement.
- **Reason:** Perspective changes apparent scale across depth, which can bias perceived magnitudes [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uniform interpretability across all x-positions.
- **The Risk:** Viewers may misinterpret perspective distortion as data distortion if depth cues are weak [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding “gratuitous” perspective without a clear focus+context purpose.
- **Why it fails:** If the perspective doesn’t intentionally allocate attention/area, it becomes chart junk rather than a functional transform [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** The back of the chart becomes unreadable, or viewers disagree on relative magnitudes across depth.
- **The Test:** Ask a reader to compare a foreground value to a background value; if they can’t do it consistently, your perspective/depth cues are insufficient [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Strengthen depth cues (e.g., visible reference grid/planes) so perspective is interpretable.
- **Best Fix:** Use perspective only when it directly serves the focus+context/log-like goal and keeps key comparisons within the readable region [@brath3DInfoVisHere2014].
