## 2025-05-14 - Structural Landmark Pattern
**Learning:** Pairing a "Skip to Content" link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users. In legacy monolithic HTML projects, these are the highest priority accessibility improvements.
**Action:** Always implement a skip link and `<main>` landmark as the first step when auditing monolithic static sites for accessibility.
