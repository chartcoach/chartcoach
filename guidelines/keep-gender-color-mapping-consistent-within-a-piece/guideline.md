---
id: keep-gender-color-mapping-consistent-within-a-piece
title: Keep Gender Color Mapping Consistent Within an Article
bibliography: references.bib
description: Once you assign colors to genders, keep that mapping stable across all
  charts in the same piece to prevent misreading.
labels:
- chart:general
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- topic:gender
- source:datawrapper
---

## The Rule <!-- role: advice -->

After assigning colors to gender categories, use the same colors for the same genders across every chart in the article; do not swap mappings between charts. [@muth_gendercolor_2018]

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Consistency reduces cognitive load and prevents readers from applying the wrong learned mapping.
- **The Evidence:** The post reiterates the “mantra in Data Vis” that the same colors should represent the same things within an article, and warns that flipping stereotypical colors can be “dangerous” because readers may not consult the legend and can reach the wrong conclusion. [@muth_gendercolor_2018]

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Compare genders across multiple figures or sections without re-learning encodings.
- **Data Type:** Multi-chart stories or reports with repeated men/women (gender) breakdowns.
- **Audience:** General readers who scan and rely on pattern recognition more than legend-reading. [@muth_gendercolor_2018]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You are intentionally using different encodings because the category definition changes (e.g., different groupings or a different concept of gender categories) and you clearly reintroduce the mapping.
- **Reason:** The post’s consistency argument is about “the same things”; if the “thing” changes, the mapping is not the same and must be redefined. [@muth_gendercolor_2018]

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Less freedom to optimize colors per chart or per surrounding UI/theme.
- **The Risk:** A single chosen palette might be less ideal for some charts (e.g., less contrast against a particular background), but consistency still prevents misinterpretation. [@muth_gendercolor_2018]

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Reusing a newsroom’s general brand colors (e.g., pink and blue) without a fixed decision for which gender gets which color, leading to mixed usage across authors/charts.
- **Why it fails:** The post shows that unclear assignment (even within one publication) increases the chance that readers apply the wrong assumption and don’t check the legend, producing incorrect takeaways. [@muth_gendercolor_2018]

## How to Check <!-- role: check -->

- **Visual Sign:** In a multi-chart piece, the same hue represents different genders in different figures.
- **The Test:** Create a quick “mapping audit”: list each chart and write down “women = \_\_, men = \_\_”; if any row differs, you’ve broken the rule. [@muth_gendercolor_2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Standardize on one mapping and update all charts to match it; then ensure each chart still has adequate contrast.
- **Best Fix:** Establish and document a gender color rule for the whole story (or publication) before designing charts, so multiple authors don’t diverge during production. [@muth_gendercolor_2018]
