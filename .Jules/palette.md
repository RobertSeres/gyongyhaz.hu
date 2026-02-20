## 2026-02-20 - Accessibility Polish for Interactive Components

**Learning:** Static sites often neglect ARIA states for dynamic elements like mobile menus and modals, leading to a poor experience for screen reader users. Proper use of `role="dialog"`, `aria-modal`, `aria-expanded`, and `aria-hidden` is essential. Swapping icons (bars to xmark) also provides clear visual feedback for sighted users.

**Action:** Always implement a unified toggle function for mobile menus that synchronizes ARIA attributes and visual states. Ensure modals have correct roles and manage focus/visibility via ARIA.
