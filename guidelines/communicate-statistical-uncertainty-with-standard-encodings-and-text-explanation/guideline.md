---
id: communicate-statistical-uncertainty-with-standard-encodings-and-text-explanation
title: Communicate statistical uncertainty with standard uncertainty encodings and
  a plain-language textual explanation
bibliography: references.bib
description: Show confidence or uncertainty using clear visual conventions and explain
  what it means in text so readers can interpret the data without ambiguity.
labels:
- chart:general
- task:judge
- visual:annotation
- impact:clarity
- data:statistical
- audience:novice
- accessibility:cognitive
- principle:understandable
- topic:uncertainty
---

## Communicate uncertainty unambiguously in both visuals and text <!-- role: advice -->

When you show statistical uncertainty (such as a confidence interval), encode it using clear, recognizable uncertainty conventions and add a plain-language textual explanation of what the uncertainty represents. If uncertainty is present in the analysis but not shown, explicitly state that it is not being displayed.

## Why uncertainty needs both conventions and explanation <!-- role: reason -->

Uncertainty is easy to misread as “noise,” “error,” or “range,” especially when readers do not share the chart author’s statistical assumptions. Using recognizable visual conventions plus a short textual explanation reduces ambiguity about what the interval or distribution means, helping readers make better judgments and decisions from the chart.

**Mechanism:** Clear uncertainty encodings provide a perceptible cue that values are estimates rather than exact, while text disambiguates the meaning (what quantity is uncertain, what level, and how to interpret it), lowering cognitive load and reducing misinterpretation.

**Evidence:** Uncertainty displays that use clear conventions (such as error bars, violin plots, gradients, quantile dotplots, or cumulative distribution functions) combined with textual explanations improve understanding of uncertainty and support better decision-making outcomes. [@doi_communicating_statistical; @fernandes_uncertainty_displays_2018] This requirement is included as an Understandable accessibility heuristic for visualization auditing to minimize ambiguity and cognitive burden. [@elavskyHowAccessibleMy2022]

**Notes:** There can be cases where the “best” uncertainty communication approach is not obvious due to contextual complexity and ethical considerations around interpretation. [@elavskyHowAccessibleMy2022]

## When this applies in charts and dashboards <!-- role: context -->

- **User Goal:** Make an informed decision while accounting for uncertainty in estimates or predictions.
- **Task:** Judge reliability, compare options, or assess risk given uncertain outcomes.
- **Data:** Estimates with statistical uncertainty (for example, confidence intervals, predictive distributions, or probabilistic outcomes).
- **Chart Setting:** Any static or interactive visualization where uncertainty exists or affects conclusions, including decision-support contexts.
- **Audience:** Mixed statistical literacy; readers who may need reduced cognitive load and unambiguous interpretation.
- **Success Criterion:** Readers correctly recognize and interpret uncertainty and can explain what it means for the conclusion or decision.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is purely descriptive and contains no statistical uncertainty or inferential claims. **Why:** Adding uncertainty encodings would imply statistical inference that is not present and can confuse interpretation. [@elavskyHowAccessibleMy2022]

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Visual space and simplicity, since uncertainty encodings and explanatory text add marks and words. **Risk:** Overloading a chart can increase cognitive burden or distract from the primary message. **Mitigation:** Keep the explanation short and focused on what the uncertainty means for interpretation and decision-making. [@elavskyHowAccessibleMy2022]

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Showing a confidence interval (or similar band/interval) without stating what it represents or what level it uses. **Why it fails:** Readers cannot reliably infer the meaning of the uncertainty display, increasing ambiguity and misinterpretation. [@elavskyHowAccessibleMy2022]
- **Mistake:** Using a non-standard visual encoding for uncertainty without explanation. **Why it fails:** Readers may not recognize it as uncertainty or may interpret it as another data variable. [@doi_communicating_statistical; @elavskyHowAccessibleMy2022]
- **Mistake:** Reporting point estimates as if they are exact when uncertainty exists in the underlying analysis. **Why it fails:** It hides uncertainty, encouraging overconfident conclusions and poorer decisions. [@elavskyHowAccessibleMy2022]

## Quick tests for unclear uncertainty communication <!-- role: check -->

**Failure Sign:** The chart includes intervals, bands, or distribution-like marks, but there is no text explaining what they mean. **Quick Check:** Ask, “Can a reader identify what is uncertain and what the interval/distribution represents using only the chart’s on-chart text?” **Stronger Test:** Give the chart to a reader and ask them to explain, in one sentence, what the uncertainty marks mean and how they should affect a decision; treat inconsistent answers as a failure. [@elavskyHowAccessibleMy2022]

## What to do instead <!-- role: fix -->

- Add a brief caption or annotation that defines the uncertainty being shown and how to interpret it for the chart’s main takeaway. [@elavskyHowAccessibleMy2022]
- Use a recognizable uncertainty encoding (such as error bars, violin/gradient approaches, quantile dotplots, or cumulative distribution functions) rather than inventing a novel uncertainty mark. [@doi_communicating_statistical; @fernandes_uncertainty_displays_2018]
- If uncertainty is important for the decision, switch from a single-point display to a distribution-oriented display that makes variability explicit. [@fernandes_uncertainty_displays_2018]
- If you cannot clearly communicate uncertainty in the current design, add a textual disclosure that uncertainty exists but is not shown and explain the consequence for interpretation. [@elavskyHowAccessibleMy2022]
