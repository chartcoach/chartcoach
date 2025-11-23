---
id: pause-animation-for-reading
title: Pause Animation During Text Reading
bibliography: references.bib
description: Halt visual movement when introducing text labels to prevent attentional
  clashes.
labels:
- visual:animation
- visual:text
- task:read
- impact:comprehension
---

## The Rule <!-- role: advice -->
Stop all on-screen motion when revealing a complex label or caption. Allow specific static time for reading before resuming action.

## The Logic <!-- role: reason -->
Reading text and tracking motion use the same cognitive resources. Eye-tracking data shows that users often fail to track an object if they are busy reading a label, or conversely, they fail to read the label because they are tracking motion [@faraday_designing_1997]. The brain struggles to process linguistic and dynamic visual information simultaneously if they are spatially separated.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the name or function of a specific component.
*   **Data Type:** Multimedia presentations with text labels or captions.
*   **Audience:** Low-domain knowledge users who do not recognize the terminology on sight.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The label is extremely short (1-2 words) and moves *with* the object.
*   **Reason:** If the text is attached to the object, the eye can process both as a single unit.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The presentation duration increases due to the added pauses.
*   **The Risk:** The presentation may feel "stop-and-start" or disjointed if pauses are too frequent.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Speaking the label while the text appears and the object moves.
*   **Why it fails:** Even with audio support, the visual competition between reading and tracking degrades recall of the visual action.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are words appearing while objects are flying across the screen?
*   **The Test:** Try to read the label out loud while watching the animation. If you miss the visual action, the design is flawed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Freeze the animation for 2-3 seconds immediately upon displaying a label.
*   **Best Fix:** sequence the presentation: Reveal object -> Pause -> Reveal Label -> Pause -> Resume Animation.
