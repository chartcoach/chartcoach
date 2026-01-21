---
id: explain-purpose-and-how-to-read
title: "Explain the Chart\u2019s Purpose and How to Read It"
bibliography: references.bib
description: Provide an explicit purpose statement and brief reading/interpretation
  instructions so people can understand and use the visualization without guesswork.
labels:
- chart:general
- task:interpret
- visual:multichannel
- impact:clarity
- data:multivariate
- audience:novice
- source:chartability
---

## The Rule <!-- role: advice -->

Explicitly state (1) what the chart is for and (2) how to read, use, and interpret it.

## The Logic <!-- role: reason -->

- **The Principle:** Reduce ambiguity and interpretation burden by externalizing the “how to read” knowledge that authors often assume is obvious.
- **The Evidence:** Charts with descriptive titles and supporting text are more likely to be correctly recognized and recalled, indicating that explanatory framing materially improves comprehension and memory [@xiong_curse_of_2020]. Chartability flags missing purpose/reading guidance as a critical Understandable failure because even simple visualizations can be hard to interpret without explicit instruction [@elavskyHowAccessibleMy2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting what the visualization means and how to use it to answer the intended question.
- **Data Type:** Any visualization where reading conventions, encodings, or interactions are not self-evident from the display alone (including “simple” charts that still require correct interpretation).
- **Audience:** Especially people unfamiliar with the data, chart type, or interaction model (e.g., first-time or general audiences) [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** None supported by the provided evidence.
- **Reason:** Chartability treats the absence of purpose/how-to-read guidance as a critical issue and the cited study links descriptive framing/supporting text with better recall [@elavskyHowAccessibleMy2022] [@xiong_curse_of_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and authoring time to add explanatory text.
- **The Risk:** If poorly written, the explanation can add extra material for users to process, potentially increasing reading time [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a generic title or labeling only the chart name (e.g., “Sales Chart”) instead of explaining what it is for.
- **Why it fails:** A non-descriptive label does not convey purpose or how to interpret the encodings, leaving users to infer meaning and interaction on their own [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The visualization appears without any nearby text that clarifies the intended takeaway or gives guidance on reading/using the chart.
- **The Test:** Ask, “Does the chart itself (via accompanying text) tell me what it’s for and how to read/use it?” If not, it fails this critical heuristic [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a concise purpose statement and a short “how to read” note adjacent to the chart (e.g., a descriptive title plus 1–2 sentences explaining interpretation).
- **Best Fix:** Add purpose plus supporting text that guides interpretation (e.g., descriptive title + supporting explanation of what encodings mean and how to interpret the result), leveraging the demonstrated benefit of descriptive framing/supporting text for recognition and recall [@xiong_curse_of_2020] and the critical Chartability requirement to explain how to read complex (and even simple) visualizations [@elavskyHowAccessibleMy2022].
