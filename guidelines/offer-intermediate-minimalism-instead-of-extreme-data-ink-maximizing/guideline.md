---
id: offer-intermediate-minimalism-instead-of-extreme-data-ink-maximizing
title: Offer an intermediate minimalism option instead of extreme data-ink maximizing
  for bar charts
bibliography: references.bib
description: When moving toward minimalist bar charts, include mid-step designs because
  users may accept moderate changes but reject extreme minimalism.
labels:
- chart:bar
- task:compare
- visual:ink
- impact:acceptance
- data:quantitative
- audience:novice
- pattern:maya
---

## Use intermediate steps when increasing data-ink ratio in bar charts <!-- role: advice -->

When proposing a minimalist redesign of a bar chart, include at least one intermediate version between the conventional chart and the most extreme data-ink maximizing version. Use the intermediate option as a candidate default if it is preferred over both extremes.

## Moderate minimalism can be acceptable while extremes are rejected <!-- role: reason -->

Acceptance appears to be non-linear: viewers may prefer a moderately simplified design but reject the most minimalist version, so offering only an extreme minimalist option can unnecessarily drive preference toward the conventional chart.

**Mechanism:** Intermediate designs can preserve enough familiar structure to feel clear and usable while reducing some non-data ink, making them more acceptable than an unfamiliar extreme minimalist form.

**Evidence:** When participants were shown a standard bar graph, an extreme minimalist version, and intermediate versions, preferences shifted toward an intermediate design while none selected the extreme minimalist design [@inbarMinimalismInformationVisualization2007].

**Notes:** Presenting intermediate alternatives also changed subjective clarity ratings across conditions, suggesting that framing and comparison set can influence perceived clarity [@inbarMinimalismInformationVisualization2007].

## Context for choosing intermediate minimalism <!-- role: context -->

- **User Goal:** Modernize or simplify an existing bar-chart style without losing acceptance.
- **Task:** Choose among multiple visual styles that encode identical bar-chart data.
- **Data:** Quantitative values across categories, suited to bar charts.
- **Chart Setting:** Style guidelines, reporting templates, or UI chart components where you can present alternatives.
- **Audience:** Viewers likely accustomed to conventional bar charts.
- **Success Criterion:** A redesign that is preferred (or at least not disliked) while reducing some non-data ink.

## Exceptions for using intermediate options <!-- role: exceptions -->

**Break it when:** You cannot present or support multiple style options (only one design can be shown or implemented). **Why:** The advantage comes from giving viewers a non-extreme choice set.

## Costs of intermediate minimalism options <!-- role: costs -->

**Sacrifice:** More design and evaluation effort because you must create multiple variants. **Risk:** The chosen intermediate may not maximize the data-ink ratio and may disappoint stakeholders seeking strict minimalism. **Mitigation:** Align on acceptance as a goal and treat data-ink maximizing as one competing objective.

## Mistakes in “standard vs extreme minimalist” comparisons <!-- role: mistakes -->

- **Mistake:** Testing only a conventional bar chart against the most extreme minimalist alternative. **Why it fails:** Viewers may reject the extreme option even if they would accept a moderate reduction in non-data ink.
- **Mistake:** Interpreting rejection of the extreme minimalist design as rejection of any simplification. **Why it fails:** Preferences can favor an intermediate design even when the extreme is never chosen.

## Check for an intermediate “sweet spot” <!-- role: check -->

**Failure Sign:** The extreme minimalist design receives near-zero preference when included among options. **Quick Check:** Add one intermediate variant and see whether preference moves away from the standard chart. **Stronger Test:** Replicate the comparison set across different groups to confirm the intermediate option remains competitive.

## Fix when extreme minimalism is rejected <!-- role: fix -->

- Add one or more intermediate designs that remove some, but not all, conventional scaffolding.
- Select the intermediate design if it attracts substantial preference relative to both the standard and extreme minimalist charts.
- Keep the extreme minimalist version only as an optional style rather than the default.
- Re-evaluate subjective clarity and ease-of-use for the intermediate variant to confirm it does not degrade perceived usability.
