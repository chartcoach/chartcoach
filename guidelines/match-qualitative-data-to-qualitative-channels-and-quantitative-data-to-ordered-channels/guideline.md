---
id: match-qualitative-data-to-qualitative-channels-and-quantitative-data-to-ordered-channels
title: Match Data Type to the Right Kind of Visual Channel
bibliography: references.bib
description: Encode qualitative variables with qualitative channels (e.g., hue/shape)
  and quantitative variables with ordered channels (e.g., size/intensity).
labels:
- visual:color
- visual:shape
- visual:size
- data:categorical
- data:quantitative
- impact:correctness
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

Encode qualitative (nominal) variables with qualitative channels (e.g., shape or color hue) and encode quantitative variables with quantitatively ordered channels (e.g., size or color intensity with sequential/diverging/cyclic order).

## The Logic <!-- role: reason -->

The framework distinguishes qualitative vs. quantitative graphic variables and explains that qualitative channels lack intrinsic ordering, while quantitative channels support ordered mappings (sequential, diverging, cyclic).

- **The Principle:** Qualitative-vs-quantitative channel compatibility
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Avoid implying order where none exists; support correct ranking/magnitude reading when order does exist
- **Data Type:** Mixed datasets with categories plus measures
- **Audience:** Designers mapping columns to visual properties

## When to Break It <!-- role: exceptions -->

- **Scenario:** Intentionally binning a quantitative variable into categories
- **Reason:** After binning, you are encoding a qualitative/ordinal variable and should use appropriate channels for the transformed scale [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer “creative” color uses (you can’t treat rainbow hue as ordered magnitude by default)
- **The Risk:** Running out of distinct qualitative categories if too many groups must be encoded

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using color hue gradients to represent ordered magnitude without specifying a sequential/diverging/cyclic schema
- **Why it fails:** Hue is treated as qualitative in the framework; it can suggest categories rather than ordered magnitude [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers cannot tell which of two colored marks represents “more,” or they infer false ordering among categories.
- **The Test:** For each encoded variable, state whether the channel is qualitative or quantitative; they must match (or be an explicit, documented transformation) [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap hue/shape encodings for categories; swap to size or color intensity for magnitude.
- **Best Fix:** Redesign the mapping so each data scale (nominal/ordinal/interval/ratio) is paired with a compatible channel and ordering direction (sequential/diverging/cyclic where appropriate) [@bornerDataVisualizationLiteracy2019].
