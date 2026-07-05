# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2025-05-14 - Structural Landmark Pattern
**Learning:** In monolithic landing pages with fixed navigation, the absence of structural landmarks and skip links significantly hinders keyboard and screen reader accessibility. Pairing a 'Skip to Content' link with a `<main>` landmark (using `tabindex="-1"` and `focus:outline-none`) provides a high-impact, low-churn improvement that allows users to bypass repetitive navigation elements.
**Action:** Always prioritize implementing the 'Structural Landmark Pattern' (Skip Link + `<main>`) as the foundational accessibility layer for single-page applications.
