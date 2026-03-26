## 2025-05-15 - [Mobile Menu Accessibility Refactor]
**Learning:** For mobile menus with multiple triggers (main button and individual links), a unified `toggleMenu` function is essential to keep ARIA attributes (`aria-expanded`, `aria-label`), icon states, and visibility in sync. Relying on simple `classList.toggle` on individual elements leads to inconsistent accessibility states.
**Action:** Always implement a single state management function for UI components that have more than one interaction point to ensure screen reader accuracy and visual consistency.
