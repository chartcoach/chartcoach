---
id: avoid-staggered-transitions-for-multi-object-tracking
title: Avoid Staggering When Users Must Track Many Moving Marks
bibliography: references.bib
description: "Staggered start times rarely improve\u2014and can sometimes hurt\u2014\
  people\u2019s ability to track multiple moving elements during animated transitions."
labels:
- chart:scatter
- task:track
- visual:position
- impact:accuracy
- data:multivariate
- audience:expert
- animation:pacing
---

## The Rule <!-- role: advice -->

Avoid staggered animated transitions (incremental per-element start delays) when users must visually track multiple elements across a transition.

## The Logic <!-- role: reason -->

Staggering can slightly reduce proximity-based interference (crowding) in some cases, but the paper finds that these benefits are generally negligible and can be outweighed by costs introduced by non-simultaneous motion (loss of shared motion cues and less predictable motion start times), yielding little or even negative impact on tracking performance [@chevalierNotsoStaggeringEffectStaggered2014].

- **The Principle:** Tracking performance is strongly limited by inter-object spacing/crowding, and additional pacing irregularities can remove helpful motion-grouping and predictability cues.
- **The Evidence:** The authors’ simulations show only modest/rare crowding reductions from staggering and potential increases in deformation; their controlled experiment finds only small best-case gains and otherwise negligible effects [@chevalierNotsoStaggeringEffectStaggered2014].

## Where to Apply <!-- role: context -->

This advice is designed for transitions where maintaining correspondence of individual marks matters.

- **User Goal:** Track multiple items from old positions to new positions (correspondence).
- **Data Type:** Dense point sets / dot clouds (e.g., animated scatterplot remapping).
- **Audience:** Analysts who rely on accurate element correspondence.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The transition is primarily aesthetic or attention-directing and exact correspondence is not required.
- **Reason:** The paper notes staggering may “feel” easier even when it does not measurably improve tracking, so it can still be acceptable when accuracy is not the goal [@chevalierNotsoStaggeringEffectStaggered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up a familiar staggered “cascade” aesthetic.
- **The Risk:** If you do stagger anyway, you risk reduced motion predictability and weaker common-motion grouping, which can negate any crowding reduction [@chevalierNotsoStaggeringEffectStaggered2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding staggering to “reduce occlusion” by default.
- **Why it fails:** The paper finds crowding reductions are modest/rare on general dot-cloud transitions, and staggering can introduce new perceptual costs that cancel the benefit [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers frequently lose track of which dot became which, even though motion looks smoother or “less overwhelming.”
- **The Test:** Run a quick internal MOT-style check: cue 3 targets, animate, then ask viewers to identify their final locations/identities; compare staggered vs non-staggered accuracy [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Turn staggering off (start all marks simultaneously with the same overall duration).
- **Best Fix:** If you must use staggering, restrict it to cases where you can verify it reduces target crowding without increasing other complexity factors (see other guidelines) [@chevalierNotsoStaggeringEffectStaggered2014].
