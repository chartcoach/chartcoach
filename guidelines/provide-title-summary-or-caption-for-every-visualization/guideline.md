---
id: provide-title-summary-or-caption-for-every-visualization
title: Provide a Title, Summary, or Caption
bibliography: references.bib
description: "Include descriptive text (title, summary, context, or caption) so the\
  \ chart\u2019s meaning is clear and memorable."
labels:
- chart:any
- task:interpret
- visual:text
- impact:clarity
- data:any
- audience:general
- accessibility:understandable
- source:chartability
---

## The Rule <!-- role: advice -->

Provide at least one piece of descriptive text for every visualization: a **title**, **summary**, **context statement**, or **caption** that communicates what the chart is and what it is meant to convey.

## The Logic <!-- role: reason -->

Descriptive text reduces ambiguity by anchoring the viewer’s interpretation of what they are seeing and what matters, improving recognition and recall of what the visualization conveys.

- **The Principle:** Cognitive scaffolding through narrative anchoring
- **The Evidence:** Visualization recall research links clear titles/labels/narratives to improved recognition and recall [@borkin_beyond_memorability_2016], and Chartability elevates missing titles/summaries/captions as a critical Understandable accessibility failure [@elavskyHowAccessibleMy2022].

## Where to Apply <!-- role: context -->

This advice is designed for any situation where a person must interpret a chart without guessing the intended meaning.

- **User Goal:** Understand what the chart is about and what takeaway to extract
- **Data Type:** Any (the requirement is about interpretation, not encoding)
- **Audience:** Anyone, especially people who benefit from reduced cognitive load (Chartability’s Understandable focus) [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** None supported by the provided evidence.
- **Reason:** The cited heuristic treats missing descriptive text as a critical failure rather than an optional enhancement [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and editorial effort to write and place descriptive text.
- **The Risk:** If the text is vague, it can fail to reduce ambiguity and may not anchor interpretation effectively, undermining the intended benefit [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Including a title/caption that is present but non-descriptive (e.g., generic naming that doesn’t clarify meaning).
- **Why it fails:** The heuristic targets ambiguity and cognitive load; text that does not provide context or a clear takeaway does not address the underlying problem [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart appears without any visible descriptive text (no title, summary, context, or caption) [@elavskyHowAccessibleMy2022].
- **The Test:** Scan the visualization container: if you cannot find a title, summary, context statement, or caption that clarifies what the chart conveys, the rule is violated [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear title **or** short caption that states the chart’s subject and intended takeaway [@elavskyHowAccessibleMy2022].
- **Best Fix:** Add both: a descriptive title plus a brief summary/context line that clarifies what the viewer should understand or remember from the chart [@borkin_beyond_memorability_2016; @elavskyHowAccessibleMy2022].
