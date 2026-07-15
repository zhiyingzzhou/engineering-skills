# Forward Tests

Use these prompts when validating this skill. Pass the skill and task to a fresh agent without revealing the expected fixes.

## Positive Prompts

1. "Use $frontend-performance to diagnose poor LCP on a product page where the hero image appears late and Lighthouse shows high render delay."
2. "Use $frontend-performance to review a dashboard interaction with bad INP after filtering a large table."
3. "Use $frontend-performance to design performance budgets for a marketing route, app shell, and third-party analytics scripts."

## Misfire Prompt

- "Use the best frontend skill to fix card overflow, long filenames, and image cropping on mobile."

Expected behavior: choose `frontend-responsive-layout`, not this skill, unless the task centers Web Vitals or measured performance impact.

## Acceptance

- The agent records data source, baseline, route, device, and validation conditions.
- The agent separates field data from lab data.
- The agent ties fixes to LCP, INP, CLS, resource cost, or a named budget.
