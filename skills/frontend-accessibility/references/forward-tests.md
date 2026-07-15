# Forward Tests

Use these prompts when validating this skill. Pass the skill and task to a fresh agent without revealing the expected fixes.

## Positive Prompts

1. "Use $frontend-accessibility to review a React dialog that opens from a settings button, traps focus inconsistently, and does not restore focus on close."
2. "Use $frontend-accessibility to fix a tab component built from `div` elements where arrow keys do not work and selected state is visual-only."
3. "Use $frontend-accessibility to audit a dashboard page for heading order, landmark structure, icon-only buttons, and keyboard operation."

## Misfire Prompt

- "Use the best frontend skill to improve checkout field validation copy, address autofill, and duplicate submit handling."

Expected behavior: choose `frontend-forms`, not this skill, unless the task specifically centers accessibility behavior.

## Acceptance

- The agent reads core references and only reads ARIA or assistive technology references when relevant.
- The agent prefers native HTML and explains when ARIA is required.
- The agent reports validation gaps instead of overstating accessibility confidence.
