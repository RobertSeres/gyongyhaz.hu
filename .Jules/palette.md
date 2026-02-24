## 2025-05-15 - [Unified State Management for Mobile Menu]
**Learning:** For mobile menus that can be closed by multiple elements (toggle button, overlay, menu links), using a unified state management function ensures that ARIA attributes (aria-expanded), icons (fa-bars/fa-xmark), and accessibility labels remain synchronized across all triggers.
**Action:** Always implement a dedicated `toggleMenu(forceState)` or `updateMenuUI()` function instead of scattered class toggles.

## 2025-05-15 - [A11y for CSS-only Hidden Elements]
**Learning:** Elements hidden with Tailwind's `opacity-0` or `pointer-events-none` for transition effects remain in the accessibility tree and can be "seen" by screen readers.
**Action:** Manually toggle the `aria-hidden` attribute or use the `hidden` class in conjunction with transitions to ensure non-visible elements are correctly ignored by assistive technology.
