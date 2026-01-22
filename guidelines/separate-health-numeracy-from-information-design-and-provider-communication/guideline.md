---
id: separate-health-numeracy-from-information-design-and-provider-communication
title: Design quantitative health communication as a system, not just a patient skill
  test
bibliography: references.bib
description: Treat successful use of quantitative health information as the combined
  result of patient skills, information design, and provider communication.
labels:
- chart:general
- task:decide
- visual:annotation
- impact:clarity
- data:quantitative
- audience:novice
- domain:health
---

## Treat quantitative health communication as a system outcome <!-- role: advice -->

Evaluate and design quantitative health communication as the combined effect of patient health numeracy, information artifact design, and provider communication skills. Do not attribute failure to the patient’s computation ability alone.

## Distributed-cognition framing for quantitative health information use <!-- role: reason -->

Quantitative understanding and decision-making can be distributed across people (patients, clinicians, family) and external representations (documents, charts, devices). When the artifact or communication is poorly designed, even people with strong skills can fail; when well designed, artifacts and communication can compensate for weaker skills.

**Mechanism:** Shifting from “individual deficit” to “system fit” reduces mismatches between task demands and user capability by making design and communication part of the cognitive system.

**Evidence:** Productive use of quantitative health information depends not only on patient numeracy but also on document/device design and provider communication, consistent with a distributed cognition perspective [@anckerRethinkingHealthNumeracy2007].

**Notes:** This framing applies to both patient-facing and provider-facing displays, since provider interpretation and explanation are part of the same system.

## System-level quantitative communication situations <!-- role: context -->

- **User Goal:** Use numbers to guide health behavior or make a health decision.
- **Task:** Understand, compare, compute, or apply quantitative health information.
- **Data:** Risks, lab values, medication schedules, nutrition facts, probabilities.
- **Chart Setting:** Patient education materials, portals/personal health records, decision aids, telehealth dashboards, device readouts.
- **Audience:** Patients with variable numeracy; clinicians explaining quantitative information.
- **Success Criterion:** Accurate understanding and actionable use of the numbers in context.

## When not to treat it as a system problem <!-- role: exceptions -->

**Break it when:** The task is purely a math-skills assessment with no intention to support real-world decisions. **Why:** The goal is measurement of individual capability rather than improving artifact- and communication-mediated performance.

## Tradeoffs of a system framing <!-- role: costs -->

**Sacrifice:** More design and evaluation effort across artifacts and workflows. **Risk:** Accountability can become diffuse, making it harder to choose what to fix first. **Mitigation:** Prioritize the highest-friction step where misunderstanding causes downstream errors.

## Common failure modes in quantitative health communication framing <!-- role: mistakes -->

**Mistake:** Blaming misunderstanding solely on “low numeracy” after users fail a task. **Why it fails:** It ignores representational and communication barriers that can cause failure even for capable users.

## Quick tests for system fit <!-- role: check -->

**Failure Sign:** Users can read values in one representation (e.g., device) but cannot use the same values in another (e.g., table/portal). **Quick Check:** Ask users to restate what a displayed number means and what action it suggests. **Stronger Test:** Observe a real task end-to-end (e.g., medication scheduling) and identify where cognition breaks across people and artifacts.

## What to do instead of individual-blame diagnoses <!-- role: fix -->

- Audit the quantitative demands of the artifact and reduce unnecessary computation and navigation steps.
- Add provider scripts or prompts to verify patient understanding of quantities during discussion.
- Redesign the representation (format, framing, graphics, annotations) so the intended inference is supported by the display.
- Enable collaborative review of the same artifact between patient and provider (shared viewing and discussion).
