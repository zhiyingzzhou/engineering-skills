---
name: frontend-design-system
description: Use this skill for frontend design-system work involving design token modeling, token pipelines, component API contracts, state matrices, Storybook or equivalent documentation, component governance, deprecation, migration, and reusable accessibility ownership. Do not use it for one-off page layout, form-flow UX, performance profiling, or E2E test design unless the design-system contract is the primary concern.
---

# Frontend Design System Skill

## Core Workflow

1. Map the system layers before editing: source tokens, semantic tokens, component tokens, primitives, composed components, and product-specific usage.
2. Stabilize contracts around intent, state, slots, events, and accessibility responsibilities instead of temporary visual tweaks.
3. Document every meaningful variant and state with executable examples, not stale prose.
4. Govern change deliberately: detect duplicates, avoid business leakage into primitives, version breaking changes, and migrate affected consumers.
5. Validate with the strongest available checks: type tests, stories, interaction tests, accessibility checks, visual review, build, and consumer migration tests.

## Read References By Task

Always read:

- `references/token-modeling.md`
- `references/component-contracts.md`

Read only when relevant:

- `references/storybook-docs.md` for Storybook, docs, interaction tests, accessibility tests, and visual review.
- `references/governance.md` for ownership, semver, deprecation, migration, or component consolidation.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Identify the token source of truth, output targets, theme mechanism, and naming conventions.
- Identify which components are primitives, composed components, or product/business components.
- Identify current documentation, Storybook, test, build, and package release commands.
- Identify whether the change is additive, breaking, deprecated, or migration-only.

## Implementation Rules

- Prefer semantic tokens for product meaning and component tokens only for real local mapping needs.
- Model component APIs as stable contracts: variants, sizes, slots, state, events, controlled/uncontrolled behavior, refs, and accessibility ownership.
- Do not add one-off props, tokens, or variants for a single page without a governance decision.
- Keep docs, tests, and migration notes synchronized with the changed contract.
- Do not keep duplicate components or token aliases indefinitely; record a deprecation or consolidation path.

## Delivery Requirements

- State which tokens, component contracts, docs, tests, or migration paths changed.
- State whether the change is breaking, additive, deprecated, or internal-only.
- Report validation commands and any uncovered consumers, states, or theme outputs.
