---
id: order-stacked-areas-by-importance-and-put-the-key-series-on-the-baseline
title: Put the most important series at the bottom of a stacked area chart and highlight
  it with color
bibliography: references.bib
description: Stacked area charts are easier to read when the key series sits on a
  consistent baseline and is visually emphasized.
labels:
- chart:area
- task:focus
- visual:color
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## Place the key area on the baseline and make it visually distinct <!-- role: advice -->

In a stacked area chart, put the most important series at the bottom of the stack and use color to make it stand out.

## The baseline is the easiest reference line in a stacked area chart <!-- role: reason -->

Only the bottom series in a stacked area chart shares a stable baseline, which enables more reliable comparisons over time than the floating baselines of higher layers.

**Mechanism:** A constant baseline reduces perceptual and cognitive effort by removing the need to infer thickness relative to a shifting reference.

**Evidence:** Readers can compare values more easily in stacked areas when important values share the same baseline, and emphasizing the key value with color is recommended [@muth_area_charts_2018].

**Notes:** “Most important” should be defined by the communication goal (headline series, primary stakeholder, or main takeaway).

## When this applies <!-- role: context -->

- **User Goal:** Track the most important component’s trend while still seeing the full composition.
- **Task:** Read one series accurately and the rest contextually.
- **Data:** Multi-series time composition suitable for stacked areas.
- **Chart Setting:** Explanatory charts where one component is the narrative anchor.
- **Audience:** Broad audiences who need clear guidance on what to look at first.
- **Success Criterion:** The key component can be read without mentally subtracting other layers.

## When not to follow this <!-- role: exceptions -->

**Break it when:** No single series is more important than the others. **Why:** Baseline privilege and highlight color can bias attention toward a series that should not dominate interpretation [@muth_area_charts_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some other series may become harder to compare if moved away from the baseline. **Risk:** Highlight color can be interpreted as normative emphasis rather than editorial guidance. **Mitigation:** Ensure the highlighted series aligns with the chart title and accompanying text [@muth_area_charts_2018].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Leaving the default stack order so an unimportant series sits at the baseline. **Why it fails:** The easiest-to-read position is wasted, and readers may focus on the wrong component [@muth_area_charts_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The series you discuss most in the text is not the easiest one to read in the chart. **Quick Check:** Identify the primary series in the headline; confirm it is the bottom layer. **Stronger Test:** Ask a reader which series they think is most important; if they pick a different one, reorder and recolor [@muth_area_charts_2018].

## What to do instead <!-- role: fix -->

- Reorder the stack so the series central to the narrative is at the bottom [@muth_area_charts_2018].
- Use a stronger, distinct color for the key series and more muted colors for the others [@muth_area_charts_2018].
- If multiple series are equally important to compare, switch to a line chart instead of relying on stack order [@muth_area_charts_2018].
