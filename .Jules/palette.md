# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-05-14 - Mobile Menu Accessibility & Interaction Pattern
**Learning:** Mobile menus need more than just a `hidden` toggle. They require `aria-expanded` and `aria-controls` for screen readers, and visual feedback like icon swapping (e.g., hamburger to X) for sighted users. Using a unified `toggleMenu` function ensures these states remain synchronized.
**Action:** When implementing or fixing mobile menus, always use a unified state management function to update ARIA attributes, labels, and icon classes simultaneously.
