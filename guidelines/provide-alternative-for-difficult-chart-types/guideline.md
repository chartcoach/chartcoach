---
id: provide-alternative-for-difficult-chart-types
title: Provide an Alternative for Difficult Chart Types
bibliography: references.bib
description: Offer an alternative chart or controllable presentation mode when a chart
  type is likely to be cognitively difficult or easy to misinterpret.
labels:
- chart:pie
- chart:line
- chart:bar
- task:interpret
- task:compare
- visual:shape
- visual:position
- impact:accessibility
- impact:clarity
- data:categorical
- data:temporal
- audience:novice
- audience:idd
- principle:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

When you use a chart type that is cognitively difficult or high-risk for misinterpretation (e.g., pie charts, line charts without discrete marks, or bar charts without countable isotypes), provide an alternative chart or alternative explanation that lets the user accomplish the same analytical task, and optionally allow the user to switch the presentation style.

## The Logic <!-- role: reason -->

Providing alternatives and user-controlled switching reduces the cognitive difficulty and misinterpretation risk associated with certain visual encodings, while preserving the same underlying analytical task through a different representation, aligning with the “Flexible” accessibility principle described in Chartability [@elavskyHowAccessibleMy2022].

- **The Principle:** User-controlled representation switching to match cognitive needs.
- **The Evidence:** Tools and guidance for people with intellectual and developmental disabilities emphasize avoiding or adapting difficult chart types and allowing users to switch between representations to support comprehension [@wu_understanding_data_2021; @cu-visualab_state_states].

## Where to Apply <!-- role: context -->

This advice is designed for charts that are likely to be confusing or misread by some users.

- **User Goal:** Correctly interpret the data and complete the same analysis even if the default chart is hard to understand (e.g., make comparisons or understand change).
- **Data Type:** Categorical breakdowns (commonly shown as pies/bars) and temporal trends (commonly shown as lines).
- **Audience:** Broad audiences, especially users who may face higher cognitive load or interpretive difficulty (including people with intellectual and developmental disabilities) [@wu_understanding_data_2021].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The user is already offered a different representation or explanation that enables the same task.
- **Reason:** The requirement is satisfied once an equivalent alternative is available and usable for the same purpose [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** More design/development effort to create and maintain multiple representations or explanations.
- **The Risk:** Users may be overwhelmed by additional options if switching controls or multiple views are presented without care [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Keeping the difficult chart type and only adding minor stylistic tweaks (without providing an alternative representation or explanation for the same task).
- **Why it fails:** The core cognitive difficulty remains, and users still lack a usable path to complete the analysis via a different form [@wu_understanding_data_2021; @elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The visualization relies on a cognitively difficult form (e.g., a pie chart; a line with no discrete marks; bars that cannot be counted via isotypes) with no accompanying alternative representation or explanation.
- **The Test:** Verify that a user can choose or access an alternative chart/explanation that supports the same analytical task (e.g., switching from pie to an alternative representation; adding discrete marks to line intervals; adding countable isotypes to segment bars) [@cu-visualab_state_states; @wu_understanding_data_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an alternative explanation and an alternative chart alongside the difficult chart type that supports the same task [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide user control to switch presentation styles to an easier alternative while preserving the task (e.g., allow changing pies into treemaps or stacked bars; add discrete marks to line intervals; add countable isotypes to divide bars) [@wu_understanding_data_2021; @cu-visualab_state_states; @elavskyHowAccessibleMy2022].
