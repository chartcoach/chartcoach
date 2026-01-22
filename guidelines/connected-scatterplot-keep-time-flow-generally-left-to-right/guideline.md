---
id: connected-scatterplot-keep-time-flow-generally-left-to-right
title: Arrange axes so connected-scatterplot time flow is generally left-to-right
bibliography: references.bib
description: Reduce directional confusion by choosing axis assignments that make the
  connected path progress mostly left-to-right over time.
labels:
- chart:scatter
- task:interpret
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- custom:connected-scatterplot
---

## Prefer a left-to-right temporal drift in a connected scatterplot <!-- role: advice -->

Choose which series goes on which axis (and their polarities) so the connected path tends to move left-to-right as time advances. Avoid designs where large sections require reading time right-to-left.

## Left-to-right sequence expectations can clash with connected-scatterplot paths <!-- role: reason -->

A connected scatterplot encodes time as traversal along a line rather than along a dedicated axis, so viewers must reconcile sequence with spatial movement. When the path runs right-to-left, viewers can interpret it as reverse chronology or become uncertain about how to read the chart.

**Mechanism:** Aligning temporal progression with common left-to-right scanning reduces cognitive friction in mapping “earlier” to “later.”

**Evidence:** In qualitative responses, viewers called out right-to-left time progression as surprising and interpreted it as reverse chronology; viewers also reversed time order in connected-scatterplot tasks, especially when translating between formats [@harozConnectedScatterplotPresenting2016].

**Notes:** This guideline is about the global drift being left-to-right, not about forcing monotonic movement.

## Situations where left-to-right drift helps most <!-- role: context -->

- **User Goal:** Read the chart quickly and accurately without instruction.
- **Task:** Identify phases or compare early vs late periods.
- **Data:** Paired time series where axis assignment can change the path’s global direction.
- **Chart Setting:** Static journalism-style graphics, slide decks, or any context with skimming.
- **Audience:** General audiences with low familiarity with connected scatterplots.
- **Success Criterion:** Readers do not describe the chart as “reverse chronological” or hesitate about reading order.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary message requires a particular axis assignment (for example, matching a conventional “cause on horizontal, effect on vertical” framing) that would be compromised by swapping axes. **Why:** Preserving semantic conventions may outweigh left-to-right drift.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Freedom to assign variables to axes purely by semantic preference. **Risk:** Forcing a left-to-right drift can yield less intuitive axis meanings for the intended story. **Mitigation:** Use explicit labeling and annotations to reinforce the chosen mapping.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Leaving axis assignment arbitrary, resulting in long right-to-left segments. **Why it fails:** Viewers explicitly reported confusion and reverse-chronology interpretations for such paths [@harozConnectedScatterplotPresenting2016].

## Quick tests for left-to-right readability <!-- role: check -->

**Failure Sign:** Multiple viewers describe time as going “backwards” or ask how to read direction. **Quick Check:** Trace the line from start to end and confirm the path’s overall drift is left-to-right. **Stronger Test:** Ask naive readers to narrate the trend; flag any reverse-time narratives.

## What to do instead <!-- role: fix -->

- Swap which variable is on the horizontal vs vertical axis to improve left-to-right drift.
- Reverse the polarity of an axis if it improves left-to-right progression while keeping labels clear.
- If the story needs extensive right-to-left reading, use a dual-axis line chart with time on the horizontal axis.
