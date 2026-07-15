# Autofill

Use this reference for sign-in, sign-up, password change, one-time code, checkout, address, payment, and profile forms.

## General Rules

- Use stable field names, labels, order, and grouping so browsers and password managers can recognize the form.
- Provide correct `autocomplete` tokens for common fields.
- Do not block paste, autofill, password managers, or one-time-code insertion without a security requirement.
- Do not rewrite field values before submit in a way that breaks browser or password-manager detection.

## Authentication

- Use `username` for the account identifier.
- Use `current-password` for sign-in and `new-password` for account creation or password reset.
- Use `one-time-code` for OTP fields where supported.
- Keep password visibility toggles keyboard-accessible and stateful.

## Identity And Contact

- Common tokens: `name`, `given-name`, `family-name`, `email`, `tel`, `organization`.
- Do not split names unless the backend or locale requirement truly needs it.
- Phone and postal formats vary by locale; avoid overly strict client patterns.

## Address And Payment

- Common address tokens: `street-address`, `address-line1`, `address-line2`, `address-level1`, `address-level2`, `postal-code`, `country`.
- Use `shipping` and `billing` section prefixes when both appear in one flow.
- Payment forms should preserve browser payment/autofill compatibility and avoid unnecessary custom entry widgets.

## Verification

- Test at least one modern browser autofill path when fields are changed.
- Record unverified password manager, payment autofill, address autofill, and OTP behavior.
