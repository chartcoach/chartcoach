---
id: avoid-gray-as-a-diminishing-color-for-other-or-multiracial-groups
title: "Avoid gray for \u201COther\u201D or \u201CMultiracial\u201D categories when\
  \ visualizing people"
bibliography: references.bib
description: "Do not use gray to encode \u201COther\u201D or \u201CMultiracial\u201D\
  \ groups because it can signal lesser importance."
labels:
- chart:bar
- task:compare
- visual:color
- impact:fairness
- data:categorical
- audience:general
- domain:demographics
---

## Give “Other” and “Multiracial” groups equal visual weight in the palette <!-- role: advice -->

Avoid using gray to encode “Other” or “Multiracial” categories in charts about people. Assign these categories colors that carry comparable visual importance to the other groups.

## Gray can communicate “less important” for human categories <!-- role: reason -->

Gray often functions as a de-emphasis cue in visual design; when used for a group of people, it can imply that the group matters less. For sensitive demographic topics, that implication can be disrespectful and can distort the intended reading of the data.

**Mechanism:** Viewers interpret saturation and chroma as signals of prominence; mapping a people-category to a de-emphasized neutral can create a hierarchy that isn’t in the data.

**Evidence:** Using gray for “other” or “multiracial” is identified as potentially inappropriate because gray can communicate diminished importance for categories that represent people [@muth_race_ethnicity_colors_2024].

**Notes:** This concern is strongest when gray is uniquely assigned to a people-category rather than used consistently for non-data scaffolding.

## Categorical demographic charts with an “Other” bucket <!-- role: context -->

- **User Goal:** Compare demographic groups without implying that some groups are “less real” or less important.
- **Task:** Read category shares, ranks, or trends across race/ethnicity groupings including “Other” and/or “Multiracial.”
- **Data:** Nominal categories; often includes a residual bucket (“Other,” “Two or more races,” “Did not disclose”).
- **Chart Setting:** Legends, stacked bars/areas, dot plots, or maps where color conveys group identity.
- **Audience:** General audiences; includes people who may identify with residual categories.
- **Success Criterion:** No category appears visually dismissed unless the editorial framing explicitly supports it.

## When intentional de-emphasis is the explicit story <!-- role: exceptions -->

**Break it when:** Your narrative explicitly treats a category as background context (not a focal group) and that de-emphasis is clearly explained in text and design. **Why:** The hierarchy is intentional and communicated, rather than an accidental message that “these people don’t matter” [@muth_race_ethnicity_colors_2024].

## Tradeoffs of not using gray for residual categories <!-- role: costs -->

**Sacrifice:** You may lose an easy way to push a residual bucket into the background. **Risk:** A fully equal palette can make the chart feel busier when there are many small categories. **Mitigation:** Use labeling, ordering, or grouping rather than color dulling to manage complexity.

## Common ways designers unintentionally dismiss groups <!-- role: mistakes -->

**Mistake:** Coloring “Other,” “Multiracial,” or “Did not disclose” in gray while all other groups get saturated hues. **Why it fails:** It can imply the gray group is less important even when it represents real people in the data [@muth_race_ethnicity_colors_2024].

## Quick checks for unintended hierarchy <!-- role: check -->

**Failure Sign:** One category reads like background decoration rather than data about people. **Quick Check:** Squint at the chart and see which groups “drop out” first; if it’s a people-category, reassess. **Stronger Test:** Ask “If I were in that category, would I feel dismissed by the color choice?”

## Ways to keep categories respectful without losing readability <!-- role: fix -->

- Assign “Other” and “Multiracial” a normal palette color with similar saturation and lightness to other categories.
- Reduce clutter with direct labels and ordering, not by dulling a people-category.
- If a residual bucket must be visually quieter, explain that editorial choice in accompanying text and make the de-emphasis subtle rather than stark.
- Consider splitting residual categories (when data supports it) so “Other” isn’t a catch-all that invites visual sidelining.
