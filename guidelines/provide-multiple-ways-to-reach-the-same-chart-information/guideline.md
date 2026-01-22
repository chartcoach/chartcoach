---
id: provide-multiple-ways-to-reach-the-same-chart-information
title: Provide at least two ways to reach the same chart information when access depends
  on multi-step UI flows
bibliography: references.bib
description: Ensure the same chart state or information can be reached through more
  than one navigation or interaction process.
labels:
- chart:dashboard
- task:navigate
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- a11y:compromising
- complexity:advanced
---

## Provide multiple paths to the same chart state <!-- role: advice -->

Provide more than one process to reach the same chart information or interactive state when access depends on multi-step interface flows. Ensure an alternative path exists alongside the primary flow (for example, a parallel control or a search-based path).

## Why multiple ways reduce access barriers in complex analysis flows <!-- role: reason -->

Requiring a single process to reach information concentrates failure risk: if a user cannot perform one step (or cannot discover it), they cannot reach the information at all. Providing multiple routes makes the information flow more tolerant to different interaction preferences and assistive-technology workflows, and reduces reliance on remembering or discovering one “correct” path.

**Mechanism:** Multiple routes provide redundancy in information architecture, so users can choose a path that matches their input method and navigation strategy rather than being blocked by one fragile sequence.

**Evidence:** Providing at least two ways to locate content (such as navigation and search) reduces navigation burden and supports users with disabilities in finding information more easily, including reducing reliance on memory [@w3c_understanding_multiple_2]. This principle is applied to visualization accessibility auditing as a Compromising heuristic to ensure transparent, tolerant information flows in complex data interfaces [@elavskyHowAccessibleMy2022].

**Notes:** “Same information” includes reaching the same filtered view, selected state, drill-down view, page, or analysis result, not just the same page URL.

## When charts participate in multi-step or stateful UI navigation <!-- role: context -->

- **User Goal:** Reach a specific chart insight, view, filtered subset, or drill-down state.
- **Task:** Navigate, locate, and return to previously seen chart states; compare states across filters or pages.
- **Data:** Any data type; commonly high-cardinality or multi-dimensional dashboards where filtering and state changes are central.
- **Chart Setting:** Dashboards or analytic applications with transitions between views/states, filter chains, paging, or stepwise interaction flows.
- **Audience:** Mixed audiences, including users of assistive technologies and users who prefer different navigation strategies.
- **Success Criterion:** The user can reliably reach the same chart information even if one navigation method is unusable, undiscoverable, or inefficient.

## When a single path is inherent to the experience <!-- role: exceptions -->

**Break it when:** The experience is intentionally linear and the chart information cannot meaningfully be reached outside that single sequence. **Why:** Multiple routes would not lead to the same state or would fundamentally change what “the same information” means.

## Tradeoffs of adding alternative routes <!-- role: costs -->

**Sacrifice:** Additional design and engineering effort to maintain parallel paths to the same state. **Risk:** Inconsistent states across routes can confuse users if routes drift or produce different results. **Mitigation:** Keep routes functionally equivalent and verify they arrive at the same chart state and information.

## Common ways teams accidentally keep a single fragile path <!-- role: mistakes -->

- **Mistake:** Hiding a key state only behind a sequence of filter interactions or view transitions. **Why it fails:** Users who cannot complete or discover one step lose access to the information entirely.
- **Mistake:** Providing an alternative path that lands “near” the target but cannot reproduce the same state (for example, a different filter logic). **Why it fails:** The user still cannot reach the same information.

## Quick checks for single-process access traps <!-- role: check -->

**Failure Sign:** A chart view or state can only be reached by completing a specific multi-step interaction chain (filters → drilldown → page change) with no alternative route. **Quick Check:** Try to reach the same chart state using a different navigation method than the intended one; if you cannot, the experience is single-process. **Stronger Test:** Ask an auditor to locate a target chart state using two distinct strategies; if one strategy fails, add an alternative path.

## Ways to add a second route to the same information <!-- role: fix -->

- Add a parallel control that can reach the same chart state without requiring the primary multi-step flow.
- Provide a search-based way to locate the target chart view or state when the interface contains multiple pages, views, or deep navigation.
- Create a secondary navigation structure that can reach the same destinations as the primary structure (for example, complementary navigation patterns).
- Ensure the alternative route produces the same state and information as the primary route, not an approximation.
