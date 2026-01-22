---
id: use-provenance-cues-to-signal-transparency-and-credibility
title: Add provenance cues (sources, methods, exceptions, uncertainty) to support
  transparency judgments
bibliography: references.bib
description: Use citations and uncertainty notes to signal trustworthiness and limits
  in narrative visualizations.
labels:
- chart:general
- task:assess
- visual:text
- impact:trust
- data:uncertainty
- audience:general
- custom:rhetoric-provenance
---

## Provide provenance information and limits alongside the chart <!-- role: advice -->

Include data sources, methodological notes, exceptions/corrections, and explicit uncertainty or inferential limits in the presentation.

## Why provenance cues change how messages are received <!-- role: reason -->

In narrative visualization, viewers form trust judgments partly from signals of transparency. Provenance elements can rhetorically reinforce impartiality and credibility, while uncertainty signals can prevent overconfident readings of patterns.

**Mechanism:** Provenance and uncertainty cues act as interpretive scaffolding: they reduce ambiguity about where the data came from and how far conclusions can be extended, shaping both trust and inference.

**Evidence:** The paper groups source citations, methodological notes, exceptions/corrections, and uncertainty expressions under “provenance rhetoric,” describing them as techniques that signal transparency and trustworthiness in narrative visualization [@hullmanVisualizationRhetoricFraming2011a]. It also observes that uncertainty is often communicated textually in narrative visualizations (for example, “forecast” or “leap-of-faith” notes), implying a practical reliance on annotations to set inferential limits for general audiences [@hullmanVisualizationRhetoricFraming2011a].

**Notes:** Provenance cues can coexist with other rhetorical moves; they do not guarantee neutrality.

## When provenance cues are most important <!-- role: context -->

- **User Goal:** Decide whether to accept the visualization’s implied story.
- **Task:** Evaluate credibility and interpret conclusions under uncertainty.
- **Data:** Survey data, forecasts, modeled estimates, or any aggregated/cleaned dataset.
- **Chart Setting:** Journalism, public-facing reports, or high-stakes organizational communication.
- **Audience:** Non-experts who may not infer methods or uncertainty unaided.
- **Success Criterion:** Viewers can identify source, method, and limits without leaving the page.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is an internal exploratory view where provenance is handled elsewhere in the workflow. **Why:** Redundant provenance in the display may distract from analysis without improving interpretation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Layout space and attention. **Risk:** Viewers may over-trust merely because sources are cited, even if choices elsewhere strongly frame the message. **Mitigation:** Pair provenance with clear scope/definition notes when relevant.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Citing a source but omitting key methodological choices (for example, aggregation rules). **Why it fails:** Viewers still cannot assess how transformations shaped the message.
- **Mistake:** Using vague uncertainty language without specifying what part is inferred or forecast. **Why it fails:** Viewers may not know where confidence should drop.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers ask where the data came from or whether the chart is a forecast.\
**Quick Check:** Can a reader answer “source, method, limits” from what’s visible?\
**Stronger Test:** Remove the provenance block and see if the story becomes overconfident or under-specified.

## What to do instead <!-- role: fix -->

- Add a visible data source citation and, when relevant, a link to details.
- Summarize key transformations (aggregation, exclusions, scaling) in a short note.
- Mark exceptions, corrections, or unusual cases where they affect reading.
- Label inferred or forecast segments explicitly in the text around the chart.
