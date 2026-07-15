---
name: frontend-performance
description: Use this skill for frontend performance measurement, diagnosis, optimization, or review when the task involves Core Web Vitals, LCP, INP, CLS, field data, lab data, critical rendering path, resource priority, JavaScript cost, code splitting, third-party scripts, performance budgets, profiling, or regression guards. Do not use it for generic accessibility, responsive layout design, form UX, or test coverage unless performance is the primary concern.
---

# Frontend Performance Skill

## Core Workflow

1. Measure before editing. Record route, device class, network, browser, build mode, data source, and reproduction steps.
2. Prefer field data for prioritization. Use lab tools to reproduce, isolate, and compare under controlled conditions.
3. Classify the issue as loading, interaction, layout stability, rendering, JavaScript execution, network, server, or third-party cost.
4. Fix the biggest user-visible bottleneck first and avoid trading maintainability for cosmetic score gains.
5. Add a regression guard when the repository has an appropriate build, budget, analysis, monitoring, or CI surface.

## Read References By Task

Always read:

- `references/measurement.md`
- `references/common-regressions.md`

Read only when relevant:

- `references/rendering-and-assets.md` for critical rendering path, images, fonts, script loading, third-party code, and resource priority.
- `references/budgets.md` for budget design, CI gates, bundle analysis, or performance review thresholds.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Identify the affected page, route, interaction, user segment, and business-critical path.
- Identify whether the evidence is RUM, CrUX, synthetic lab data, profiler traces, bundle analysis, or subjective feedback.
- Identify existing build, analyze, Lighthouse, WebPageTest, profiler, monitoring, and test commands.
- Identify current baselines, budgets, device assumptions, and release constraints.

## Implementation Rules

- Treat LCP, INP, and CLS as separate systems; do not assume a bundle-size change fixes all of them.
- Compare like with like: same route, build mode, device class, network, viewport, and cache state.
- Use p75 mobile and desktop field data where available; use lab data to explain and verify hypotheses.
- Prioritize late-discovered LCP resources, long tasks and excessive re-rendering for INP, and missing dimensions or late insertion for CLS.
- Keep performance budgets specific to routes, resources, interactions, or page types.

## Delivery Requirements

- State the metric, route, data source, baseline, change, and validation method.
- Report commands run and whether results are field data, lab data, or local profiling only.
- Record untested devices, routes, traffic segments, third-party dependencies, or monitoring gaps.
