---
id: account-for-transformed-values-when-writing-items-for-relative-or-derived-encodings
title: Account for transformed values when writing items for relative, approximate,
  or derived encodings
bibliography: references.bib
description: 'Write items that match what the chart actually encodes: relative proportions,
  approximate bins, or derived counts rather than raw values.'
labels:
- chart:stacked-bar
- chart:pie
- chart:treemap
- chart:choropleth
- chart:histogram
- task:retrieve
- visual:position
- impact:validity
- data:categorical
- audience:novice
- method:assessment
---

## Account for transformed values when writing items for relative, approximate, or derived encodings <!-- role: advice -->

Write questions to match whether a visualization encodes absolute values, relative proportions, approximate ranges, or derived values, and avoid asking for raw values when the encoding does not support them.

## Why mismatched value types create invalid difficulty <!-- role: reason -->

If an item asks for information not directly represented by the marks (e.g., absolute values from a purely relative encoding), errors may reflect impossible inference rather than low literacy. Aligning the value type in the stem with the value type encoded ensures performance reflects reading and interpretation skill.

**Mechanism:** Item-to-encoding alignment reduces construct-irrelevant variance caused by requiring unencoded computation or guessing.

**Evidence:** The VLAT blueprint explicitly distinguishes cases where tasks rely on relative values (e.g., pie, 100% stacked bar, treemap), approximate values (choropleth), or derived values (histogram bins), and marks these as special cases in task assignment [@leeVLATDevelopmentVisualization2017].

**Notes:** Some charts (stacked bar/stacked area) can support both absolute and relative reasoning depending on the task.

## When value-type alignment matters most <!-- role: context -->

- **User Goal:** Assess reading/interpretation rather than unencoded computation.
- **Task:** Item writing and task selection per visualization type.
- **Data:** Compositional data, binned distributions, region-level rates, hierarchical totals.
- **Chart Setting:** Static charts without interaction for exact lookup.
- **Audience:** Non-experts likely to rely on what is visually explicit.
- **Success Criterion:** Item difficulty reflects reasoning demand, not missing encodings.

## When to intentionally break alignment <!-- role: exceptions -->

**Break it when:** You explicitly want to test whether readers notice that the chart cannot support an absolute read (a “chart limitation awareness” item). **Why:** The target outcome is meta-comprehension of encodings, not value retrieval.

## Tradeoffs of strict alignment <!-- role: costs -->

**Sacrifice:** Some potentially interesting questions are excluded because they require computations not visually available. **Risk:** Over-simplifying tasks to only what is obvious in the encoding. **Mitigation:** Use multiple item types per chart (absolute vs relative where supported) to maintain challenge.

## Common alignment mistakes <!-- role: mistakes -->

**Mistake:** Asking for exact state values from a choropleth with binned legend ranges. **Why it fails:** The display provides only approximate ranges, so the task becomes guesswork.

## Quick checks for alignment <!-- role: check -->

**Failure Sign:** Participants’ wrong answers cluster around plausible-but-unencoded numeric choices. **Quick Check:** For each item, point to the exact mark/legend element that directly supports the requested answer type. **Stronger Test:** Have an independent reviewer attempt the item using only the displayed encoding without additional calculations.

## What to do if an item needs information the chart does not encode <!-- role: fix -->

- Rewrite the stem to ask for relative, approximate, or derived values consistent with the encoding.
- Switch to a visualization type that directly encodes the needed value type for the task.
- Add explicit legend/annotation changes that make the requested value type readable (while keeping the visualization static if required).
- Remove the item from the instrument if it measures computation beyond reading/interpretation.
