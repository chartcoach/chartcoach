---
id: use-rectangular-cartograms-when-filter-accuracy-evidence-favors-them
title: Use rectangular cartograms when your filtering condition matches one where
  they rank highest in accuracy
bibliography: references.bib
description: A filtering condition showed rectangular cartograms ranking highest in
  accuracy among tested cartogram types.
labels:
- chart:cartogram
- task:filter
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:rectangular
---

## Prefer rectangular cartograms for the filtering condition they win <!-- role: advice -->

Use a rectangular cartogram for filtering only when your filtering question format matches a condition where rectangular cartograms rank highest in accuracy among cartogram types. Do not assume rectangular cartograms are generally best for filtering outside that condition.

## Why rectangular cartograms can outperform on accuracy in some filtering setups <!-- role: reason -->

A more schematic, regularized representation can sometimes make it easier to identify and compare regions under a specific prompt structure, improving correctness despite other distortions.

**Mechanism:** Regular shapes can simplify region discrimination for certain filtering questions.

**Evidence:** In one filtering condition, rectangular cartograms ranked highest in accuracy among the tested cartogram types, with significant differences reported versus some other types [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** This is conditional; other filtering conditions in the same source rank rectangular lower.

## When to apply this condition-specific choice <!-- role: context -->

- **User Goal:** Maximize correctness on a filtering prompt that matches the tested condition where rectangular wins.
- **Task:** Filter.
- **Data:** Map regions with a quantitative variable encoded by area.
- **Chart Setting:** Static cartogram comparison where the rectangular variant is a feasible option.
- **Audience:** Users who benefit from schematic layouts for the specific filtering prompt.
- **Success Criterion:** Higher accuracy under that filtering prompt type.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your filtering prompts match a condition where rectangular cartograms rank lowest in accuracy. **Why:** The same evidence base contains a filtering condition where rectangular performs worst.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce faithfulness to original shapes and positions. **Risk:** Using rectangular cartograms for the wrong filtering prompt can reduce accuracy rather than improve it. **Mitigation:** Validate the prompt match with a small pilot before deploying.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Picking rectangular cartograms to “simplify” all filtering tasks. **Why it fails:** The accuracy ranking for rectangular cartograms varies by filtering condition in the evidence.

## Quick tests <!-- role: check -->

**Failure Sign:** Accuracy drops when switching to rectangular cartograms for filtering. **Quick Check:** Test your exact filtering prompt format with rectangular vs contiguous and compare error rate. **Stronger Test:** Run a controlled study or product A/B test for your filtering prompts and check statistical differences.

## What to do instead <!-- role: fix -->

- Use a contiguous cartogram if your filtering task matches the condition where contiguous ranks highest in accuracy.
- Use a non-contiguous cartogram if your filtering task matches the condition where non-contiguous is significantly more accurate.
- Keep rectangular cartograms as an optional view and default to the task-winner for your primary filtering prompt.
- Segment by task: choose cartogram type per filtering prompt family rather than using one default.
