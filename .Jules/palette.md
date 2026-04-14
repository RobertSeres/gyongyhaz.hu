## 2025-01-24 - Mobile Menu Accessibility Synchronization
**Learning:** In static sites with mobile menus, failing to synchronize ARIA attributes (`aria-expanded`, `aria-hidden`) and visual icons (hamburger vs. close) when the menu is toggled by different triggers (button vs. links) leads to an inconsistent and inaccessible experience.
**Action:** Use a unified `toggleMenu(forceClose)` function that manages all state transitions (visibility, ARIA attributes, labels, and icon classes) in one place to ensure consistency across all interaction points.
