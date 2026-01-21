---
id: rotate-color-assignments-across-projects-for-racial-data
title: Rotate Color Assignments Across Projects for Racial Data
bibliography: references.bib
description: Avoid permanently linking any race to a specific color by changing category-color
  mappings across projects.
labels:
- chart:all
- task:categorize
- visual:color
- impact:bias-reduction
- data:categorical
- audience:general
- topic:race-ethnicity
- practice:workflow
- source:datawrapper
---

## The Rule <!-- role: advice -->

Do not consistently assign the same color to the same racial category across different projects; intentionally reshuffle category-color mappings over time.

## The Logic <!-- role: reason -->

All colors carry associations, so repeatedly pairing one group with one color creates a durable mental link that can drift into stereotype-like coding (“this color belongs to that race”). Rotating assignments helps prevent that fixation.

- **The Principle:** Prevent entrenched color-category stereotypes
- **The Evidence:** [@muth_race_ethnicity_colors_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Interpret repeated race/ethnicity charts without learning biased or stereotyped color mappings
- **Data Type:** Recurring publications/dashboards/series that repeatedly visualize race/ethnicity categories
- **Audience:** Returning readers and regular users

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single long-running product requires strict within-product consistency for usability (readers must compare across issues quickly)
- **Reason:** Consistency can support faster recognition; in such cases, mitigate by ensuring the chosen mapping is not stereotype-driven and avoids problematic associations described in the post [@muth_race_ethnicity_colors_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced cross-edition consistency and slower recognition for repeat readers.
- **The Risk:** Viewers may misread categories if they assume last project’s mapping still applies.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the same mapping because “it worked last time” without reconsidering associations
- **Why it fails:** It gradually naturalizes that mapping and can cement unconscious links between color and race [@muth_race_ethnicity_colors_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Your organization’s race charts always show the same group in the same color year after year.
- **The Test:** Audit the last 5–10 visuals: if category-color mappings are identical across projects, you’re not rotating [@muth_race_ethnicity_colors_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap two or more category colors in the next project and ensure the legend/labels are explicit.
- **Best Fix:** Establish a small set of vetted palettes and rotate mappings intentionally, while avoiding stereotype-prone colors (skin tones, brown/olive, de-emphasizing grays, strong-blue-for-Europe) [@muth_race_ethnicity_colors_2024].
