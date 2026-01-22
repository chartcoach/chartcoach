---
id: use-supporting-text-when-visual-is-not-distinct-to-aid-recognition
title: Use supporting text as a semantic hook when the visualization is not visually
  distinctive
bibliography: references.bib
description: When a chart lacks strong visual distinctiveness, viewers use titles
  and other text to recognize it.
labels:
- chart:general
- task:recognize
- visual:text
- impact:memorability
- data:general
- audience:general
- complexity:low-distinctiveness
---

## Use text to support recognition when visuals are confusable <!-- role: advice -->

When many charts share similar templates or look alike, add clear supporting text (especially titles) that uniquely identifies the topic and message.

## Why semantic hooks matter for recognition <!-- role: reason -->

If a visualization lacks a strong visual association, viewers perform more exploratory eye movements during recognition and rely on textual elements to retrieve it from memory.

**Mechanism:** Text provides semantic associations that can disambiguate visually similar charts and trigger retrieval when visual cues are insufficient.

**Evidence:** Less recognizable visualizations elicited more exploration during recognition (including fixations toward titles/text), and titles received the highest total fixation time during recognition; titles functioned as semantic associations used for recognition when visual distinctiveness was low [@borkinMemorabilityVisualizationRecognition2016].

**Notes:** This effect was especially relevant for sources with repeated templates and less distinctive aesthetics.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Recognize a previously seen visualization quickly.
- **Task:** Rapid recognition among many similar-looking charts.
- **Data:** Repeated reporting where many charts share formats (e.g., dashboards, recurring reports).
- **Chart Setting:** Collections, feeds, or sequences where confusion across charts is plausible.
- **Audience:** Viewers with limited time who may only glance during recognition.
- **Success Criterion:** Correct recognition with minimal visual search.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization already contains a strong, unique visual hook that reliably distinguishes it. **Why:** Additional text may be redundant for recognition.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Visual simplicity and available space. **Risk:** Excess text can shift attention away from data marks. **Mitigation:** Keep supporting text concise and message-focused.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Reusing the same generic title structure across many charts. **Why it fails:** It does not provide a discriminating semantic cue.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate and scan multiple regions before saying they recognize the chart. **Quick Check:** Show charts for 2 seconds and ask “seen before?”; note whether people look to the text to decide. **Stronger Test:** Compare recognition rates for versions with and without the supporting text.

## What to do instead <!-- role: fix -->

- Add a specific title that names the entity, time frame, and key result.
- Add a short explanatory sentence near the data that states the main conclusion.
- Use distinctive labels or annotations on key marks to create unique semantic anchors.
- Reduce template sameness across a set by varying non-data elements that remain consistent with the message.
