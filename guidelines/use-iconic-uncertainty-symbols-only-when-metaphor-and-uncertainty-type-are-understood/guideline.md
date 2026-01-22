---
id: use-iconic-uncertainty-symbols-only-when-metaphor-and-uncertainty-type-are-understood
title: Use iconic uncertainty symbols only when the uncertainty type and metaphor
  are likely to be understood
bibliography: references.bib
description: Iconic uncertainty symbols are only beneficial if viewers grasp both
  the uncertainty concept and the intended metaphor; otherwise they add time without
  consistent gains.
labels:
- chart:map
- task:interpret
- visual:iconicity
- impact:comprehension
- data:uncertainty
- audience:expert
- complexity:advanced
---

## Apply iconic metaphors for uncertainty only when users can recognize the mapping <!-- role: advice -->

Use iconic metaphoric uncertainty symbols only in contexts where your audience is likely to understand both the uncertainty category (e.g., spatial precision vs. trustworthiness) and the metaphor embedded in the icon.

## Why metaphor decoding can fail even if icons look “logical” <!-- role: reason -->

Iconic symbols require the viewer to connect the picture to a specific uncertainty concept; if either the concept or metaphor is unclear, the icon’s extra complexity increases effort without reliably improving performance.

**Mechanism:** Metaphor-based signification adds a cognitive interpretation step that depends on shared conceptual models; mismatches reduce interpretability and slow judgments.

**Evidence:** Across uncertainty conditions, iconic symbol sets were rated only slightly more intuitive on average than abstract sets, and the difference was not consistently significant within individual conditions; response times were generally longer for iconic sets in both intuitiveness rating and aggregation tasks [@maceachrenVisualSemioticsUncertainty2012].

**Notes:** The observed variability by condition indicates that iconicity benefits are not uniform across uncertainty types.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Understand what kind of uncertainty is present, not just how much.
- **Task:** Interpret uncertainty category-specific symbols.
- **Data:** Multiple uncertainty conditions (space/time/attribute × type) may be represented.
- **Chart Setting:** Displays where icons are used to cue category distinctions.
- **Audience:** Mixed expertise or limited training time.
- **Success Criterion:** Consistent correct interpretation of what each symbol set signifies.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You can rely on repeated exposure and training within a stable user group. **Why:** Users can learn a metaphor mapping even if it is not broadly shared initially.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Designing and validating metaphors takes time and iteration. **Risk:** Users may over-trust an icon that “looks meaningful” but is interpreted differently than intended. **Mitigation:** Use clear labeling of the uncertainty condition alongside the icon set.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a clever metaphor without checking that users share it. **Why it fails:** Icon interpretation varies, reducing consistency.
- **Mistake:** Treating different uncertainty conditions as interchangeable in symbol design. **Why it fails:** Users did not show a uniform preference for iconicity across conditions.

## Quick tests <!-- role: check -->

**Failure Sign:** Users can rank certainty but cannot explain what uncertainty type the icon represents. **Quick Check:** Ask users to name the uncertainty concept the icon is meant to convey. **Stronger Test:** Include both naming and task-performance trials to see if interpretation aligns with use.

## What to do instead <!-- role: fix -->

- Use abstract ordered symbols for magnitude and label the uncertainty type in text.
- Encode uncertainty category via grouping/legend structure rather than pictorial metaphors.
- Provide an explicit preview/legend step before tasks that use category-specific symbols.
- Limit the number of uncertainty categories shown at once.
