# Forward Tests

Use these prompts when validating this skill. Pass the skill and task to a fresh agent without revealing the expected fixes.

## Positive Prompts

1. "Use $frontend-responsive-layout to fix a pricing grid that overflows at 390px and leaves cards too wide inside a sidebar."
2. "Use $frontend-responsive-layout to repair responsive images where the hero crop loses the product on mobile and downloads oversized files."
3. "Use $frontend-responsive-layout to review a mobile form page where the fixed footer covers fields when the virtual keyboard opens."

## Misfire Prompt

- "Use the best frontend skill to diagnose slow LCP caused by a late hero image request."

Expected behavior: choose `frontend-performance`, not this skill, unless the task centers layout or responsive media constraints.

## Acceptance

- The agent identifies viewport vs container causes.
- The agent checks overflow, media stability, and touch/keyboard constraints.
- The agent reports exact viewport and device-simulation coverage.
