---
id: use-credible-intervals-that-incorporate-validity-and-science-strength-not-just-confidence-intervals
title: Use credible intervals that incorporate validity and science-strength judgments
bibliography: references.bib
description: Expand uncertainty summaries beyond sampling variability by reflecting
  internal validity, external validity, and field strength.
labels:
- chart:interval
- task:estimate
- visual:position
- impact:trust
- data:uncertainty
- audience:decision-maker
- domain:evidence-synthesis
---

## Report uncertainty as a credible interval that reflects more than sampling error <!-- role: advice -->

When presenting an interval estimate for decision-making, report a credible interval that accounts for variability plus threats to internal validity, external validity, and the strength of the underlying science. Do not present a narrow confidence interval as if it captures all meaningful uncertainty.

## Why confidence intervals can understate decision-relevant uncertainty <!-- role: reason -->

Confidence intervals typically reflect only observed variability under modeling assumptions, while decision makers also face uncertainty from bias, study execution, generalizability, proxies, and weak theoretical foundations. A credible interval communicates what you actually believe about the plausible true range after considering these additional uncertainties.

**Mechanism:** Incorporating validity and pedigree judgments widens or shifts the interval to match the uncertainty that matters for decisions, reducing surprise and misplaced confidence.

**Evidence:** Credible intervals should differ from confidence intervals when there are non-negligible threats to internal validity, external validity, or the strength of the science, because these add uncertainty beyond observed variability [@fischhoffCommunicatingScientificUncertainty2014]. Explicit quantitative uncertainty is generally more usable than improvised verbal uncertainty expressions, which can be interpreted inconsistently [@fischhoffCommunicatingScientificUncertainty2014].

**Notes:** If you cannot provide a final interval, supplying structured judgments about validity threats can allow others to infer an implied credible range.

## When an interval estimate is used to support choices <!-- role: context -->

- **User Goal:** Decide among options or policies based on estimated outcomes and uncertainty.
- **Task:** Compare intervals; judge whether uncertainty crosses a decision threshold.
- **Data:** Experimental or observational estimates; model-based projections; synthesized evidence.
- **Chart Setting:** Evidence tables, effect-size plots, model output summaries, policy briefs.
- **Audience:** Decision makers who may conflate statistical precision with real-world certainty.
- **Success Criterion:** Users understand that uncertainty includes bias and generalizability, not only sample size.

## When not to provide a credible interval <!-- role: exceptions -->

**Break it when:** You cannot specify what sources of uncertainty were considered and cannot defend any bounded range. **Why:** An interval without a defensible basis can create false confidence [@fischhoffCommunicatingScientificUncertainty2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More effort and potential controversy in expressing judgment. **Risk:** Readers may compare your wider interval to others’ narrower ones and assume your work is worse rather than more complete. **Mitigation:** Pair the interval with a concise statement of included uncertainty sources.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Publishing only confidence intervals while ignoring validity and applicability threats. **Why it fails:** Decision makers treat the interval as complete uncertainty and may be overconfident [@fischhoffCommunicatingScientificUncertainty2014].
- **Mistake:** Avoiding intervals entirely and substituting qualitative hedges. **Why it fails:** Verbal uncertainty is poorly calibrated across readers and hard to use in choices [@fischhoffCommunicatingScientificUncertainty2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Stakeholders are surprised by outcomes that were plausible given known biases or generalization gaps.\
**Quick Check:** Ask “Would my interval change if the study had selection/attrition/performance issues or weak proxies?” If yes, a pure confidence interval is insufficient.\
**Stronger Test:** Have independent experts review whether the stated interval plausibly reflects known threats to validity and field strength.

## What to do instead <!-- role: fix -->

- Add a brief uncertainty audit summary (internal validity, external validity, strength of science) adjacent to the interval.
- Present two intervals when helpful: a sampling-only interval and a decision-grade credible interval.
- Explain whether the interval accounts for potential bias direction (overestimate vs underestimate).
- If you cannot defend a numeric range, provide the structured validity profile so others can adjust uncertainty explicitly.
