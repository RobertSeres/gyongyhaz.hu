## 2025-05-14 - Structural Landmark Pattern in Monolithic HTML
**Learning:** In legacy monolithic HTML projects with fixed navigation, adding a 'Skip to Content' link paired with a `<main>` landmark is the highest-impact accessibility improvement. It significantly reduces repetitive tabbing for keyboard users.
**Action:** Always implement a 'Skip to Content' link (using `sr-only focus:not-sr-only`) as the first element in `<body>`, and ensure it targets a `<main id="main-content" tabindex="-1">` landmark that wraps the primary page content.

## 2025-05-14 - Modal and Form Labeling in Hungarian Locale
**Learning:** For sites with a specific locale (like Hungarian), ARIA labels must match the language of the interface (e.g., `aria-label="Bezárás"` instead of "Close") to provide a consistent experience for screen reader users.
**Action:** Audit all icon-only buttons (like close buttons) and form inputs for missing or English-only labels and replace them with localized, descriptive ARIA labels.
