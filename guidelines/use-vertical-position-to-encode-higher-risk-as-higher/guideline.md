---
id: use-vertical-position-to-encode-higher-risk-as-higher
title: Encode higher risk with higher vertical position in bars or risk ladders
bibliography: references.bib
description: Use height and vertical ordering to communicate increasing risk because
  audiences reliably interpret higher as greater.
labels:
- chart:bar
- chart:risk-ladder
- task:rank
- task:compare
- visual:position
- impact:clarity
- data:probability
- audience:novice
- domain:risk-communication
---

## Use vertical placement so higher means more risk <!-- role: advice -->

When designing risk comparisons, use vertical position or height so greater risk is shown higher than lower risk.

## Why vertical position is an intuitive cue for magnitude <!-- role: reason -->

People readily map “higher” to “more” in common graphical conventions, which supports quick ranking and comparison without requiring detailed numeracy.

**Mechanism:** Familiar magnitude metaphors reduce interpretive ambiguity and allow rapid ordinal judgments of risk size.

**Evidence:** Viewers are sensitized to graphs that use height or vertical placement to signify greater risk likelihood, including bar graphs and risk ladders, and easily interpret higher placement as greater risk. [@lipkusNumericVerbalVisual2007]

**Notes:** This supports ordinal understanding; exact magnitude still benefits from numeric labels.

## When to rely on vertical position <!-- role: context -->

- **User Goal:** Identify which risk is larger or smaller across multiple items.
- **Task:** Rank or compare risk magnitudes.
- **Data:** Multiple risks to compare; often heterogeneous events or groups.
- **Chart Setting:** Patient education, environmental/health hazard ladders, summaries.
- **Audience:** Broad public; time-limited readers.
- **Success Criterion:** Correct ordering and quick identification of higher-risk items.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The medium forces a horizontal-only layout with constrained vertical space. **Why:** The intended “higher means more” cue may be weak or lost.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Vertical ordering can limit how much annotation fits alongside items. **Risk:** Readers may focus only on rank and ignore the size of differences. **Mitigation:** Add numeric values or brief labels indicating magnitude differences.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using vertical position inconsistently (some higher marks represent less risk). **Why it fails:** It breaks a strong learned convention and invites misinterpretation.

## Quick tests <!-- role: check -->

**Failure Sign:** Users disagree about which item is riskier when looking at the ladder or bars. **Quick Check:** Ask “which is higher risk?” for a few items; answers should be immediate and consistent. **Stronger Test:** Measure ranking accuracy across a small set of users without providing extra explanation.

## What to do instead <!-- role: fix -->

- Reorder items so the highest risk appears at the top of the display.
- Use a conventional vertical scale where larger numeric values are higher on the axis.
- Add a short caption stating that higher placement indicates higher risk.
- Provide numeric risk values next to items to support magnitude, not just rank.
