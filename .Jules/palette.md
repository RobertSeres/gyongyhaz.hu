# Palette's Journal - Gyöngy Ház

## 2024-05-23 - Accessible Static Overlays and Focus Management
**Learning:** In static single-page sites built with Tailwind, accessibility regressions often occur due to `focus:outline-none` and desynchronized ARIA states. Replacing global focus suppression with `focus-visible:ring-2` provides a clean UI for mouse users while ensuring keyboard navigability. Additionally, overlays that use CSS transitions (like transforms) for visibility must have their `aria-hidden` attribute toggled manually in JavaScript to remain accurate in the accessibility tree.
**Action:** Audit all interactive elements for focus indicators and use `focus-visible`. Implement centralized JavaScript functions to toggle both CSS visibility classes and ARIA attributes (hidden/expanded) for all menus and modals.
