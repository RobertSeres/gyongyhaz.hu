## 2026-01-07 - Landmarks and Interactive States
**Learning:** In a single-page architecture built with Tailwind and absolute/fixed positioning, it's easy to accidentally nest site-wide landmarks (like <main> wrapping <footer>) which confuses screen readers. Additionally, forms without visual feedback for asynchronous-like operations (simulated or real) feel "dead" and lead to multiple submissions.
**Action:** Always verify landmark hierarchy (main and footer should be siblings). Implement loading and success states for all forms to ensure clear user feedback.

## 2026-01-07 - Mobile Menu ARIA Synchronization
**Learning:** Mobile menus with multiple triggers (toggle button and internal links) require a centralized state management function to keep `aria-expanded`, dynamic `aria-label`, and icon classes in sync.
**Action:** Use a `toggleMenu(forceClose)` pattern to handle all triggers consistently.

## 2026-01-07 - Star Rating Accessibility
**Learning:** Star rating components using `flex-row-reverse` for hover effects need explicit Hungarian `aria-label` values on each link to provide context for screen readers in this locale.
**Action:** Add 'Értékelés: X csillag' to rating links and ensure 'rel="noopener noreferrer"' for external review links.
