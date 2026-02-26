## 2026-02-26 - Accessible Mobile Menu Pattern
**Learning:** For mobile menu implementations in this repository, follow the established pattern of toggling `aria-expanded`, setting `aria-controls` to the menu container's ID, updating `aria-label`, and swapping Font Awesome icon classes (e.g., `fa-bars` to `fa-xmark`) via JavaScript.
**Action:** Use a unified state management function for UI components with multiple trigger points (e.g., mobile menu toggle and links) to ensure ARIA attributes and visual states remain synchronized.
