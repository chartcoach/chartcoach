---
id: do-not-optimize-only-for-common-axis-position-when-tasks-are-not-value-ratio
title: Do not optimize only for common-axis position when the task is not two-value
  ratio reading
bibliography: references.bib
description: "Choose encodings based on the user\u2019s actual perceptual task, not\
  \ just maximum precision for reading individual ratios."
labels:
- chart:scatter
- chart:dot
- task:compare
- visual:position
- impact:clarity
- data:quantitative
- audience:general
- complexity:foundational
---

## Match encoding choice to the perceptual task, not only ratio precision <!-- role: advice -->

Do not default to dot plots or scatter plots just because position on a common axis is most precise for reading two-value ratios. Choose encodings that support the specific perceptual judgment the viewer needs to make.

## Perceptual tasks extend beyond two-point ratio extraction <!-- role: reason -->

A ranking derived from how precisely viewers judge the ratio between two encoded values does not automatically transfer to other common visualization tasks, such as judging the “big picture,” summarizing sets of values, filtering, or spotting patterns. When the viewer’s goal is not “read two values precisely,” an encoding optimized for that narrow operation can be a poor fit for how people actually perceive and interpret collections, trends, and emergent structure.

**Mechanism:** Different tasks rely on different perceptual operations (pairwise metric judgments, ordinal judgments, ensemble/aggregate perception, pattern perception), and some “less precise” channels for individual values can better support holistic or aggregate judgments.

**Evidence:** Many practical visualization tasks go beyond two-point ratio judgments, and evidence about channel performance for those tasks is often sparse or does not align with a “position is always best” conclusion [@bertiniWhyShouldntAll2020]. Example comparisons show that a position-only dot plot can be subjectively worse for seeing overall structure than alternatives like line charts (trend/shape cues) or heatmaps (overview of distributions), despite reduced precision for exact value extraction [@bertiniWhyShouldntAll2020].

**Notes:** This does not reject channel rankings; it limits their scope to the tasks they were derived from.

## Contexts where precision-first position encoding is the wrong default <!-- role: context -->

- **User Goal:** Understand overall structure, patterns, or distributions; not read exact values.
- **Task:** Summarize, cluster, detect outliers, compare averages, judge trend/shape, filter “high vs. low,” or other N-point judgments.
- **Data:** Many values (grids, time series collections, matrices), where emergent patterns matter.
- **Chart Setting:** Overview-first or exploratory views where “big picture” comprehension is primary.
- **Audience:** Mixed or time-constrained readers who need fast gestalt rather than exact extraction.
- **Success Criterion:** Correct high-level inference (pattern, trend, grouping) more than exact numeric accuracy.

## Exceptions: when position-first is appropriate <!-- role: exceptions -->

**Break it when:** The dominant task is reading or comparing specific values (especially ratios/differences) with high numeric accuracy. **Why:** Position on a common axis is optimized for that narrow perceptual judgment and can reduce error.

## Costs of task-matched (not precision-maximized) encoding choices <!-- role: costs -->

**Sacrifice:** You may lose exact numeric readability for individual points. **Risk:** Viewers may misinterpret magnitudes if they try to do precise lookup from an encoding meant for overview. **Mitigation:** Clarify intent with labels/annotations or provide details-on-demand if interaction is available.

## Mistakes: common misapplications of channel rankings <!-- role: mistakes -->

**Mistake:** Replacing a visualization that supports overview or pattern tasks with a scatter/dot plot solely to increase “precision.” **Why it fails:** It optimizes the wrong perceptual operation and can make the intended “big picture” judgment harder [@bertiniWhyShouldntAll2020].

## Check: quick tests for task–encoding mismatch <!-- role: check -->

**Failure Sign:** Viewers can read points precisely but struggle to describe patterns, clusters, or trends without laborious point-by-point inspection. **Quick Check:** Ask what single sentence the viewer should be able to say after a 5–10 second glance; if it’s a pattern/trend summary, a position-only design may be misfit. **Stronger Test:** Pilot two designs with a task that matches the real goal (e.g., summarization or pattern finding) and compare success rates, not just value-reading error.

## Fix: what to do instead of a scatter/dot-by-default approach <!-- role: fix -->

- Use a line chart or connected representation when the intended judgment is trend/shape over ordered data.
- Use a heatmap when the intended judgment is overview across a 2D grid of values and emergent patterns matter.
- Add encodings that create useful emergent cues (e.g., connection/shape cues) when the task is holistic rather than pointwise.
- Split tasks: provide an overview design for pattern detection and a separate precise view for exact value lookup.
