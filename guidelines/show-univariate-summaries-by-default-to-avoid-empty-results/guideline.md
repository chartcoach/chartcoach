---
id: show-univariate-summaries-by-default-to-avoid-empty-results
title: Show Univariate Summaries Before Any User Input
bibliography: references.bib
description: Start exploration with automatic one-variable summaries to prevent empty
  states and reduce premature fixation.
labels:
- chart:histogram
- task:overview
- visual:position
- impact:discoverability
- data:univariate
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

On initial load, automatically display a univariate summary for every variable.

## The Logic <!-- role: reason -->

Univariate summaries provide immediate orientation, reduce the chance of “empty results,” and encourage users to examine variables before jumping to relationships—an explicit goal in Voyager’s design [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Orientation-first exploration and avoiding empty states
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Learn what each field contains and how values are distributed
- **Data Type:** New/unfamiliar dataset; mixed variable types
- **Audience:** Analysts starting exploratory data analysis

## When to Break It <!-- role: exceptions -->

- **Scenario:** The dataset has so many fields that showing all univariate summaries would overwhelm the interface or performance budget.
- **Reason:** Voyager notes the need for bounded presentation and loads a fixed number of views for performance [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Screen space and rendering time spent on summaries the user may not care about.
- **The Risk:** Users may skim too quickly and miss important distributions if summaries are overly compact.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a blank canvas that requires the user to pick fields before anything appears.
- **Why it fails:** It increases friction and can cause users to fixate on a few familiar variables instead of scanning broadly [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** The interface initially shows no charts until a variable is selected.
- **The Test:** New users ask “What should I do first?” or repeatedly pick the same obvious fields.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Auto-generate one chart per variable as the initial gallery.
- **Best Fix:** Combine univariate summaries with a schema panel that lets users immediately include/exclude variables and choose basic transformations [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
