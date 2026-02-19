## 2026-02-19 - ARIA Synchronization in Static Projects
**Learning:** In static HTML/JS projects using Tailwind, ARIA attributes (like `aria-expanded`, `aria-hidden`) and icon classes must be explicitly toggled in JavaScript alongside visual state changes (like the `hidden` class) to ensure the accessibility tree remains accurate for screen readers.
**Action:** Use unified JavaScript functions to toggle UI components (like menus or modals) that handle both CSS class changes and ARIA attribute updates simultaneously.
