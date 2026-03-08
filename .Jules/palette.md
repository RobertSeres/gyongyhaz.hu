## 2025-05-14 - Unified Mobile Menu State Management

**Learning:** When a UI component has multiple trigger points (e.g., a menu toggle button and internal navigation links), manually updating classes in multiple places leads to state desynchronization (e.g., the menu closes but the icon stays as an "X").

**Action:** Implement a unified `toggleMenu(forceClose)` function that handles all visual (icon classes, visibility) and accessibility (aria-expanded, aria-label) updates in one place. Use this function for both the main toggle and closing events.
