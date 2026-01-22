---
id: reduce-curse-of-knowledge-by-adding-market-discipline-to-forecasting-tasks
title: "Add market trading with profit-and-loss to reduce curse-of-knowledge bias\
  \ in forecasts of others\u2019 beliefs"
bibliography: references.bib
description: Use market trading (not just incentives or feedback) to cut curse-of-knowledge
  bias when people must predict less-informed beliefs.
labels:
- chart:none
- task:forecast
- visual:none
- impact:accuracy
- data:uncertainty
- audience:expert
- domain:behavioral-economics
- complexity:advanced
---

## Reduce curse-of-knowledge bias using market trading <!-- role: advice -->

Use a trading market with profit-and-loss to elicit forecasts of less-informed beliefs when you need to reduce curse-of-knowledge bias. Keep the forecasters’ private information fixed while letting prices and trades discipline biased judgments.

## Market discipline reduces bias via differential trader influence <!-- role: reason -->

When better-informed forecasters try to predict what less-informed people think, they systematically overweight their own extra information; market interaction partially corrects this because traders closer to the correct “less-informed” forecast participate more and pull outcomes toward less-biased values.

**Mechanism:** Trading aggregates dispersed judgment quality: participants who are less biased act more, and their bids/offers shift prices, reducing (but not eliminating) the average bias in the group outcome.

**Evidence:** In controlled experiments where informed subjects traded assets whose dividends equaled uninformed subjects’ forecasts, market prices converged between the unbiased benchmark and the “pure bias” benchmark, rejecting both extremes [@camererCurseKnowledgeEconomic1989]. Compared with incentivized individual judgments (with or without feedback), market judgments showed roughly half as much curse-of-knowledge bias [@camererCurseKnowledgeEconomic1989].

**Notes:** Feedback alone did not measurably reduce bias in individual judgment, so the reduction is attributed to market forces rather than learning-by-feedback in the same task [@camererCurseKnowledgeEconomic1989].

## Contexts requiring forecasts of others under asymmetric information <!-- role: context -->

- **User Goal:** Predict what a less-informed group believes or will pay, despite having extra private information.
- **Task:** Forecast a forecast (e.g., estimate others’ mean belief) rather than forecast the underlying state directly.
- **Data:** Two information sets where the forecaster’s information strictly includes the target group’s information (asymmetric information).
- **Chart Setting:** Not a charting problem; applies to elicitation or decision workflows (pricing, valuation, underwriting-like settings).
- **Audience:** Analysts, traders, negotiators, or researchers producing estimates that must reflect less-informed beliefs.
- **Success Criterion:** Reduced systematic drift of forecasts toward the informed party’s private signal.

## Exceptions where markets cannot be used or will not discipline bias <!-- role: exceptions -->

**Break it when:** You cannot allow trading, short selling, or repeated interaction that generates a price signal. **Why:** The documented bias reduction relies on market participation and pricing dynamics; without those forces, bias looks like individual judgment [@camererCurseKnowledgeEconomic1989].

## Costs of using markets as a debiasing device <!-- role: costs -->

**Sacrifice:** Market setups are more complex than individual elicitation and require time for trading rounds. **Risk:** Markets reduce bias but do not eliminate it, so decisions can remain systematically distorted. **Mitigation:** Treat prices as partially debiased signals rather than fully unbiased ground truth.

## Mistakes that fail to reduce the curse of knowledge <!-- role: mistakes -->

**Mistake:** Adding performance pay to individual forecasts and assuming bias will disappear. **Why it fails:** Incentives did not remove the curse-of-knowledge bias in the tested forecasting-of-forecasts task [@camererCurseKnowledgeEconomic1989].

**Mistake:** Adding trial-by-trial feedback to individual forecasters and assuming learning will fix the bias. **Why it fails:** Feedback produced little or no reduction in bias relative to incentives alone [@camererCurseKnowledgeEconomic1989].

## Check whether market discipline actually reduced bias <!-- role: check -->

**Failure Sign:** Outcomes (prices or aggregated judgments) sit closer to the informed value than to the uninformed benchmark across items. **Quick Check:** Compute a normalized bias index that scales the estimate between the uninformed forecast and the informed value; values near 1 indicate near-complete curse-of-knowledge anchoring. **Stronger Test:** Compare the index between a market condition and an incentivized individual condition; a substantial drop indicates market debiasing.

## Fixes when you cannot run a market <!-- role: fix -->

- Use a separate uninformed group’s forecasts directly as the target quantity instead of asking informed people to simulate them.
- Aggregate multiple independent uninformed forecasts to define the decision input, rather than relying on an informed intermediary’s estimate.
- If you must use informed estimators, report both their estimate and the informed value side-by-side to make residual bias visible in review.
- Run a small pilot comparing informed estimators’ forecasts to actual uninformed forecasts to quantify and correct systematic bias.
