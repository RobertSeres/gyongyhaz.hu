## 2025-05-22 - Improved Landmark and Modal Accessibility
**Learning:** Single-page Tailwind sites often lack basic accessibility landmarks and proper state management for interactive elements like mobile menus and modals. Timed popups can interfere with background interactions if not managed correctly in verification scripts.
**Action:** Always include a 'Skip to Content' link, wrap main content in `<main>`, and synchronize ARIA attributes (`aria-expanded`, `aria-label`) with JavaScript state changes. Ensure forms have visible or `sr-only` labels associated with inputs.
