---
id: connected-scatterplot-do-not-assume-correlation-takeaway
title: Do Not Rely on Connected Scatterplots to Convey Correlation
bibliography: references.bib
description: If correlation is the key takeaway, use a format that makes it more salient
  than a connected scatterplot.
labels:
- chart:scatter
- task:explain
- visual:shape
- impact:clarity
- data:temporal
- audience:novice
- chart:connected-scatterplot
- concept:correlation
---

## The Rule <!-- role: advice -->

If your main message is positive/negative correlation, do not assume a connected scatterplot will make that conclusion salient; choose another format or explicitly annotate the correlational pattern.

## The Logic <!-- role: reason -->

Viewers described the same data with substantially more correlational language in dual-axis line charts than in connected scatterplots, suggesting correlation may be less cognitively cued in the CS form without learned associations [@harozConnectedScatterplotPresenting2016].

- **The Principle:** Salience depends on learned pattern-to-meaning mappings
- **The Evidence:** Post-hoc analysis found many more correlation-related descriptions for DALCs than for connected scatterplots when participants discussed the same datasets [@harozConnectedScatterplotPresenting2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Walk away understanding “these move together” vs. “these move oppositely.”
- **Data Type:** Paired time series where correlation (not temporal lead/lag or looping) is the main story.
- **Audience:** Readers unfamiliar with connected scatterplot conventions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You will explicitly annotate the diagonal/segment patterns as indicating correlation within the connected scatterplot.
- **Reason:** Added instruction can supply the missing association between CS geometry and correlation meaning [@harozConnectedScatterplotPresenting2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the unique loop/lag storytelling affordances of connected scatterplots.
- **The Risk:** Switching formats can reduce novelty/engagement.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Publishing a connected scatterplot expecting viewers to infer correlation “because it’s a scatterplot.”
- **Why it fails:** The study suggests viewers did not spontaneously frame CS patterns in correlational terms the way they did for DALCs [@harozConnectedScatterplotPresenting2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers describe the path as “weird/loopy/erratic” but do not mention moving together/oppositely.
- **The Test:** Ask a pilot viewer “are these positively or negatively related overall?” If they hesitate or avoid correlation terms, don’t rely on CS alone.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an annotation calling out a segment as “both rising” / “one rises while the other falls.”
- **Best Fix:** Use a dual-axis line chart (or another more conventional presentation) when correlation is the primary intended takeaway [@harozConnectedScatterplotPresenting2016].
