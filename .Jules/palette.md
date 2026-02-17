## 2025-05-14 - Accessible Mobile Menu Toggles
**Learning:** For mobile menu implementations in this repository, follow the established pattern of toggling `aria-expanded`, updating `aria-label`, and swapping Font Awesome icon classes (e.g., `fa-bars` to `fa-xmark`) via JavaScript. Use a unified state management function to ensure all trigger points (menu button and links) remain synchronized.
**Action:** Always implement a `setMenuState` or `toggleMenu` function that updates both visual and ARIA states simultaneously.

## 2025-05-14 - UI Interaction Conflict with Timed Popups
**Learning:** Aggressive timed popups (like the newsletter modal appearing after 1s) can interfere with automated UI verification and user interactions. Elements with `opacity-0` but still present in the DOM can intercept clicks if they have a high z-index.
**Action:** When writing Playwright verification scripts for this project, explicitly wait for and close timed popups, or wait for the `hidden` class to ensure they are non-blocking.
