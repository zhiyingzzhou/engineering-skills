# Common Regressions

Use this reference to choose likely diagnostic paths after measurement.

## LCP

- Server or HTML response is slow.
- LCP resource is discovered late through JavaScript, CSS, or client rendering.
- LCP resource is downloaded late because of priority, competing resources, or lazy loading.
- Element render is delayed by hydration, render-blocking CSS, font loading, or main-thread work.

## INP

- Event handler does long synchronous work.
- Interaction triggers broad re-render, heavy layout, expensive selectors, or large state updates.
- Main thread is busy with analytics, hydration, third-party code, or background work.
- Visual feedback waits for data or non-critical work.

## CLS

- Images, embeds, ads, charts, or video lack stable dimensions.
- Late banners, errors, recommendations, consent prompts, or injected content push layout.
- Font swap changes text metrics.
- Skeletons or placeholders do not match final content size.

## Bundle And Dependency

- Low-frequency features enter the initial chunk.
- Dynamic import boundaries are too late or too broad.
- A small UI change imports a large library.
- Polyfills or legacy bundles are served to modern browsers unnecessarily.

## Fix Order

1. Confirm the metric and affected user path.
2. Find the largest time, byte, or layout-shift contributor.
3. Reduce critical work or reserve stable space.
4. Add a guard if the repository has a reliable enforcement surface.
