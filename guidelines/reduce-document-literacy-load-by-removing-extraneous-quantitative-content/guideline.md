---
id: reduce-document-literacy-load-by-removing-extraneous-quantitative-content
title: Remove extraneous quantitative details so users can find and apply the needed
  numbers
bibliography: references.bib
description: Simplify quantitative documents and displays by stripping irrelevant
  or complex content that impedes locating and using the key numbers.
labels:
- chart:table
- task:lookup
- visual:layout
- impact:clarity
- data:quantitative
- audience:novice
- domain:health
---

## Strip nonessential numeric content from patient-facing artifacts <!-- role: advice -->

Remove extraneous quantitative details and present only the numbers required for the user’s decision or action. Make the required inputs and outputs easy to locate within the document or screen.

## Why simplification helps document literacy and quantitative action <!-- role: reason -->

Many real-world quantitative errors come from navigation, selection, and algorithm-choice failures rather than arithmetic mistakes. Reducing clutter and narrowing the content to what is personally relevant lowers the document literacy burden and supports correct use.

**Mechanism:** Simplifying the information environment reduces search, filtering, and rule-inference demands, allowing limited cognitive resources to focus on interpretation and action.

**Evidence:** In tasks like nutrition label interpretation, many errors arise from difficulty excluding extraneous information or misapplying serving-size context rather than from calculation alone; design recommendations include removing extraneous information and presenting totals more directly [@anckerRethinkingHealthNumeracy2007].

**Notes:** This is compatible with tailoring approaches that show only personally relevant facts.

## Situations where document-literacy load is the main barrier <!-- role: context -->

- **User Goal:** Extract a value and apply it to a decision or behavior.
- **Task:** Locate numbers in a label/table/form and interpret what to do.
- **Data:** Serving sizes, totals, medication instructions, thresholds.
- **Chart Setting:** Labels, forms, patient instructions, portal tables.
- **Audience:** Users with limited document literacy and variable numeracy.
- **Success Criterion:** Users can reliably find the right number and use the correct rule without external help.

## When not to remove detail <!-- role: exceptions -->

**Break it when:** Regulatory, clinical safety, or informed-consent requirements mandate inclusion of specific quantitative details. **Why:** Omitting required information can create legal, ethical, or safety risks.

## Tradeoffs of simplifying numeric content <!-- role: costs -->

**Sacrifice:** Less completeness and fewer “power user” details in the primary view. **Risk:** Users may need secondary access to omitted context for trust or deeper decisions. **Mitigation:** Provide optional access to details without placing them in the primary path.

## Common simplification failures <!-- role: mistakes -->

- **Mistake:** Leaving all original fields and adding highlighting as the only change. **Why it fails:** Users still face the same search and filtering burden.
- **Mistake:** Simplifying numbers but not simplifying the required rule (algorithm) the user must infer. **Why it fails:** Users can still choose the wrong operation or apply the wrong context.

## Quick tests for document burden <!-- role: check -->

**Failure Sign:** Users ask “Which number do I use?” or use serving-size numbers incorrectly even when they can compute. **Quick Check:** Time how long it takes a user to find the needed number and explain what it represents. **Stronger Test:** Observe completion of a realistic task (e.g., compute total intake for a package) and code whether failures are search/selection versus arithmetic.

## Alternatives when you cannot simplify the artifact much <!-- role: fix -->

- Present precomputed totals for the whole unit a user actually consumes (e.g., entire package) alongside per-unit values.
- Add explicit step cues that state which number to use and which operation is intended.
- Tailor the display to remove fields not relevant to the user’s current decision.
- Break the task into smaller chunks across screens/sections so each step has only the necessary numbers.
