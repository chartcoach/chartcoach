---
id: deprioritize-granularity-transitions-when-other-cost-1-options-exist
title: Deprioritize granularity transitions when other single-change transitions are
  available
bibliography: references.bib
description: If multiple one-attribute transitions are possible, treat granularity
  changes as less preferred than temporal or comparison changes.
labels:
- chart:multi
- task:sequence
- visual:layout
- impact:clarity
- data:hierarchical
- audience:general
- complexity:intermediate
---

## Use granularity shifts only when they serve the immediate narrative step <!-- role: advice -->

When you can choose among several one-attribute transitions, prefer temporal or comparative transitions before switching levels of detail (granularity), unless the story is specifically about zooming in or out.

## Viewers rate single-step granularity changes as weaker “next” steps <!-- role: reason -->

Even when a granularity transition changes only one attribute, viewers may find it a less natural continuation than time steps or comparison steps.

**Mechanism:** Changing level of detail can feel like a navigational move (overview/detail) rather than a continuation of the same explanatory thread.

**Evidence:** In cost-constant choices (all transitions cost 1), granularity transitions were less preferred than temporal transitions and also less preferred than both dimension-walk and measure-walk transitions [@hullmanDeeperUnderstandingSequence2013].

**Notes:** This result concerns preference judgments for “best next slide,” not accuracy on specific analytic questions.

## Context: When multiple one-change transitions are plausible <!-- role: context -->

- **User Goal:** Follow a coherent narrative path through a set of prepared views.
- **Task:** Choose an ordering principle for consecutive slides.
- **Data:** Hierarchical or filterable data with multiple levels of detail plus other varying attributes (time, measures, dimensions).
- **Chart Setting:** Slide-based narrative or stepper interface.
- **Audience:** General audiences.
- **Success Criterion:** The next step feels like a natural continuation rather than a detour.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The narrative purpose is explicitly “overview then detail” (or “detail then overview”). **Why:** Granularity is the main rhetorical move and should be foregrounded.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may delay providing detail that some viewers want early. **Risk:** Avoiding granularity changes can produce long runs of similar-level views. **Mitigation:** Use granularity shifts at segment boundaries or when you need to ground an abstract point in specifics.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Switching to a more detailed view as the default next step whenever it exists. **Why it fails:** Viewers may not see how the detail relates to the prior slide’s claim unless the zoom is narratively motivated.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers interpret the next slide as “just zooming” rather than “adding a new point.” **Quick Check:** Ask “what new claim does this step make?”; if the answer is only “it’s more detailed,” reconsider. **Stronger Test:** Run pairwise tests between a granularity-next option and a temporal/comparison-next option.

## Fix: What to do instead <!-- role: fix -->

- Insert a short framing step that explains the purpose of moving to detail before applying a granularity change.
- Use a temporal step first to establish change, then use a granularity step to explain where or for whom the change matters.
- Use a dimension-walk step first to establish group differences, then drill into one group via granularity.
- Reserve granularity moves for moments where the story explicitly shifts from general context to specific evidence (or back).
