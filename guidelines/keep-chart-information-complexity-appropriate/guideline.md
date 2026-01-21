---
id: keep-chart-information-complexity-appropriate
title: Limit Chart Information Complexity
bibliography: references.bib
description: Keep chart encodings and structure simple enough for the task by avoiding
  dual axes, unnecessary 3D, and too many categories.
labels:
- chart:general
- task:understand
- visual:encoding
- impact:clarity
- data:categorical
- audience:general
- accessibility:cognitive
- source:chartability
---

## The Rule <!-- role: advice -->

Keep information complexity appropriate to the task: do not use more than one X or Y axis without first presenting the charts separately, do not encode a third spatial dimension (z) unless the data itself is truly 3D, and avoid showing more than 5 categories in a single chart. [@elavskyHowAccessibleMy2022] [@ed_design_guidelines]

## The Logic <!-- role: reason -->

Reducing the number of simultaneous encodings and structural elements lowers cognitive load and reduces ambiguity when interpreting statistical graphics. Limiting categories and avoiding dual axes and unnecessary 3D helps people correctly map what they see to what the chart means, instead of spending attention resolving competing scales or visual dimensions. [@elavskyHowAccessibleMy2022] [@ed_design_guidelines]

- **The Principle:** Minimize cognitive load by limiting concurrent information structures (axes, dimensions, categories).
- **The Evidence:** Federal guidance recommends limiting charts to about five categories and avoiding dual axes and 3D graphics to prevent cognitive overload and improve comprehension. [@ed_design_guidelines]

## Where to Apply <!-- role: context -->

Use this rule whenever the chart must be understandable without specialized training.

- **User Goal:** Quickly and reliably interpret what the chart shows without ambiguity. [@elavskyHowAccessibleMy2022]
- **Data Type:** Categorical comparisons or multi-variable displays where designers may be tempted to add dual axes, 3D, or many categories. [@elavskyHowAccessibleMy2022]
- **Audience:** Broad audiences, including accessibility contexts where cognitive load must be minimized. [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The dataset is inherently 3D (spatial, modeling, or other truly three-dimensional data).
- **Reason:** A z dimension is then part of the data itself rather than a decorative or compressive encoding. [@elavskyHowAccessibleMy2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need multiple charts instead of one, or you may need to omit/aggregate categories beyond five.
- **The Risk:** Readers may need to view more than one panel to get the full picture, and some detailed distinctions may be hidden by grouping. [@elavskyHowAccessibleMy2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using dual axes to “fit more stories” into a single chart without first showing separate charts.

- **Why it fails:** Dual axes increase attentional burden and can make interpretation ambiguous for a broad audience. [@elavskyHowAccessibleMy2022] [@ed_design_guidelines]

- **The Wrong Fix:** Adding 3D to a 2D dataset to imply depth or improve aesthetics.

- **Why it fails:** A third spatial dimension adds interpretive complexity without adding corresponding data meaning when the data is not truly 3D. [@elavskyHowAccessibleMy2022] [@ed_design_guidelines]

- **The Wrong Fix:** Displaying many categories (more than 5) in one view.

- **Why it fails:** Too many categories increases cognitive load and reduces clarity, making the chart harder to interpret. [@ed_design_guidelines] [@elavskyHowAccessibleMy2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple x/y scales are present; the chart uses perspective/3D depth for non-3D data; or the legend/categories exceed five distinct groups.
- **The Test:** Count (1) the number of distinct x/y axes, (2) whether a z dimension is used, and (3) the number of categories shown—if you have >1 axis per orientation without separate charts first, any z for non-3D data, or >5 categories, you’ve violated the rule. [@elavskyHowAccessibleMy2022] [@ed_design_guidelines]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories to five or fewer (e.g., by grouping or selecting a subset) and remove dual axes or 3D effects. [@ed_design_guidelines] [@elavskyHowAccessibleMy2022]
- **Best Fix:** Split the visualization into separate charts before combining information, ensuring each chart has a single clear axis structure and only uses z when the data is truly 3D. [@ed_design_guidelines] [@elavskyHowAccessibleMy2022]
