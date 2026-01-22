---
id: use-interaction-defaults-and-menu-order-as-anchoring-framing-devices
title: Set default views, fixed comparisons, and menu order intentionally because
  they anchor interpretation
bibliography: references.bib
description: Treat defaults and navigation structure as rhetorical anchors that prioritize
  certain readings.
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:framing
- data:multivariate
- audience:general
- custom:rhetoric-procedural
---

## Treat defaults and navigation as interpretive anchors <!-- role: advice -->

Choose default views, fixed comparisons, and menu ordering as if they will be the primary story most viewers take away.

## Why interaction structure frames what people conclude <!-- role: reason -->

Interactive narrative visualizations use procedural constraints—what is shown first, what is easy to compare, and what paths are suggested—to steer attention and exploration. Because many users do not exhaustively explore, early anchors and curated paths disproportionately shape interpretation.

**Mechanism:** Anchoring through defaults and guided comparisons limits the explored hypothesis space over time and makes particular patterns feel more salient or “intended.”

**Evidence:** The paper identifies “procedural rhetoric” techniques such as default views, fixed comparisons, spatial ordering, partial animation, goal suggestions, and search/menu constraints as ways interaction rules prioritize interpretations [@hullmanVisualizationRhetoricFraming2011a]. The case discussion of an interactive census map illustrates how a default view and menu ordering can privilege certain variables (for example, race/ethnicity first) relative to other available views [@hullmanVisualizationRhetoricFraming2011a].

**Notes:** These effects can be positive (helping users find meaningful views) or distortive (over-weighting a curated slice).

## When anchoring effects matter most <!-- role: context -->

- **User Goal:** Learn “the story” quickly and decide what it implies.
- **Task:** Browse, compare, and form impressions with limited time.
- **Data:** Many possible slices, metrics, or subgroup views.
- **Chart Setting:** Interactive narrative pieces with menus, search, steps, or guided sequences.
- **Audience:** Casual viewers likely to stop after the first few interactions.
- **Success Criterion:** The initial experience aligns with the intended scope and does not unintentionally over-privilege a single dimension.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The goal is open-ended exploratory analysis for trained users who will configure views deliberately. **Why:** Strong anchoring can reduce analytical freedom and bias exploration.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some openness and user autonomy. **Risk:** Viewers may mistake the default as “most important” or “most true.” **Mitigation:** Make alternative views discoverable and label what the default represents.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Treating the default view as a purely technical starting point. **Why it fails:** Defaults are interpretive anchors that many users never leave.
- **Mistake:** Burying alternative views behind extra clicks without signaling their existence. **Why it fails:** The interaction design becomes an omission device that narrows interpretations.

## Quick tests <!-- role: check -->

**Failure Sign:** Most users’ summaries match only the first view or the first menu item.\
**Quick Check:** Ask what conclusion a viewer would draw if they saw only the landing state.\
**Stronger Test:** Swap default view/menu order and check whether the dominant takeaway changes.

## What to do instead <!-- role: fix -->

- Choose a default view that reflects the most defensible high-level framing of the data.
- Provide clear entry points to alternative views if multiple interpretations are plausible.
- Use fixed comparisons only when you are comfortable privileging those baselines.
- Add lightweight goal suggestions that broaden exploration rather than narrowing it to a single slice.
