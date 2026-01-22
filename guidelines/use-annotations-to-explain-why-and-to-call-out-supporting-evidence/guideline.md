---
id: use-annotations-to-explain-why-and-to-call-out-supporting-evidence
title: Annotate the chart to highlight evidence and add context the chart cannot show
bibliography: references.bib
description: Use annotations and highlights to point to supporting moments and to
  provide necessary context such as causes or events.
labels:
- chart:general
- task:explain
- visual:annotation
- impact:clarity
- data:general
- audience:general
- technique:callouts
---

## Add annotations that point to the evidence and provide key context beyond the data marks <!-- role: advice -->

Use annotations and visual highlights (such as shaded ranges) to draw attention to the parts of the chart that support your point and to add essential context the data alone cannot convey.

## Why annotations bridge the gap between patterns and meaning <!-- role: reason -->

Charts can show patterns but often cannot encode causal or contextual explanations; annotations help readers connect a visible change to an external event and notice the specific evidence relevant to the message.

**Mechanism:** Callouts focus attention on a specific region or moment while supplying interpretive context that would otherwise require the reader to infer or already know it.

**Evidence:** Annotations and highlights guide attention to supporting evidence and can provide additional information that goes beyond the central statement, including “why”-type context the chart itself cannot explain [@muth_better_charts_2017].

**Notes:** Annotations work best when they are tethered to a specific, visible feature in the data.

## When to use annotations and highlights <!-- role: context -->

- **User Goal:** Understand what matters and what happened at key moments.
- **Task:** Connect a change in the data to an event, threshold, or transition that readers should notice.
- **Data:** Time series or sequences where specific intervals or turning points are meaningful.
- **Chart Setting:** Explanatory or narrative charts where the reader needs guidance to the most relevant evidence.
- **Audience:** Readers without deep domain context who benefit from brief explanations.
- **Success Criterion:** Readers can identify the key moment(s) and understand the provided context without guessing.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is meant to be an open-ended exploration where the reader should draw their own conclusions without editorial framing. **Why:** Annotations can over-direct attention and narrow interpretation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space and visual simplicity. **Risk:** Too many annotations can clutter the chart and compete with the data. **Mitigation:** Keep annotations limited to the few moments that most directly support the point.

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Annotating everything interesting. **Why it fails:** The chart becomes text-heavy and the prioritization signal is lost.
- **Mistake:** Adding an annotation that is not anchored to a clearly visible feature. **Why it fails:** Readers cannot see what the note refers to, so it doesn’t guide interpretation.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers miss the key moment you intended to highlight. **Quick Check:** Remove annotations and see if the point is still obvious; if not, add one targeted callout. **Stronger Test:** Ask a reader to point out the evidence supporting the headline; if they point elsewhere, your callout is misdirected or missing.

## What to do instead <!-- role: fix -->

- Add one callout that explicitly references the specific change or interval that supports the headline.
- Use a subtle highlight (like a shaded band) to mark an important period rather than adding multiple text labels.
- Move secondary context into surrounding article text if it cannot be tied to a specific chart feature.
- If explanation requires many paragraphs, split the story into multiple charts with fewer callouts each.
