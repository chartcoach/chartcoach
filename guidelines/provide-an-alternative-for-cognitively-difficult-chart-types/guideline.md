---
id: provide-an-alternative-for-cognitively-difficult-chart-types
title: Provide an alternative view when a chart type is cognitively difficult
bibliography: references.bib
description: When a chart type is likely to be cognitively difficult or misinterpreted,
  provide an alternative chart or explanation that supports the same analytic task.
labels:
- chart:pie
- chart:line
- chart:bar
- task:interpret
- visual:form
- impact:accessibility
- data:categorical
- data:temporal
- audience:novice
- principle:flexible
- disability:cognitive
---

## Provide an alternative view for cognitively difficult chart types <!-- role: advice -->

Provide an alternative chart or explanation whenever a chart type is likely to be cognitively difficult or easy to misinterpret, and ensure the alternative supports the same analytic task. If possible, let the user switch the presentation (for example, change the chart type or add features that make values more discrete and countable).

## Why flexible alternatives reduce cognitive barriers in chart interpretation <!-- role: reason -->

Offering alternative representations reduces the chance that the user’s understanding depends on a single, high-risk visual form, and it allows the user to choose a representation that better matches their cognitive needs and interpretation strategies.

**Mechanism:** A second, task-equivalent representation can lower cognitive load and reduce misinterpretation by providing a clearer or more concrete mapping from data to visual elements (for example, making values easier to count or compare).

**Evidence:** Allowing users to switch between visual representations and providing simplified alternatives supports data accessibility for people with intellectual and developmental disabilities (IDD) in interactive data tools. [@wu_understanding_data_2021] An accessible demonstration for IDD applies practices such as avoiding pie charts, limiting categories, and using discrete marks or pictograms, showing how interactive charts can adapt to different user needs. [@cu-visualab_state_states] Chart auditing heuristics identify a need to respect user control and provide adaptable presentations when complex chart forms create barriers. [@elavskyHowAccessibleMy2022]

**Notes:** This guideline targets flexibility in the chart’s presentation, not only adding descriptive text; the alternative should still enable the same decision or comparison.

## When to add an alternative chart or switchable presentation <!-- role: context -->

- **User Goal:** Understand the data well enough to make a decision, comparison, or explanation without relying on a single visually complex form.
- **Task:** Interpret values, compare parts, compare trends, or extract meaning from a chart that may be easy to misread.
- **Data:** Categorical part-to-whole data (often shown as pies), temporal data (often shown as lines), or quantities that are hard to enumerate in their current form.
- **Chart Setting:** Interactive or digital charts where multiple views can be presented, or where the user can be given presentation controls.
- **Audience:** People who may face cognitive accessibility barriers, including people with intellectual and developmental disabilities (IDD), or audiences likely to benefit from simplified representations.
- **Success Criterion:** Users can complete the same analytic task with the alternative representation without increased confusion or effort.

## When not to add an alternative chart or switchable presentation <!-- role: exceptions -->

**Break it when:** The visualization is constrained to a single, fixed form with no space or capability to add another view or control. **Why:** The intended flexibility cannot be delivered in the given medium without removing required content.

## Tradeoffs of providing alternative chart types <!-- role: costs -->

**Sacrifice:** Additional space, design effort, and implementation complexity to maintain multiple representations. **Risk:** Users may be unsure which view to use or may see differences between views as contradictions. **Mitigation:** Ensure alternatives are task-equivalent and clearly labeled as different presentations of the same data.

## Common ways this guideline is implemented incorrectly <!-- role: mistakes -->

**Mistake:** Offering an alternative chart that changes the question (for example, a different aggregation or a different subset of the data). **Why it fails:** The user cannot use the alternative to accomplish the same analytic task, so the barrier remains.

## Quick checks for missing alternatives to difficult chart types <!-- role: check -->

**Failure Sign:** The chart relies on a form identified as high-risk for cognitive difficulty (for example, a pie chart) and there is no other chart or explanation that enables the same task. **Quick Check:** Ask whether a user can choose a different representation that still answers the same question without extra interpretation steps. **Stronger Test:** Have a user from the target audience attempt the task using the provided alternatives and confirm they can complete it using the alternative alone.

## What to do instead when a chart type is cognitively difficult <!-- role: fix -->

- Provide an additional chart or explanation that supports the same analytic task alongside the difficult chart type.
- Add a user control to switch the chart’s presentation into an alternative representation that still answers the same question.
- Modify the chart to make values more discrete or concrete (for example, by adding discrete marks or pictograms) while keeping the task unchanged.
- Limit the number of categories shown in cognitively demanding views and provide a complementary alternative for full detail when needed.
