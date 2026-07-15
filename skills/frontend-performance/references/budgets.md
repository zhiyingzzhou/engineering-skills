# Budgets

Use this reference when establishing or reviewing performance budgets and regression guards.

## Budget Types

- Metric budgets: LCP, INP, CLS, TTFB, first render, route transition, or interaction latency.
- Resource budgets: initial JavaScript, route chunk, CSS, image bytes, font bytes, third-party bytes.
- Count budgets: number of blocking scripts, font files, critical requests, or third-party origins.
- Process budgets: performance review required above a threshold.

## Budget Rules

- Budgets need explicit numbers and scope. Avoid "keep it small".
- Bind budgets to critical routes, route groups, resources, or interactions.
- Track p75 field values where possible and lab values for repeatable CI checks.
- Use warnings for early adoption and blocking gates only when the signal is stable enough.

## CI And Reporting

- Prefer existing tooling: bundle analyzer, Lighthouse CI, custom size checks, WebPageTest, Playwright trace checks, or RUM dashboards.
- Report before/after values and diff context.
- Store budget failures with owner, expected action, and exception process.

## Review Checks

- Is the budget tied to the user path that matters?
- Does the gate catch regressions without blocking unrelated changes?
- Are third-party and media costs visible?
