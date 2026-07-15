# Test Strategy

Use this reference when choosing a test layer or reviewing coverage.

## Layer Choice

- Unit: pure logic, validation rules, reducers, formatting, transforms, and permission decisions.
- DOM/component: rendered UI, accessible names, user interactions, state changes, errors, loading, and component integration.
- Storybook or equivalent: reusable component states, interaction demos, accessibility checks, and visual review.
- Integration: routing, providers, data loading, caching, auth boundaries, and multi-component flows.
- E2E/browser: critical user journeys, real browser behavior, permissions, downloads, cross-page flows, and high-risk regressions.
- Visual snapshots: spacing, layout, theme, density, responsive states, and screenshot parity.

## Principles

- Choose the cheapest layer that can observe the real risk.
- Avoid duplicating the same assertion at every layer.
- Mock only boundaries that are not the responsibility of the chosen layer.
- Keep each test focused on one user-relevant behavior.
- Include failure, empty, loading, permission, and recovery paths when they are part of the risk.

## Review Checks

- Does the test fail for the bug it is meant to prevent?
- Is the assertion about user-visible behavior or a stable public contract?
- Is the setup deterministic and owned by the test?
- Is the command cost appropriate for the protected risk?
