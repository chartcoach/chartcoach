---
id: respect-user-style-and-preference-overrides-in-data-visualizations
title: Respect user-applied styles and preferences in charts (do not override them)
bibliography: references.bib
description: Ensure charts do not block or undo user styling and preference changes
  from browsers, operating systems, or assistive technologies.
labels:
- chart:interactive
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:all
- principle:flexible
- standard:wcag
---

## Respect user styles and preference overrides <!-- role: advice -->

Do not prevent, override, or negate styling changes made by the user or user agent when viewing a chart (for example custom style sheets or user-controlled presentation settings). Ensure the chart remains readable and operable after those user style changes are applied.

## Why respecting user styles keeps charts accessible <!-- role: reason -->

Respecting user and user-agent presentation settings preserves user agency to adapt content to their access needs while keeping the experience robust across different environments and assistive technology configurations. When a visualization overrides these changes, it can remove the user’s chosen readability and operability adaptations, making the chart effectively inaccessible even if its default styling appears acceptable.

**Mechanism:** Users rely on browser, operating system, and assistive-technology settings (including user styles) to adjust perceptual and interaction requirements; overriding those settings breaks the user’s adaptation pathway and can reintroduce barriers.

**Evidence:** Visualization accessibility auditing frameworks treat failure to respect user style changes as a critical issue under a “Flexible” principle that emphasizes robustness and respecting user-agent settings [@elavskyHowAccessibleMy2022]. This requirement is grounded in web accessibility success criteria covering text resizing, reflow, text spacing, time limits, flashing/animation risk, and related operability constraints that depend on honoring user-controlled settings [@Ini].

**Notes:** This guideline targets styling and preference overrides, not merely choosing a good default theme.

## When to apply this in visualization work <!-- role: context -->

- **User Goal:** Adjust presentation or interaction to make the chart readable/usable with their preferred settings.
- **Task:** Read labels/annotations, navigate interactive elements, and interpret encodings without losing access after preference changes.
- **Data:** Any data type; risk increases when the chart relies on precise layout, dense labels, or small text.
- **Chart Setting:** Web-embedded or application-embedded charts where users can apply custom styles or system/browser preferences (including accessibility modes).
- **Audience:** People using accessibility features, assistive technologies, or personal style overrides; also users with situational constraints who adjust settings.
- **Success Criterion:** The same information and functionality remain perceivable and operable after user style changes are applied.

## When not to follow it <!-- role: exceptions -->

**Break it when:** A user-applied style change would remove or obscure essential information or controls in a way that cannot be made robust for the chart. **Why:** The visualization cannot simultaneously preserve the user override and maintain a usable representation without a different representation or fallback path [@elavskyHowAccessibleMy2022].

## Tradeoffs of respecting user style changes <!-- role: costs -->

**Sacrifice:** Some tightly controlled visual aesthetics and pixel-perfect layouts may be harder to guarantee across environments. **Risk:** The chart may look inconsistent across users or platforms. **Mitigation:** Treat the chart as a resilient interface: prioritize readability, navigation, and information access under user-controlled presentation changes [@elavskyHowAccessibleMy2022].

## Common ways teams fail this guideline <!-- role: mistakes -->

- **Mistake:** Hard-coding chart styles so user styles (including custom style sheets) cannot affect text size, spacing, or contrast. **Why it fails:** It blocks user adaptations that are required to make content perceivable and operable in their environment [@elavskyHowAccessibleMy2022; @Ini].
- **Mistake:** Resetting or overriding user-agent defaults (for example forcing fixed text sizes or fixed layout dimensions). **Why it fails:** It can prevent reflow/resizing and negate user readability settings that the user depends on [@elavskyHowAccessibleMy2022; @Ini].

## Quick checks to detect style-override failures <!-- role: check -->

**Failure Sign:** The chart becomes unreadable or unusable when user styling or user-agent presentation settings are changed. **Quick Check:** Apply a user style change (such as a custom style sheet) and verify the chart’s text, layout, and controls still work and still convey the same information. **Stronger Test:** Audit against the relevant web accessibility success criteria connected to user-controlled presentation and interaction constraints, and confirm the chart does not interfere with those adaptations [@elavskyHowAccessibleMy2022; @Ini].

## Practical fixes when user styles are not respected <!-- role: fix -->

- Ensure chart text and layout can adapt when users apply style overrides, rather than forcing fixed sizes and spacing.
- Avoid styling approaches that block user-agent or user style changes from taking effect on chart content and controls.
- Provide an alternative representation that remains accessible under user-controlled presentation changes when the primary chart cannot remain robust.
- Verify interactive affordances and feedback remain operable after user style changes are applied, not only in the default theme.
