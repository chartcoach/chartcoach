---
id: express-user-questions-as-pro-forma-task-templates
title: Translate user analytic questions into pro-forma task templates before designing
  views
bibliography: references.bib
description: Rewrite user questions into standard pro-forma task statements to clarify
  the analytic goal and required data operations.
labels:
- chart:general
- task:requirements
- visual:annotation
- impact:clarity
- data:multivariate
- audience:designer
- custom:taxonomy
---

## Convert each analytic question into a pro-forma task statement <!-- role: advice -->

Rewrite each user question into the matching pro-forma abstract for its low-level analytic task (or a composition of them) before choosing encodings and interactions.

## Why pro-forma templates reduce ambiguity in analytic intent <!-- role: reason -->

Many user questions differ in wording but share the same underlying analytic intent (for example, “high” values as filters versus “highest” values as extrema). Pro-forma task abstracts force the question into a precise structure—cases, attributes, sets, and aggregation functions—so designers can build direct support for the intended operation and avoid implementing the wrong capability.

**Mechanism:** Standard templates normalize diverse natural-language questions into a small set of operational goals, clarifying inputs (set S, attributes A/X/Y) and required transformations (filtering, aggregation, ranking).

**Evidence:** A large set of natural-language analysis questions clustered into ten task types, each defined with a pro-forma abstract that captures the core knowledge goal of questions in that group [@amarLowlevelComponentsAnalytic2005]. Ambiguities like “high” versus “highest” distinguish Filter from Find Extremum and require explicit operational definitions to be answerable [@amarLowlevelComponentsAnalytic2005].

**Notes:** Some questions are compound and should be expressed as compositions (e.g., Compute Derived Value followed by Sort).

## When pro-forma rewrites are especially useful <!-- role: context -->

- **User Goal:** Turn informal questions into implementable visualization requirements.
- **Task:** Requirements gathering, task analysis, evaluation scripting, or feature scoping.
- **Data:** Case–attribute datasets where users ask about subsets, summaries, rankings, distributions, anomalies, similarity, or relationships.
- **Chart Setting:** Any system where multiple views or interactions could plausibly answer the same question in different ways.
- **Audience:** Designers and researchers translating user needs into tool capabilities.
- **Success Criterion:** Each requirement is operationally unambiguous about cases, attributes, sets, and any aggregation.

## When pro-forma templates are not enough <!-- role: exceptions -->

**Break it when:** The question depends on subjective or uncertain criteria (e.g., “tasty,” “better,” “most valued customers”) without an agreed definition. **Why:** The pro-forma templates assume measurable conditions or relationships; uncertain value judgments are not fully specified by the ten primitives.

## Tradeoffs of forcing questions into templates <!-- role: costs -->

**Sacrifice:** Some rich, exploratory goals may be flattened into oversimplified forms. **Risk:** Over-templating can hide that the team has not agreed on definitions (e.g., what counts as “high fiber”). **Mitigation:** Record any missing operational definitions explicitly as open decisions.

## Common failure modes when templating questions <!-- role: mistakes -->

- **Mistake:** Treating “high X” as the same as “highest X.” **Why it fails:** “High” is a Filter that requires a threshold definition; “highest” is a Find Extremum that depends on all other cases in the dataset.
- **Mistake:** Writing a compound question as a single primitive. **Why it fails:** It obscures needed intermediate steps such as aggregating by category before ranking.

## Quick tests to validate your pro-forma rewrite <!-- role: check -->

**Failure Sign:** Two people implement different features for the “same” question. **Quick Check:** Ask a teammate to identify the task type from your pro-forma; if they choose a different task, the requirement is still ambiguous. **Stronger Test:** For each requirement, list the required set S and attributes explicitly; if you cannot, the pro-forma is incomplete.

## What to do instead when a question does not fit a single template <!-- role: fix -->

- Decompose the question into a sequence of the ten primitives (for example, Filter then Determine Range).
- Add an explicit operating definition for thresholds implied by words like “high,” “low,” or “typical.”
- Represent the goal as an aggregate-over-groups problem when the “cases” are derived relationships (e.g., counts per actor) rather than original rows.
- Treat unresolved value judgments as a separate decision step, not as a visualization primitive.
