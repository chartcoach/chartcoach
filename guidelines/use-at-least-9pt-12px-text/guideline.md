---
id: use-at-least-9pt-12px-text
title: Use at Least 9pt/12px Text
bibliography: references.bib
description: Ensure all chart text is at least 9pt/12px, reserving this minimum only
  for minor labels.
labels:
- chart:general
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:general
- source:chartability
---

## The Rule <!-- role: advice -->

Render no text smaller than 9pt/12px. Use 9pt/12px only for minor text (e.g., axis labels) and make all other text larger. [@elavskyHowAccessibleMy2022]

## The Logic <!-- role: reason -->

Small print reduces legibility and reading performance, making chart labels and annotations harder to perceive and interpret.

- **The Principle:** Discriminability depends on text size
- **The Evidence:** Text smaller than about 9pt (≈12px on screens) significantly reduces readability. [@arditi_rethinking_ada_2017] This is operationalized as a critical “Small text size” heuristic in Chartability. [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for any visualization where users must read chart text.

- **User Goal:** Reading labels/annotations and extracting meaning from textual elements in the visualization
- **Data Type:** Any (because the constraint is on text, not on data structure)
- **Audience:** Broad audiences, including people who may experience reduced readability with small text [@arditi_rethinking_ada_2017]

## When to Break It <!-- role: exceptions -->

- **Scenario:** None supported by the provided evidence.
- **Reason:** The cited guidance defines a strict minimum (no smaller than 9pt/12px). [@elavskyHowAccessibleMy2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less space for plotted marks and potentially more crowding or need for layout adjustments.
- **The Risk:** Increasing text size may force repositioning, shortening, or removal of some labels to maintain a clean layout. [@elavskyHowAccessibleMy2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving small text in place because “WCAG 2.1 has no requirement for text size.”

- **Why it fails:** The heuristic is research-driven and treats small text as a critical accessibility risk even without a WCAG 2.1 criterion. [@elavskyHowAccessibleMy2022]

- **The Wrong Fix:** Assuming the size is “fine” without verifying it because measurement is inconvenient.

- **Why it fails:** Font-size testing is explicitly noted as complex when sizes are not stored or known, so unverified small text often slips through. [@elavskyHowAccessibleMy2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Labels, ticks, captions, or annotations appear tiny relative to other UI text and are hard to read.
- **The Test:** Verify the rendered text size is ≥ 9pt/12px for every textual element (and confirm only minor text uses the minimum), noting that measurement may be difficult without metadata/tooling. [@elavskyHowAccessibleMy2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the font size of any text below 9pt/12px to meet the minimum. [@elavskyHowAccessibleMy2022]
- **Best Fix:** Treat 9pt/12px as a minimum reserved for minor labels and increase all other chart text above this threshold to improve readability. [@elavskyHowAccessibleMy2022]
