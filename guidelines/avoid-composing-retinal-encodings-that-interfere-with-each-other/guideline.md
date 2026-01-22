---
id: avoid-composing-retinal-encodings-that-interfere-with-each-other
title: Avoid composing retinal encodings that interfere with each other at small mark
  sizes
bibliography: references.bib
description: Do not combine retinal channels like shape and size when the resulting
  mark sizes make one channel hard to perceive.
labels:
- chart:scatter
- task:encode
- visual:shape
- impact:legibility
- data:multivariate
- audience:general
- concept:encoding-interaction
---

## Do not combine shape and size if marks become too small to distinguish <!-- role: advice -->

Avoid composing shape and size encodings when the size variation makes small marks hard to recognize by shape.

## Why retinal channel interactions can reduce effectiveness <!-- role: reason -->

Composing encodings can create side effects where one channel degrades another. When size is reduced, differences in shape become difficult to perceive, so the shape encoding no longer functions reliably.

**Mechanism:** Size reduction reduces the visual detail available for shape discrimination, collapsing distinct shapes into perceptually similar marks.

**Evidence:** An explicit example shows that composing size and shape makes the shapes of small objects begin to look the same, reducing effectiveness, and the system accounts for this by preventing marks from getting too small [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** This is a composition-specific constraint: each encoding might work alone, but the combination fails at certain scales.

## When this applies <!-- role: context -->

- **User Goal:** Encode multiple variables on the same marks using retinal properties.
- **Task:** Distinguish categories (shape) while also representing magnitude or levels (size).
- **Data:** Multivariate data requiring multiple encodings on a single mark set.
- **Chart Setting:** Limited screen or page space that forces small marks.
- **Audience:** Readers needing reliable category identification.
- **Success Criterion:** Shapes remain discriminable across the full size range.

## When to break it <!-- role: exceptions -->

**Break it when:** Mark sizes remain large enough across the entire range that shape distinctions are consistently visible. **Why:** The interference arises specifically when sizes become small enough to erase shape detail [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** You may be unable to encode as many variables on a single mark, reducing integration. **Risk:** Avoiding the combination can force additional views or different encodings. **Mitigation:** Use a different retinal channel or restructure the composition.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Adding shape encoding on top of a size-encoded scatter plot without checking minimum symbol size. **Why it fails:** Small marks lose identifiable shape, so the encoded categories become unreadable [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** At the smallest mark size, multiple shapes are indistinguishable at normal viewing distance. **Quick Check:** Render the smallest-size marks alone and verify shape identification remains possible. **Stronger Test:** Ask a reader to identify shapes at the smallest size without zooming; frequent errors indicate interference.

## What to do instead <!-- role: fix -->

- Use color (when available) instead of shape for the categorical variable in a size-encoded view.
- Keep shape constant and encode the extra variable with an axis position in a composed design if possible.
- Increase available space or reduce the size range so minimum mark size stays above a legibility threshold.
- Split the encodings across coordinated views when the combined mark cannot support both reliably.
