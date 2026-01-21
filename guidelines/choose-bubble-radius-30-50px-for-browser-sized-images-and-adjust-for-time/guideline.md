---
id: choose-bubble-radius-30-50px-for-browser-sized-images-and-adjust-for-time
title: "Choose a 30\u201350px Bubble Radius and Scale It with Time Constraints"
bibliography: references.bib
description: Use moderate bubble sizes that approximate foveal vision and tune bubble
  radius upward when viewing time is short.
labels:
- task:plan-study
- visual:spatial-resolution
- impact:signal-quality
- audience:researcher
- method:BubbleView
- parameter:bubble-radius
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

Start with a BubbleView bubble radius around 30–50 pixels for typical browser-sized stimuli, and increase radius when viewing time is short or images are information-dense.

## The Logic <!-- role: reason -->

Across multiple experiments, bubble radius often had no significant effect on similarity to fixations, but smaller bubbles increased effort/time (more clicks) and could underperform when time was constrained; on webpages, bubble size interacted with viewing time (larger bubbles helped at 10s, while very large bubbles hurt at 30s) [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Bubble size trades off coverage per click vs. spatial precision
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Efficiently approximate fixations/importance on static images.
- **Data Type:** Images sized roughly in the ranges used in the paper (≈500×500 to 1000×600).
- **Audience:** Crowdsourced participants using a mouse/trackpad.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have very small text or tiny UI elements that must be inspected precisely.
- **Reason:** Larger bubbles can blur distinctions between adjacent small targets and reduce localization precision [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Smaller bubbles increase clicks and time; larger bubbles reduce precision.
- **The Risk:** Mis-tuned bubble size can either frustrate participants (too small) or dilute hotspots (too large) [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing the smallest bubble “to match the fovea” without considering task duration.
- **Why it fails:** Small bubbles can be too slow under short viewing times, especially for dense stimuli like webpages [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Participants make very few clicks and maps look under-sampled (too small for the time), or hotspots look overly broad (too large).
- **The Test:** Track clicks/sec and completion complaints during piloting; adjust radius until participants can meaningfully inspect content within the allotted time [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If time is fixed and short, increase bubble radius.
- **Best Fix:** Prefer longer viewing time with a moderate/smaller bubble for better precision, especially on complex images [@kimBubbleViewInterfaceCrowdsourcing2017].
