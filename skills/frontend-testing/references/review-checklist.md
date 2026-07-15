# Testing Review Checklist

Use this reference for PR reviews, test gap audits, and flaky test triage.

## Start

- Identify changed behavior and highest-risk failure modes.
- Identify existing test layers, commands, fixtures, helpers, mocks, and CI cost.
- Identify which paths are critical, high-traffic, revenue-sensitive, security-sensitive, or historically flaky.

## Coverage

- Happy path, error path, empty state, loading state, permission state, and recovery path are covered where relevant.
- DOM tests query by user-observable semantics.
- E2E tests cover only critical browser journeys or integration risks.
- Visual and accessibility checks are present when UI regressions are likely.
- Tests avoid implementation details unless testing pure logic.

## Stability

- No fixed sleeps for normal UI waiting.
- Data setup and cleanup are owned by each test or fixture.
- External services are controlled unless the test intentionally covers them.
- Randomness, time, animation, and network are stable where visual or timing assertions matter.

## Delivery

- State which commands were run and what failed.
- State remaining untested risks and why they were left out.
- Distinguish product failures from environment or data failures.
