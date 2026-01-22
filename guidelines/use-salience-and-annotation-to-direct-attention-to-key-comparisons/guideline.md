---
id: use-salience-and-annotation-to-direct-attention-to-key-comparisons
title: Highlight and annotate only the decision-relevant elements to direct attention
bibliography: references.bib
description: Use visual salience and nearby text to steer viewers toward the intended
  comparisons without overwhelming them.
labels:
- chart:line
- task:interpret
- visual:salience
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## Use selective highlighting plus nearby annotations to guide reading <!-- role: advice -->

Make the decision-relevant series, region, or point visually salient and annotate it with brief text placed adjacent to the relevant marks. Avoid calling out too many elements or placing explanatory text far from what it describes.

## Attention is guided by salience and language <!-- role: reason -->

Salient features attract attention, and language can direct viewers to what to look for and how to interpret it. When highlighting and annotation align with the key message, they reduce search and help viewers integrate conclusions with the data.

**Mechanism:** Visual salience prioritizes certain marks for attention, while close-by text reduces the need for memory and guides interpretation over multiple viewing steps.

**Evidence:** Salient objects attract attention and can be used to guide viewers to comparisons of interest, and annotation helps direct viewers while preserving the ability to verify claims by inspecting the data [@zacksDesigningGraphsDecisionMakers2020].

**Notes:** The benefit drops when too many callouts compete, because attention becomes fragmented.

## Use when viewers may not know what to look for <!-- role: context -->

- **User Goal:** Understand the main takeaway and verify it in the data.
- **Task:** Identify a key change, threshold crossing, discrepancy, or exception.
- **Data:** Multi-series or multi-feature displays where the message is not visually dominant by default.
- **Chart Setting:** Reports, presentations, public communication, policy contexts.
- **Audience:** Non-experts or mixed expertise groups.
- **Success Criterion:** Viewers reliably state the intended message and can point to supporting data.

## When exploration is the primary goal <!-- role: exceptions -->

**Break it when:** The chart is meant for open-ended exploration with no single privileged message. **Why:** Strong highlighting can bias attention and reduce discovery of alternative patterns.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Emphasis on one message can de-emphasize secondary insights. **Risk:** Overuse of highlights and callouts can feel manipulative or cluttered. **Mitigation:** Keep callouts sparse and ensure the underlying data remain visible for self-verification.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Highlighting many elements at once. **Why it fails:** Competing salience prevents attention from settling on the decision-relevant comparison [@zacksDesigningGraphsDecisionMakers2020].
- **Mistake:** Putting annotations in a distant caption and expecting viewers to connect them to specific marks. **Why it fails:** Separation forces slow searching and memory load [@zacksDesigningGraphsDecisionMakers2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers describe different “main points” or miss the intended comparison. **Quick Check:** Show the chart for 10 seconds and ask what matters most; if the answer varies widely, attention is not guided. **Stronger Test:** A/B test a version with selective highlighting and adjacent annotations versus a plain version on message recall and accuracy.

## What to do instead <!-- role: fix -->

- Apply a single, clear highlight to the decision-relevant marks and mute the rest.
- Place short annotation text directly next to the highlighted marks it references.
- Replace multiple callouts with one concise statement of the key comparison.
- If multiple messages are required, split into multiple small charts with separate highlights.
