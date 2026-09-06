---
name: contribute
description: Draft a chartcoach catalog issue when searches expose missing or misleading guidance.
---

# chartcoach Contribute

Draft a catalog issue when searches reveal a missing topic, unclear wording,
weak labels, duplicate records, or unsupported source claims. Keep the draft
local until a human approves issue creation. Read `core` first so
`CHARTCOACH_SOURCE` is set before running searches and reading referenced
guidelines.

## Confirm the catalog problem

Record:

| Field             | Evidence                                                                |
| ----------------- | ----------------------------------------------------------------------- |
| User task         | The critique, recommendation, discussion, or search question            |
| Searches          | Words, labels, roles, SQL, and indexed searches tried                   |
| Result            | Missing, partial, surprising, duplicate, or weakly sourced record       |
| Diagnosis         | How record wording, labels, relationships, or sources caused the result |
| Related entry IDs | Records that partially match, conflict, duplicate, or need revision     |

Read and cite every named record:

```sh
chartcoach catalog read <guideline-entry-id> --source-detail minimal
chartcoach catalog cite <guideline-entry-id>
```

Report crashes, installation errors, cache errors, and storage errors at
`https://github.com/chartcoach/chartcoach/issues`. File a catalog issue when
record wording or labels caused a false match.

## Choose one change

- Add a missing topic.
- Rewrite unclear guidance.
- Add, remove, or replace labels.
- Split duplicate ideas or merge duplicate records.
- Add a relationship between records.
- Repair or add source citations.
- Add a section role or label family to the manifest.

Choose one primary change so the issue gives the catalog maintainer a clear
action.

## Draft the issue

```md
## Summary

<Catalog problem and the recurring case where it appeared.>

## Evidence from use

- Task:
- Searches:
- Result:
- Content diagnosis:

## Related guidelines

- `<guideline-entry-id>`: `<title>`
  - Relevant section:
  - Exact-read command:
  - Citation:
  - Why it applies or falls short:

## Suggested change

<One concrete wording, label, relationship, or source change.>

## Before publication

- [ ] Remove private user data and local paths.
- [ ] Check every guideline entry ID with `catalog read`.
- [ ] Identify the cited sources with `catalog cite`, then inspect those sources
      before judging whether a claim is supported.
- [ ] Name anything the catalog maintainer still needs to verify.
```

For a missing topic, write `None found` and keep the failed search terms.

## Hand off for approval

Return the proposed title, Markdown body, and a prefilled issue URL:

```python
from urllib.parse import urlencode

title = "[Missing topic]: <short title>"
body = """## Summary

<reviewed issue body>
"""
url = "https://github.com/chartcoach/catalog/issues/new?" + urlencode(
    {"title": title, "body": body}
)
print(url)
```

Create the issue through `gh` or another GitHub integration only after a human
approves the reviewed title and body.
