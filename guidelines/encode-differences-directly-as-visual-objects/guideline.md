---
id: encode-differences-directly-as-visual-objects
title: Show Differences as Their Own Visual Marks
bibliography: references.bib
description: Turn relational judgments into direct perceptual reads by encoding deltas
  explicitly.
labels:
- chart:bar
- task:compare
- visual:length
- impact:speed
- data:paired
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When the key task is comparing paired values, encode the **difference (delta)** directly as its own mark instead of making viewers compare two separate marks.

## The Logic <!-- role: reason -->

- **The Principle:** Comparisons are slow and serial; direct encodings convert multi-step comparisons into single-step perception.
- **The Evidence:** The paper illustrates that finding a decreasing pair among many bars is hard until the differences are turned into “visual objects” that can be scanned quickly [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Determining which pairs increase/decrease or by how much.
- **Data Type:** Paired “before/after” or “A vs B” values repeated across many categories.
- **Audience:** Viewers who need fast, accurate relational judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When absolute levels (not differences) are the primary decision criterion.
- **Reason:** A delta-only view can obscure magnitude context that matters for decisions [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some immediate access to the original raw values if you only show deltas.
- **The Risk:** Viewers may over-focus on deltas and ignore baselines.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Expecting viewers to mentally subtract across many pairs.
- **Why it fails:** It requires repeated, slow comparisons and increases error risk [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers trace back and forth between paired marks to decide direction/magnitude.
- **The Test:** Ask “Which categories decreased?” If it takes more than a quick scan, deltas aren’t directly encoded.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a delta indicator (e.g., a small bar/marker showing change) alongside existing values.
- **Best Fix:** Redesign around the delta as the primary encoding, optionally providing the raw values secondarily for verification [@zacksDesigningGraphsDecisionMakers2020].
