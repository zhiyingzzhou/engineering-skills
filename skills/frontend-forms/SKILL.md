---
name: frontend-forms
description: Use this skill for frontend form design, implementation, remediation, or review when the task involves native controls, labels, descriptions, validation timing, field errors, error summaries, focus on submit, autofill, password managers, OTP, sign-in, checkout, address, payment, profile editing, privacy, or internationalized input. Do not use it for complex ARIA widgets, responsive page layout, performance profiling, or design-system API governance unless form behavior is the primary concern.
---

# Frontend Forms Skill

## Core Workflow

1. Map the form contract: fields, groups, required/optional status, defaults, dependencies, submission target, success, client errors, server errors, and recovery paths.
2. Choose native controls and browser capabilities first: correct `type`, `inputmode`, `autocomplete`, submit semantics, fieldsets, and labels.
3. Design validation timing to reduce interruption: hint before input, validate after meaningful interaction, summarize blocking errors on submit.
4. Preserve user work across failures and prevent duplicate submissions without breaking autofill or password managers.
5. Verify success, field errors, server errors, autofill/password manager behavior, keyboard flow, and focus recovery.

## Read References By Task

Always read:

- `references/controls-and-labels.md`
- `references/validation-and-errors.md`

Read only when relevant:

- `references/autofill.md` for sign-in, sign-up, password change, OTP, address, payment, and browser autofill behavior.
- `references/security-and-i18n.md` for authentication, checkout, privacy, international addresses, names, phone numbers, or localized validation.
- `references/form-review-checklist.md` for PR, page, or flow reviews.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Identify the user goal, submission API, backend validation contract, and post-submit destination.
- Identify existing form components, validation libraries, error patterns, and field wrappers.
- Identify whether the task includes authentication, payment, address, personal data, or regulated data.
- Identify available unit, DOM, E2E, preview, and manual browser validation commands.

## Implementation Rules

- Every field needs a programmatic label; placeholders are hints, not labels.
- Associate help, constraints, and errors with fields through real relationships.
- Use `fieldset` and `legend` for related radio/checkbox groups and multi-field concepts.
- Use `aria-invalid` only while the current field value is invalid, and keep error text discoverable.
- Focus the first actionable error or error summary after a failed submit.
- Never clear valid user input after failed validation unless security requires it, and explain that exception.

## Delivery Requirements

- State which field contracts, validation timing, error semantics, autofill tokens, or privacy rules changed.
- Report validation commands and manual browser checks performed.
- Call out unverified password manager, autofill, OTP, payment, address, server-error, or locale paths.
