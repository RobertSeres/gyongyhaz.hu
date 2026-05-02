# Palette UX & Accessibility Journal

This file documents critical UX/accessibility learnings and repository-specific patterns for the Gyöngy Ház project.

## 2026-01-24 - Initial Accessibility Audit
**Learning:** The site uses a single-page architecture with multiple interactive overlays (newsletters, review prompts, coupons). Without a `<main>` landmark and "Skip to Content" link, keyboard users must tab through the entire navigation and overlays on every page load. Form inputs also lacked explicitly associated labels, relying solely on placeholders.
**Action:** Implement `<main>` landmark, "Skip to Content" link, and `sr-only` labels for all form inputs to ensure WCAG compliance without altering the visual design.
