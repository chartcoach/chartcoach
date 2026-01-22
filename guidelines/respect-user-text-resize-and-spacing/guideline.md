---
id: respect-user-text-resize-and-spacing
title: Respect user text resizing and spacing changes without loss of content or functionality
bibliography: references.bib
description: Ensure chart text responds to user-controlled font size and text spacing
  adjustments without breaking readability, layout, or interaction.
labels:
- chart:any
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:low-vision
- category:flexible
- source:chartability
---

## Respect user-controlled text size and spacing in charts <!-- role: advice -->

Allow users to increase font size and adjust text spacing using their user agent (browser, operating system, or custom style sheet) without losing chart content or functionality. The chart must not block or override these programmatic text changes.

## Why honoring user text adjustments improves accessibility <!-- role: reason -->

When chart text respects user-controlled resizing and spacing, people who rely on larger text or altered spacing can still perceive labels, instructions, and values without needing a separate alternative experience. Blocking these adjustments forces users into a fixed presentation that can make chart text unreadable or cause essential information and controls to disappear.

**Mechanism:** Preserving user-agent text scaling and spacing keeps chart text legible while maintaining access to the same information and interactions.

**Evidence:** Text should be resizable up to 200% without assistive technology and without loss of content or functionality, so users with low vision can enlarge text for readability [@w3c_understanding_resize]. Evaluating whether visualizations respect user settings and provide robust, flexible control is a key heuristic for accessible data experiences [@elavskyHowAccessibleMy2022].

**Notes:** This guideline concerns programmatic changes driven by user settings (including browser zoom and custom styles), not manual author-controlled font toggles.

## When to apply user-respected text resizing and spacing <!-- role: context -->

- **User Goal:** Read chart titles, labels, annotations, legends, tooltips, and instructions at a comfortable size/spacing.
- **Task:** Identify values, categories, axes, and interaction instructions without missing information.
- **Data:** Any dataset where text carries meaning (labels, units, categories, notes, or explanations).
- **Chart Setting:** Any chart embedded in a user agent that can change font size or text spacing (e.g., browser zoom, custom style sheets).
- **Audience:** People who need larger text or adjusted spacing for readability, including low-vision users.
- **Success Criterion:** Text can be enlarged and spacing adjusted while all essential content remains visible and all interactions remain usable.

## Exceptions: When not to follow it <!-- role: exceptions -->

Break it when there is no text in the chart or surrounding visualization experience that conveys meaning or instructions. **Why:** There is no user-adjustable text to respect in the first place.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Layout stability and pixel-perfect alignment may be harder to maintain under large text and spacing changes. **Risk:** Labels may overlap or consume additional space, which can reduce visible plotting area. **Mitigation:** Treat this as a robustness requirement and prioritize preserving content and functionality over fixed layout fidelity.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Converting meaningful text into non-text graphics so it cannot be resized by user settings. **Why it fails:** Users cannot apply their text preferences, and readability barriers persist even when the user agent is configured for accessibility.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Text becomes clipped, overlaps to the point of unreadability, or disappears, or chart interactions stop working after user text adjustments. **Quick Check:** Increase text size using the user agent and confirm all chart text remains readable and all interactive features still work. **Stronger Test:** Increase text size to 200% and verify there is no loss of chart content or functionality under that condition [@w3c_understanding_resize].

## Fix: What to do instead <!-- role: fix -->

- Use text as real, resizable text so user-agent font size and spacing changes apply.
- Ensure chart layout can reflow so resized text does not cause loss of labels, instructions, or other essential content.
- Avoid overriding or blocking user style changes (including custom style sheets and user-agent zoom) that adjust font size and text spacing.
- If the chart cannot preserve both readability and functionality under resizing, provide an alternative presentation within the same experience that remains functional under user text adjustments.
