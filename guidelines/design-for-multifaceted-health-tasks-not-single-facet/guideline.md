---
id: design-for-multifaceted-health-tasks-not-single-facet
title: Design Visualizations to Encode Multiple Data Facets Simultaneously
bibliography: references.bib
description: Avoid single-facet charting for big health data; encode multiple facets
  in one integrated view to support complex sensemaking.
labels:
- chart:multiview
- task:sensemaking
- visual:structure
- impact:insight
- data:multifaceted
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Design the visualization to show multiple facets and elements of big health data at the same time, not one or two facets per chart.

## The Logic <!-- role: reason -->

Big health data work involves exploration of non-explicit relationships and inter-related subtasks; simple charts typically encode only one or two facets and become ineffective for these complex sensemaking tasks. Integrating multiple facets in a single space helps users quickly perceive patterns, form hypotheses, and compare related elements without constantly switching views.

- **The Principle:** Multifaceted encoding for complex, co-occurring tasks
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Explore relationships, compare across facets, develop and discard hypotheses (e.g., cause–risk–location–age)
- **Data Type:** Large, varied public health datasets with multiple attributes, levels, and relationships
- **Audience:** Public health professionals and analysts; also motivated lay users doing investigative exploration

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is a narrow, simple perceptual query (e.g., rank diseases by a single metric).
- **Reason:** A simple chart may be more efficient and readable than an elaborate multifaceted view. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher visual density and learning effort.
- **The Risk:** Overly elaborate designs can overwhelm users if not systematically structured. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more separate small charts to a dashboard to cover each facet.
- **Why it fails:** Users must mentally integrate scattered views; crowded dashboards increase cognitive burden and may impose arbitrary layout unrelated to data structure. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** Users must frequently switch views or mentally “join” separate charts to answer basic cross-facet questions.
- **The Test:** Try answering a question that requires two+ facets (e.g., “Which risks drive which causes in this region for this age group?”). If it requires flipping between views or memorizing values, the design breaks the rule. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an integrated relationship view that simultaneously presents key facets (e.g., cause–risk–location links) alongside the existing charts.
- **Best Fix:** Redesign as a single, systematically structured visualization that encodes multiple facets in one space using explicit organizational structures (e.g., coordinated axes + links; stacked tracks). [@olaSimpleChartsDesign2016]
