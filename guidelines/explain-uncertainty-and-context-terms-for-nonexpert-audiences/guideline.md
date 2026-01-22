---
id: explain-uncertainty-and-context-terms-for-nonexpert-audiences
title: Explain uncertainty ranges and contextual baselines in text when the audience
  may not know them
bibliography: references.bib
description: Add plain-language explanations for uncertainty displays and contextual
  reference terms (like baselines or timeframes) so non-expert readers can interpret
  the visual correctly.
labels:
- chart:line
- task:interpret
- visual:annotation
- impact:clarity
- data:uncertainty
- audience:novice
- concept:uncertainty
- concept:baseline
- concept:scenario
---

## Explain uncertainty visuals and reference terms in accompanying text <!-- role: advice -->

When you show uncertainty ranges, future scenarios, or technical reference terms (such as baseline periods or specific timeframes), explain what they mean in nearby text like a caption or callout. Use plain language so readers can interpret the visual without guessing what the ranges or references represent.

## Why explanations prevent uncertainty from being misread <!-- role: reason -->

Unexplained uncertainty and contextual reference terms often trigger the wrong mental model: readers may treat ranges as “the data is unreliable,” or they may not know what a baseline/timeframe implies, which shifts interpretation away from the intended message. A short, plain-language explanation lets viewers map the visual device (shaded band, scenario envelope, reference period) to the correct meaning and reduces confusion and distrust.

**Mechanism:** Explanations supply the missing semantic link between a visual cue (e.g., a shaded band) and the intended concept (e.g., plausible range, scenario spread, reference baseline), improving comprehension and preserving trust.

**Evidence:** Some lay viewers misunderstood or distrusted uncertainty ranges when they were not explained, sometimes interpreting them as unreliability; adding explanations in surrounding text was recommended when uncertainty was not central to the message [@schuster_being_2024]. Visualization practitioners reported that uncertainty for climate-related future scenarios often requires explanation to avoid confusion, and many preferred clarifying it in accompanying text rather than relying on the visual alone [@schuster_who_2023]. Viewers were also confused by unexplained contextual references such as baseline periods (e.g., “1850–1900”), and captions or surrounding text could have prevented misinterpretation [@schuster_being_2024].

**Notes:** “Explain” can be as small as defining what the band represents, what it does not represent, and how to read it relative to the central estimate.

## When to add explanations for uncertainty and context cues <!-- role: context -->

- **User Goal:** Understand what the chart implies and how confident to be in the trend or comparison.
- **Task:** Interpret ranges, compare outcomes across scenarios, or contextualize values relative to a baseline or reference period.
- **Data:** Quantities with uncertainty intervals, model outputs, forecast ranges, scenario families, or values expressed relative to a baseline/reference timeframe.
- **Chart Setting:** Static charts, dashboards, reports, presentations, or social media posts where readers may not have prior context; limited interactivity.
- **Audience:** Mixed or general audiences, non-specialists, or readers unfamiliar with uncertainty communication or domain baselines.
- **Success Criterion:** Readers can correctly describe what the range/baseline means and draw the intended conclusion without increased distrust.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The audience is consistently expert and already shares a stable convention for the uncertainty encoding and any reference terms (e.g., a specialized internal tool with onboarding and standards). **Why:** Extra explanations can add noise and reduce scanability without improving comprehension.

## Tradeoffs and risks of adding explanations <!-- role: costs -->

**Sacrifice:** You give up space and simplicity in the caption or surrounding text. **Risk:** Over-explaining can distract from the main message or make the visualization feel more complicated than it is. **Mitigation:** Keep the explanation short and focused on how to read the uncertainty or reference term, not on methodology details.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Showing a shaded uncertainty band or multiple future-scenario lines with no caption defining what the range or scenarios represent. **Why it fails:** Readers may treat the visual as unreliability, ignore it, or interpret it as a different quantity than intended.\
**Mistake:** Using technical reference labels (e.g., baseline periods or timeframes) without defining what the reference means for interpretation. **Why it fails:** Readers cannot anchor comparisons correctly and may draw conclusions from the wrong frame of reference.

## Quick tests for whether your explanation is sufficient <!-- role: check -->

**Failure Sign:** A reader asks “What does the shaded area mean?” or “Why that baseline/time period?” **Quick Check:** Ensure the caption (or nearby text) defines the uncertainty/baseline in one sentence and states how to read it. **Stronger Test:** Ask 2–3 representative non-expert readers to paraphrase what the range/baseline means and what conclusion they would take from it.

## What to do instead <!-- role: fix -->

- Add a one-sentence caption defining the uncertainty range or scenario spread and how to interpret it relative to the main line/estimate.
- Replace technical labels with plain-language equivalents, and define any necessary reference periods (e.g., what the baseline is and why values are shown relative to it).
- If the uncertainty is not central, deemphasize it visually and move the interpretation guidance to surrounding text so the main message remains scannable.
- If uncertainty is central and cannot be explained briefly, restructure the presentation by separating the “main pattern” view from a dedicated “uncertainty/how to read this” panel or note.
