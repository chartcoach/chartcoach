---
id: add-breathing-room-and-remove-competing-labels-for-map-annotations
title: Add Padding and Remove Competing Labels
bibliography: references.bib
description: Create space for map annotations by increasing map padding and removing
  nonessential labels that compete for attention.
labels:
- chart:map
- task:annotate
- visual:layout
- impact:clarity
- data:geospatial
- audience:general
- complexity:basic
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Add padding around the map and delete nonessential base labels (like city names) so annotations don’t compete with other text.

## The Logic <!-- role: reason -->

Reducing competing text and increasing whitespace lowers visual competition, giving annotations and data marks clear priority and improving scanability across the map, as shown in the redesign steps in [@mintzer_map_annotations_2024].

- **The Principle:** Reduce competing visual elements to clarify hierarchy
- **The Evidence:** [@mintzer_map_annotations_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Notice and understand several regional patterns called out by annotations
- **Data Type:** Dense dot map (many marks) with multiple narrative notes
- **Audience:** General readers, including mobile viewers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The map’s main task is wayfinding (readers must identify specific cities/places)
- **Reason:** Removing base labels can make orientation harder than the annotation clutter it solves.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less geographic reference information (fewer place names) and slightly less map area (due to padding).
- **The Risk:** Some readers may feel less confident locating regions without familiar labels.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping all city labels and just shrinking annotation text to “make it fit.”
- **Why it fails:** The map still has too many competing words; the annotation becomes harder to read while clutter remains (the problem described and addressed in [@mintzer_map_annotations_2024]).

## How to Check <!-- role: check -->

- **Visual Sign:** Your eye bounces between city labels and annotations, and the narrative notes don’t feel “settled” into open space.
- **The Test:** Temporarily hide all base labels; if the annotations instantly feel clearer (without losing essential orientation), the labels were competing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a small border/padding (e.g., ~5%) and remove city labels first, then reassess.
- **Best Fix:** Keep only the minimal geographic references needed for orientation, and allocate generous whitespace so annotations can sit without crowding, following the approach in [@mintzer_map_annotations_2024].
