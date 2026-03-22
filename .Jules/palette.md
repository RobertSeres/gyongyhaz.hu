## 2025-05-14 - Improve Mobile Menu Accessibility and Visual State
**Learning:** Mobile menus often lack proper ARIA attributes and visual feedback for the toggle state. Using a unified state management function ensures that `aria-expanded`, `aria-label`, and icon classes stay in sync across multiple trigger points (toggle button and internal links).
**Action:** Always implement `aria-expanded`, `aria-controls`, and dynamic `aria-label` for mobile toggles, and use `focus-visible` for better keyboard navigation.
