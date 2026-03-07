# Palette's UX Journal

## 2026-03-07 - Enhanced Mobile Navigation and Modal Accessibility
**Learning:** For components with multiple trigger points (like a mobile menu toggle and internal navigation links), a unified state management function (e.g., `toggleMenu`) is essential to ensure that ARIA attributes (`aria-expanded`, `aria-label`), icon classes, and visibility classes (`hidden`) remain perfectly synchronized. Additionally, when using CSS transitions for visibility (like opacity or transforms), manually toggling `aria-hidden` is critical for screen reader accuracy as the element may remain in the accessibility tree even when visually "hidden".
**Action:** Use a single source of truth function for UI state transitions and always pair visual visibility changes with `aria-hidden` or `aria-expanded` updates.
