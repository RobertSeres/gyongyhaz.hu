## 2025-05-22 - Accessible Landmarks and Navigation
**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn.
**Action:** Always check for `<main>` and skip links as the first step in an accessibility audit for single-page sites.

## 2025-05-22 - Handling Non-Deterministic UI in Verification
**Learning:** Playwright verification scripts for this project must account for non-deterministic timed popups (newsletter ~1-2s, review ~5s) that frequently obstruct interactions.
**Action:** Proactively dismiss the newsletter modal (text: 'Nem, lemaradok a kedvezményekről' or 'Mégse') to ensure the page is interactable for subsequent tests.
