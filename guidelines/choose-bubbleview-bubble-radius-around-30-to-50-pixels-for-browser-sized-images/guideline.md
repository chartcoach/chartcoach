---
id: choose-bubbleview-bubble-radius-around-30-to-50-pixels-for-browser-sized-images
title: "Set BubbleView bubble radius to ~30\u201350 pixels for typical browser-sized\
  \ images"
bibliography: references.bib
description: Use a mid-sized bubble radius that supports efficient exploration without
  changing aggregate click-map similarity.
labels:
- chart:other
- task:study-design
- visual:focus
- impact:efficiency
- data:experimental
- audience:researcher
- method:bubbleview
---

## Use a mid-sized bubble radius as a default <!-- role: advice -->

Set BubbleView’s bubble radius to roughly 30–50 pixels for images that fit comfortably in a browser window, and avoid very small bubbles that increase effort without improving aggregate similarity.

## Why bubble size mostly affects effort, not aggregate patterns <!-- role: reason -->

Across tested image types, bubble radius changes the number of clicks and task time more than it changes which regions are ultimately selected in aggregate. Very small bubbles increase clicking workload and participant burden.

**Mechanism:** Smaller bubbles require more clicks to extract the same information, but participants tend to target the same informative regions; larger bubbles reduce click count per image by revealing more area per click.

**Evidence:** On information visualizations, varying bubble radius over a tested range produced similar click-to-fixation similarity, while smaller bubbles increased effort and time and triggered participant complaints [@kimBubbleViewInterfaceCrowdsourcing2017]. Across experiments, bubble radius often showed no significant main effect on similarity scores, while click rates changed monotonically with bubble size [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** Bubble radius interacts with available viewing time on dense pages, so “default” may require adjustment.

## When this bubble-size default applies <!-- role: context -->

- **User Goal:** Configure BubbleView for efficient data collection with good fixation approximation.
- **Task:** Free-viewing or description on static images.
- **Data:** Images in the paper’s tested size range (roughly 500×500 to 1000×600 pixels).
- **Chart Setting:** Browser-based deployment with typical mouse input.
- **Audience:** Crowdsourced participants with varied patience and hardware.
- **Success Criterion:** Participants can explore without excessive clicking while aggregate maps remain stable.

## When not to use this default bubble size <!-- role: exceptions -->

**Break it when:** The viewing time is very short on information-dense stimuli (e.g., webpages). **Why:** A larger bubble may be needed to reveal enough information per click within the time limit [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Larger bubbles reduce spatial precision of what is “inspected” per click. **Risk:** Very small bubbles increase fatigue and can reduce participant compliance. **Mitigation:** Adjust bubble size together with time per image for dense stimuli [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a very small bubble radius to “force precision.” **Why it fails:** It increases workload and cost without reliably improving aggregate similarity to fixations [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Participants generate extremely high click counts per image or complain about difficulty, without clearer maps. **Quick Check:** Compare average clicks per image and completion time across two bubble sizes in a pilot. **Stronger Test:** Compute similarity-to-fixation (if available) or stability of aggregate maps at each bubble size using the same participant count [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Increase the bubble radius if participants cannot reveal enough information within the allotted time.
- Reduce the bubble radius and increase viewing time if you need tighter localization on dense content.
- Keep the bubble radius constant within a study to avoid confounding comparisons across images.
- Monitor click counts and completion time in early pilots and tune bubble size accordingly [@kimBubbleViewInterfaceCrowdsourcing2017].
