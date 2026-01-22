---
id: use-sensitivity-analysis-to-decide-which-uncertainties-to-visualize-or-explain
title: Use sensitivity analysis to prioritize which uncertainties to communicate
bibliography: references.bib
description: Focus communication on uncertainties that could change the decision,
  not every technical caveat.
labels:
- chart:annotation
- task:prioritize
- visual:text
- impact:clarity
- data:uncertainty
- audience:decision-maker
- domain:decision-analysis
---

## Communicate only decision-sensitive uncertainties, identified via sensitivity analysis <!-- role: advice -->

Before adding uncertainty details to a visualization or summary, determine which uncertain inputs could plausibly change the preferred decision. Communicate those uncertainties prominently and treat decision-insensitive uncertainties as background or omit them.

## Why decision sensitivity determines what uncertainty is worth showing <!-- role: reason -->

Uncertainty information is useful only to the extent that it affects choices. Sensitivity analysis formalizes whether plausible parameter variation would change the best option, preventing overwhelm from irrelevant caveats and ensuring that missing uncertainty does not flip a conclusion unnoticed.

**Mechanism:** By linking uncertainty to choice reversals, sensitivity analysis converts “more information” into “decision-relevant information,” aligning communication with what users need to act.

**Evidence:** Sensitivity analysis is described as a common formalism for assessing how much people need to know about uncertainty by asking whether any plausible values would affect the preferred option [@fischhoffCommunicatingScientificUncertainty2014]. Communications should simplify and complicate scientific discourse by removing irrelevant uncertainty while uncovering omitted decision-relevant uncertainty [@fischhoffCommunicatingScientificUncertainty2014].

**Notes:** When uncertainty is decision-insensitive, reducing it further may have no practical value for the choice.

## When you are comparing options or policies under uncertainty <!-- role: context -->

- **User Goal:** Choose among fixed options or decide whether to wait for more information.
- **Task:** Determine whether uncertainty could change rankings or threshold crossings.
- **Data:** Model parameters, effect estimates, forecasts with plausible ranges.
- **Chart Setting:** Comparative charts, decision briefs, dashboards with “key drivers” panels.
- **Audience:** Decision makers with limited time; may over- or under-weight uncertainty.
- **Success Criterion:** Attention is allocated to the uncertainties that matter for the decision.

## When not to down-prioritize uncertainties <!-- role: exceptions -->

**Break it when:** The communication’s purpose is to create options or improve a mental model of the system, not to choose among fixed options. **Why:** Broader uncertainty knowledge may be needed to devise new interventions [@fischhoffCommunicatingScientificUncertainty2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may omit details that some technical reviewers expect. **Risk:** Users may assume omitted uncertainties are nonexistent rather than immaterial. **Mitigation:** Add a short note that other uncertainties exist but are not decision-changing under plausible ranges.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Presenting every caveat with equal visual prominence. **Why it fails:** Users are overwhelmed and may ignore all uncertainty, including what matters [@fischhoffCommunicatingScientificUncertainty2014].
- **Mistake:** Highlighting uncertainty that is easy to quantify rather than uncertainty that affects the decision. **Why it fails:** Communication optimizes for convenience rather than decision value [@fischhoffCommunicatingScientificUncertainty2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users cannot tell which uncertainties could change the decision.\
**Quick Check:** Ask “If this uncertainty moved within a plausible range, would the recommended option change?” for each displayed uncertainty.\
**Stronger Test:** Run a small scenario analysis and see whether the chosen option changes; display only the drivers of change.

## What to do instead <!-- role: fix -->

- Identify a small set of decision-driving uncertain parameters and foreground them in the visualization narrative.
- Provide a compact “would this change the choice?” note for each uncertainty you include.
- Move decision-insensitive uncertainties to a methods appendix or expandable detail.
- If rankings are robust, communicate robustness explicitly rather than adding more uncertain detail.
