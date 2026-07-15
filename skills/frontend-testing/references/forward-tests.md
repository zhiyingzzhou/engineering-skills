# Forward Tests

Use these prompts when validating this skill. Pass the skill and task to a fresh agent without revealing the expected fixes.

## Positive Prompts

1. "Use $frontend-testing to add coverage for a component that loads results asynchronously, shows empty and error states, and supports keyboard selection."
2. "Use $frontend-testing to fix a flaky Playwright checkout test that uses CSS selectors, shared data, and fixed waits."
3. "Use $frontend-testing to design test coverage for a reusable modal component across DOM, Storybook, accessibility, visual, and E2E layers."

## Misfire Prompt

- "Use the best frontend skill to reduce a page's JavaScript cost and improve INP."

Expected behavior: choose `frontend-performance`, not this skill, unless the task is specifically about performance test coverage.

## Acceptance

- The agent chooses a test layer based on risk.
- The agent uses semantic locators and async queries correctly.
- The agent addresses isolation and flaky root causes before retries.
