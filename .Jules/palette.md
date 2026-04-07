## 2025-01-24 - Mobile Navigation Accessibility
**Learning:** For mobile menus in this repository, toggling 'aria-expanded' and 'aria-label' alongside the Font Awesome icon classes (e.g., 'fa-bars' vs 'fa-times') is essential for screen reader users to understand the state of the navigation.
**Action:** Use a centralized JavaScript function (like 'toggleMenu') to synchronize ARIA attributes and visual states across all menu trigger points.

## 2025-01-24 - Visible Focus States
**Learning:** Using 'focus:outline-none' on interactive elements creates accessibility barriers for keyboard users.
**Action:** Always pair 'focus:outline-none' with a clear visible focus indicator, such as 'focus:ring-2 focus:ring-pastel-purple', to maintain keyboard navigation usability.
