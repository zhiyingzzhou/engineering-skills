# Governance

Use this reference for ownership, package changes, deprecation, migration, duplication, and design-system review gates.

## Ownership

- Every token group and reusable component needs an owner or review path.
- New primitives require a clear consumer set and a reason existing primitives cannot cover the need.
- Product-specific components should not move into the foundation layer without removing business coupling.

## Change Types

- Patch: internal implementation or docs change with no consumer contract change.
- Minor: additive token, prop, variant, state, or documented behavior.
- Deprecation: old contract remains but warns and has a replacement.
- Major: removal, renamed token, changed defaults, changed DOM/focus behavior, or incompatible styling API.

## Migration

- Breaking changes need a migration path, codemod or checklist when feasible, and affected consumer inventory.
- Deprecated tokens and props should include replacement names and removal timing.
- Duplicate components need a convergence plan and an owner.

## Review Gates

- Token output builds for every target theme/platform.
- Stories and docs cover the changed state matrix.
- Accessibility behavior remains owned by the component or explicitly delegated.
- Consumer migrations are completed or tracked with a clear follow-up.
