---
id: do-not-assume-direction-term-consistency-cueing-improves-verification
title: "Do not rely on cueing the \u2018left/right/above/below\u2019 side to improve\
  \ sentence\u2013picture verification"
bibliography: references.bib
description: Direction-consistent cueing (highlighting the named side first) was not
  a robust driver of faster verification compared to target/reference alignment.
labels:
- chart:none
- task:verify
- visual:attention
- impact:robustness
- data:categorical
- audience:novice
- domain:spatial-relations
---

## Prefer target/reference alignment over direction-word alignment <!-- role: advice -->

When designing a speeded relation-verification prompt, prioritize cueing the sentence’s target object rather than cueing the side named by the directional term (e.g., the “left” item for “left” questions). Treat direction-consistent cueing as unreliable unless you test it in your specific setup.

## Direction-word compatibility is weaker than role compatibility <!-- role: reason -->

In these tasks, multiple potential compatibilities could influence performance (cue matches target role, cue matches directional term, cue matches absolute side, cue matches absolute color). The most reliable speed benefit came from aligning attention with the linguistic target role, while direction-term consistency produced weaker or inconsistent effects.

**Mechanism:** Target/reference roles are structurally required to interpret asymmetric categorical relations, so cueing can directly bias role assignment; cueing the direction-word side competes with other cues and may not systematically align with how the relation is encoded.

**Evidence:** For “Is (target) (direction) of (reference)?” questions, the target-first benefit was robust, while direction-term consistency effects were at best marginal and not robust across experiments. [@rothAsymmetricCodingCategorical2012]\
For “Which is (Direction)?” questions, direction-consistency benefits were mixed (weak/inconsistent in left/right; present in above/below), and the authors note interpretive ambiguity (e.g., response priming). [@rothAsymmetricCodingCategorical2012]

**Notes:** Even when a direction-consistency effect appears, it may reflect priming of an object identity response rather than improved relational encoding.

## Use in prompts that name a direction word <!-- role: context -->

- **User Goal:** Answer prompts that include explicit direction terms (left/right/above/below).
- **Task:** Verify a described relation or report which object occupies a named side.
- **Data:** Two-object displays with categorical directional relations.
- **Chart Setting:** Any visualization or UI that uses staged reveal/highlight to guide attention during relation judgments.
- **Audience:** General users; time-pressured verification contexts.
- **Success Criterion:** A cueing strategy that generalizes across relations and minimizes unintended biases.

## When direction-first cueing may be acceptable <!-- role: exceptions -->

**Break it when:** Your task is explicitly “Which object is on side X?” and your response method is not identity-priming-sensitive in your implementation. **Why:** The prompt’s structure itself may make side-first cueing more directly relevant than target/reference roles, but you must confirm it does not just prime responses.

## Tradeoffs of deprioritizing direction-word cueing <!-- role: costs -->

**Sacrifice:** You may miss a possible speed gain in some “which side” tasks where direction-consistent cueing helps. **Risk:** Overcorrecting could lead to a cueing scheme that feels less intuitive to users who expect “left” to be highlighted when asked about “left.” **Mitigation:** Validate with a quick pilot because the paper shows mixed outcomes depending on prompt type and dimension.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Always highlight the “left/above” item first whenever the text contains “left/above,” regardless of sentence structure. **Why it fails:** It can underperform compared to highlighting the linguistic target, and may produce inconsistent effects across relation types and question formats.

## Quick checks <!-- role: check -->

**Failure Sign:** Direction-consistent highlighting improves one question format (e.g., “Which is left?”) but not another (e.g., “Is red left of green?”), or results vary by relation axis. **Quick Check:** Compare direction-consistent vs. target-consistent cueing within the same prompts and measure time-to-response at matched accuracy. **Stronger Test:** Randomize cueing strategy within-subject and analyze whether effects replicate across both left/right and above/below prompts.

## What to do instead <!-- role: fix -->

- Cue the first-mentioned object in the sentence (the linguistic target) rather than the side named by the direction word.
- Rewrite prompts so the object you can reliably cue is the one that must be identified first (e.g., name the intended target first).
- If using “Which side?” prompts, remove or reduce identity-response priming by changing responses away from direct color-name keys and validating with a pilot.
- If you need direction emphasis, add a persistent neutral reference (e.g., a labeled axis or frame cue) instead of transiently cueing an object on that side.
