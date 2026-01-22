---
id: provide-title-summary-or-caption-for-every-chart
title: Provide a title and a short summary or caption for every chart
bibliography: references.bib
description: "Add descriptive text (title plus summary/caption/context) so viewers\
  \ can understand the chart\u2019s purpose and takeaway without guesswork."
labels:
- chart:all
- task:interpret
- visual:text
- impact:accessibility
- data:any
- audience:all
- a11y:understandable
- chartability:critical
---

## Provide a title and a short summary or caption for every chart <!-- role: advice -->

Provide a descriptive title and a short summary, caption, or context text for every chart. Ensure the text communicates what the chart is about and the intended takeaway.

## Descriptive text reduces ambiguity and supports recall <!-- role: reason -->

Clear chart text reduces ambiguity about what the graphic represents and what the viewer should conclude, lowering the mental effort needed to interpret the display and improving the chance the message is retained.

**Mechanism:** A title and summary/caption set expectations, define what the viewer is looking at, and anchor interpretation around a stated message rather than forcing the viewer to infer intent from marks alone.

**Evidence:** Memorable and better-remembered visualizations are associated with clear titles, labels, and narrative framing, supporting the need for descriptive chart text as part of understanding and recall [@borkin_beyond_memorability_2016]. A visualization accessibility audit framework treats missing titles/summaries/captions as a critical Understandable failure because the chart’s meaning is otherwise left ambiguous for many readers [@elavskyHowAccessibleMy2022].

**Notes:** This guideline concerns the presence of descriptive text, not only the quality of headings if they happen to exist.

## When every chart needs a title, summary, or caption <!-- role: context -->

- **User Goal:** Understand what the visualization shows and what it implies.
- **Task:** Interpret, learn, remember, or communicate a takeaway from data.
- **Data:** Any dataset where meaning depends on context (units, population, time window, definitions, scope).
- **Chart Setting:** Static or interactive charts, dashboards, reports, or embedded visuals where viewers may encounter the chart out of its original narrative.
- **Audience:** Mixed audiences, including people who need reduced cognitive load or who may not share the chart author’s context.
- **Success Criterion:** The chart can be understood without guesswork about purpose, scope, or intended conclusion.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is purely decorative and not intended to communicate data or support any decision. **Why:** Adding interpretive text would imply an informational intent that the artifact does not have [@elavskyHowAccessibleMy2022].

## Tradeoffs of adding descriptive text <!-- role: costs -->

**Sacrifice:** Space and editorial time to write and maintain supporting text. **Risk:** Overly forceful summaries can bias interpretation if they overstate certainty or omit relevant context. **Mitigation:** Keep the summary concise and scoped to what the visualization is intended to communicate [@elavskyHowAccessibleMy2022].

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Using a generic title (e.g., “Chart” or a dataset name) with no takeaway. **Why it fails:** It does not reduce ambiguity about what the viewer should learn or remember [@elavskyHowAccessibleMy2022].
- **Mistake:** Providing only axis labels but no summary/caption/context. **Why it fails:** Labels may identify encodings but still leave the purpose, scope, and main message unclear [@elavskyHowAccessibleMy2022].

## Quick tests for missing chart text <!-- role: check -->

**Failure Sign:** The chart appears with no title and no accompanying summary/caption/context, or the only text is a non-descriptive label. **Quick Check:** Ask whether a reader can state what the chart is about and the intended takeaway using only the visible text. **Stronger Test:** Show the chart briefly without additional explanation and check whether readers describe the same intended message consistently [@elavskyHowAccessibleMy2022].

## How to fix a chart with no title, summary, or caption <!-- role: fix -->

- Add a descriptive title that names the subject and what is being measured.
- Add a short summary or caption that states the intended takeaway or key pattern the viewer should notice.
- Add context text that clarifies scope (population, time window, units, definitions) when misunderstanding is likely.
- If the visualization’s message cannot be summarized honestly in brief text, revise the visualization or narrative framing so the intended takeaway is clear [@elavskyHowAccessibleMy2022].
