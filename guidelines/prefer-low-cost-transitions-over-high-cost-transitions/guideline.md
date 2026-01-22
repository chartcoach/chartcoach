---
id: prefer-low-cost-transitions-over-high-cost-transitions
title: Prefer lower transformation-cost transitions when choosing the next slide
bibliography: references.bib
description: When multiple next-slide options exist, prioritize the one that differs
  from the current slide on fewer data attributes.
labels:
- chart:multi
- task:sequence
- visual:layout
- impact:clarity
- data:multivariate
- audience:general
- complexity:intermediate
---

## Choose the next slide with the fewest attribute differences <!-- role: advice -->

When selecting what visualization should follow the current one, prefer the candidate that changes fewer key attributes (dimension, measure, time, granularity) relative to the current slide.

## Lower-cost next steps match viewer expectations for continuity <!-- role: reason -->

When multiple candidate continuations are possible, viewers tend to judge the continuation with smaller differences as the better “next” step in a narrative sequence.

**Mechanism:** Lower differences support continuity and comparison by helping viewers reuse their current mental model of the view while updating only one aspect.

**Evidence:** In cost-varying choices, participants were much less likely to choose higher-cost transitions compared to cost-1 transitions, showing a strong preference for lower-cost next steps in a slideshow sequence [@hullmanDeeperUnderstandingSequence2013].

**Notes:** The reported results showed a clear preference for cost-1 over cost-2 or cost-3 options in the study’s setup.

## Context: When you have multiple plausible next-slide candidates <!-- role: context -->

- **User Goal:** Pick a “best next” slide among several candidate views.
- **Task:** Sequence/authoring decision-making during story construction.
- **Data:** Many pre-made views that differ along multiple attributes.
- **Chart Setting:** Linear narrative (slide deck, scrollytelling steps, stepper UI).
- **Audience:** General audiences where the author wants predictable transitions.
- **Success Criterion:** The audience perceives the flow as coherent with minimal confusion between steps.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The story needs a hard pivot to a new topic to reset context. **Why:** A higher-cost transition can act as a boundary marker between segments.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Potentially fewer “interesting” jumps, since you bias toward incremental change. **Risk:** You may miss a rhetorically effective juxtaposition. **Mitigation:** Use occasional high-cost jumps only at clearly marked narrative boundaries.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Picking the next slide solely because it is individually compelling, ignoring how much it differs from the current slide. **Why it fails:** The narrative is experienced as a sequence; high per-slide quality does not prevent a confusing transition.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** The next slide feels unrelated unless the viewer rereads titles/labels. **Quick Check:** Compare candidates by counting changed attributes; pick the smallest count. **Stronger Test:** Run a simple pairwise preference test with viewers for the candidate next slides.

## Fix: What to do instead <!-- role: fix -->

- Create an intermediate view that bridges the current and desired next view by changing only one attribute.
- Reframe the intended next view so it shares the current slide’s dimension or time, then introduce the remaining change afterward.
- Split one complex intended transition into two simpler ones by separating time changes from measure/dimension changes.
- If a large jump is necessary, treat it as a new segment and provide explicit framing text before the jump.
