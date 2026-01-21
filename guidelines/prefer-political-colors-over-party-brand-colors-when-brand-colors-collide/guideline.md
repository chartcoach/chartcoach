---
id: prefer-political-colors-over-party-brand-colors-when-brand-colors-collide
title: Use Political Colors When Party Brand Colors Collide
bibliography: references.bib
description: If party logo/brand colors are too similar to distinguish, switch to
  ideology-linked political colors for clearer election reporting.
labels:
- chart:map
- chart:bar
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- domain:election-reporting
- source:datawrapper
---

## The Rule <!-- role: advice -->

When party brand/logo colors are too similar to tell apart, do not force them—use ideology-linked political colors (e.g., green for greens, yellow for liberals) to achieve clearer party separation. [@muth_partycolors_2018]

## The Logic <!-- role: reason -->

Party brand palettes are designed for party identity, not for multi-category comparison; they can cluster around the same hues (the post highlights major parties in Germany using near-identical reds), making election charts/maps ambiguous. Political colors provide an alternate convention that can reduce overlap and support one-color-per-party differentiation in coverage. [@muth_partycolors_2018]

- **The Principle:** Use a category encoding that optimizes discriminability, not brand fidelity
- **The Evidence:** [@muth_partycolors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish parties quickly in legends, charts, and region maps.
- **Data Type:** Multiple parties where at least two important parties share similar brand hues.
- **Audience:** Broad readership encountering party colors in repeated election coverage. [@muth_partycolors_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Brand colors are already distinct enough across all relevant parties.
- **Reason:** If brand colors do not create confusion, there’s no need to deviate from what parties use publicly. [@muth_partycolors_2018]
- **Scenario:** There is an established, widely recognized non-ideological convention you must follow in your context.
- **Reason:** The post shows that conventions can become entrenched (e.g., US red/blue assignment) even if not ideology-based. [@muth_partycolors_2018]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less alignment with official party branding/logos. [@muth_partycolors_2018]
- **The Risk:** Political-color conventions can vary for some parties (the post notes ambiguity for “The Left” in Germany), so you may still need an internal decision and documentation. [@muth_partycolors_2018]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Copying brand colors even when they create near-duplicates among major parties.
  - **Why it fails:** Readers can’t reliably decode party identity from color. [@muth_partycolors_2018]
- **The Wrong Fix:** Mixing brand colors for some parties with political colors for others without ensuring the full set remains distinct.
  - **Why it fails:** You can reintroduce collisions and reduce overall palette coherence. [@muth_partycolors_2018]

## How to Check <!-- role: check -->

- **Visual Sign:** Readers would plausibly confuse two parties in a legend or map because their colors are extremely close. [@muth_partycolors_2018]
- **The Test:** Compare party swatches side-by-side; if two major parties appear nearly identical (especially in small legend chips), treat brand colors as “colliding.” [@muth_partycolors_2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reassign only the colliding parties to clearer political-color choices while keeping other assignments stable. [@muth_partycolors_2018]
- **Best Fix:** Build a full party palette primarily from political colors (ideology-linked) so each party has a unique, non-overlapping slot, then apply it consistently across all election visuals. [@muth_partycolors_2018]
