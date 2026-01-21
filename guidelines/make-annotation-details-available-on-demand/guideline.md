---
id: make-annotation-details-available-on-demand
title: Provide Annotation Details on Hover and Link Out for Depth
bibliography: references.bib
description: Show concise annotation labels by default, and reveal richer details
  and the full source only on interaction.
labels:
- chart:line
- task:explore
- visual:interaction
- impact:readability
- data:temporal
- audience:general
- domain:journalism
---

## The Rule <!-- role: advice -->

Show brief annotation text by default (e.g., titles), and reveal additional detail (e.g., snippets) on hover; let users click annotations to navigate to the full source.

## The Logic <!-- role: reason -->

This preserves limited screen space while still supporting deeper investigation. Contextifier’s design keeps the visualization scannable and uses interaction to turn the chart into an entry point for exploration without overcrowding the display.

- **The Principle:** Details-on-demand balances spatial constraints with access to depth.
- **The Evidence:** Contextifier displays article titles by default, shows snippets on hover, and supports clicking annotations to navigate to full articles to enable exploration from the visualization [@hullmanContextifierAutomaticGeneration2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Skim quickly, then drill down into a few items of interest.
- **Data Type:** Charts with text annotations that have longer supporting descriptions (e.g., headlines + snippets).
- **Audience:** Online readers with interactive-capable devices.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Static print graphics or environments where hover/click is unavailable.
- **Reason:** Without interaction, hiding detail makes the annotation incomplete.

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires interaction; some users may not discover hidden content.
- **The Risk:** If hover targets are small or crowded, interaction becomes frustrating and detail remains effectively inaccessible.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Putting full snippets directly on the chart for every annotation.
- **Why it fails:** It overwhelms the chart and violates the concision and readability constraints the interaction is meant to solve [@hullmanContextifierAutomaticGeneration2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Default view feels text-heavy or the line is obscured by paragraphs.
- **The Test:** In the default state, confirm you can still perceive overall trend and key movements without reading.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace snippet text with short titles in the default view.
- **Best Fix:** Implement hover-to-reveal snippets and click-to-open sources, keeping the chart readable while preserving depth [@hullmanContextifierAutomaticGeneration2013].
