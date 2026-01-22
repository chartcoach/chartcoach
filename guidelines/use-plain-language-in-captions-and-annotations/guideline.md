---
id: use-plain-language-in-captions-and-annotations
title: Explain context in plain language in captions and annotations
bibliography: references.bib
description: Use concrete, non-technical wording in captions and annotations so viewers
  can understand the context without specialized knowledge.
labels:
- chart:general
- task:interpret
- visual:text
- impact:clarity
- data:general
- audience:novice
- tag:annotations
---

## Use plain, concrete wording for contextual text <!-- role: advice -->

Write captions, annotations, and scenario descriptions in plain language and define any unavoidable jargon. Prefer specific, concrete terms over abstract or high-level phrasing.

## Plain language reduces cognitive load and misinterpretation <!-- role: reason -->

When contextual text is dense, technical, or abstract, viewers spend effort decoding the language instead of interpreting the message, which increases misunderstanding and reduces confidence—especially for non-experts. Plain language makes the intended takeaway easier to parse and helps audiences connect the context to what they see.

**Mechanism:** Familiar words and concrete phrasing lower reading effort and ambiguity, freeing attention for interpreting the visualization and improving consistency of understanding across audiences.

**Evidence:** Viewers criticized complex or abstract wording in captions/annotations, and lay audiences in particular struggled with technical terms and high-level scenario descriptions in climate visualizations [@schuster_being_2024]. Older, more scientific caption language was harder to distill into clear messages than newer, plainer captions, which supported narrative comprehension more effectively [@koesten_what_2023]. Practitioners emphasize simplifying language in titles, labels, and annotations as essential guidance for newcomers [@schuster_who_2023].

**Notes:** Plain language can still be precise; the goal is to remove unnecessary complexity, not to remove meaning.

## Situations where contextual text carries meaning <!-- role: context -->

- **User Goal:** Understand what the chart shows, why it matters, and how to interpret labels, scenarios, or uncertainty statements.
- **Task:** Interpret an annotation, caption, or narrative takeaway; connect a described scenario or assumption to the visual evidence.
- **Data:** Potentially unfamiliar domain concepts; may include modeled scenarios, projections, uncertainty, or processing steps that require explanation.
- **Chart Setting:** Reports, dashboards, presentations, or social media where captions/annotations are a primary source of context and are read quickly.
- **Audience:** Mixed expertise, especially lay or novice readers; readers with limited domain literacy or limited time.
- **Success Criterion:** Viewers can accurately paraphrase the intended context and key takeaway without asking for definitions.

## When technical language is the point <!-- role: exceptions -->

**Break it when:** You are writing for a specialist audience that expects formal terminology (e.g., regulatory, clinical, or scientific documentation) and precision depends on standard terms. **Why:** Replacing established terms can introduce ambiguity or conflict with required definitions.

## Tradeoffs of simplifying language <!-- role: costs -->

**Sacrifice:** You may lose some nuance or compress complex methodology into fewer words. **Risk:** Over-simplification can sound misleading, overly certain, or inaccurate to experts. **Mitigation:** Keep the plain-language statement, then add a brief definition or parenthetical clarification for critical terms.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Using abstract phrases like “robust,” “significant,” “optimized,” or “high uncertainty” without specifying what they mean in the viewer’s terms. **Why it fails:** Readers cannot map vague qualifiers to a concrete interpretation, so they guess or disengage.

## Fast checks for plain-language context <!-- role: check -->

**Failure Sign:** A caption or annotation cannot be paraphrased by a non-expert without asking what multiple words mean. **Quick Check:** Circle every term a general reader might not know (jargon, acronyms, statistical terms); if more than a couple remain undefined, rewrite. **Stronger Test:** Ask a lay reader to restate the caption in one sentence; if their restatement changes the meaning, simplify and define terms.

## Practical revisions that improve clarity <!-- role: fix -->

- Replace abstract qualifiers with concrete descriptions (what changes, by how much, and under what condition).
- Define unavoidable technical terms the first time they appear and remove the rest of the jargon.
- Rewrite scenario or projection text to name who/what/when explicitly (e.g., “If emissions keep rising through 2050…” rather than “under SSP-like pathways…”).
- Split one dense caption into a short headline takeaway plus one short clarifying sentence that explains the assumption or limitation.
