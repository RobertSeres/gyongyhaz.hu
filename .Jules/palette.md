## 2025-05-27 - [Testing sr-only elements in Playwright]
**Learning:** Playwright's `is_hidden()` method returns `False` for elements using the Tailwind `sr-only` utility because they are not set to `display: none`. They are technically visible to the browser but hidden from the visual layout.
**Action:** Verify these accessible-only elements by asserting the presence of the `sr-only` class string and checking that they are not visually visible until focused (e.g., via `focus:not-sr-only`).

## 2025-05-27 - [High-impact A11y for Monolithic HTML]
**Learning:** In legacy monolithic HTML projects with fixed navigation, adding a `<main>` landmark and a "Skip to Content" link provides the highest immediate value for keyboard and screen reader accessibility with minimal code churn.
**Action:** Always check for these landmarks first when auditing a static single-page site for accessibility.
