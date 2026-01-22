---
id: use-3d-volume-graphs-when-memorability-is-the-primary-goal
title: Use 3D volume graphs when memorability is the primary goal
bibliography: references.bib
description: Choose 3D volume styling over 2D when the graph must be remembered later
  without reference.
labels:
- chart:bar
- task:remember
- visual:depth
- impact:memorability
- data:quantitative
- audience:novice
- complexity:basic
---

## Use 3D volume graphs for memorability-focused use <!-- role: advice -->

Use a 3D volume-style graph rather than a 2D area-style graph when the key requirement is that viewers remember the content later.

## Why 3D volume styling can support memorability goals <!-- role: reason -->

When the goal shifts from immediate reading to later recall, viewers may value visual distinctiveness and salience more, and 3D volume cues can provide that distinctiveness.

**Mechanism:** Added depth cues can make the figure feel more distinctive as a visual object, supporting later recall in viewers’ judgments.

**Evidence:** In forced-choice comparisons between 2D area and 3D volume graphs, 3D volume was significantly preferred in the memorability (“later”) scenario, whereas 2D was preferred in most other scenarios [@levyGratuitousGraphicsPutting1996].

**Notes:** In the same study, showing data to others produced no strong preference difference between 2D and 3D.

## When this applies <!-- role: context -->

- **User Goal:** Remember the chart content later without re-checking the source.
- **Task:** Later recall; keeping one message distinct from competing messages.
- **Data:** 2D quantitative data rendered with optional depth cues.
- **Chart Setting:** Presentations or materials where delayed recall matters.
- **Audience:** Viewers who will compare later from memory.
- **Success Criterion:** Memorability or distinctiveness rather than immediate precision.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart must support an immediate, correct decision and recall is irrelevant. **Why:** Viewers’ preferences shifted toward 2D for “now/immediate” use [@levyGratuitousGraphicsPutting1996].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce perceived suitability for quick, straightforward reading. **Risk:** Dimensional embellishment can be perceived as unnecessary for immediate comprehension. **Mitigation:** Reserve 3D volume styling for contexts explicitly optimized for recall.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using 3D volume styling while still expecting the chart to function as a quick “gist at a glance” graphic. **Why it fails:** Preferences for 3D shifted toward detail and memory scenarios, not toward gist-focused scenarios [@levyGratuitousGraphicsPutting1996].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers remember the “look” of the chart but cannot restate the main quantitative pattern later. **Quick Check:** If the deliverable is meant to be recalled weeks later, consider 3D volume. **Stronger Test:** Run a delayed recall check with a small sample and ask what they remember after a time gap.

## What to do instead <!-- role: fix -->

- Use a 2D design if immediate accuracy is the primary success metric.
- If 3D is not acceptable, differentiate the chart in other ways (for example, unique layout or distinctive labeling) while staying 2D.
- If the message is about trends, switch to a line chart rather than relying on 3D styling to create impact.
