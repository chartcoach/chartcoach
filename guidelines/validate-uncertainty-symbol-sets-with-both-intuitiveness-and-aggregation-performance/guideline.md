---
id: validate-uncertainty-symbol-sets-with-both-intuitiveness-and-aggregation-performance
title: Validate uncertainty symbol sets with both intuitiveness ratings and multi-symbol
  aggregation tasks
bibliography: references.bib
description: 'Assess uncertainty symbols with a two-stage evaluation: perceived logical
  mapping and performance in region-level aggregation with multiple symbols.'
labels:
- chart:map
- task:evaluate
- visual:encoding
- impact:confidence
- data:uncertainty
- audience:expert
- process:user-testing
---

## Test uncertainty symbols for both perceived logic and task performance before adopting them <!-- role: advice -->

Evaluate candidate uncertainty symbol sets with an intuitiveness rating task and a separate task that requires aggregating uncertainty across multiple points, then choose symbols based on the outcome that matches your usage.

## Why two tests are needed to choose robust uncertainty symbols <!-- role: reason -->

Perceived logic (intuitiveness) and operational effectiveness (accuracy/speed in a map-like task) do not necessarily align, especially when iconic metaphors introduce extra processing cost.

**Mechanism:** A symbol can be easy to “agree with” in isolation yet still be slow or error-prone when repeated many times in a dense display that requires aggregation.

**Evidence:** Symbol sets varied in intuitiveness across uncertainty conditions, and iconic sets tended to take longer to rate even when judged slightly more intuitive overall [@maceachrenVisualSemioticsUncertainty2012]. In a region-comparison aggregation task, uncertainty condition significantly affected both accuracy and response time, and iconicity affected response time without a consistent accuracy advantage [@maceachrenVisualSemioticsUncertainty2012].

**Notes:** Using both tests helps surface tradeoffs between interpretability and speed.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Reliably read uncertainty in real use, not just in a legend.
- **Task:** Mix of symbol decoding and aggregating across many marks.
- **Data:** Repeated point symbols; uncertainty shown per item.
- **Chart Setting:** Production dashboards/maps where symbol choice will be reused.
- **Audience:** GIS/visualization-literate users or mixed groups.
- **Success Criterion:** Chosen symbols support the intended task (fast vs. accurate vs. intuitive).

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is purely illustrative and not used for repeated judgments. **Why:** Task-performance optimization is less critical if no decisions depend on it.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Running two evaluations increases design time. **Risk:** Overfitting to a single lab task may miss other real-world tasks. **Mitigation:** Align evaluation tasks with your actual user workflow.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Selecting symbols solely from preference or “looks intuitive” feedback. **Why it fails:** Intuitiveness and performance can diverge in multi-symbol displays.
- **Mistake:** Testing only single-symbol interpretation. **Why it fails:** Aggregation across many points introduces different perceptual demands.

## Quick tests <!-- role: check -->

**Failure Sign:** Symbols feel understandable but users are slow when scanning a full map. **Quick Check:** Run a timed region-comparison with a handful of users. **Stronger Test:** Compare multiple symbol sets across the same set of region configurations and measure both accuracy and response time.

## What to do instead <!-- role: fix -->

- Add a second evaluation task that mimics real map reading (e.g., region-level uncertainty comparison).
- Keep evaluation stimuli consistent across symbol sets so difficulty is comparable.
- Use both accuracy and response time to decide between symbol options.
- Re-run the test when changing symbol size, density, or background context.
