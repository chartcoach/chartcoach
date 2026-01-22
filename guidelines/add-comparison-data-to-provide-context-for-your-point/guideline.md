---
id: add-comparison-data-to-provide-context-for-your-point
title: Add comparison data that directly supports the point you want to make
bibliography: references.bib
description: Make the chart meaningful by adding the comparisons needed to put the
  main series into perspective.
labels:
- chart:general
- task:compare
- visual:position
- impact:clarity
- data:general
- audience:general
- technique:comparison
---

## Add the comparison series or baseline your claim depends on <!-- role: advice -->

Include the comparison data that lets readers judge your main series in context, choosing comparisons that directly support the point your headline makes.

## Why comparison data turns a value into an interpretable message <!-- role: reason -->

Without an explicit reference, many values and trends are hard to interpret; comparisons provide the context that makes magnitude and meaning legible and relatable.

**Mechanism:** Comparisons create a reference frame (across time, groups, peers, or alternatives) that lets readers evaluate whether a pattern is notable and how strong it is.

**Evidence:** Comparisons are central to making data visualization informative, and selecting the right comparison depends on the point the chart needs to prove [@muth_better_charts_2017].

**Notes:** The “right” comparison is not universal; it is the one that answers “compared to what?” for the specific message.

## When to add comparison data <!-- role: context -->

- **User Goal:** Understand whether something is large/small, growing/declining, or exceptional.
- **Task:** Compare a focal series against peers, alternatives, or a prior period to assess significance.
- **Data:** Any dataset where a single series could be misread without reference (e.g., product performance, category totals).
- **Chart Setting:** Explanatory charts where the takeaway depends on relative performance.
- **Audience:** General audiences who may not have internal benchmarks for the metric.
- **Success Criterion:** The reader can answer “Is this big?” or “Is this unique?” from the chart alone.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Additional comparisons would clutter the chart so much that the focal message becomes hard to see. **Why:** Excess series can overwhelm attention and reduce interpretability.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More data preparation and more visual complexity. **Risk:** Irrelevant comparisons can distract or change the story away from the intended point. **Mitigation:** Keep comparisons tightly tied to the specific claim.

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Adding “nice to have” series that are not needed to evaluate the claim. **Why it fails:** The chart becomes busy without improving understanding.
- **Mistake:** Using comparisons that don’t match the stated point. **Why it fails:** Readers can’t verify the headline because the reference frame is misaligned.

## Quick tests <!-- role: check -->

**Failure Sign:** The chart shows a trend but the reader can’t say whether it is impressive or merely normal. **Quick Check:** Ask “Compared to what?”; if the chart can’t answer, it needs a comparison. **Stronger Test:** Ask a reader to justify the headline using only what is plotted; if they need outside facts, the comparison context is missing.

## What to do instead <!-- role: fix -->

- Add a small set of directly relevant peer series that represent the alternatives readers would naturally compare against.
- Replace multiple peer series with a single benchmark series that captures the needed context.
- If the comparison is the real story, redesign the chart around the comparison (e.g., make the focal and comparator series equally readable).
- Move secondary comparisons into a separate chart if they cannot be shown without diluting the main message.
