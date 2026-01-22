---
id: minimize-tedious-navigation-and-interaction-across-input-modalities
title: Minimize interaction steps and make repeated content skippable across input
  modalities
bibliography: references.bib
description: Prevent accessibility time/effort gaps by making repeated blocks skippable
  and ensuring tasks are not substantially more laborious with keyboard or assistive
  technologies than with a mouse.
labels:
- chart:any
- task:navigate
- visual:any
- impact:accessibility
- data:any
- audience:all
- interaction:keyboard
- assistive:screen-reader
- complexity:high
---

## Reduce labor by skipping repetition and limiting interaction steps <!-- role: advice -->

Make repeated blocks of content skippable and ensure no task requires substantially more interaction steps or time with a keyboard or assistive technology than with a mouse. Treat labor-intensive interaction paths as non-essential unless an equally efficient alternative is provided.

## Why interaction labor becomes an accessibility barrier <!-- role: reason -->

When navigation and interaction require long, repetitive sequences, users who rely on sequential input (such as keyboard navigation used by many assistive technologies) pay a disproportionate time and effort cost to reach the same information or functionality, creating an access gap based on input modality rather than user intent.

**Mechanism:** Skipping repeated blocks and reducing step counts lowers the cumulative effort imposed by sequential navigation and prevents efficiency disparities across modalities.

**Evidence:** Providing mechanisms to bypass repeated blocks (for example, skip links or structural navigation landmarks) reduces repetitive navigation burden for keyboard and screen reader users [@w3c_understanding_bypass]. Measuring and comparing interaction labor across modalities is a critical accessibility heuristic for data experiences where unequal time-on-task becomes an access barrier [@elavskyHowAccessibleMy2022].

**Notes:** Interaction labor is commonly treated as a usability cost, but becomes an accessibility cost when it systematically differs by modality and increases cognitive load over long sequences [@elavskyHowAccessibleMy2022].

## When to evaluate for tedious navigation and interaction <!-- role: context -->

- **User Goal:** Reach key chart content quickly and complete a chart-related task without disproportionate time/effort.
- **Task:** Navigate, explore, filter, select, drill down, or otherwise operate chart functionality.
- **Data:** Any, especially when the interface exposes many elements or repeated regions that can be traversed sequentially.
- **Chart Setting:** Interactive charts, dashboards, or data interfaces with repeated headers/controls, long menus, dense mark sets, or multi-step interactions.
- **Audience:** People using keyboard-only interaction, screen readers, alternative input devices, or voice workflows; also users with higher cognitive load sensitivity.
- **Success Criterion:** Comparable time and interaction count to complete the same task across mouse, sequential keyboard navigation, search, voice, and other supported modalities.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The experience has no repeated blocks and no interactive tasks (for example, a simple static figure with no navigation regions). **Why:** There is no modality-dependent navigation or interaction path to bypass or equalize.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional design and engineering effort to add bypass mechanisms or alternative navigation paths. **Risk:** Over-optimizing for fewer steps can hide detail or reduce discoverability for some users. **Mitigation:** Keep both efficient and explicit paths available so users can choose their preferred navigation strategy.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Shipping a data interface where keyboard or screen reader users must traverse long repeated menus, headers, or controls before reaching chart content. **Why it fails:** It forces unnecessary sequential labor that bypass mechanisms are intended to eliminate [@w3c_understanding_bypass].

## Quick tests <!-- role: check -->

**Failure Sign:** Reaching chart content or completing a common task requires many sequential focus moves or repeated traversal of the same blocks.\
**Quick Check:** Attempt the primary task using only the keyboard and note whether you must repeatedly tab through the same regions to reach chart content.\
**Stronger Test:** Measure steps or time to complete the same task using mouse versus sequential keyboard navigation (and other supported modalities) and flag large disparities as accessibility failures [@elavskyHowAccessibleMy2022].

## What to do instead <!-- role: fix -->

- Provide a mechanism to bypass repeated blocks so users can jump directly to the main chart content or primary interactive region [@w3c_understanding_bypass].
- Ensure that any essential interaction can be completed without long sequential traversal by offering a more direct modality-compatible path to the same function.
- Measure interaction steps or time for the same task across supported modalities and remediate workflows that impose substantially higher labor on keyboard or assistive-technology users [@elavskyHowAccessibleMy2022].
- Remove or demote non-essential interactive steps so core tasks do not depend on tedious navigation sequences [@elavskyHowAccessibleMy2022].
