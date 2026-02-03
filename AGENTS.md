# ChartCoach Agent & Engineering Guidelines

This repo is research-grade code intended to survive scrutiny from reviewers and future research engineers.
Optimize for correctness, reproducibility, and clarity over “demo speed”.

## Workflow (Required)

- Plan any non-trivial change (3+ steps, refactors, architectural decisions) in `tasks/todo.md`.
- Track progress by checking items off as you complete them.
- After *any* correction or surprise, record the lesson in `tasks/lessons.md` as a guardrail.
- Don’t mark work done until you can prove it with a command (tests/typecheck/build/UI smoke test as relevant).

## Repo Layout (Orientation)

- `guidelines/`: guideline entries + `catalog.parquet`
- `packages/chartcoach-py/`: Python retrieval/indexing + evaluation harness
- `apps/eval-ui/`: UI for rating retrieved guidelines per scenario
- `evals/`: scenario specs (inputs only; retrieval strategies must not depend on them)

## Commands (Common)

```bash
pnpm dev:site
pnpm dev:eval
pnpm test:eval

uv run ruff format .
uv run ruff check .
uv run ty check .
uv run pytest
```

## Commit Messages

Use Conventional Commits:
`<type>(<scope>): <short summary>`

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `style`.
Keep scopes meaningful (e.g., `retrieval`, `eval-ui`, `catalog`) and avoid over-granularity.

## Retrieval Research Guardrails (Non-Negotiable)

### Scenario-Agnostic Strategies

- Retrieval strategies must be reusable across arbitrary scenarios.
- Do not hardcode logic against concrete scenario IDs/spec fields, “known” benchmark patterns, or dataset-specific labels.
- Strategies must not reference `evals/scenarios/**` or `nogit/**` (those are evaluation artifacts, not model inputs).
- Any “intelligence” beyond deterministic IR operators must come from explicit LLM/DSPy/VLM steps.

### No Hint Files / No Hidden Leakage

- No `hints_*.py` (or equivalents) anywhere in the repo. If found, delete and remove all references.
- Do not embed curated scenario-specific keyword lists in prompts or code.

### Configuration Discipline

- Strategies/pipelines must not read environment variables.
- Centralize env/YAML parsing in `packages/chartcoach-py/src/chartcoach/retrieval/config.py` and inject config via services/registry.
- Log the resolved, secret-safe config snapshot into artifacts so runs are reproducible.

### Tests (Signal > Coverage)

- Prefer contract/invariant tests over branch-coverage tests.
- Avoid monkeypatch-heavy “line-hitting” tests unless they protect a real interface contract.
- If a test doesn’t increase confidence for a paper claim or an engineering contract, delete it.

