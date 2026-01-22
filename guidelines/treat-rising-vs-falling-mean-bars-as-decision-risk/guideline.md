---
id: treat-rising-vs-falling-mean-bars-as-decision-risk
title: Do not use rising-versus-falling mean bars to imply different action directions
bibliography: references.bib
description: Whether a mean bar rises from a lower axis or falls from an upper axis
  can shift decisions even when the mean is identical.
labels:
- chart:bar
- task:decide
- visual:direction
- impact:trust
- data:summary
- audience:general
- cognitive-bias:within-the-bar
---

## Avoid using bar direction (rising vs falling) to encode the same mean in decision contexts <!-- role: advice -->

Do not present the same mean as a rising bar in one place and as a falling bar in another when viewers will use the chart to choose an action direction. Keep the depiction of the mean directionally neutral.

## Bar direction changes which side of the mean feels like “inside,” shifting choices <!-- role: reason -->

When a mean is shown as the edge of a bar, whichever side is visually “within the bar” becomes subjectively favored as more likely or more central, and that can carry over into what action seems safer or more appropriate. Flipping the bar to rise or fall flips which side is perceptually privileged, even though the numerical mean is unchanged.

**Mechanism:** The bar’s extent creates a visually privileged region (“inside”), and action preferences can align with moving outcomes toward that visually privileged region.

**Evidence:** Decisions about whether to increase versus decrease a quality measure shifted depending on whether the identical mean was shown with a rising or falling bar, while a no-graph control did not show the same directional shift [@newmanBarGraphsDepicting2012]. This downstream effect aligns with the demonstrated within-the-bar likelihood bias across earlier experiments [@newmanBarGraphsDepicting2012].

**Notes:** The decision shift occurred even though participants were told that values existed both above and below the mean, and the mean itself provided no objective reason to prefer either direction [@newmanBarGraphsDepicting2012].

## When chart-driven action direction is on the line <!-- role: context -->

- **User Goal:** Choose whether to increase vs. decrease, tighten vs. loosen, or otherwise move a metric up vs. down.
- **Task:** Directional decision-making based on summary statistics.
- **Data:** A mean (often at a target such as zero) with unspecified distribution shape.
- **Chart Setting:** Executive summaries, dashboards, media graphics, or reports where the bar could plausibly be drawn to rise or fall to the same mean.
- **Audience:** Decision makers or the general public relying on quick graphical impressions.
- **Success Criterion:** The chosen action direction should not change when the mean and the described data situation are unchanged.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The metric’s semantics require a specific direction from a fixed baseline (for example, values only accumulate upward from zero). **Why:** A directional bar then matches the real constraint of the measure rather than arbitrarily changing which side is “inside” [@newmanBarGraphsDepicting2012].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up a stylistic option that can make layouts feel balanced (e.g., mirroring panels with rising and falling bars). **Risk:** For signed data around zero, forcing only one direction may visually underemphasize negative values or positive values depending on your layout. **Mitigation:** Use a neutral mean marker rather than relying on bar direction for symmetry.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Flipping a mean bar to “match” the sign convention (positive-up, negative-down) while still using a filled bar from an axis. **Why it fails:** Flipping also flips which test values are perceived as inside the bar, and that can change judgments and decisions even when the mean is identical [@newmanBarGraphsDepicting2012].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers recommend increasing in one version of the graphic and decreasing in an otherwise equivalent version that only flips bar direction. **Quick Check:** Create a mirrored version of your chart (rising vs. falling) and see whether your own intuitive “safe” direction changes. **Stronger Test:** A/B test the two versions with a single forced-choice decision; a systematic direction shift indicates vulnerability to the bias.

## What to do instead <!-- role: fix -->

- Represent the mean with a directionally neutral mark that does not create an “inside the bar” region.
- Keep the same mean depiction orientation across panels and pages so that “inside” does not flip across views.
- Provide the distribution (or an explicit statement about symmetric likelihood around the mean) when decisions depend on what values are plausible.
- Use a no-bar summary (text-only mean) in high-stakes decision prompts when you cannot show distributional context.
