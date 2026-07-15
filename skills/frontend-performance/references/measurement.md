# Measurement

Use this reference before diagnosing or changing performance behavior.

## Data Priority

- Field data: use RUM or CrUX-like data to decide user impact and priority when available.
- Lab data: use Lighthouse, WebPageTest, Playwright traces, browser profiles, or local measurements to reproduce and isolate causes.
- Subjective reports: convert to a route, interaction, device class, network, and reproduction path before editing.

## Web Vitals Baseline

- Evaluate Core Web Vitals using the 75th percentile where field data is available.
- Segment mobile and desktop instead of averaging them together.
- Typical good thresholds: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1.
- Treat thresholds as triage guidance, not a substitute for product-specific user impact.

## Record Before And After

- Route, URL, user state, build mode, browser, viewport, device class, CPU/network throttling, cache state, and test location.
- Data source, sample window, percentile, and whether the result is field, lab, or local-only.
- Baseline, change, and confidence.

## Tool Fit

- Use browser Performance panel or traces for long tasks, rendering, scripting, and interaction latency.
- Use bundle analysis for JavaScript cost and dependency shifts.
- Use network waterfalls for critical resource discovery and priority.
- Use monitoring or CI budgets for regression protection.
