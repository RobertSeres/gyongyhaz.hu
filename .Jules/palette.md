## 2026-03-28 - Accessible Mobile Menu Pattern
**Learning:** For mobile menu implementations in this repository, follow the established pattern of toggling `aria-expanded`, setting `aria-controls` to the menu container's ID, updating `aria-label`, and swapping Font Awesome icon classes (e.g., `fa-bars` to 'fa-times') via JavaScript.
**Action:** Use a unified state management function for UI components with multiple trigger points (e.g., mobile menu toggle and links) to ensure ARIA attributes and visual states remain synchronized.

## 2026-03-28 - Keyboard Visibility for Icon Buttons
**Learning:** For keyboard accessibility on this project, the standard focus indicator is `focus-visible:ring-2 focus-visible:ring-pastel-purple rounded-sm`.
**Action:** Always replace `focus:outline-none` with this pattern on interactive elements to ensure they are navigable via keyboard.
