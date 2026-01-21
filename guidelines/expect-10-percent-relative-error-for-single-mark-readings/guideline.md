---
id: expect-10-percent-relative-error-for-single-mark-readings
title: Plan for ~10% Relative Error in Single-Mark Readings
bibliography: references.bib
description: "People\u2019s reproduction error scales with value, yielding roughly\
  \ constant ~10% proportion-corrected error."
labels:
- chart:bar
- task:read-value
- visual:position
- impact:accuracy
- data:proportional
- audience:general
- model:weber-like
---

## The Rule <!-- role: advice -->

Assume viewers will be off by roughly 10% of the value when extracting a single bar/dot magnitude, and don’t design decisions that require finer discrimination without additional support.

## The Logic <!-- role: reason -->

Errors increased for larger presented values, but dividing error by the presented value yielded an approximately constant proportion-corrected error (~0.10). This is consistent with Weber-like scaling of precision for these mark reproductions.

- **The Principle:** Precision scales with magnitude (approximately constant relative error)
- **The Evidence:** Across conditions and experiments, average proportion-corrected error was ~10% and largely stable across values [@mccolemanNoMarkIsland2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Read a single value from a bar chart or dot plot (not a computed ratio report).
- **Data Type:** Percent-like magnitudes (1–99%) encoded by height/position.
- **Audience:** General users performing quick reads.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your task is not single-value extraction (e.g., explicit part-to-whole verbal ratio reporting).
- **Reason:** The paper targets a reproduction paradigm that removes verbal ratio translation; other tasks can introduce different error sources [@mccolemanNoMarkIsland2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to simplify claims or avoid emphasizing tiny differences.
- **The Risk:** Over-engineering precision expectations can lead to misleading takeaways if the chart implies viewers can reliably discriminate finer than they can.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating small visual differences as decisively readable because the encoding is “position/length (the best).”
- **Why it fails:** Even with these encodings, the measured reproduction precision is about 10% relative error on average [@mccolemanNoMarkIsland2021].

## How to Check <!-- role: check -->

- **Visual Sign:** The story depends on differences smaller than ~10% of the values involved (e.g., distinguishing 60% from 64%).
- **The Test:** Compute 10% of each critical value; if your claimed differences are at or below that threshold, your design is likely asking too much.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit numeric communication outside the mark reproduction burden (e.g., accompany with numbers in surrounding text).
- **Best Fix:** Redesign the analysis narrative to focus on differences that exceed the expected perceptual error band implied by the findings [@mccolemanNoMarkIsland2021].
