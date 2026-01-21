---
id: avoid-stacked-columns-for-many-categories-or-long-labels
title: Avoid Stacked Column Charts with Many Totals or Long Category Labels
bibliography: references.bib
description: Use stacked columns only for a small number of totals with short labels;
  otherwise switch to row-based displays like stacked bars or tables.
labels:
- chart:stacked-column
- task:compare
- visual:layout
- impact:readability
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper
---

## The Rule <!-- role: advice -->

Don’t use stacked column charts when you have many totals (roughly more than 10) or when category labels are long; use a row-based alternative instead.

## The Logic <!-- role: reason -->

On screens, chart width is limited but height is flexible. Many columns or long labels quickly exceed available width and make the x-axis unreadable; row-based charts (like stacked bars) scale better vertically [@muth_stacked_columns_2018].

- **The Principle:** Fit the chart to screen constraints (width-limited, height-flexible)
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan and compare many categories without label strain
- **Data Type:** Many categorical totals, each split into parts
- **Audience:** Screen-based readers (mobile/desktop) [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have only a few totals and short labels.
- **Reason:** Stacked columns can work well and can display part labels more cleanly than stacked bars [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Switching away from stacked columns may reduce how easily you can place/see labels for parts (compared with columns).
- **The Risk:** Row-based charts can become tall; readers may need to scroll [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shrinking text or rotating long x-axis labels to “make them fit.”
- **Why it fails:** Labels remain hard to read and the chart becomes visually cluttered [@muth_stacked_columns_2018].
- **The Wrong Fix:** Keeping dozens of columns because “height isn’t used.”
- **Why it fails:** Width, not height, becomes the limiting factor on screens [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Crowded columns, overlapping/truncated labels, or heavily rotated x-axis text.
- **The Test:** If you can’t comfortably read every category label at normal size, switch to a row-based design [@muth_stacked_columns_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert to a stacked bar chart to use vertical space for labels.
- **Best Fix:** Consider dot plots, tables, or other row-based chart types when categories are many and parts are few [@muth_stacked_columns_2018].
