# Permissions And Extraction

Use this reference before collecting source, assets, source maps, copy, SVG, fonts, screenshots, or bundle-derived details.

## Authorization Classes

- Owned/internal: company-owned production, staging, internal template, or repository-linked property.
- Explicitly permitted: client-authorized, licensed, or documented permission for reconstruction and asset use.
- Public third-party: visible on the web but not owned or explicitly permitted.
- Unknown: unclear ownership, unclear client authorization, or mixed assets.

## Direct Extraction Rules

- Owned/internal and explicitly permitted targets may use direct extraction within the approved scope.
- Public third-party and unknown targets must not copy source maps, source, bundle internals, exact copy, SVG paths, proprietary images, fonts, brand assets, or private structure.
- For public third-party targets, default to non-copying analysis: layout observations, interaction notes, high-level structure, and independently implemented approximations.
- Source maps and browser-accessible bundles are debugging surfaces, not automatic reuse permission.

## Intake Requirements

- Confirm who owns the target or who granted permission.
- Confirm whether direct reuse of copy, images, SVG, fonts, and code is allowed.
- Confirm whether the result is for testing, migration, recovery, internal parity, or public reuse.
- Record any asset or code category that must be excluded.

## Delivery

- State authorization assumptions.
- State which sources were extracted and which were intentionally not copied.
- Label inferred details and independently recreated elements.
