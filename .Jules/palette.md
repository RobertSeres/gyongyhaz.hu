## 2026-11-05 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a `<main id="main-content" tabindex="-1" class="focus:outline-none">` landmark allows keyboard and screen reader users to bypass repetitive navigation effortlessly while avoiding persistent visual focus rings. Ensuring `focus:fixed` and high z-index (`z-[150]`) prevents fixed navigation and overlays from hiding the focused link.
**Action:** Always implement this structural landmark pattern as the foundation on monolithic landing pages lacking bypass mechanisms.
