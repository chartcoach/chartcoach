---
id: avoid-same-open-closed-class-symbol-pairs-for-numerosity-and-trend-judgments
title: Avoid using two symbols from the same open/closed class for numerosity or trend
  judgments in a single scatterplot
bibliography: references.bib
description: Same-class open/closed distractors slow and degrade numerosity and linear-relationship
  judgments when two symbol sets are mixed.
labels:
- chart:scatter
- task:estimate
- visual:shape
- impact:accuracy
- data:categorical
- audience:general
- task:numerosity
- task:trend
---

## Use different open/closed classes for mixed-symbol numerosity and trend tasks <!-- role: advice -->

When a single scatterplot mixes two symbol sets and viewers must judge which set is more numerous or which set shows a linear relationship, use symbols from different open/closed classes. Do not pair two open symbols or two closed symbols for these mixed-symbol judgments.

## Same-class distractors interfere with ensemble judgments that require segregation <!-- role: reason -->

Numerosity and trend judgments in heterogeneous displays depend on first segregating points by symbol type before extracting the higher-level property. When the two symbol types are within the same open/closed class, interference increases; when they cross the open/closed boundary, segregation is easier and judgments are faster and/or more accurate.

**Mechanism:** Open/closed categorization supports rapid partitioning of the visual field into two sets; weakening that partition (same-class pairings) increases distractor competition during ensemble coding.

**Evidence:** In single-plot numerosity tasks, same-feature (same open/closed class) distractors increased reaction times by hundreds of milliseconds and increased errors relative to different-feature distractors, with effects modulated by whether the target was open or closed [@burlinsonOpenVsClosed2018a]. In single-plot linear-relationship tasks, closed targets were faster than open targets and same-feature distractors lengthened reaction times, with strong interactions across difficulty levels [@burlinsonOpenVsClosed2018a].

**Notes:** These effects were not observed in homogeneous, separate-plot displays where viewers did not need to segregate two symbol sets within the same panel.

## Context: When ensemble coding depends on separating two symbol sets <!-- role: context -->

- **User Goal:** Decide which class has more points or which class follows a linear relationship.
- **Task:** Numerosity comparison or trend identification for one of two interleaved classes.
- **Data:** Two categorical classes encoded by shape; many marks; possible clutter.
- **Chart Setting:** Single plot with both symbol sets shown together; limited interaction; fast judgments.
- **Audience:** General audiences; analysts scanning many plots.
- **Success Criterion:** Faster reaction time and fewer class-attribution errors.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The two classes are not interleaved (e.g., clearly separated clusters) or are shown in separate plots. **Why:** The interference effect is tied to mixed, heterogeneous displays that force symbol-based segregation before judgment [@burlinsonOpenVsClosed2018a].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Constrains which exact symbols you can choose if you must also satisfy other design constraints. **Risk:** Over-relying on open/closed may not generalize to tasks like average-value judgments where effects were weak or inconsistent. **Mitigation:** Treat this as task-specific guidance for numerosity and linear-relationship judgments.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Pairing square and triangle (both closed) for two classes and asking viewers to identify which class shows the trend. **Why it fails:** Same-feature distractors increased interference in mixed-symbol trend judgments [@burlinsonOpenVsClosed2018a].
- **Mistake:** Pairing plus and asterisk (both open) for two classes and asking which class is more numerous. **Why it fails:** Same-feature distractors increased reaction times and errors in mixed-symbol numerosity judgments [@burlinsonOpenVsClosed2018a].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users frequently misattribute points to the wrong class when estimating “which has more” or “which is linear,” or they slow down markedly. **Quick Check:** Swap one class’s symbol across the open/closed boundary and see if the judgment becomes easier without changing data. **Stronger Test:** Run a small timed test on your own plots: same-class symbol pairing versus different-class pairing, tracking accuracy and reaction time.

## Fix: What to do instead <!-- role: fix -->

- Replace one of the two symbols so the pair crosses the open/closed boundary (one open, one closed).
- If symbols must remain same-class, switch to separate plots so each plot contains only one symbol type.
- Reduce the need for segregation by decreasing clutter (fewer points or less overlap) before running the numerosity or trend task.
- Change the workflow so the numerosity or trend judgment is made on one class at a time rather than on two interleaved symbol sets.
