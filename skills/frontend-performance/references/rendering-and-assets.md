# Rendering And Assets

Use this reference for critical rendering path, images, fonts, scripts, third-party code, and resource loading.

## LCP Path

- Identify the LCP element and whether it is text, image, video poster, or background-like content.
- Check time to first byte, resource discovery, resource load delay, resource load duration, and element render delay.
- Do not lazy-load the likely LCP image.
- Use preload or fetch priority only for truly critical resources.

## JavaScript And Rendering

- Keep non-critical JavaScript out of the initial path.
- Split by route, interaction, or capability, not arbitrary file boundaries.
- Watch hydration cost, long tasks, expensive event handlers, layout thrashing, and unnecessary re-renders.
- Prefer reducing work over hiding it behind more loading UI.

## Images And Fonts

- Serve images close to rendered size and density.
- Provide stable width/height or aspect-ratio to avoid layout shifts.
- Choose font loading behavior intentionally and avoid long invisible text.
- Remove unused font weights, scripts, and third-party tags from critical routes.

## Third Parties

- Treat third-party scripts as budgeted dependencies.
- Load non-critical third parties after the main task path.
- Document owner, purpose, cost, and removal criteria for expensive third-party code.
