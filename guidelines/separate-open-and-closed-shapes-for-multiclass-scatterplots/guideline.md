---
id: separate-open-and-closed-shapes-for-multiclass-scatterplots
title: Assign categories to symbols from different open/closed shape classes in dense
  multiclass scatterplots
bibliography: references.bib
description: Use one open and one closed symbol (rather than two opens or two closeds)
  to reduce perceptual interference when comparing classes in a scatterplot.
labels:
- chart:scatter
- task:compare
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- encoding:open-closed
- complexity:advanced
---

## Prefer cross-category open/closed symbol pairings for class separation <!-- role: advice -->

Assign different categories to symbols drawn from different open/closed shape classes (one open, one closed) when multiple classes must be discriminated within the same scatterplot. Avoid mapping two categories to two different symbols that are both open or both closed when the display is cluttered.

## Open/closed class boundaries reduce within-category competition <!-- role: reason -->

Open and closed symbols behave like perceptual categories: discriminating between symbols within the same category produces more interference than discriminating across the open/closed boundary. In heterogeneous plots where viewers must separate two interleaved symbol sets, same-category distractors slow judgments and increase errors compared to different-category distractors.

**Mechanism:** Categorization by “open” versus “closed” reduces competition during attentional selection; when target and distractor share the same open/closed class, processing interference increases.

**Evidence:** In a Same/Different reaction-time task, different-shape/same-feature (same open/closed class) trials were significantly slower than different-shape/different-feature trials, and closed shapes were processed faster overall than open shapes [@burlinsonOpenVsClosed2018a]. In single-plot scatterplot tasks, same-feature distractors lengthened reaction times and increased errors for numerosity and linear-relationship judgments compared to different-feature distractors [@burlinsonOpenVsClosed2018a].

**Notes:** Effects were most evident when symbols were mixed within one plot (heterogeneous displays), not when plots were separated and each plot used a single symbol type.

## Contexts where symbol interference matters most <!-- role: context -->

- **User Goal:** Distinguish multiple categorical classes of points without misattribution.
- **Task:** Compare two classes within one plot (e.g., which class is more numerous or shows a stronger trend).
- **Data:** Many points; overplotting or close spacing; at least two categories shown together.
- **Chart Setting:** Single scatterplot (not small multiples) with two symbol types interleaved.
- **Audience:** General audiences or time-constrained analysts who rely on fast perceptual separation.
- **Success Criterion:** Faster and more accurate class-based judgments under clutter.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Each category is shown in separate plots (small multiples) rather than mixed in one plot. **Why:** Open/closed differences did not affect response times in separate-plot baseline tasks where each plot was homogeneous [@burlinsonOpenVsClosed2018a].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reduces the available symbol palette if you reserve open/closed as a primary grouping dimension. **Risk:** Overcommitting to open/closed may limit differentiation among more than two categories if shape is the only channel. **Mitigation:** Treat open/closed as the first split (coarse grouping) and use additional encodings for additional classes.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding two classes with two different open symbols (e.g., plus vs. asterisk) in a dense plot. **Why it fails:** Within-category discrimination produces more interference than across-category discrimination in both perceptual and plot-based tasks [@burlinsonOpenVsClosed2018a].
- **Mistake:** Encoding two classes with two different closed symbols (e.g., square vs. triangle) in a dense plot. **Why it fails:** Same-category distractors caused slower and less accurate judgments in heterogeneous plot tasks [@burlinsonOpenVsClosed2018a].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers frequently confuse which points belong to which class, or take noticeably longer when two symbol types are mixed. **Quick Check:** Toggle one class’s symbol from open to closed (or vice versa) and see if class separation becomes immediately easier at a glance. **Stronger Test:** Run a short timed numerosity or trend-identification pilot with same-category vs different-category symbol pairings and compare reaction times and accuracy.

## Fix: What to do instead <!-- role: fix -->

- Use one open and one closed symbol for the two most important classes that must be compared within the same plot.
- If you must keep same-category symbols, switch from a single mixed plot to separate plots so each plot is symbol-homogeneous.
- Reduce heterogeneous interference by limiting the number of symbol types shown simultaneously in one panel.
- Reframe the task so the judgment can be made without per-point class discrimination (for example, separate the classes into separate views).
