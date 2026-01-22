---
id: avoid-fragile-technology-support-for-chart-access
title: Provide chart access across browsers, devices, operating systems, and concurrent
  input mechanisms
bibliography: references.bib
description: "Ensure the chart\u2019s information and functionality are not locked\
  \ to a single platform or input method by supporting multiple environments and interchangeable\
  \ input mechanisms."
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- a11y:robust
---

## Provide cross-platform and concurrent-input access for the same chart experience <!-- role: advice -->

Make the chart’s information and functionality usable across browsers, devices, operating systems, and assistive technologies without requiring a specific platform or exclusive input method. Ensure users can switch among available input mechanisms (for example, keyboard, mouse, and touch) without losing access.

## Robust access requires interoperable, non-fragile interaction pathways <!-- role: reason -->

When chart access depends on a single browser, device, operating system, software stack, or exclusive gesture, users who rely on different assistive technology setups or input modalities can be blocked from perceiving or operating the same content. Supporting diverse technology environments and concurrent input mechanisms reduces brittleness and increases the likelihood that compliant assistive technologies can interoperate with the chart.

**Mechanism:** Multiple compatible access pathways prevent a single technical dependency from becoming a hard barrier to perceiving or operating chart content, especially when users need to change or mix input mechanisms during interaction.

**Evidence:** Content should not restrict users from switching between concurrent input mechanisms (such as keyboard, mouse, touch, or other inputs), because prohibiting specific inputs or requiring certain gestures can exclude users who rely on different devices or assistive technologies [@w3c_understanding_concurrent]. Chart accessibility should not be isolated to one browser, device, software, or operating system, and should support diverse technological means of access to chart information and functionality [@elavskyHowAccessibleMy2022].

**Notes:** This guideline targets robustness of access rather than any single encoding choice, so it applies to both the chart’s interactive controls and any non-visual access pathways that expose the same information and functionality.

## Situations where fragile technology support becomes an accessibility barrier <!-- role: context -->

- **User Goal:** Access the chart’s information and use its available functionality regardless of platform or input device.
- **Task:** Operate interactions (such as focus, selection, filtering, navigation) and retrieve the same information outcomes.
- **Data:** Any dataset where the chart is the primary interface for understanding or interacting with information.
- **Chart Setting:** Web or app-based charts that include interaction or controls and may be used with assistive technologies.
- **Audience:** Users with diverse assistive technology configurations and users who need to switch input mechanisms.
- **Success Criterion:** The same chart information and functionality remains available when the user changes browser/device/OS or switches input mechanisms.

## When not to enforce cross-environment interaction parity <!-- role: exceptions -->

**Break it when:** The chart is delivered in a fixed, non-interactive medium where no input mechanisms exist to support or restrict. **Why:** The constraint is the publication format itself, not a fragile restriction introduced by the chart’s interaction design.

## Tradeoffs of supporting diverse environments and inputs <!-- role: costs -->

**Sacrifice:** More implementation and testing effort across platforms and input modes. **Risk:** Inconsistent behavior can emerge if different interaction pathways diverge in what they expose. **Mitigation:** Define a single set of required chart capabilities and verify they remain available under different input mechanisms and environments.

## Common ways teams accidentally lock charts to one technology or input <!-- role: mistakes -->

- **Mistake:** Implementing interactions that require a specific gesture or pointer-only actions. **Why it fails:** Users who rely on other input mechanisms may be unable to operate the chart or complete the same tasks [@w3c_understanding_concurrent].
- **Mistake:** Building chart access that only works reliably in one browser, OS, or device class. **Why it fails:** The chart becomes brittle and can exclude users whose assistive technologies or workflows depend on other compliant environments [@elavskyHowAccessibleMy2022].

## Fast signals that the chart is technology-fragile <!-- role: check -->

**Failure Sign:** The chart works only on one platform or becomes unusable when switching input methods (for example, touch works but keyboard cannot operate the same controls). **Quick Check:** Try to complete the same chart interaction using at least two different input mechanisms without changing the task goal. **Stronger Test:** Verify the chart remains usable when changing major environments (browser/device/OS) and while switching among available input mechanisms during the same session [@w3c_understanding_concurrent].

## Ways to reduce platform and input fragility in chart access <!-- role: fix -->

- Implement chart interaction so users can operate the same functionality through different input mechanisms without requiring exclusive gestures [@w3c_understanding_concurrent].
- Ensure the chart’s information and functionality can be accessed through multiple technological environments rather than only one browser, device, software, or operating system [@elavskyHowAccessibleMy2022].
- Provide an alternative technological means to access the chart’s information and functionality when a specific environment cannot support the primary interaction channel [@elavskyHowAccessibleMy2022].
- Test and document supported environments and input mechanisms so failures can be detected and remediated before deployment [@elavskyHowAccessibleMy2022].
