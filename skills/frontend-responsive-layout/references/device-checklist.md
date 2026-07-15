# Device Checklist

Use this reference for touch devices, orientation changes, safe areas, virtual keyboards, zoom, and input modality.

## Viewport Matrix

- Minimum supported narrow width.
- Common mobile portrait and landscape.
- Tablet or intermediate width when layout changes there.
- Standard desktop.
- Wide desktop where line length and max width matter.

## Interaction Matrix

- Touch targets are large enough and not crowded.
- Pointer and hover assumptions are guarded with media features where needed.
- Focus states remain usable for keyboard and hybrid devices.
- Virtual keyboard does not hide active fields, submit buttons, or blocking errors.
- Orientation change does not leave overlays, sticky elements, or measured heights stale.

## Modern Viewport Concerns

- Use safe-area insets when fixed elements touch device edges.
- Use dynamic viewport units when browser chrome changes height.
- Avoid fixed bottom controls that cover content or form fields.
- Respect reduced motion when layout changes animate.

## Delivery

- State which sizes and input modes were tested.
- Separate simulated device checks from real-device checks.
- Record untested zoom, orientation, safe area, virtual keyboard, and touch scenarios.
