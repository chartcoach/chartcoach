---
id: avoid-excessive-font-size-variation-in-dense-semantic-clouds
title: Limit Font Size Variation When It Disrupts Group Reading
bibliography: references.bib
description: Avoid font size variation that makes grouped word sets harder to scan,
  especially in cloud-like layouts.
labels:
- chart:word-cloud
- task:summarize
- visual:size
- impact:readability
- data:text
- audience:general
- source:hearst-2020
---

## The Rule <!-- role: advice -->

If font size variation makes group reading feel chaotic or harder to scan, reduce the variation—especially in cloud-like (non-column) layouts.

## The Logic <!-- role: reason -->

The paper found that within Wordle-style layouts, multiple font sizes did not improve performance and showed suggestive evidence of harm, while in at least one subjective setting tighter, more cloud-like semantic layouts may have been penalized due to increased font-size variation. This implies that size variation can interfere with efficient scanning when layout is already visually complex [@hearstEvaluationSemanticallyGrouped2020].

- **The Principle:** Competing visual salience can disrupt systematic scanning.
- **The Evidence:** No performance benefit from multiple fonts within Wordles; aesthetic/readability tension noted when font size variation increased in semantic clouds [@hearstEvaluationSemanticallyGrouped2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify categories/topics quickly from grouped sets.
- **Data Type:** Word clouds where grouping is encoded by proximity and/or color (not strict columns).
- **Audience:** General viewers performing an analytic task.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A structured layout (e.g., columns) remains easy to scan even with some size variation.
- **Reason:** In the paper’s column layouts, multiple font sizes actually scored higher than single font sizes, suggesting size variation is less harmful when structure is strong [@hearstEvaluationSemanticallyGrouped2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less typographic “liveliness” and visual play.
- **The Risk:** If you remove variation entirely, the display may become less engaging for some contexts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add large size differences to make the cloud feel “Wordle-like,” even when the task is analytic.
- **Why it fails:** In Wordle-like layouts, size variation didn’t improve accuracy and may distract from integrating all cue words needed to infer a topic [@hearstEvaluationSemanticallyGrouped2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Your eyes keep jumping to oversized words and you ignore smaller words that are necessary to infer the category.
- **The Test:** Try to infer a category using only one group’s words; if smaller words are consistently missed, size variation is likely too strong [@hearstEvaluationSemanticallyGrouped2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the size range (bring the largest down and/or smallest up).
- **Best Fix:** Use a more structured grouped layout (e.g., clear zones/columns) so moderate size variation doesn’t compromise scanning [@hearstEvaluationSemanticallyGrouped2020].
