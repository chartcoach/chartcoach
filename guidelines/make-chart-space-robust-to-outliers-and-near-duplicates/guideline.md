---
id: make-chart-space-robust-to-outliers-and-near-duplicates
title: Make chart space robust to outliers and near-duplicates (or disclose and let
  users filter)
bibliography: references.bib
description: Prevent extreme values or near-identical values from collapsing the readable
  chart area by adapting the view or clearly disclosing the issue and enabling user-driven
  filtering.
labels:
- chart:general
- task:compare
- visual:position
- impact:accessibility
- data:quantitative
- audience:general
- heuristic:assistive
---

## Handle outliers and near-duplicates without collapsing the plot area <!-- role: advice -->

Ensure extreme outliers and near-identical values do not compress marks into unreadable space; the chart must adapt automatically or clearly annotate what is happening and provide a way to sort, split, or filter the view.

## Why extremes break readability and increase user labor <!-- role: reason -->

When a single scale must accommodate values that are extremely far apart or extremely close together, the chart can stop functioning as a perceptual aid: marks become visually indistinguishable, meaningful comparisons require extra effort, and users must compensate by mentally reconstructing structure or by trial-and-error interaction. Reducing that labor is assistive because it preserves the chart’s role as an efficient interface for understanding data rather than forcing users to “fight” the space allocation.

**Mechanism:** Adaptive layout or explicit disclosure prevents the chart from hiding variation (near-duplicates) or hiding structure (outliers) by avoiding wasted or over-contended space, making the data readable without requiring extra cognitive work.

**Evidence:** Managing white space as a deliberate design element supports readability by preventing visual crowding and improving clarity when space is constrained or misallocated [@towardsdatascience_data_visualisation_2]. Reducing the labor required to interpret and operate a visualization is a core accessibility auditing concern for data interfaces, especially when real data and user-driven parameters produce extreme distributions [@elavskyHowAccessibleMy2022].

**Notes:** This guideline addresses both extremes in magnitude (outliers stretching scales) and extremes in similarity (near-overlap that makes differences hard to perceive).

## Where this shows up in real charts and interactive dashboards <!-- role: context -->

- **User Goal:** Detect patterns, compare values, and notice differences that matter.
- **Task:** Compare series or categories when values may be unevenly distributed or nearly identical.
- **Data:** Quantitative data with outliers, heavy tails, or clusters of very similar values; often driven by dynamic filtering or parameter changes.
- **Chart Setting:** Interactive analytical environments where chart type is fixed but data changes via controls; static exports that cannot rely on user interaction still need disclosure.
- **Audience:** Mixed audiences, including people who rely on clarity and reduced cognitive load to interpret the visualization efficiently.
- **Success Criterion:** Differences and structure remain legible without requiring disproportionate user effort; the chart communicates when scale effects are distorting visibility.

## When not to apply this rule as written <!-- role: exceptions -->

**Break it when:** The data and task intentionally require a single unbroken scale to preserve a specific, non-negotiable comparison across views. **Why:** Altering the space allocation could undermine the intended meaning of that fixed comparison and conflict with the communicative goal [@elavskyHowAccessibleMy2022].

## Tradeoffs of adapting space for extremes <!-- role: costs -->

**Sacrifice:** Adaptive handling can add design and implementation complexity, especially in parameter-driven dashboards. **Risk:** Users may misunderstand what changed (for example, why a view looks different after filtering) if the adaptation is not made transparent. **Mitigation:** Clear, visible annotations that disclose what is happening reduce confusion and keep the experience understandable [@elavskyHowAccessibleMy2022].

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Letting an outlier force all other values into an unreadable sliver without any disclosure. **Why it fails:** The chart stops supporting comparison and shifts interpretation work onto the user [@elavskyHowAccessibleMy2022].
- **Mistake:** Showing multiple lines or series that are nearly overlapping with no alternative view or user control. **Why it fails:** Visual differences become effectively invisible, making the chart unreadable for similarity-heavy data [@elavskyHowAccessibleMy2022].
- **Mistake:** Assuming “white space is wasted space” and not treating space as a readability tool. **Why it fails:** Poor space allocation increases crowding and reduces clarity, especially under extremes [@towardsdatascience_data_visualisation_2].

## Fast ways to spot the problem during an audit <!-- role: check -->

**Failure Sign:** Most marks appear compressed into margins or overlap so tightly that differences cannot be distinguished, especially after filtering or parameter changes. **Quick Check:** Try the chart’s most extreme plausible filter/parameter settings and see whether comparisons remain readable without guesswork. **Stronger Test:** Ask a reviewer to describe what changes between two very close series or among non-outlier values; if they cannot do so without extra steps, the space handling is failing [@elavskyHowAccessibleMy2022].

## Practical remediations when space collapses <!-- role: fix -->

- Add an explicit annotation that explains when outliers or near-duplicates are compressing the readable area and what that implies for interpretation.
- Provide controls that let users sort, split, or filter the data so they can reclaim readable space when automatic adaptation is not feasible.
- Change the chart type or representation when the current form cannot make close differences or non-outlier structure legible under the data’s extrema.
- Ensure white space is treated as a readability resource by adjusting layout so the view does not waste space where it harms clarity [@towardsdatascience_data_visualisation_2].
