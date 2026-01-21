---
id: support-zoom-and-reflow
title: Support Zoom and Reflow Without Losing Information
bibliography: references.bib
description: Ensure charts can be zoomed and will reflow without cutting off content
  or requiring two-direction scrolling.
labels:
- chart:general
- task:read
- visual:layout
- impact:accessibility
- data:any
- audience:all
- principle:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Make the chart zoomable with assistive technology (or an equivalent control) and ensure that, when zoomed, all text, geometries, and interactive elements resize appropriately and reflow so no information or functionality is lost or cut off in two directions [@elavskyHowAccessibleMy2022] [@w3c_understanding_reflow].

## The Logic <!-- role: reason -->

Zoom changes the effective viewport and text/element sizing; if the chart does not reflow, users can lose access to content or controls and be forced into two-direction navigation, undermining operability and perceivability in real use [@elavskyHowAccessibleMy2022]. WCAG’s reflow requirement formalizes this by requiring content to be presented without loss of information or functionality when zoomed or constrained to a narrow viewport [@w3c_understanding_reflow].

- **The Principle:** Respect user-agent zoom and reflow so access methods can scale content without breaking layout or interaction [@elavskyHowAccessibleMy2022].
- **The Evidence:** [@w3c_understanding_reflow]

## Where to Apply <!-- role: context -->

This advice is designed for charts embedded in interfaces where users may rely on browser/OS/app zoom or narrow viewports.

- **User Goal:** Read labels, values, and operate chart controls while zoomed or on a narrow viewport [@elavskyHowAccessibleMy2022].
- **Data Type:** Any chart with text, marks (geometries), and/or interactive controls that could be clipped or become unreachable after zoom [@elavskyHowAccessibleMy2022].
- **Audience:** People who need magnification or enlarged UI, and anyone viewing on small screens or using narrow windows [@w3c_understanding_reflow].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart has no meaningful information or functionality to preserve at zoomed/narrow sizes (e.g., purely decorative content).
- **Reason:** The reflow requirement targets preserving information and functionality; if none exists, the constraint is not applicable as described [@w3c_understanding_reflow].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to rearrange the chart’s layout at different sizes (e.g., repositioning components) to preserve access during reflow [@elavskyHowAccessibleMy2022].
- **The Risk:** Re-arrangement can change the presentation order or spatial relationships and requires additional design/engineering effort to maintain equivalent meaning and interaction [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Allowing zoom but keeping a fixed-size chart container so content becomes clipped.
- **Why it fails:** Users can zoom text/marks into invisibility (cut off) and lose information or controls [@elavskyHowAccessibleMy2022] [@w3c_understanding_reflow].
- **The Wrong Fix:** Making users scroll both horizontally and vertically to see the zoomed chart.
- **Why it fails:** This is explicitly the failure mode reflow is meant to avoid (two-direction navigation to access content) [@w3c_understanding_reflow].

## How to Check <!-- role: check -->

- **Visual Sign:** After zooming, labels/marks/controls are truncated, overlap into illegibility, or disappear outside the viewport; the user must pan in two directions to access chart content.
- **The Test:** Zoom the page and/or constrain the viewport width and confirm the chart reflows with no loss of information or functionality and no two-direction cut-off behavior [@w3c_understanding_reflow] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the chart container and internal layout so zoomed content isn’t clipped, and ensure text/marks scale with the zoom method being used [@elavskyHowAccessibleMy2022].
- **Best Fix:** Implement responsive reflow behavior that rearranges the display at narrow widths/zoomed states so all meaningful information and functionality remains available without two-direction cut-off, explicitly preserving chart content through reflow [@w3c_understanding_reflow] [@elavskyHowAccessibleMy2022].
