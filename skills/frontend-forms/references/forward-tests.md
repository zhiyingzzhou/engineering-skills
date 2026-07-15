# Forward Tests

Use these prompts when validating this skill. Pass the skill and task to a fresh agent without revealing the expected fixes.

## Positive Prompts

1. "Use $frontend-forms to review a sign-in form with username, password, OTP, remember-me, server errors, and a password visibility toggle."
2. "Use $frontend-forms to improve a checkout address and payment form that has weak labels, poor autofill, and duplicate-submit bugs."
3. "Use $frontend-forms to design validation timing and error focus for a profile edit form with client and server validation."

## Misfire Prompt

- "Use the best frontend skill to repair a custom menu button with wrong ARIA roles and broken arrow-key navigation."

Expected behavior: choose `frontend-accessibility`, not this skill, unless the menu is part of a form and form behavior is the primary issue.

## Acceptance

- The agent maps the field contract before changing validation.
- The agent preserves autofill and password-manager behavior.
- The agent reports unverified browser, server, locale, and privacy-sensitive paths.
