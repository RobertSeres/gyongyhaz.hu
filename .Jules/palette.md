## 2025-05-14 - Mobile Menu Accessibility & Interaction Polish
**Learning:** Consolidating mobile menu logic into a single toggle function ensures that ARIA attributes (aria-expanded, aria-label) and visual states (icon swapping) remain synchronized even when the menu is closed via link clicks rather than the toggle button.
**Action:** Always use a unified state management function for UI components that have multiple entry points for state changes (e.g., toggles that can be closed by clicking backdrop or links).
