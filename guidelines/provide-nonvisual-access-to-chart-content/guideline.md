---
id: provide-nonvisual-access-to-chart-content
title: Provide Complete Non-Visual Access to Chart Content
bibliography: references.bib
description: "Ensure every chart\u2019s information, trends, annotations, and narrative\
  \ can be understood without seeing the visual by exposing equivalent content to\
  \ assistive technologies."
labels:
- chart:any
- task:understand
- visual:any
- impact:accessibility
- data:any
- audience:assistive-technology-users
- disability:blindness-low-vision
- standard:wcag
- source:chartability
---

## The Rule <!-- role: advice -->

Expose all information in the chart without relying on vision: every data value needed to understand the chart, all annotations, all “visually apparent” trends or features, and all major narrative elements must be accessible to screen readers and braille readers; videos, presentations, and animations must include synchronized audio descriptions [@elavskyHowAccessibleMy2022] [@w3c_wcag_quick].

## The Logic <!-- role: reason -->

If information is only encoded visually, assistive technologies can only announce an “image” or incomplete content, preventing non-visual users from accessing the same meaning and function as sighted users; providing text alternatives enables the information to be presented via speech or braille output [@w3c_wcag_quick] and aligns with Chartability’s “Content is only visual” critical heuristic [@elavskyHowAccessibleMy2022].

- **The Principle:** Text alternatives enable equivalent non-visual presentation (speech/braille) of non-text chart content.
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@w3c_wcag_quick] [@youtube_accessible_chart]

## Where to Apply <!-- role: context -->

Use this whenever a chart communicates meaning through marks, layout, styling, or motion that a non-visual user would otherwise miss.

- **User Goal:** Understand the chart’s message and important features (including highlighted insights, trends, and annotations) without seeing it [@elavskyHowAccessibleMy2022].
- **Data Type:** Any (because the failure is modality-dependent, not data-dependent) [@elavskyHowAccessibleMy2022].
- **Audience:** People using screen readers or braille displays (e.g., VoiceOver, NVDA, JAWS) [@elavskyHowAccessibleMy2022] [@apple_voiceover_user] [@nvaccess_home_free] [@freedomscientific_jaws_screen].

## When to Break It <!-- role: exceptions -->

Do not treat “non-visual access” as optional based on medium.

- **Scenario:** The chart is delivered as video, presentation, or animation and you only provide the visuals.
- **Reason:** The rule still applies; these formats must include synchronized audio descriptions to avoid being “only visual” [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional authoring effort to ensure narrative elements, annotations, and trends are represented in non-visual form and validated in multiple AT/browser combinations [@elavskyHowAccessibleMy2022].
- **The Risk:** If you only partially expose content, users may receive an incomplete or misleading understanding even though “something” is announced by AT [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming that providing an image (or a chart embedded as an image) is sufficient because the page is otherwise accessible.
- **Why it fails:** Assistive technologies may only announce “image” or omit the chart’s information, trends, annotations, and narrative because the meaning remains only visual [@elavskyHowAccessibleMy2022] [@w3c_wcag_quick].
- **The Wrong Fix:** Testing with only one screen reader or only one browser/device.
- **Why it fails:** Chartability calls for testing across common AT/platform pairings to confirm the information is truly available non-visually [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart’s meaning depends on what you can see (patterns, trends, callouts, highlighted regions, or narrative framing) but there is no non-visual way to obtain those insights [@elavskyHowAccessibleMy2022].
- **The Test:** Verify non-visual access at minimum by testing with JAWS + Chrome, NVDA + Firefox (Windows), VoiceOver + Safari (Mac), and VoiceOver + Safari (iOS); confirm these can access all chart information, including annotations, trends/features, and major narrative elements [@elavskyHowAccessibleMy2022] [@apple_voiceover_user] [@nvaccess_home_free] [@freedomscientific_jaws_screen].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add text alternatives that convey the chart’s information so it can be presented via screen reader or braille output (including the chart’s major narrative elements and any visually apparent trends/features) [@w3c_wcag_quick] [@elavskyHowAccessibleMy2022].
- **Best Fix:** Implement and validate a fully accessible chart experience where all chart information, annotations, and trends are exposed to assistive technologies and the approach is verified across the minimum AT/browser/device set specified by Chartability; include synchronized audio descriptions for videos, presentations, and animations [@elavskyHowAccessibleMy2022] [@youtube_accessible_chart].
