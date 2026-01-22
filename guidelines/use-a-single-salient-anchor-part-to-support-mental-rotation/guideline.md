---
id: use-a-single-salient-anchor-part-to-support-mental-rotation
title: Provide a single salient anchor part for mental rotation and keep judgments
  tied to that anchor
bibliography: references.bib
description: People naturally select and track one part (often the top) during mental
  rotation, so designs should supply and rely on one explicit anchor.
labels:
- chart:none
- task:mentally-rotate
- visual:attention
- impact:robustness
- data:categorical
- audience:novice
- domain:spatial-cognition
---

## Add one explicit anchor part for imagined rotation <!-- role: advice -->

Make one object part clearly identifiable as the anchor for rotation and structure the task so users only need to track that anchor through the imagined motion. Keep any required comparison or verification keyed to that single anchored part.

## Attention and gaze lock onto one part (typically the top) and track its path <!-- role: reason -->

Mental rotation behavior is dominated by selective attention: viewers pick one part and then track its imagined location as the object turns. This creates a privileged “tracked” part (often the topmost part) that drives both eye movements and which feature swaps are noticed.

**Mechanism:** A single attentional focus acts like a pointer that follows one part’s trajectory; information attached to that part is preserved better than information attached elsewhere.

**Evidence:** Eye-tracking during mental rotation showed that the last fixation before rotation typically landed on the topmost part, and gaze then followed the imagined rotation trajectory of that selected part [@xuCapacityVisualFeatures2015]. Behavioral swap detection was much higher for swaps involving the top part than for swaps that did not involve it, consistent with a single anchored selection [@xuCapacityVisualFeatures2015].

**Notes:** This pattern appeared across multi-part objects and was reflected in correlation between how closely gaze tracked the intended rotation and success in detecting orientation offsets.

## Context: When a user must imagine continuous clockwise/counterclockwise rotation <!-- role: context -->

- **User Goal:** Mentally rotate an object and verify its orientation or correspondence at the end state.
- **Task:** Continuous imagined rotation with later comparison (same/different; detect wrong orientation; detect swaps).
- **Data:** Objects composed of multiple parts where at least one part can serve as a stable reference.
- **Chart Setting:** Instructional materials, assessment items, or interfaces that rely on mental imagery during a blank/delay.
- **Audience:** General users, students, or anyone without domain heuristics for analytic rotation.
- **Success Criterion:** Fewer orientation errors and fewer missed changes that involve the tracked reference.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The task demands equal fidelity across multiple parts’ feature bindings during rotation. **Why:** Users will still prioritize one part, so an anchor alone will not prevent errors on non-anchored parts [@xuCapacityVisualFeatures2015].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Emphasizing one anchor can bias users to ignore other parts. **Risk:** Users may over-trust the anchored part and miss changes elsewhere. **Mitigation:** Reserve anchor-based designs for tasks where one-part tracking is sufficient for correctness.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Assuming users will distribute attention evenly across parts during mental rotation if all parts are equally salient. **Why it fails:** Users still tend to select and track a single part, producing asymmetric detection across parts [@xuCapacityVisualFeatures2015].
- **Mistake:** Designing swap/change checks that exclude the naturally tracked part (e.g., changes only among non-anchor parts) while still expecting high detection. **Why it fails:** Performance for swaps that do not involve the selected part can drop toward chance [@xuCapacityVisualFeatures2015].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users’ change detection is strongly dependent on whether the change involves one specific part, and eye gaze clusters on that part before/during rotation. **Quick Check:** In a pilot, measure accuracy separately for changes involving the intended anchor versus not; a large gap means users are not monitoring non-anchor parts. **Stronger Test:** Eye-track or cursor-track during the imagined rotation period to confirm users are following the intended anchor path [@xuCapacityVisualFeatures2015].

## Fix: What to do instead <!-- role: fix -->

- Redesign the judgment so that correctness depends on the anchored part (e.g., ask about that part’s final position/orientation).
- Provide separate sub-questions that each use the same anchor rather than requiring simultaneous multi-part verification.
- Replace imagined rotation with visible rotation so users can visually inspect non-anchor parts as they move.
- Reduce the number of parts whose feature bindings must be preserved through rotation.
