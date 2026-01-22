---
id: provide-a-default-opinionated-view-before-build-your-own-analysis
title: Provide a default, opinionated view before offering build-your-own charting
bibliography: references.bib
description: When users must assemble charts by choosing and combining variables,
  start them with a sensible default view of the data.
labels:
- chart:dashboard
- task:explore
- visual:interaction
- impact:accessibility
- data:multivariate
- audience:novice
- disability:cognitive
- principle:assistive
- source:community-practice
---

## Default-first analysis workflows <!-- role: advice -->

Provide a default, opinionated view of the data whenever the interface asks users to build their own chart by selecting and combining variables. The default view should be immediately usable as a starting point without requiring configuration.

## Reduce cognitive and functional labor in analytic chart-building <!-- role: reason -->

Requiring users to start from a blank slate shifts the primary work from interpreting data to constructing the representation, which increases cognitive load and makes exploration harder to initiate and sustain. A default view scaffolds sensemaking by giving users an immediate anchor for what the data contains and how it can be read, reducing the labor required to begin and proceed.

**Mechanism:** A usable starting state reduces decision fatigue (what to choose, in what order, and how to combine it) and lowers the interaction burden needed to reach a meaningful first insight.

**Evidence:** Build-your-own analytical experiences can be cognitively difficult, especially when combined with other access needs, so providing a default view reduces the labor barrier to use in data interfaces [@elavskyHowAccessibleMy2022]. Accessibility guidance for data experiences emphasizes designing for a good experience beyond mere compliance, including reducing the effort required of users to access information and functionality [@elavskyHowAccessibleMy2022].

**Notes:** This guideline targets the starting state of an analytic workflow, not the long-term flexibility of exploration.

## Where build-your-own charting creates a blank-slate barrier <!-- role: context -->

- **User Goal:** Quickly understand what the dataset is about and find a plausible first insight or direction.
- **Task:** Exploratory analysis, sensemaking, and early hypothesis formation.
- **Data:** Multivariate datasets where many variable combinations are possible and the “right” first view is not obvious.
- **Chart Setting:** Analytical environments that require users to choose fields, encodings, aggregations, filters, or chart types before anything meaningful is shown.
- **Audience:** People with cognitive accessibility needs, mixed-ability audiences, and anyone unfamiliar with the dataset or tool.
- **Success Criterion:** Users can start interpreting the data immediately without configuration and can proceed to customization from a stable baseline.

## When not to require a default view <!-- role: exceptions -->

**Break it when:** The purpose of the tool is explicitly educational and the learning objective is to teach chart construction from first principles. **Why:** A default view may short-circuit the intended learning activity and reduce deliberate practice.

## Tradeoffs of opinionated defaults <!-- role: costs -->

**Sacrifice:** Some flexibility and perceived neutrality in the starting experience. **Risk:** The default can bias user attention toward one narrative or pattern and may be misread as “the” correct view. **Mitigation:** Treat the default as a starting point and make it clear that users can change variables and views.

## Common failures in build-your-own analysis tools <!-- role: mistakes -->

**Mistake:** Showing an empty canvas with only controls and requiring users to pick multiple fields before any view appears. **Why it fails:** Users must do substantial cognitive and interaction work before they can even begin interpreting the data.

## Quick ways to verify a default-first workflow <!-- role: check -->

**Failure Sign:** First-time users must make several choices (fields, chart type, encoding) before any data view appears. **Quick Check:** Load the experience and attempt to gain a basic takeaway without touching any controls; if you cannot, it fails. **Stronger Test:** Observe whether a new user can describe what the data is and what the view shows within a short first interaction without guidance [@elavskyHowAccessibleMy2022].

## Practical remediations for blank-slate charting <!-- role: fix -->

- Provide a preselected default chart with a clear title or takeaway so the first screen is interpretable without configuration.
- Offer a small set of curated starting views (for common questions) rather than a single empty builder as the only entry point.
- Include an example configuration that users can modify (pre-filled variable assignments and encodings) instead of requiring manual assembly.
- Provide an immediately available alternate representation (such as a summary view) so users can start from content even if they later customize the chart [@elavskyHowAccessibleMy2022].
