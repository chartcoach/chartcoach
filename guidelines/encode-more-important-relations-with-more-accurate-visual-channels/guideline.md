---
id: encode-more-important-relations-with-more-accurate-visual-channels
title: Encode more important relations with more accurate visual channels
bibliography: references.bib
description: When multiple relations must be shown, map the most important ones to
  the most accurate perceptual encodings (especially position).
labels:
- chart:multivariate
- task:prioritize
- visual:position
- impact:accuracy
- data:relational
- audience:expert
- concept:importance-ordering
---

## Allocate the best encoding channels to the most important relations <!-- role: advice -->

When presenting multiple relations at once, assign the highest-accuracy perceptual channels to the relations the user has indicated are most important.

## Why importance ordering improves overall effectiveness <!-- role: reason -->

Effectiveness comparisons based only on perceptual-task rankings can leave multiple designs incomparable when they use the same set of channels. Introducing an explicit importance ordering resolves ties by ensuring that the most critical information uses the most accurate encodings.

**Mechanism:** Importance ordering turns a partial ordering of designs into a practical choice rule by aligning channel accuracy with informational priority.

**Evidence:** A principle of importance ordering is introduced to decide between otherwise-unordered multivariate designs by encoding more important information more effectively [@mackinlayAutomatingDesignGraphical1986b]. An example contrasts two scatter-plot variants that use the same channels but assign position to different variables, selecting the design that gives position to the more important relations [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** Importance is part of the input (for example, a tuple ordering of relations), not inferred from the chart.

## When this applies <!-- role: context -->

- **User Goal:** Understand several relations in one presentation.
- **Task:** Compare or interpret multiple variables with different priorities.
- **Data:** Multiple relations that can be composed into a single design.
- **Chart Setting:** Limited number of high-quality channels (especially axes) relative to variables.
- **Audience:** Readers who need to focus on key variables first.
- **Success Criterion:** The most important relations are easiest and most accurate to read.

## When not to follow it <!-- role: exceptions -->

**Break it when:** All relations are genuinely equal priority and no ordering is provided or justified. **Why:** The rule depends on a declared importance ordering to make a principled allocation decision [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Less important relations may become harder to read if encoded with lower-accuracy channels. **Risk:** If the importance ordering is wrong, the design will optimize the wrong information. **Mitigation:** Make the importance ordering explicit and revisable.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Treating all variables symmetrically and assigning channels arbitrarily. **Why it fails:** It can waste the most accurate channels on less important relations, reducing the presentation’s effectiveness for the main goal [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** The variable the reader cares about most is encoded with a low-accuracy channel (for example, size) while a secondary variable uses position. **Quick Check:** Identify the top one or two “must-read” relations and confirm they are encoded by position where possible. **Stronger Test:** Ask readers to answer questions about the most important relation; if they struggle, the channel allocation is likely wrong.

## What to do instead <!-- role: fix -->

- Reassign axis position to the most important quantitative relations.
- Demote less important relations to retinal encodings that remain expressive for their data type.
- Partition the presentation so high-priority relations get their own high-accuracy view when composition would dilute them.
- Request or infer a clear importance ordering from the application workflow before selecting encodings.
