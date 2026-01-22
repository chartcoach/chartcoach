---
id: do-not-move-uncertainty-to-text-to-fix-bar-chart-bias
title: Do not move uncertainty to text as a fix for bar-chart inference bias
bibliography: references.bib
description: Text-only margins of error reduce some bias but make inference tasks
  substantially less accurate and can increase misplaced confidence.
labels:
- chart:bar
- task:infer
- visual:annotation
- impact:accuracy
- impact:calibration
- data:uncertainty
- audience:novice
---

## Keep uncertainty visually encoded instead of offloading it to text for inference tasks <!-- role: advice -->

Do not try to fix bar-chart misinterpretation by removing uncertainty graphics and placing margins of error (and outcomes) only in text. If the task depends on uncertainty reasoning, show uncertainty in the chart with an appropriate encoding.

## Why offloading uncertainty to text harms inference performance <!-- role: reason -->

Moving key quantities into text forces viewers to mentally project numbers back into the visual coordinate system, increasing cognitive load and reducing consistent strategy use. While removing visual containment cues can reduce within-the-bar bias, it can simultaneously degrade accuracy on basic inference judgments and miscalibrate confidence.

**Mechanism:** Text values break perceptual integration between the mean, uncertainty, and candidate outcomes, making spatial comparison error-prone; confidence can rise because the display looks simpler even when judgments are worse.

**Evidence:** When the margin of error was presented only in text (no visual error bars), participants followed the expected “trust the sample mean” strategy far less often than with standard bar charts with error bars (about 62% vs. 92%), yet they reported higher confidence in their judgments [@correllErrorBarsConsidered2014]. Moving both the proposed outcome and the margin of error to text mitigated within-the-bar bias but at the cost of substantial inaccuracy and unjustified confidence [@correllErrorBarsConsidered2014].

**Notes:** This pattern matches a common real-world practice (means shown visually, uncertainty relegated to a legend) and still performed poorly for inference.

## When you might be tempted to put uncertainty in a legend instead of the chart <!-- role: context -->

- **User Goal:** Judge how likely an outcome is, or compare uncertain groups.
- **Task:** Infer direction or confidence using both mean and margin of error.
- **Data:** Means with margins of error that must be combined perceptually.
- **Chart Setting:** Space-constrained layouts where legends or captions are used to carry uncertainty information.
- **Audience:** General audiences.
- **Success Criterion:** High accuracy in direction-of-inference judgments and calibrated confidence.

## When text-only uncertainty may be acceptable <!-- role: exceptions -->

**Break it when:** The uncertainty is provided only for compliance or metadata and is not intended to be used for the viewer’s judgment task. **Why:** If inference is not a goal, degraded inference performance is not the primary failure mode [@correllErrorBarsConsidered2014].

## Tradeoffs of keeping uncertainty visual <!-- role: costs -->

**Sacrifice:** Visual uncertainty encodings can require more space and design effort than a textual margin-of-error note. **Risk:** Poorly chosen encodings can still mislead. **Mitigation:** Prefer encodings shown to reduce bias in inferential tasks.

## Common “simplification” failures <!-- role: mistakes -->

**Mistake:** Removing error bars from the graphic while keeping the bar chart and adding “Margin of Error ±X” in a caption. **Why it fails:** Viewers become less accurate at basic inference strategy while becoming more confident [@correllErrorBarsConsidered2014].

## Quick checks for text-offloading problems <!-- role: check -->

**Failure Sign:** The reader must mentally map a textual margin of error onto an unlabeled scale to judge an outcome. **Quick Check:** Hide the caption and ask what uncertainty the chart communicates; if the answer is “none,” the display is not supporting inference. **Stronger Test:** Test whether viewers can correctly answer direction-of-inference questions at high rates without doing arithmetic.

## What to do instead of putting uncertainty only in text <!-- role: fix -->

- Use a symmetric uncertainty encoding (such as gradient or violin) so uncertainty is perceivable directly in the plot.
- If space is tight, keep a compact visual uncertainty mark adjacent to each mean rather than only in a legend.
- If you must include text, use it to label what the visual uncertainty represents rather than replacing the visual encoding.
