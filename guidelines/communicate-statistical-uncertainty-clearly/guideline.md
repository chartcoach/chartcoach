---
id: communicate-statistical-uncertainty-clearly
title: Communicate Statistical Uncertainty with Clear Conventions and Text
bibliography: references.bib
description: Show statistical uncertainty using clear, conventional visual encodings
  and a plain textual explanation so viewers can interpret confidence unambiguously.
labels:
- chart:general
- task:interpret
- visual:annotation
- impact:clarity
- data:statistical
- audience:general
- category:understandable
- source:research
---

## The Rule <!-- role: advice -->

When your chart includes statistical uncertainty (e.g., confidence intervals), encode it using clear, conventional uncertainty displays and add a plain textual explanation of what the uncertainty means.

## The Logic <!-- role: reason -->

Clear visual conventions paired with text reduce ambiguity about what ranges or distributions represent, improving understanding and decision-making when uncertainty is present, aligning with Chartability’s Understandable principle [@elavskyHowAccessibleMy2022].

- **The Principle:** Unambiguous uncertainty communication reduces cognitive interpretation burden.
- **The Evidence:** Uncertainty displays (e.g., error bars, violin plots, gradient shading; including quantile dotplots/CDFs) combined with textual explanation improve comprehension and decision-making [@doi_communicating_statistical; @fernandes_uncertainty_displays_2018].

## Where to Apply <!-- role: context -->

This advice is designed for charts where uncertainty is part of the message.

- **User Goal:** Understand how reliable an estimate is and make decisions with confidence information.
- **Data Type:** Statistical estimates with confidence/uncertainty intervals or distributions.
- **Audience:** People who may not infer uncertainty correctly without guidance (including general audiences).

## When to Break It <!-- role: exceptions -->

- **Scenario:** No statistical confidence/uncertainty is present in the underlying data or message.
- **Reason:** Adding uncertainty encodings would introduce unnecessary complexity without representing real information [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual elements and explanatory text consume space and attention.
- **The Risk:** If the uncertainty explanation is unclear, the chart can become more confusing rather than less clear [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing confidence intervals (or uncertainty shading) without saying what interval/distribution it represents or how to interpret it.
- **Why it fails:** Viewers cannot reliably infer the meaning of uncertainty encodings without explicit conventions and explanation, leading to ambiguity [@doi_communicating_statistical; @fernandes_uncertainty_displays_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Uncertainty marks appear (e.g., bars/regions/dots/shading), but there is no accompanying text explaining what they represent.
- **The Test:** Look for an explicit statement describing the uncertainty (what it is and how to read it). If you cannot find it, the uncertainty is not clearly communicated [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short textual explanation near the chart stating what the uncertainty display represents and how to interpret it [@doi_communicating_statistical].
- **Best Fix:** Use a clear, conventional uncertainty display (e.g., error bars, violin plot, gradient shading, quantile dotplots or CDFs) and pair it with a textual explanation that removes ambiguity about statistical confidence/uncertainty [@doi_communicating_statistical; @fernandes_uncertainty_displays_2018; @elavskyHowAccessibleMy2022].
