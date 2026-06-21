## 2025-05-14 - Accessible Icon Buttons and Landmarks

**Learning:** In monolithic landing pages with high-z-index components (like modals and sticky popups), common accessibility gaps include missing `aria-label` attributes on icon-only buttons (like "times" icons for closing) and the absence of structural landmarks (<main>) or "Skip to Content" links. These gaps significantly hinder keyboard and screen reader users.

**Action:** Always verify that every interactive icon has a descriptive `aria-label` in the site's primary language (e.g., "Bezárás" for Hungarian) and that the page structure follows the 'Structural Landmark Pattern' with a visible-on-focus skip link and a corresponding `<main>` landmark.
