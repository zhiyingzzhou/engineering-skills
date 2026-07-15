# Forward Tests

Use these prompts when validating this skill. Pass the skill and task to a fresh agent without revealing the expected fixes.

## Positive Prompts

1. "Use $frontend-design-system to review a Button API with many boolean props, inconsistent loading and disabled states, and missing Storybook coverage."
2. "Use $frontend-design-system to redesign a token model where color values are copied directly into components across light and dark themes."
3. "Use $frontend-design-system to plan a deprecation path for two duplicate modal components with different focus behavior."

## Misfire Prompt

- "Use the best frontend skill to fix mobile overflow and image cropping on a marketing page."

Expected behavior: choose `frontend-responsive-layout`, not this skill, unless reusable layout primitives or token contracts are the primary issue.

## Acceptance

- The agent distinguishes token layers and component layers.
- The agent calls out migration, docs, tests, and accessibility ownership.
- The agent avoids adding one-off API surface without governance.
