---
id: remove-intermediate-rating-schemes-and-label-the-measure
title: Describe the Data Measure Directly in the Legend
bibliography: references.bib
description: Replace abstract rating systems with a direct explanation of the encoded
  variable and its units/timeframe.
labels:
- chart:map
- task:decode
- visual:text
- impact:clarity
- data:geospatial
- audience:novice
- visual:color
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Do not use a star/rating layer between the reader and the data; label the legend/color key with the **actual measure** being mapped (including units and timeframe).

## The Logic <!-- role: reason -->

An extra rating system adds a translation step (“stars” → “days”) that readers must learn before they can interpret color; removing the abstraction makes decoding immediate and lowers the chance of misunderstanding, which is the specific recommendation made in [@mintzer_fix_my_chart_text_elements_2024].

- **The Principle:** Eliminate unnecessary abstraction in encoding explanations
- **The Evidence:** [@mintzer_fix_my_chart_text_elements_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Decode what the colors mean quickly and accurately
- **Data Type:** Any quantitative measure binned into a choropleth legend (e.g., “number of 90°F+ days in summer 2050”)
- **Audience:** Non-expert readers who may not know the author’s rating rubric

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the rating system is itself the standardized reported metric (e.g., an official index people already know)
- **Reason:** If the audience already thinks in that index, translating back to raw units could reduce usefulness; the post’s guidance targets idiosyncratic ratings that obscure the chosen measure [@mintzer_fix_my_chart_text_elements_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a “friendly” summary label like “5-star counties”
- **The Risk:** If the measure name is long, the legend may become text-heavy unless you simplify wording

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping stars in the legend and adding a separate explanation elsewhere (“5 stars = under 30 days…”)
- **Why it fails:** Readers still have to learn the mapping; it preserves the unnecessary decoding step highlighted in [@mintzer_fix_my_chart_text_elements_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend categories are named with a scoring system (stars/grades) instead of the variable’s units
- **The Test:** Can a reader explain what a color means without knowing your rubric? If not, the legend is too abstract.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace star labels with the binned ranges of the measured variable (e.g., “Under 30 days of extreme heat (90°F+) expected in summer 2050…”) as modeled in [@mintzer_fix_my_chart_text_elements_2024].
- **Best Fix:** Make the legend a full decoding sentence fragment: variable + threshold + period, then list bins as ranges (and keep any “comfort” framing in the title or annotation, not in the legend), following [@mintzer_fix_my_chart_text_elements_2024].
