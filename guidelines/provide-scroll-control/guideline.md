---
id: provide-scroll-control
title: Provide Controls for Complex Scrolling Experiences
bibliography: references.bib
description: Ensure users can adjust, pause, or opt out of infinite scrolling, parallax,
  and scrollytelling interfaces.
labels:
- interaction:scrolling
- interaction:keyboard
- structure:scrollytelling
- impact:accessibility
- impact:agency
- audience:vestibular-impairment
---

## The Rule <!-- role: advice -->
Provide a mechanism for users to adjust or opt out of altered scrolling experiences. If you implement infinite scrolling, parallax effects, or "scrollytelling," you must offer the ability to turn these features off or provide an alternative navigation method, such as a "Load More" or "Next" button.

## The Logic <!-- role: reason -->
Complex scrolling behaviors can induce physical discomfort and navigation barriers.
*   **The Principle:** **Flexible (POUR+CAF)**. This principle focuses on robust user agency, ensuring that the preferences a user sets in lower-level systems are respected in higher-level environments [@elavsky_how_2022].
*   **The Evidence:** Allowing users to control how content changes reduces motion sickness (vestibular disorders) and cognitive load [@inclusivedesignprinciples_give_control_2].

## Where to Apply <!-- role: context -->
This applies to interfaces where the standard scrolling behavior is hijacked or heavily modified to present data.
*   **User Goal:** Navigating long-form data narratives or exploring large datasets without physical distress.
*   **Data Type:** "Scrollytelling" visualizations, infinite data feeds, or parallax data presentations.
*   **Audience:** Users with vestibular disorders, cognitive disabilities, or those navigating via keyboard.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standard Browser Scrolling.
*   **Reason:** If the page utilizes native, static vertical scrolling without scroll-jacking, animation triggers based on scroll position, or automatic content loading, no specific "opt-out" is required as this is the expected default behavior.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Developing dual navigation modes (e.g., a "stepper" interface alongside a "scroller" interface) increases development time and technical complexity.
*   **The Risk:** Users opting out of the primary scrolling experience may view a less "immersive" version of the data narrative.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** trapping the keyboard focus.
*   **Why it fails:** In infinite scrolling implementations without a "Load More" button, keyboard-only users may never reach the footer or content located after the feed because new data loads perpetually [@elavsky_how_2022].
*   **The Wrong Fix:** Assuming "Reduced Motion" settings are enough.
*   **Why it fails:** While respecting system preferences is vital, users may need to opt out of specific content loading behaviors (like infinite scroll) for cognitive reasons independent of motion sensitivity.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the scrollbar jump or behave unpredictably? Do elements move at different speeds (parallax)?
*   **The Test:** Navigate the interface using only a keyboard. If it is an infinite scroll, can you reach the end of the page? Is there a "Next" or "Load More" button available?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace automatic infinite scrolling with a manual "Load More" button at the bottom of the list.
*   **Best Fix:** Provide a global toggle to disable "scrollytelling" effects, converting the experience into a static, paginated, or stepper-based layout where users click "Next" to advance content [@elavsky_how_2022].
