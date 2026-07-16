---
name: discuss
description: Use this for cited visualization design discussion, tradeoff analysis, comparison, and source tracing with chartcoach.
---

# chartcoach Discuss

Use catalog records to answer a visualization design question, compare options,
or explain a tradeoff. Load `core` for catalog selection and shared command
contracts.

## Frame The Question

Record the decision before retrieval:

| Field         | Record                                                        |
| ------------- | ------------------------------------------------------------- |
| Decision      | What the user is choosing or trying to understand.            |
| Data and task | Variables, scales, cardinality, units, and reader task.       |
| Audience      | Knowledge, accessibility needs, and decision context.         |
| Medium        | Static, interactive, dashboard, paper, slide, or mobile.      |
| Constraints   | Space, color, print, interaction, uncertainty, and toolchain. |

State a reasonable assumption when one missing detail changes scope but still
allows a bounded answer.

## Find Candidate Records

Inspect the live roles and labels, then search with the user's concepts:

```sh
chartcoach catalog labels --contains "<concept>" --format json
chartcoach catalog list --contains "<concept>" --format json
```

Use SQL when the question depends on section content, labels, or sources:

```sh
chartcoach catalog sql "
  select distinct g.id, g.title, s.role
  from guidelines g
  join sections s on s.guideline_id = g.id
  where s.content ilike '%<concept>%'
  limit 20
" --format json
```

Run separate searches for competing options. Shared results often carry the
boundary between them.

Use indexed discovery when deterministic retrieval remains broad:

```sh
chartcoach catalog find \
  --profile <profile> \
  --mode fts \
  --limit 10 \
  --format compact \
  "<task> <option> <constraint>"
```

## Verify Claims

Read each selected record and its relevant section:

```sh
chartcoach catalog read <guideline-id> \
  --section <manifest-role> \
  --source-detail full \
  --format markdown
chartcoach catalog cite <guideline-id> --format markdown
```

Classify candidates as supporting, limiting, conflicting, adjacent, or rejected.
Reject a topical match when its chart family, task, audience, data type, or
interaction state differs from the user's case.

Source records establish the published basis of a guideline. They do not prove
that every detail in the source applies to the current decision. Keep that
boundary next to the affected claim.

## Write The Answer

```text
Recommendation:
Why it fits this case:
Catalog evidence:
Tradeoffs and alternatives:
Source trail:
Uncertainty:
```

Name the guideline id and title for each claim. Include the relevant section,
the exact-read command when auditability matters, and the citation output when
the response needs public links or references.
