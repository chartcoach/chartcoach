---
id: avoid-tedious-navigation-and-interaction
title: Provide Bypass Mechanisms for Repetitive and Tedious Interaction
bibliography: references.bib
description: Ensure repeated blocks can be skipped and that tasks do not require substantially
  more steps or time for keyboard and assistive-technology users.
labels:
- chart:interactive
- task:navigate
- visual:structure
- impact:accessibility
- data:any
- audience:all
- principle:assistive
- heuristic:navigation-tedium
- source:chartability
---

## The Rule <!-- role: advice -->

Provide a way to skip large repeated blocks (e.g., repeated navigation or controls) and ensure core tasks do not require significantly more interactions or time when performed via different modalities (mouse, sequential keyboard, screen reader patterns, voice, search).

## The Logic <!-- role: reason -->

Reducing repeated navigation and excessive step counts lowers the functional and cognitive labor required to reach and use content, preventing an “access gap” where users of assistive technologies must spend disproportionately more time and effort to accomplish the same task. This is framed as an accessibility requirement in Chartability’s Assistive principle and connected to bypassing repeated blocks of content as required by WCAG understanding guidance.

- **The Principle:** Labor-equitable interaction (avoid time/interaction “access gaps”)
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@w3c_understanding_bypass]

## Where to Apply <!-- role: context -->

This advice is designed for interfaces where users must move through repeated structures to reach data or controls.

- **User Goal:** Reaching chart content and completing a task without excessive navigation (e.g., operating filters, exploring marks, moving between views).
- **Data Type:** Any (the issue is interaction structure and repetition, not a specific data shape).
- **Audience:** People navigating via keyboard or assistive technologies, and anyone affected by increased cognitive load from long, repetitive interaction paths [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** There are no large repeated blocks and no multi-step interactions (e.g., a simple view where nothing repeats across the experience).
- **Reason:** If there is nothing repetitive to bypass and no task requiring significant interaction labor, the bypass requirement is not applicable [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Added interface elements or structure to support skipping repeated blocks.
- **The Risk:** Poorly integrated bypass mechanisms can complicate the interface if not aligned with how users move through content [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Leaving long repeated navigation/controls in front of the main chart content with no way to skip it.
- **Why it fails:** Users who navigate sequentially must traverse the same blocks every time, making routine tasks disproportionately slow and labor-intensive [@w3c_understanding_bypass] [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Treating a labor-intensive interaction path as “essential” simply because it exists in the design.
- **Why it fails:** Chartability notes that interactions requiring significant labor must not be considered essential in content or function when they create modality-based access gaps [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must pass through the same repeated menus/controls to reach the chart or must step through many interactive items for a single task.
- **The Test:** Compare how many interactions or how much time it takes to complete one task using different modalities (e.g., mouse pointer vs. sequential keyboard navigation vs. search/voice). If one modality requires substantially more effort solely due to navigation/interaction design, the rule is broken [@elavskyHowAccessibleMy2022]. Also verify that repeated blocks can be bypassed as described in WCAG guidance [@w3c_understanding_bypass].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a mechanism that allows users to bypass repeated blocks so they can jump directly to main chart content and key controls [@w3c_understanding_bypass].
- **Best Fix:** Redesign interaction and navigation so that completing key tasks does not require significant extra steps or time for sequential keyboard and assistive-technology use, and measure parity across modalities as part of the accessibility audit process [@elavskyHowAccessibleMy2022].
