---
id: trim-footnotes-to-essential-limitations-and-source
title: Keep Footnotes Minimal and Interpretation-Focused
bibliography: references.bib
description: Use footnotes to convey only the essential assumptions/limitations needed
  to read the graphic and provide a clear source link.
labels:
- chart:map
- task:contextualize
- visual:text
- impact:trust
- data:modeled
- audience:novice
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Cut footnotes down to the basics: include only the key limitation(s) necessary to interpret the map and a source link.

## The Logic <!-- role: reason -->

Predictive visuals can hide assumptions; a short, targeted footnote increases transparency without overwhelming the reader or competing with the title/legend for attention—an explicit tradeoff advocated in [@mintzer_fix_my_chart_text_elements_2024].

- **The Principle:** Minimum viable transparency
- **The Evidence:** [@mintzer_fix_my_chart_text_elements_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand what the visualization does *not* account for and where the data comes from
- **Data Type:** Forecasts, projections, modeled estimates, or derived indices
- **Audience:** Readers who need a quick, trustworthy summary rather than a full methods section

## When to Break It <!-- role: exceptions -->

- **Scenario:** High-stakes decision contexts where readers must see detailed assumptions immediately (e.g., policy, compliance)
- **Reason:** A minimal footnote may not provide enough context to prevent misuse; the post’s recommendation assumes the full detail can live in the linked source [@mintzer_fix_my_chart_text_elements_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less nuance and fewer caveats visible at first glance
- **The Risk:** Readers may miss important boundary conditions if the “essentials” are chosen poorly

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the footnote to explain everything (methodology, definitions, extra guidance, multiple unrelated links)
- **Why it fails:** The footnote becomes a wall of text that distracts from the map and duplicates what the legend/title should do, which [@mintzer_fix_my_chart_text_elements_2024] specifically aims to correct.

## How to Check <!-- role: check -->

- **Visual Sign:** The footnote is longer than the title or legend block, or it contains multiple tangential explanations not required to read the map
- **The Test:** Hide the footnote—can a reader still decode the map? If yes, add back only what prevents misunderstanding (plus the source). If no, the missing content belongs in the title/legend, not a longer footnote.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep one limitation sentence (what the measure is/doesn’t include) plus “Source: …” as shown in the revised example in [@mintzer_fix_my_chart_text_elements_2024].
- **Best Fix:** Move decoding info into the legend, purpose into the title, and leave the footnote as: (1) one key modeling/measurement caveat and (2) one clear source citation/link, following [@mintzer_fix_my_chart_text_elements_2024].
