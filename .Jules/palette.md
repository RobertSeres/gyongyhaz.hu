## 2025-05-14 - Mobile Menu Accessibility & Unified State
**Learning:** For mobile menus in this repository, simple class toggling is insufficient for accessibility. A unified state management function (`toggleMenu`) is needed to synchronize `aria-expanded` on the trigger, `aria-hidden` on the container, dynamic `aria-label` updates, and Font Awesome icon class swaps (`fa-bars` vs `fa-xmark`).
**Action:** Always implement a dedicated toggle function for menus that manages both visual (icons, classes) and programmatic (ARIA) states simultaneously to prevent desynchronization.

## 2025-05-14 - Focus Visibility Pattern
**Learning:** Standard focus outlines can be visually jarring or suppressed by reset styles. Using `focus-visible:ring-2 focus-visible:ring-pastel-purple rounded-sm` provides a high-contrast, theme-consistent indicator for keyboard users while remaining invisible to mouse users.
**Action:** Use this specific Tailwind utility combination for all interactive elements to ensure WCAG 2.1 compliance for focus visibility in this project.
