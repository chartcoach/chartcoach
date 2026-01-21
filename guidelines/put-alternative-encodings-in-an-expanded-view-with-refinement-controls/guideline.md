---
id: put-alternative-encodings-in-an-expanded-view-with-refinement-controls
title: Move Encoding Alternatives into an Expanded View
bibliography: references.bib
description: Keep the main gallery scannable and let users drill down to see alternative
  encodings and refine a chosen chart.
labels:
- chart:gallery
- task:refine
- visual:position
- impact:scannability
- data:multivariate
- audience:analyst
- system:interaction
---

## The Rule <!-- role: advice -->

Provide an expanded chart view that shows (a) a larger main chart and (b) thumbnails of alternative encodings of the same data, plus basic refinement controls.

## The Logic <!-- role: reason -->

Voyager separates breadth (main gallery) from depth (expanded gallery). This supports rapid scanning while still enabling users to inspect encoding variations and apply small refinements such as axis transpose, sorting, and scale changes without enumerating all variants in the main gallery [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Two-level navigation: browse broadly, drill down selectively
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** After spotting a promising relationship, evaluate alternative encodings and tune view parameters
- **Data Type:** Variable sets where multiple encodings are valid (e.g., scatter vs faceted scatter)
- **Audience:** Analysts shifting from scanning to investigating

## When to Break It <!-- role: exceptions -->

- **Scenario:** Mobile/small-screen contexts where modal expansion and thumbnails are impractical.
- **Reason:** The expanded design relies on additional screen space for a main panel + sidebar.

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra interaction step to see alternatives.
- **The Risk:** Users might not discover the expand affordance and assume alternatives don’t exist.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding every alternative (transpose, scale, sort) as separate thumbnails in the main gallery.
- **Why it fails:** It reduces data variation and makes browsing slower, opposing Voyager’s C1/C5 considerations [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** The main gallery is dominated by one variable set shown with many tiny parameter tweaks.
- **The Test:** If users must scroll extensively to get past one selection, you’ve pushed refinement into the wrong level.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an “expand” button per view that opens a larger chart and a sidebar of alternatives.
- **Best Fix:** In expanded view, support lightweight refinement controls (transpose axes, sort, linear vs log scale) so users can fine-tune without exploding the gallery [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
