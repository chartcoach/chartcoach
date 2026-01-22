---
id: treat-ensemble-judgments-as-four-perceptual-task-types
title: Classify ensemble judgments as identification, summarization, segmentation,
  or structure estimation before choosing encodings
bibliography: references.bib
description: Choose visual encodings by first identifying which ensemble-coding task
  type the viewer needs to perform.
labels:
- chart:scatter
- task:analyze
- visual:position
- impact:clarity
- data:quantitative
- audience:expert
- complexity:advanced
---

## Classify the ensemble-coding task type first <!-- role: advice -->

Classify what viewers must do as an identification, summarization, segmentation, or structure-estimation task before picking encodings. Use the task type to decide what kinds of visual statistics the display must support.

## Why task type determines which visual statistics are extractable <!-- role: reason -->

Different ensemble judgments rely on different perceptual operations over collections, so the same encoding can be effective for one task type (e.g., summarization) but ineffective for another (e.g., identification). Treating “ensemble coding” as one undifferentiated capability hides these differences and leads to mismatched encodings.

**Mechanism:** The visual system can rapidly compute different kinds of “summary” information over many marks, but the specific computation depends on whether the viewer is isolating items, averaging across items, grouping items into subsets, or inferring a relationship/structure across items.

**Evidence:** Ensemble coding tasks in data visualizations can be organized into four categories—identification, summarization, segmentation, and structure estimation—each corresponding to different kinds of judgments over visualized collections [@szafirFourTypesEnsemble2016]. A visualization-recommendation knowledge base can operationalize this task-level framing to translate perception literature into actionable guidance and constraints [@zengReviewCollationGraphical2023].

**Notes:** This guideline is about scoping the perceptual job; it does not assume one “best chart” across all four categories.

## When this task-first classification applies <!-- role: context -->

- **User Goal:** Decide something about a group/distribution of marks rather than a single mark.
- **Task:** Any of: find-extremum, find-anomalies, aggregate, characterize-distribution, retrieve-value, cluster, correlate.
- **Data:** Multiple data points where group-level properties (mean, variance, clusters, trends) matter.
- **Chart Setting:** Static charts where viewers must visually extract distributional information.
- **Audience:** Analysts or readers expected to make judgments from plotted collections.
- **Success Criterion:** The display supports the intended ensemble judgment with minimal confusion about what is being judged.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The viewer only needs single-item lookup with explicit labels or tooltips, not judgments over groups. **Why:** The task no longer depends on ensemble coding over collections.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need extra up-front clarification work (writing down the task type) before designing. **Risk:** Misclassifying the task can push you toward the wrong kind of encoding or chart. **Mitigation:** Validate the task description with a quick “what decision will you make from this view?” check.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating all “overview” needs as summarization (averaging) by default. **Why it fails:** Identification, segmentation, and structure estimation require different perceptual operations than summarization and can be poorly supported by a “mean-focused” design.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers argue about whether they are supposed to pick out specific points, estimate an overall average, find groups, or judge a relationship. **Quick Check:** Ask a reader to restate the task in one verb phrase; if it maps to more than one of the four categories, the task is underspecified. **Stronger Test:** Run a short pilot where users perform the target task and explain their strategy; mismatched strategies indicate misclassification.

## What to do instead <!-- role: fix -->

- Write the intended viewer action using one of: identify, summarize, segment, estimate-structure, then redesign to match.
- Split a single overloaded view into separate views when it is trying to support multiple task categories at once.
- Add explicit cues (titles, annotations) that name the intended task category (e.g., “Estimate overall trend” vs “Find the outliers”).
- If the task category cannot be made unambiguous, re-scope the question to a single category and defer other questions to follow-up views.
