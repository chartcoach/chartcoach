---
id: offer-progressive-context-on-demand
title: Provide Optional, On-Demand Context
bibliography: references.bib
description: Let viewers access deeper detail (methods, provenance, and raw data)
  when they want it, without cluttering the main view.
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:trust
- data:provenance
- audience:mixed
- resonance:context
---

## The Rule <!-- role: advice -->

Provide a clear overview first, and add optional pathways to more detail (e.g., tooltips, annotations, expandable panels, drill-down, or links to sources/raw data).

## The Logic <!-- role: reason -->

Missing context forces viewers to guess, which increases confusion and distrust; optional context supports curiosity and verification without overwhelming everyone.

- **The Principle:** Progressive disclosure for comprehension and trust
- **The Evidence:** Viewers of crisis maps wanted access to provenance and context when needed to avoid confusion or distrust [@koesten_encountering_2025]. Practitioners report success with layered click-through designs from overview to details to raw data [@schuster_who_2023]. Experts caution that interaction should be purposeful, and lay participants may not use interactive tools at all [@schuster_being_2024].

## Where to Apply <!-- role: context -->

This advice is designed for situations where credibility and interpretation depend on background details that not all viewers need immediately.

- **User Goal:** Understand what the view means, verify “where this came from,” and investigate anomalies or decisions
- **Data Type:** High-stakes or potentially contested data; derived indicators; multi-source or frequently updated data; crisis/incident mapping; dashboards with transformations or aggregation
- **Audience:** Mixed audiences (novices and experts), including skeptical or time-pressured viewers

## When to Break It <!-- role: exceptions -->

- **Scenario:** A non-interactive format (print/PDF/static slide) with no space for links or footnotes\
  **Reason:** “On-demand” access isn’t possible; you must choose a minimal, always-visible context instead.
- **Scenario:** Safety-, privacy-, or security-sensitive data where provenance or drill-down could expose individuals or protected locations\
  **Reason:** The added detail increases harm risk and may violate policy or law.
- **Scenario:** A single-purpose graphic for rapid consumption (e.g., emergency alert card)\
  **Reason:** Extra pathways can slow comprehension; keep only the essential context visible.

## The Price <!-- role: costs -->

- **The Sacrifice:** More design/build time (information architecture, copywriting, QA) and more maintenance (keeping sources and metadata current).
- **The Risk:** Added interaction can be ignored by some viewers, or can create a false sense of transparency if the “details” are incomplete or hard to interpret [@schuster_being_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding interaction “because we can” (filters, hover-only explanations, hidden tabs)\
  **Why it fails:** Users may never discover it, and it increases complexity without increasing understanding [@schuster_being_2024].
- **The Wrong Fix:** Putting all methodological detail into the main caption or chart area\
  **Why it fails:** Clutters the overview and overwhelms readers who only need the headline message.
- **The Wrong Fix:** Linking to a generic source page without mapping it to the specific metric, time range, or transformation\
  **Why it fails:** Viewers still can’t verify the specific claim, undermining trust (the “provenance gap”) [@koesten_encountering_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers ask “Where is this from?”, “What does this include?”, or “Can I see the underlying data?”; the chart feels like a black box.
- **The Test:** Give the graphic to a novice and an expert and ask them to (1) explain what it shows and (2) find the source, update date, and definition of the main metric within 30 seconds. If either can’t, you’re missing accessible context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a “How was this made?” or “Data & methods” link near the title with: source(s), last updated, definitions, and known limitations.
- **Best Fix:** Implement progressive layers: overview → concise annotation/tooltips for key assumptions → expandable methodology/provenance (transformations, inclusion/exclusion, uncertainty) → downloadable or viewable raw/cleaned data, mirroring the drill-down pattern practitioners describe [@schuster_who_2023].
