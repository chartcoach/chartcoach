---
id: avoid-conflicting-encodings-that-create-incongruent-anchors
title: Avoid Conflicting Encodings That Put Different Anchors on Different Items
bibliography: references.bib
description: "Don\u2019t split likely anchor cues (e.g., tallest and darkest) across\
  \ different marks when only one relation matters."
labels:
- chart:bar
- task:compare
- visual:color
- impact:efficiency
- data:categorical
- audience:novice
- custom:interference
- source:michal-franconeri-2017
---

## The Rule <!-- role: advice -->

When only one comparison is intended, do not introduce another varying visual dimension that makes a different item look like the “obvious” anchor.

## The Logic <!-- role: reason -->

Even when participants used a task-relevant anchor in their first saccade, a task-irrelevant dimension still produced behavioral interference: responses were slower when the likely anchor features from two dimensions were on different items (incongruent) than when they were on the same item (congruent).

- **The Principle:** Interference from task-irrelevant relations competing for attention
- **The Evidence:** In the orthogonal task (size+contrast varying), response times were faster for congruent vs. incongruent trials, indicating interference from the irrelevant dimension [@michalVisualRoutinesAre2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Make a quick, accurate judgment about one relation (e.g., which bar is taller / configuration ordering)
- **Data Type:** Comparisons where additional encodings (color/contrast) might vary incidentally
- **Audience:** Users under time pressure, students, or any setting where misdirected attention is costly

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires comparing two relations (e.g., both size and contrast are meaningful variables to interpret)
- **Reason:** The “conflict” is then informative; removing it would remove intended information [@michalVisualRoutinesAre2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced use of redundant encodings for additional information channels
- **The Risk:** Over-simplifying the display if secondary dimensions were actually important context

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Just tell users to ignore” the irrelevant dimension while still varying it strongly
- **Why it fails:** The paper shows that irrelevant variation can still slow judgments (congruency effects) despite instructions and task-dependent eye guidance [@michalVisualRoutinesAre2017].

## How to Check <!-- role: check -->

- **Visual Sign:** The tallest bar is not the darkest (or other “most” cues disagree), creating two competing “winners”
- **The Test:** Identify the likely anchor for each dimension present; if they point to different items during a single-relation task, you’ve created an incongruent display.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Hold the irrelevant encoding constant (e.g., uniform contrast) for that view.
- **Best Fix:** Separate relations into separate views/tasks so each view supports one anchor-driven routine without competition [@michalVisualRoutinesAre2017].
