---
name: frontend-testing
description: Use this skill for frontend test strategy, implementation, remediation, or review when the task involves unit tests, DOM/component tests, integration tests, Playwright or browser E2E, Storybook tests, accessibility checks, visual snapshots, stable locators, async assertions, test isolation, mocking, fixtures, or flaky test diagnosis. Do not use it for performance profiling, design-token modeling, pure layout fixes, or form UX unless test coverage is the primary concern.
---

# Frontend Testing Skill

## Core Workflow

1. Identify the highest-risk behavior and choose the cheapest test layer that can observe it honestly.
2. Test user-visible behavior, not implementation details, unless the task is pure logic.
3. Prefer semantic locators and web-first assertions; avoid class selectors, DOM-shape coupling, and fixed sleeps.
4. Isolate data, storage, network, time, and external dependencies enough to make failures actionable.
5. Run the smallest sufficient test set first, then broaden only when the risk surface justifies it.

## Read References By Task

Always read:

- `references/test-strategy.md`
- `references/dom-testing.md`

Read only when relevant:

- `references/e2e-best-practices.md` for Playwright, browser automation, locators, isolation, network, visual snapshots, and flaky tests.
- `references/review-checklist.md` for PR reviews, coverage audits, or refactor risk analysis.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Identify the behavior under risk and whether it is logic, rendering, interaction, routing, network, auth, permissions, browser behavior, or visual/a11y regression.
- Identify the existing test tools, commands, helpers, fixtures, mocks, data seeding, and CI constraints.
- Identify current flaky symptoms: selector failure, timing, shared state, network, animation, environment, or product behavior.
- Identify whether coverage should be unit, DOM, integration, Storybook, accessibility, visual, or E2E.

## Implementation Rules

- Use Testing Library role/name queries first, then label/text, and only then stable test IDs.
- Use `getBy*`, `queryBy*`, and `findBy*` intentionally based on synchronous presence, absence, or async appearance.
- Use user-level interactions and assertions on visible results, accessible state, URL changes, network outcomes, or persisted data.
- In Playwright, use locators, auto-waiting, web-first assertions, per-test isolation, and controlled network/data setup.
- Treat visual and accessibility checks as complementary layers, not replacements for behavior tests.

## Delivery Requirements

- State which test layer was added or changed and why that layer is sufficient.
- Report commands run, failures observed, and any suspected environment-only issues.
- Call out untested paths, intentionally mocked boundaries, and remaining flaky risk.
