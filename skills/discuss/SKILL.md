---
name: discuss
description: Compare visualization choices with chartcoach guidelines and their source citations.
---

# chartcoach Discuss

Use guideline entry records to compare visualization choices or explain a
tradeoff. Read `core` first. It sets `CHARTCOACH_SOURCE` and inspects the
current roles and labels before this workflow begins.

## Describe the decision

Record the facts that can change the answer:

| Field         | Record                                                            |
| ------------- | ----------------------------------------------------------------- |
| Decision      | What the user is choosing or trying to understand                 |
| Data and task | Variables, scales, units, number of categories, and reader task   |
| Audience      | Knowledge, accessibility needs, and decision context              |
| Medium        | Static, interactive, dashboard, paper, slide, or mobile           |
| Constraints   | Space, color, print, interaction, uncertainty, and target library |

Ask for a missing fact when it could change the recommendation. Otherwise
state the assumption beside the affected claim.

## Find records

Search with terms from the case:

```sh
chartcoach catalog labels --contains "<concept>" --format json
chartcoach catalog list --contains "<concept>" --format json
```

Search competing options separately. Records matching both can explain when
to choose one over the other.

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

If ordinary filters return too many matches and an indexed profile is
available, use full-text search:

```sh
chartcoach catalog search \
  --profile <profile-id> \
  --mode fts \
  --limit 10 \
  "<task> <option> <constraint>"
```

## Check the records

Read each selected record, then focus on the sections relevant to the
decision:

```sh
chartcoach catalog read <guideline-entry-id> \
  --source-detail minimal \
  --format markdown
chartcoach catalog cite <guideline-entry-id> --format markdown
```

Discard a record when its chart family, task, audience, data type, or
interaction state differs from the user's case.

`catalog cite` identifies the published sources attached to the guideline.
Inspect a source before attributing an explanation or claim to it. Keep limits
on its applicability beside the affected recommendation.

## Write the answer

For each recommendation or comparison, connect:

```text
decision
  -> fact from the user's case
  -> guideline entry ID, title, and applicable section
  -> tradeoff or remaining uncertainty
  -> source citation
```

Include an exact-read command when another reviewer needs to inspect the full
record.
