---
id: use-closed-shapes-for-faster-shape-identification-under-attentional-selection
title: Prefer closed symbols over open symbols when fast, accurate shape identification
  is required
bibliography: references.bib
description: Closed shapes are identified faster and with fewer errors than open shapes
  in basic perceptual tasks.
labels:
- chart:scatter
- task:identify
- visual:shape
- impact:speed
- data:categorical
- audience:general
- encoding:open-closed
- evidence:lab-study
---

## Prefer closed symbols when viewers must rapidly identify a symbol <!-- role: advice -->

Prefer closed symbols (e.g., circle, square, triangle) over open symbols (e.g., plus, asterisk, ×) when the visualization requires rapid, accurate symbol identification. This is especially relevant when viewers must respond to a specific symbol under time pressure.

## Closed targets produce faster and more accurate responses <!-- role: reason -->

Closed shapes show a processing advantage over open shapes in tasks that require selecting, identifying, or matching symbols. This suggests that closed symbols can reduce latency and errors when the viewer’s task is anchored on recognizing a symbol rather than extracting an aggregate statistic.

**Mechanism:** Closed shapes may form more efficiently processed perceptual units, reducing decision time and errors when the viewer must map a seen symbol to a response or category.

**Evidence:** In a flanker paradigm, blocks using only closed target shapes yielded faster reaction times and lower error rates than blocks using only open target shapes, with mixed-category pairs in between [@burlinsonOpenVsClosed2018a]. In a Same/Different task, closed shapes produced faster responses and fewer errors than open shapes, and shapes within each open/closed category did not differ in the same-shape condition [@burlinsonOpenVsClosed2018a].

**Notes:** The closed-shape advantage was shown in low-level perceptual tasks; it did not appear as a main effect in homogeneous side-by-side scatterplot tasks.

## Context: When symbol recognition speed is the bottleneck <!-- role: context -->

- **User Goal:** Quickly identify which symbol is present, or rapidly map symbol-to-category.
- **Task:** Detection/identification, same/different matching, or rapid classification of points by symbol.
- **Data:** Categorical classes encoded by shape; decisions depend on symbol recognition.
- **Chart Setting:** Any view where shape is the primary differentiator and viewers are time-pressured or frequently switching attention between symbols.
- **Audience:** General audiences; viewers with limited time; tasks emphasizing speed and accuracy.
- **Success Criterion:** Lower reaction time and error rate for symbol-based responses.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The task is performed on homogeneous plots where only one symbol appears per plot and the decision does not require discriminating between symbol types within a view. **Why:** No response-time differences were observed between open and closed symbols in separate-plot baseline tasks [@burlinsonOpenVsClosed2018a].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Limits stylistic flexibility if brand or convention prefers open symbols. **Risk:** Closed symbols may be less effective if other constraints dominate (e.g., other encodings carry the category). **Mitigation:** Use closed symbols specifically for the categories that must be recognized most often or most quickly.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using only open symbols for key categories that viewers must repeatedly identify quickly (e.g., plus vs. asterisk for primary classes). **Why it fails:** Open targets were slower and more error-prone than closed targets in perceptual identification tasks [@burlinsonOpenVsClosed2018a].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users hesitate or misidentify symbol categories during quick lookups or rapid filtering. **Quick Check:** Swap an open symbol used for a frequently referenced class to a closed symbol and see if identification feels faster in informal testing. **Stronger Test:** Time a short symbol-identification exercise with the current palette versus a closed-symbol palette and compare errors and latency.

## Fix: What to do instead <!-- role: fix -->

- Replace open symbols used for the most frequently referenced categories with closed symbols.
- If open symbols must be used, reduce the number of distinct open symbols that viewers must discriminate.
- Move symbol discrimination out of the main view by separating categories into different panels so each panel is symbol-homogeneous.
- Reassign the most critical category to the symbol type that yields the lowest observed confusion in your display.
