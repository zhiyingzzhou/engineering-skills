# E2E Best Practices

Use this reference for Playwright or equivalent browser automation, locators, isolation, network behavior, screenshots, and flaky tests.

## Locators And Assertions

- Prefer role/name locators and stable user-facing selectors.
- Use test IDs only when semantics cannot identify the target.
- Avoid brittle CSS and XPath paths.
- Use web-first assertions so the test waits for the expected UI condition.
- Avoid fixed sleeps; wait for state, navigation, response, or visible result.

## Isolation

- Each test should own its user, storage state, data seed, network assumptions, and cleanup.
- Do not rely on test order.
- Avoid shared mutable backend state unless it is explicitly reset.
- Mock or stub third-party services when the test is not meant to verify the third party.

## Network And Data

- Decide whether the test verifies real integration or UI behavior with controlled data.
- Use route mocking for deterministic UI states: loading, success, empty, error, permission denied, and slow network.
- Keep authentication setup explicit and fast.

## Visual And Accessibility Layers

- Use screenshots for visual regressions where layout/theme parity matters.
- Freeze animations, dates, random data, and network content for visual snapshots.
- Use accessibility scans as a fast safety net, but keep manual/semantic checks for behavior not detectable by tooling.

## Flaky Diagnosis

- Classify failures as selector, waiting, shared data, network, animation, browser, environment, or product regression.
- Remove the cause before increasing retries.
