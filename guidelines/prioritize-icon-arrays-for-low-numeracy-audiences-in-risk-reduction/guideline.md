---
id: prioritize-icon-arrays-for-low-numeracy-audiences-in-risk-reduction
title: Prioritize icon arrays for low-numeracy audiences estimating risk reduction
bibliography: references.bib
description: Use icon arrays to improve accuracy of risk-reduction estimates for audiences
  with low numeracy.
labels:
- chart:icon-array
- task:estimate
- visual:position
- impact:accessibility
- data:ratio
- audience:novice
- custom:numeracy
- custom:health-risk
---

## Use icon arrays to support risk-reduction judgments for low-numeracy users <!-- role: advice -->

When presenting treatment risk reduction to audiences likely to have low numeracy, add icon arrays to the numeric statement so the proportion in each group is visible. Keep the comparison focused on the two relevant groups (treated vs untreated) with their totals clearly shown.

## Why icon arrays disproportionately help low-numeracy viewers <!-- role: reason -->

Low numeracy increases vulnerability to ratio biases, especially when people must mentally transform counts into proportions. Icon arrays externalize that transformation by showing the whole population and the affected subset, reducing reliance on error-prone numeric manipulation.

**Mechanism:** The visualization reduces computation demands and increases proportional reasoning by making numerator-to-denominator relations perceptually available.

**Evidence:** In probabilistic national samples, low-numeracy participants were much more likely to misestimate risk reduction from numeric-only unequal-denominator scenarios; adding icon arrays reduced incorrect estimates more for low-numeracy than for high-numeracy participants [@garcia-retameroUsingVisualAids2012].

**Notes:** The improvement is strongest in conditions where denominators differ across groups.

## When numeracy is a key audience constraint <!-- role: context -->

- **User Goal:** Understand “how much the treatment helps” from outcome data.
- **Task:** Convert frequencies into an effect estimate (e.g., relative risk reduction).
- **Data:** Frequencies or counts that must be interpreted as ratios.
- **Chart Setting:** Patient decision aids, clinical discussions, brochures, web explainers.
- **Audience:** General public or patients with low numeracy.
- **Success Criterion:** Higher accuracy of estimated risk reduction and fewer systematic direction errors.

## When this may not work as expected <!-- role: exceptions -->

**Break it when:** The audience has low graph literacy and cannot reliably interpret icon arrays. **Why:** Icon-array benefits are moderated by graph literacy, reducing gains for low graph-literate viewers [@garcia-retameroUsingVisualAids2012].

## Tradeoffs of designing for low numeracy with icon arrays <!-- role: costs -->

**Sacrifice:** More design space and potentially more time to view the message. **Risk:** A visually dense icon array can be ignored or misread by some viewers. **Mitigation:** Ensure the display clearly separates the two groups and highlights the affected subset.

## Common failure modes in “helpful” visuals for low numeracy <!-- role: mistakes -->

**Mistake:** Assuming that adding any picture will help without ensuring it represents the whole group and the affected subset. **Why it fails:** The key problem is ratio interpretation; visuals that do not encode denominators do not address denominator neglect.

## Quick checks for low-numeracy robustness <!-- role: check -->

**Failure Sign:** The display allows an interpretation that the smaller numerator implies lower risk without referencing totals. **Quick Check:** Confirm that each group’s total population is explicitly represented and visually comparable. **Stronger Test:** Ask users to state which group has the higher risk and why, and verify they reference “out of how many.”

## Alternatives when icon arrays are constrained or ineffective <!-- role: fix -->

- Add a short textual restatement that pairs each numerator with its denominator adjacent to the relevant group.
- Simplify the information so users do not need to infer proportions from multiple scattered numbers.
- Provide a brief explanation of how to read the icon array when the audience is unfamiliar with such charts.
- If the message cannot accommodate a full icon array, restructure the presentation to reduce reliance on unequal denominators.
