---
id: avoid-3d-when-navigation-is-required-but-interaction-is-not-guaranteed
title: Avoid 3D when navigation is required but interaction is not guaranteed
bibliography: references.bib
description: Do not rely on 3D if the visualization becomes comprehensible only through
  rotation/zooming in contexts where viewers may see a static image.
labels:
- chart:3d
- task:interpret
- visual:interaction
- impact:reliability
- data:any
- audience:any
- custom:static-context
---

## Design 3D so the default view is readable without navigation <!-- role: advice -->

Do not choose a 3D design that requires rotation or other navigation to understand the data when the visualization may be consumed as a static image or in settings with limited shared control.

## Why navigation-dependent 3D fails in common real viewing conditions <!-- role: reason -->

If comprehension depends on interaction, then any situation that removes interaction turns the visualization into an ambiguous picture; even with interaction, complex mode switching for rotate/pan/zoom/selection can increase usability burden.

**Mechanism:** Navigation becomes a single point of failure: without it, depth relationships and occluded items cannot be resolved; with it, users must manage multiple interaction intents that are simpler in 2D.

**Evidence:** Navigation is a critical failure mode when a 3D configuration requires interaction but the situation is static (published images, slides, collaborative contexts), and mouse-based 3D navigation can be problematic due to competing drag interactions and modes [@brath3DInfoVisHere2014].

**Notes:** The risk is about dependence on navigation, not the mere presence of 3D.

## When this constraint applies <!-- role: context -->

- **User Goal:** Correctly interpret a chart in a presentation, report, or shared setting.
- **Task:** Read values/relationships without manipulating the view.
- **Data:** Any, especially where occlusion or depth ambiguity is likely.
- **Chart Setting:** Static exports, screenshots, print, slides, or group viewing with one controller.
- **Audience:** Mixed audiences, including viewers who will not interact.
- **Success Criterion:** The visualization remains understandable in a single captured frame.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is strictly interactive and interaction is guaranteed for all viewers. **Why:** Navigation can then be part of the analytic workflow rather than a liability [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some 3D benefits (spatial separation, immersive exploration) may be unavailable in static form. **Risk:** Over-simplifying to avoid navigation can remove useful structure. **Mitigation:** Use a 3D+2D linked design where the default 3D view is explanatory and 2D views provide precision.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Shipping a 3D scatterplot that only makes sense after rotating. **Why it fails:** Static contexts cannot resolve depth and occlusion [@brath3DInfoVisHere2014].
- **Mistake:** Using the same drag gesture for rotate and selection without a clear model. **Why it fails:** Users struggle with modes and lose control compared to 2D interactions [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** A screenshot of the default view is confusing or ambiguous. **Quick Check:** Export a static image and ask a viewer to explain the main takeaway without interacting. **Stronger Test:** Run a small study where one group gets only a static image and compare comprehension to the interactive version.

## What to do instead <!-- role: fix -->

- Use a 2D visualization when static comprehension is a primary requirement.
- Provide a default 3D viewpoint with strong depth cues and minimal occlusion so a static frame is interpretable.
- Add coordinated 2D views that convey the key comparisons without navigation.
- Use small multiples to separate views instead of requiring rotation to disambiguate overlap.
