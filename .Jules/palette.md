# Palette's Journal - Gyöngy Ház

## UX Standards & Patterns
- Mobile menu should always have `aria-expanded`, `aria-controls`, and synchronized icon states.
- Modals should use `role="dialog"` and `aria-modal="true"`.
- Non-modal popups should use `role="dialog"` but avoid `aria-modal="true"` to prevent unintentional focus trapping.
- Interactive elements should have visible focus states (e.g., using Tailwind `focus:ring` classes).
- Use `aria-label` for icon-only buttons and rating systems.
- Hungarian (hu) language should be used for all ARIA labels and user-facing strings.

## 2025-02-22 - Accessibility Polish
**Learning:** Initial audit revealed missing ARIA attributes on mobile menu, modals, and star ratings, which hinders accessibility for screen reader users.
**Action:** Implementing comprehensive ARIA support for these interactive components.
