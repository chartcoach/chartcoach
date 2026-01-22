---
id: separate-reference-system-selection-from-data-overlay-design
title: Select a reference system first, then design the data overlay
bibliography: references.bib
description: Treat the base map (reference system) as a distinct choice from how data
  are encoded on top of it.
labels:
- chart:general
- task:design
- visual:position
- impact:clarity
- data:general
- audience:general
- workflow:visualize
---

## Select a reference system first, then design the data overlay <!-- role: advice -->

Choose the visualization’s reference system (such as table grid, x–y axes, geospatial coordinates, or network layout) before mapping data records and attributes into overlay encodings.

## Why separating base and overlay improves design control <!-- role: reason -->

Conflating the base reference system with overlay encodings obscures which aspects of the display convey structure versus measured attributes. Treating the base as a deliberate choice clarifies what the positions mean and what additional channels (size, color, links) should communicate.

**Mechanism:** A stable reference system establishes spatial semantics (how location is interpreted), while overlays encode additional variables; separating them reduces accidental meaning and supports consistent iteration across visualization types.

**Evidence:** Visualization construction is split into picking a reference system (base map) and designing a data overlay by mapping records and variables to graphic symbols and variables, and the framework illustrates common reference systems across tables, graphs, maps, and networks [@bornerDataVisualizationLiteracy2019].

**Notes:** Some positions may come from lookup tables or layout algorithms, but they still function as the reference system for interpretation.

## When to apply base-plus-overlay thinking <!-- role: context -->

- **User Goal:** Make positional meaning unambiguous and overlays interpretable.
- **Task:** Construct or critique a visualization’s structure and encoding.
- **Data:** Any dataset where multiple encodings are possible; especially multivariate overlays.
- **Chart Setting:** Static or interactive; single or multiple coordinated views.
- **Audience:** Readers who must understand what position means versus what color/size means.
- **Success Criterion:** Readers can correctly explain what the coordinate system represents and what each overlay channel encodes.

## When base-plus-overlay separation can be relaxed <!-- role: exceptions -->

**Break it when:** The visualization is effectively only the reference system with no meaningful overlay beyond presence/absence of marks. **Why:** In that case, the base system alone carries most semantics.

## Tradeoffs of explicitly separating base and overlay <!-- role: costs -->

**Sacrifice:** Additional conceptual overhead when teaching or documenting simple charts. **Risk:** Designers may overformalize and ignore that some systems integrate base and overlay tightly. **Mitigation:** Keep the separation as a mental model and document only the parts that affect interpretation.

## Typical failures from mixing base and overlay decisions <!-- role: mistakes -->

**Mistake:** Changing overlay encodings to fix an issue that is actually caused by an inappropriate reference system. **Why it fails:** Overlay changes cannot correct a base system that does not support the intended insight need.

## Quick tests for base/overlay clarity <!-- role: check -->

**Failure Sign:** Viewers cannot state what the axes/coordinates/layout represent without guessing. **Quick Check:** Ask “What determines position?” and “What determines color/size/links?” and verify the answers are distinct. **Stronger Test:** Remove overlay channels mentally and see whether the remaining reference system still has a clear interpretation.

## What to do when position meaning is unclear <!-- role: fix -->

- Re-select a reference system whose spatial semantics match the insight need.
- Add explicit legends or captions that define what positions represent, especially for algorithmic layouts.
- Simplify overlays so the base system can be learned first, then reintroduce additional channels.
- Create separate views for competing base semantics rather than forcing one view to serve multiple incompatible meanings.
