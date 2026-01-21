---
id: support-systematic-attention-order-for-intended-relation
title: Support a Systematic Attention Order for the Intended Relation
bibliography: references.bib
description: Make it easy for viewers to consistently start their comparison from
  the task-relevant feature.
labels:
- chart:bar
- task:compare
- visual:attention
- impact:learnability
- data:categorical
- audience:novice
- custom:visual-routines
- source:michal-franconeri-2017
---

## The Rule <!-- role: advice -->

Design the display so viewers can use the same attention order repeatedly for the intended comparison (i.e., encourage a consistent first fixation on the task-relevant feature).

## The Logic <!-- role: reason -->

Participants showed highly consistent, individual anchor-point routines (first saccades) when judging relations (taller-first for size; darker-first for contrast), and these routines were selectively deployed according to which dimension was task-relevant in otherwise identical displays. This implies that the order of attention is tightly tied to the relation extracted.

- **The Principle:** Relation extraction is linked to ordered attentional shifts (visual routines)
- **The Evidence:** First-saccade distributions clustered around task-relevant anchors, and orthogonal-task preferences tracked the relevant single-dimension anchor rather than the irrelevant one [@michalVisualRoutinesAre2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly determine a between-value relation in a small comparison
- **Data Type:** Simple bar-pair comparisons used in teaching, dashboards, or checks
- **Audience:** Especially learners, because routines can be practiced and stabilized

## When to Break It <!-- role: exceptions -->

- **Scenario:** You want to encourage broad scanning/exploration rather than a single targeted comparison
- **Reason:** Enforcing a single routine can narrow interpretation, whereas exploration may require multiple routines [@michalVisualRoutinesAre2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less neutrality; the design implicitly “suggests” how to read the chart
- **The Risk:** Users may over-rely on the encouraged routine even when their question changes

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming relations are “seen at a glance” because the chart is simple
- **Why it fails:** The paper argues graph relations are extracted over time via routines, and the extracted relation depends on where attention goes first [@michalVisualRoutinesAre2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Different users could plausibly start on different features, yielding different relational framings (e.g., “taller on right” vs. “shorter on left”)
- **The Test:** For the intended task, ask: “Is there a clear, repeatable starting point for the comparison?”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce competing feature variation so the relevant anchor is the most compelling starting point.
- **Best Fix:** Create task-specific views where the only salient relational cue corresponds to the relation you want users to extract, aligning attention order with that relation [@michalVisualRoutinesAre2017].
