## 2025-05-20 - Enhanced Mobile Menu Accessibility
**Learning:** For mobile navigation menus, simply toggling visibility isn't enough for a great UX. Synchronizing 'aria-expanded', 'aria-controls', and dynamic 'aria-label' attributes with the visual state (like icon swaps between 'fa-bars' and 'fa-times') ensures that screen reader users and sighted users receive consistent feedback about the menu's state.
**Action:** Always use a centralized 'toggleMenu' function for mobile navigation that handles both the visual (CSS classes, icons) and semantic (ARIA attributes) state changes in one place.
