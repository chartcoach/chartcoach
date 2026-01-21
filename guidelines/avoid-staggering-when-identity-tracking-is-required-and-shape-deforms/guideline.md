---
id: avoid-staggering-when-identity-tracking-is-required-and-shape-deforms
title: Avoid Staggering That Increases Target-Shape Deformation in Identity Tasks
bibliography: references.bib
description: Increasing deformation of the configuration formed by targets harms identity
  tracking, and staggering tends to increase deformation.
labels:
- chart:scatter
- task:track
- visual:position
- impact:accuracy
- data:multivariate
- audience:expert
- animation:pacing
- task:identify
---

## The Rule <!-- role: advice -->

When users must track which target is which (identity tracking), avoid staggered pacing that increases deformation of the targets’ configuration over time.

## The Logic <!-- role: reason -->

The paper shows deformation (changes in inter-target distances over time) is a strong driver of difficulty for identity (ID) tracking; additionally, simulations show staggering tends to increase deformation by breaking coherent motion where points move together [@chevalierNotsoStaggeringEffectStaggered2014].

- **The Principle:** Identity tracking is sensitive to maintaining stable relational structure among targets; deformation disrupts these relations and increases identity swaps.
- **The Evidence:** Experiment 1 finds deformation harms ID performance (and increases misidentification); the staggering analysis shows deformation often increases under staggering, especially at higher dwell [@chevalierNotsoStaggeringEffectStaggered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Track multiple targets and retain their identities (e.g., which point corresponds to which entity).
- **Data Type:** Transitions where targets form a configuration (e.g., triangle of 3 targets) whose shape can stretch/compress over time.
- **Audience:** Analysts for whom identity swaps are costly.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Identity is externally reinforced (e.g., persistent encodings not removed during motion) such that identity swaps are less likely.
- **Reason:** The paper’s tasks intentionally removed distinguishing features during motion to test pure tracking; if identity is continuously visible, deformation may matter less (not tested here) [@chevalierNotsoStaggeringEffectStaggered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may forgo stagger styles that create strong “cascade” effects but distort group motion.
- **The Risk:** If you keep deformation low by avoiding stagger, you may preserve common motion cues but may not reduce crowding (trade-off) [@chevalierNotsoStaggeringEffectStaggered2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing dwell (more sequential motion) without checking whether it breaks coherent motion patterns among targets.
- **Why it fails:** The paper’s simulations show higher dwell can increase deformation, and deformation is especially harmful when identities must be maintained [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Targets appear to “accordion” relative to each other (inter-target distances change a lot), and viewers swap identities at the end.
- **The Test:** Track inter-target distances across frames; if these distances fluctuate more with staggering than without, you have increased deformation risk for ID tasks [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce or remove staggering (lower dwell toward simultaneous motion).
- **Best Fix:** Select or tune pacing that preserves coherent relational motion among targets (minimize deformation) while validating with an ID-tracking check (identity-specific accuracy) [@chevalierNotsoStaggeringEffectStaggered2014].
