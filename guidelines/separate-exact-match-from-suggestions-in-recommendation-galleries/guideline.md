---
id: separate-exact-match-from-suggestions-in-recommendation-galleries
title: Separate Exact-Match Views From Suggested-Variable Views
bibliography: references.bib
description: Partition the gallery so users can distinguish charts that use only their
  selections from charts that add system-suggested fields.
labels:
- chart:gallery
- task:browse
- visual:layout
- impact:orientation
- data:multivariate
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

Partition the recommendation gallery into (1) views containing only user-selected variables and (2) views that include additional suggested variables.

## The Logic <!-- role: reason -->

Separating “exact match” from “suggestion” keeps the user oriented about what is under their direct control versus what the system added, supporting mixed-initiative exploration and contextual reading across many charts [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Mixed-initiative transparency and context maintenance
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Browse many recommended charts without losing track of intent
- **Data Type:** Any dataset where recommendations add fields beyond the current selection
- **Audience:** Analysts iterating between broad scanning and follow-up

## When to Break It <!-- role: exceptions -->

- **Scenario:** The system never adds variables (only changes encodings).
- **Reason:** The distinction provides little value if there are no system-added fields.

## The Price <!-- role: costs -->

- **The Sacrifice:** More UI structure (headers/sections) and potentially more scrolling.
- **The Risk:** Users might ignore one section if it is visually deprioritized.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mixing user-only and system-augmented views in one undifferentiated grid.
- **Why it fails:** Users can’t tell whether a chart is answering their selection or proposing a new direction [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask “Why is this variable here?” when viewing a recommendation.
- **The Test:** Have users predict what will appear after selecting a variable; confusion indicates insufficient separation/labeling.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Create two labeled sections with brief header descriptions summarizing what each contains.
- **Best Fix:** Also visually differentiate “selected” vs “suggested” variable tokens inside each chart (e.g., distinct capsule styles) [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
