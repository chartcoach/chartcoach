---
id: double-encode-status-with-symbols-not-just-color
title: Add Symbols to Reinforce Color-Coded Status
bibliography: references.bib
description: Use symbols (e.g., checkmarks) alongside color to communicate good/bad
  or other statuses without relying on hue alone.
labels:
- chart:table
- task:signal
- visual:shape
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

When color indicates a status (e.g., good/bad), add a symbol to each colored value so the status remains clear even if the colors are indistinguishable.

## The Logic <!-- role: reason -->

Symbols provide a non-color cue that survives color vision deficiencies; combining symbol + adjusted lightness further increases separability when scanning [@muth_colorblindness_2020].

- **The Principle:** Redundant encoding with a non-color channel
- **The Evidence:** The article recommends using symbols when you can’t rely on color alone (e.g., due to brand colors) and shows an example using checkmarks plus lightness adjustments to improve skimmability for red/green-blind readers [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly classify items as pass/fail, good/bad, on/off, increased/decreased
- **Data Type:** Categorical status values in tables or annotated charts
- **Audience:** Mixed audiences, including colorblind readers and fast scanners [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart already uses shapes to encode another variable and adding symbols would confuse meaning
- **Reason:** Competing shape semantics can increase cognitive load and misinterpretation [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual elements and slightly denser layout
- **The Risk:** Symbols can feel visually repetitive or cluttered in large tables [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping red/green status colors but adding a legend note like “red = bad, green = good”
- **Why it fails:** If the hues collapse, the legend cannot disambiguate the marks themselves during scanning [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** In grayscale or simulation, “good” and “bad” cells look the same
- **The Test:** Convert to black and white; confirm you can still classify each item correctly using symbols alone [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a simple icon (✔/✖, ▲/▼) next to each colored value
- **Best Fix:** Use symbols plus lightness-separated colors, and consider reducing reliance on background fills in favor of clear marks and labels [@muth_colorblindness_2020].
