## 2025-01-24 - Mobile Menu Accessibility and Feedback
**Learning:** For mobile menus in this repository, simply toggling visibility is insufficient for a good UX. Screen readers need `aria-expanded` and `aria-controls` on the trigger, and all users benefit from a clear visual state change in the icon (e.g., hamburger to X) and updated `aria-label` to indicate the next action.
**Action:** Always use a unified state management function for mobile menus to keep ARIA attributes, labels, and icons in sync across all trigger points (menu button and internal links).
