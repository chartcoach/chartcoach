---
id: provide-nonvisual-access-to-all-chart-information
title: Expose all chart information and narrative meaning to screen readers and braille
  (when the chart is otherwise visual-only)
bibliography: references.bib
description: Ensure every data value, trend, annotation, and narrative element in
  a chart is available without vision via accessible text and assistive-technology
  navigation.
labels:
- chart:any
- task:interpret
- visual:any
- impact:accessibility
- data:any
- audience:blind
- audience:low-vision
- assistive-tech:screen-reader
- assistive-tech:braille
- platform:web
---

## Provide a complete non-visual equivalent of the chart <!-- role: advice -->

Provide all information and meaning in the chart—data, annotations, trends/features that are visually apparent, and narrative elements—so it can be accessed without vision via screen readers and braille. If the chart includes video, presentation, or animation, include synchronized audio descriptions.

## Why “not visual-only” makes the visualization perceivable <!-- role: reason -->

When information is conveyed only through visual encodings, users who rely on non-visual output cannot access the underlying content or the intended narrative structure, so the visualization fails as information rather than just as graphics.

**Mechanism:** Text alternatives and accessible structure allow assistive technologies to present the same informational content through speech or braille, enabling non-visual perception and navigation of chart meaning.

**Evidence:** Non-text content must have text alternatives so that information can be presented through modalities such as screen readers or braille. [@w3c_wcag_quick] A practical accessibility evaluation heuristic for charts is that all chart information, annotations, and visually apparent trends/features must be exposed to screen readers, with demonstrations emphasizing keyboard navigation plus audio description for non-visual understanding. [@elavskyHowAccessibleMy2022; @youtube_accessible_chart]

**Notes:** This guideline evaluates perceivability through assistive technologies, including both screen reader and braille output, rather than relying on visual inspection alone. [@elavskyHowAccessibleMy2022; @nvaccess_home_free; @freedomscientific_jaws_screen; @apple_voiceover_user]

## When to require non-visual access for chart content <!-- role: context -->

- **User Goal:** Understand and use the chart’s information without relying on sight.
- **Task:** Read values, understand trends/outliers, follow the narrative (titles/captions/annotations), and operate any provided chart functionality.
- **Data:** Any dataset where meaning is encoded visually (position, color, size, shape, text labels, annotations, callouts).
- **Chart Setting:** Static or interactive charts, including embedded charts and charts delivered as images, and any video/presentation/animation that communicates chart information.
- **Audience:** People who use screen readers and/or braille displays (including blind and low-vision users).
- **Success Criterion:** All chart information and major meaning can be obtained through screen reader or braille output without referencing the visual rendering. [@elavskyHowAccessibleMy2022]

## When not to follow it <!-- role: exceptions -->

**Break it when:** The “chart” contains no information beyond purely decorative visuals. **Why:** There is no informational content to expose as a non-visual alternative.

## Tradeoffs of exposing full chart content non-visually <!-- role: costs -->

**Sacrifice:** Authoring and testing time increases because you must ensure all chart information and narrative meaning are available to assistive technologies. **Risk:** Poorly structured or overly verbose text alternatives can make non-visual access inefficient even if technically present. **Mitigation:** Validate by testing with representative assistive technologies and navigation patterns rather than relying on assumptions. [@elavskyHowAccessibleMy2022]

## Common ways “text alternatives” still fail <!-- role: mistakes -->

- **Mistake:** Providing only an image with no usable semantics for assistive technologies. **Why it fails:** Users get none of the underlying data, annotations, or trends without vision. [@w3c_wcag_quick]
- **Mistake:** Exposing only a generic label (e.g., “image” or a filename) for the chart. **Why it fails:** The informational content and narrative meaning remain inaccessible non-visually. [@elavskyHowAccessibleMy2022]
- **Mistake:** Leaving out “visually apparent” trends or key narrative callouts from the non-visual experience. **Why it fails:** Users miss the intended interpretation even if some raw data is present. [@elavskyHowAccessibleMy2022; @youtube_accessible_chart]

## Quick checks for “content is only visual” failures <!-- role: check -->

**Failure Sign:** A screen reader announces little more than “image,” or it cannot reach key chart content (values, annotations, trends) through navigation. **Quick Check:** Test the chart using at least one screen reader on your platform and verify that annotations and major narrative elements are discoverable without looking at the chart. **Stronger Test:** Test with JAWS + Chrome, NVDA + Firefox (Windows), VoiceOver + Safari (macOS), and VoiceOver + Safari (iOS) and confirm all chart information is accessible through screen reader output (including braille support where available). [@elavskyHowAccessibleMy2022; @freedomscientific_jaws_screen; @nvaccess_home_free; @apple_voiceover_user]

## Ways to make chart meaning accessible without vision <!-- role: fix -->

- Provide text alternatives that include the chart’s key message plus access to the underlying information needed to understand it non-visually. [@w3c_wcag_quick]
- Ensure annotations, key trends/features, and other major narrative elements are exposed to screen readers as readable content rather than being only visual callouts. [@elavskyHowAccessibleMy2022; @youtube_accessible_chart]
- Test and adjust the non-visual experience using common screen readers across platforms (including braille output support where applicable). [@elavskyHowAccessibleMy2022; @freedomscientific_jaws_screen; @nvaccess_home_free; @apple_voiceover_user]
- Add synchronized audio descriptions for chart information presented via video, presentation, or animation. [@elavskyHowAccessibleMy2022; @youtube_accessible_chart]
