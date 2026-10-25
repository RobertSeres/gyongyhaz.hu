## 2026-01-12 - Structural Landmark Pattern & Modal Close ARIA Labels

**Learning:** Pairing a 'Skip to Content' link with a `<main>` landmark (`tabindex="-1" class="focus:outline-none"`) allows keyboard users to bypass navigation blocks smoothly, satisfying WCAG 2.1 SC 2.4.1 without leaving an unwanted focus outline when focused programmatically. Interactive modal close buttons require `aria-label="Bezárás"` in Hungarian to ensure full screen reader accessibility.

**Action:** Always include a 'Skip to Content' link as the first child of `<body>` pointing to `<main id="main-content">`, and verify all icon-only modal close buttons carry descriptive Hungarian ARIA labels.
