---
id: respect-bar-vs-line-conventions-for-intended-message
title: 'Match Chart Type to the Message: Bars for Comparisons, Lines for Trends'
bibliography: references.bib
description: Choose conventional graph types that align with what viewers expect to
  extract.
labels:
- chart:bar
- task:compare
- visual:schema
- impact:comprehension
- data:categorical
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Use **bar charts** when you want viewers to focus on **discrete comparisons**; use **line charts** when you want viewers to focus on **continuous trends**.

## The Logic <!-- role: reason -->

- **The Principle:** Viewers apply learned graph schemas that steer interpretation.
- **The Evidence:** The paper reports that people describe the same dataset differently depending on whether it’s shown as bars (comparisons) or lines (trends), and mismatches can produce erroneous inferences [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpreting the intended relationship (comparison vs trend).
- **Data Type:** Discrete categories (bars) vs ordered/continuous sequences (lines).
- **Audience:** General audiences relying heavily on familiar conventions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When you explicitly need to violate convention for a special purpose and can clearly teach the mapping.
- **Reason:** Breaking schemas is possible but demands additional guidance and careful design [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some flexibility; the “best” analytic form might be less conventional.
- **The Risk:** If you choose a nonstandard mapping, viewers may import the wrong interpretation automatically.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a line chart for a binary categorical comparison because it “looks cleaner.”
- **Why it fails:** Viewers may infer a continuous dimension or causal continuum where none exists [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers describe trends when you intend discrete differences (or vice versa).
- **The Test:** Ask a naive viewer to describe “what this shows” in one sentence; if they give the wrong kind of statement, the schema is mismatched.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to the conventional chart type that matches the intended message.
- **Best Fix:** If you must keep the unconventional form, add strong annotation and layout cues that explicitly frame the intended interpretation [@zacksDesigningGraphsDecisionMakers2020].
