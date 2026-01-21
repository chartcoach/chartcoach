---
id: increase-viewing-time-for-information-dense-stimuli-like-webpages
title: Increase Viewing Time for Information-Dense Stimuli
bibliography: references.bib
description: Give more per-image time in BubbleView for dense layouts (e.g., webpages)
  to better approximate fixation distributions.
labels:
- task:plan-study
- impact:signal-quality
- audience:researcher
- method:BubbleView
- stimulus:webpage
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

Use longer BubbleView viewing times on information-dense images (like webpages), or switch to a defined task, rather than relying on short free-viewing windows.

## The Logic <!-- role: reason -->

For webpages, the paper found a significant effect of viewing time on similarity to fixations and an interaction with bubble size; longer viewing (e.g., 30s vs 10s) improved approximation, and description (unlimited time) could converge faster for small participant counts [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Dense stimuli require more sampling time for consistent coverage
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Approximate fixation patterns on interfaces with many competing elements.
- **Data Type:** Static webpages or similarly dense designs.
- **Audience:** Crowdsourced participants who must click to inspect.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need the very top-most “headline” regions of importance (not broader coverage).
- **Reason:** Short tasks may still identify only the most dominant regions, but won’t approximate full fixation distributions well [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher time and cost per image.
- **The Risk:** Participant fatigue if sessions become too long without breaks [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a 10s free-viewing window and shrinking bubble size to “increase precision.”
- **Why it fails:** With too little time, small bubbles can under-sample content and reduce agreement with fixations [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Heatmaps miss many regions that appear in fixation maps, especially across multiple page sections.
- **The Test:** Pilot at 10s vs 30s and compare map stability/similarity; if 10s looks under-sampled, extend time or use description [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase time per image (e.g., from 10s to 30s for dense stimuli).
- **Best Fix:** Use a defined task (description) when budget allows and participant counts are limited [@kimBubbleViewInterfaceCrowdsourcing2017].
