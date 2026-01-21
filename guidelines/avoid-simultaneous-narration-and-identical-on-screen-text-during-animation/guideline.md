---
id: avoid-simultaneous-narration-and-identical-on-screen-text-during-animation
title: Remove Duplicate On-Screen Text When Narration and Animation Are Present
bibliography: references.bib
description: Reduce unnecessary processing by avoiding redundant streams of the same
  words in both audio and text when animation is also shown.
labels:
- chart:animation
- task:explain
- visual:attention
- impact:comprehension
- data:causal
- audience:novice
- principle:redundancy
- source:mayer-moreno-2003
---

## The Rule <!-- role: advice -->

When animation is paired with narration, do not also display the same sentences as on-screen text at the same time.

## The Logic <!-- role: reason -->

Presenting identical verbal information in speech and text can prompt learners to process and reconcile both streams, creating incidental processing that reduces capacity for essential processing of the animation and explanation.

- **The Principle:** Eliminating redundancy / Redundancy effect
- **The Evidence:** Learners show better transfer with narration-only words (with animation) than with narration+identical on-screen text [@mayerNineWaysReduce2003].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand an animated explanation of a system/process.
- **Data Type:** Any narrated animation where on-screen text would compete for visual attention.
- **Audience:** Learners at risk of split attention due to limited working memory.

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is no animation competing for the visual channel.
- **Reason:** The paper notes that adding on-screen text can help when it does not have to compete with animation [@mayerNineWaysReduce2003].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less support for users who prefer reading or need textual confirmation.
- **The Risk:** Accessibility constraints may require text support (but the guideline here is about avoiding *identical simultaneous duplication* during animation).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating captions as a verbatim transcript always visible during the animation.
- **Why it fails:** It creates redundant processing demands that can reduce understanding [@mayerNineWaysReduce2003].

## How to Check <!-- role: check -->

- **Visual Sign:** Users read the text and miss the animation events (or vice versa).
- **The Test:** If the on-screen text repeats the narration word-for-word while the animation runs, redundancy is present.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the verbatim on-screen text during the animation.
- **Best Fix:** Keep narration with animation as the primary pairing; if text is needed, avoid simultaneous verbatim duplication during animated segments [@mayerNineWaysReduce2003].
