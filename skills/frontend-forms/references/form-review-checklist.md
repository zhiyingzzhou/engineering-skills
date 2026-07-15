# Form Review Checklist

Use this reference for PR reviews, page audits, and release-risk summaries.

## Start

- List fields, groups, required status, dependencies, and submit destination.
- Identify client rules, server rules, normalization, and persistence.
- Identify whether authentication, payment, address, personal data, or locale-specific formats are involved.
- Identify available unit, DOM, E2E, browser, and manual validation commands.

## Minimum Review

- Labels, help, requirements, errors, and grouped controls are associated correctly.
- Keyboard flow, submit, reset/cancel, and recovery are predictable.
- Success, field errors, server errors, network errors, loading, and duplicate submit states are covered.
- Autofill, password manager, OTP, address, and payment behavior are not broken where relevant.
- Sensitive values are not exposed in logs, URLs, analytics, or unnecessary persisted state.

## Delivery

- State changed validation timing, field contracts, error behavior, autofill tokens, and privacy handling.
- Report verified success/failure paths and unverified browser/platform paths.
- Do not claim password-manager or autofill compatibility without a real check or explicit caveat.
