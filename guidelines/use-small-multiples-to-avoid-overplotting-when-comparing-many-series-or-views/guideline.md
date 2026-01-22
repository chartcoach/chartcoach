---
id: use-small-multiples-to-avoid-overplotting-when-comparing-many-series-or-views
title: Use small multiples to avoid overplotting when comparing many series or views
bibliography: references.bib
description: Repeat the same chart design in separate panels to compare many items
  without overlapping marks.
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:legibility
- data:temporal
- audience:general
- complexity:foundational
---

## Separate series into repeated panels when overlays become cluttered <!-- role: advice -->

Use small multiples by giving each series its own repeated chart when plotting many series together would create overlap and reduce legibility.

## Repetition preserves comparability without collisions <!-- role: reason -->

Overlaid lines compete for attention and can hide each other; small multiples keep a consistent design while preventing occlusion.

**Mechanism:** Separating items into aligned panels reduces visual interference while maintaining consistent scales and encodings across views.

**Evidence:** Plotting many series in one set of axes can produce overlapping curves that reduce legibility, and small multiples provide an alternative by showing each series in its own chart; small multiples can be constructed for many visualization types beyond time series [@heerTourVisualizationZoo2010].

**Notes:** Small multiples can also support normalization within each panel when relative patterns matter.

## Context: Many comparable items <!-- role: context -->

- **User Goal:** Compare patterns across many categories/items.
- **Task:** Spot trends, seasonality, outliers per item while retaining comparability.
- **Data:** Multiple series (time series or repeated subsets) with moderate-to-large count.
- **Chart Setting:** Grid or list layout; static or interactive.
- **Audience:** General audiences who need quick scanning without decoding overlaps.
- **Success Criterion:** Each item remains readable and comparable across panels.

## Exceptions: When panel space is unavailable <!-- role: exceptions -->

**Break it when:** The display area is too constrained to keep each panel interpretable. **Why:** Small multiples can shrink charts to the point where patterns are no longer resolvable [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Small multiples consume more space than a single combined plot. **Risk:** If panels are too small, viewers may miss fine variation. **Mitigation:** Limit the number of panels shown at once or enable scrolling/filtering.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Forcing all series into a single plot even after overlaps obscure patterns. **Why it fails:** Overlapping marks reduce legibility and impair comparison [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Lines or marks frequently overlap such that individual series cannot be traced. **Quick Check:** Ask a viewer to follow one series end-to-end; if they lose it, switch to small multiples. **Stronger Test:** Compare error rates on “which series peaks earlier?” using overlay versus small multiples.

## Fix: What to do instead <!-- role: fix -->

- Split the view into small multiples with consistent scales and encodings.
- Normalize within each panel when relative pattern comparison is the goal.
- Add filtering to show only a subset of panels at a time.
- Use a denser time-series technique (such as a horizon graph) when many tiny panels are required.
