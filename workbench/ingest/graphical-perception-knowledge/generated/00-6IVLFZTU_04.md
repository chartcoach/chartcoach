---
id: use-animation-for-propagation-direction
title: "Use animated maps to quickly identify propagation direction"
tags:
  - impact:performance
  - impact:perceptual
  - chart:map
  - medium:animation
  - task:direction
  - task:trend
  - data:spatiotemporal
audience:
  - audience:expert
medium:
  - medium:interactive
evidence:
  strength: medium
  summary: "In an experiment on geovisualizations (Peña-Araya et al., 2020; n=18), an animated map was the fastest technique for determining the overall direction of a propagating phenomenon. Participants completed the task 2.9s faster with animation than with small multiples. However, this speed came at a cost: animation was also the most error-prone technique for this task."
sources:
  - type: research
    ref: Peña-Araya et al., 2020
    url: http://dx.doi.org/10.1145/3313831.3376350
    note: "The study (n=18) found that for the 'Direction' task, animation was the fastest visualization (9.2s) compared to small multiples (12.18s) and glyph maps (15.92s). However, its error rate (7.41%) was higher than the others."
    role: primary
---
## Guidance
To help users quickly get a sense of the direction of movement or spread in spatiotemporal data, use an animated map. Be aware, however, that this may lead to lower accuracy compared to static alternatives.

## Why
Animation leverages the human visual system's sensitivity to motion, making the flow and direction of a phenomenon feel intuitive and immediately apparent. The sequential presentation of frames creates a strong impression of movement. This allows for very fast, gestalt judgments of direction. The trade-off is that it is difficult to review or precisely compare frames, which can lead to errors.

## When it applies
- The primary task is to understand the general flow or directional trend of a phenomenon spreading over a map (e.g., "Is the hurricane moving north-east?").
- A quick, high-level understanding is more important than precision.
- The visualization is used for presentation or to give a general audience an intuitive feel for the data.

## Exceptions
- When accuracy is critical. A static small-multiples display, while slower, is less error-prone.
- When the propagation is complex, with multiple directions or non-contiguous jumps. Animation can make these complex patterns difficult to deconstruct.

## Trade-offs
- **Speed vs. Accuracy:** Animation is fast for this task but is also the most error-prone. You are trading precision for speed.
- **Cognitive Load:** While animation feels intuitive, it places a heavy load on working memory if viewers need to recall specific states or make comparisons, a drawback that static small multiples avoid.

## Signs of Trouble
- **Low Confidence:** Users say they *think* they know the direction but are not sure.
- **Inaccurate Takeaways:** Different users come to different conclusions about the direction of spread.
- **Constant Replaying:** Users have to replay the animation multiple times to confirm their initial impression, negating the speed advantage.

## How to Improve
- **Quick Fix: Control the Speed.** Allow users to slow down the animation speed. This gives them more time to process each frame and can improve accuracy.
- **Moderate Redesign: Pair Animation with a Static Summary.** Complement the animation with a static graphic, like an arrow overlay on the map, that explicitly shows the primary direction of movement as a summary.
- **Comprehensive Redesign: Offer Multiple Views.** Provide both an animated view (for the quick, intuitive understanding) and a small-multiples view (for detailed, accurate analysis). Allow the user to switch between them.