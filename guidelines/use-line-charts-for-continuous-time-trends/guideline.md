---
id: use-line-charts-for-continuous-time-trends
title: Use Line Charts to Show Continuous Change Over Time
bibliography: references.bib
description: Use a line chart when your main message is how a value changes across
  many time points.
labels:
- chart:line
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:mainstream
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a line chart when you need to show how one or more values develop over time across many time points.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Continuous time is most intuitively read as a connected trajectory, making change (direction, pace, turning points) easy to perceive.
- **The Evidence:** The post calls the classic line chart “intuitive to read and usually a solid choice” for showing how numbers change over months or years [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Seeing development over time (e.g., temperature, inflation, poll numbers).
- **Data Type:** Time series with many points (months/years), one or several series.
- **Audience:** Mainstream/general readers [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You only have a few time points.
- **Reason:** The post suggests column charts are usually a good fit for just a few points in time [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** With many categories, multiple lines can become visually overwhelming (“spaghetti”).
- **The Risk:** Readers may struggle to follow individual series when many lines overlap [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Plotting lots of categories as one “multiple lines” chart without changing the layout.
- **Why it fails:** Overlap and clutter make comparison hard; the post recommends small multiples (multiple lines chart split into panels) to tame this [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** A “spaghetti monster” where lines overlap and are hard to trace.
- **The Test:** If you can’t reliably trace a single series from start to end at a glance, the single-panel multi-line approach is failing [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of series shown or highlight only a few key lines.
- **Best Fix:** Use small multiples (a multiple-lines chart with each line in its own panel) when many categories overlap heavily [@muth_chart_types_guide_2025].
