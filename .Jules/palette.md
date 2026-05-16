## 2025-05-14 - Automated Verification & Interstitial Modals
**Learning:** Playwright verification scripts for this project frequently encounter non-deterministic marketing popups (newsletter and review solicitations) that intercept clicks and keyboard focus, causing test failures in what should be straightforward UI assertions.
**Action:** Always include a proactive "dismissal" check in Playwright scripts that attempts to locate and close the newsletter modal (using Hungarian text identifiers like 'Nem, lemaradok a kedvezményekről') before performing core verification steps to ensure the page state is interactable.

## 2025-05-14 - Structural Accessibility in Legacy Layouts
**Learning:** In monolithic single-page HTML projects, adding a `<main>` landmark combined with a 'Skip to Content' link provides the highest accessibility ROI for keyboard and screen reader users with minimal impact on existing CSS/JS.
**Action:** Prioritize these structural landmarks as the first step when auditing legacy layouts for accessibility gaps.
