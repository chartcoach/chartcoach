---
id: expect-icon-arrays-to-lower-perceived-seriousness-vs-numeric-risk-presentations
title: Treat icon arrays as potentially lowering perceived risk seriousness compared
  with numbers
bibliography: references.bib
description: Icon arrays can make the same risk and benefit seem less serious or less
  helpful than numerical presentations.
labels:
- chart:icon-array
- task:judge
- visual:icon
- impact:perception
- data:probability
- audience:general
- domain:health-risk
---

## Anticipate lower perceived seriousness when using icon arrays instead of numbers <!-- role: advice -->

Assume icon arrays may reduce perceived seriousness of baseline risk and perceived helpfulness of risk reduction compared with an equivalent numerical presentation.

## Why icon arrays can dampen perceived seriousness <!-- role: reason -->

When viewers see the full denominator (many unaffected individuals) alongside the numerator (affected individuals), attention may shift away from the harmed cases, making the overall risk feel less alarming than when expressed numerically.

**Mechanism:** Salience of the unaffected group can dilute the emotional weight of the affected group, changing subjective seriousness without changing objective risk.

**Evidence:** Baseline cancer risks and the helpfulness of screenings were rated lower when shown as icon arrays than when shown as numerical ratios conveying the same values [@galesicUsingIconArrays2009].

**Notes:** The measured effect was on perceived seriousness and helpfulness ratings, not on comprehension accuracy.

## When perception effects matter most <!-- role: context -->

- **User Goal:** Form a subjective judgment of how serious a risk is or how helpful a treatment is.
- **Task:** Rate seriousness or helpfulness (attitudinal judgment), not compute a value.
- **Data:** Equivalent risks expressed either visually (icon arrays) or numerically (ratios).
- **Chart Setting:** Patient education, screening decision aids, public health messaging.
- **Audience:** General audiences where affect and worry influence decisions.
- **Success Criterion:** Perceived seriousness/helpfulness stays aligned with communication intent and ethical goals.

## When not to follow this exactly <!-- role: exceptions -->

**Break it when:** The primary goal is to reduce exaggerated fear while preserving accurate understanding of the magnitude. **Why:** A decrease in perceived seriousness may be desirable in that specific communication goal.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose persuasive impact or urgency compared with numbers-only framing. **Risk:** Underestimation of seriousness or undervaluation of benefits could reduce uptake of beneficial actions. **Mitigation:** Measure perceived seriousness/helpfulness alongside comprehension in pilots.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming icon arrays are perception-neutral because they are “more intuitive.” **Why it fails:** The same values can produce different seriousness and helpfulness judgments depending on visual versus numeric presentation.

## Quick tests <!-- role: check -->

**Failure Sign:** Users describe the risk as “not that serious” despite correctly recalling the numeric level.\
**Quick Check:** Collect seriousness/helpfulness ratings for both number-only and icon-array versions with identical values.\
**Stronger Test:** Run a small randomized test measuring both comprehension and attitude outcomes before deployment.

## What to do instead <!-- role: fix -->

- Use a numerical ratio format if maintaining higher perceived seriousness/helpfulness is essential.
- Pair icon arrays with a clear textual statement of seriousness context (e.g., explicitly naming the baseline risk level and the change).
- Evaluate both comprehension and perception outcomes during development rather than only comprehension.
- If the goal is calibrated concern, compare multiple presentation formats and select the one that matches target perception without harming understanding.
