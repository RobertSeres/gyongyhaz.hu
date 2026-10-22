## 2025-05-18 - Structural Landmark Pattern & Skip Link
**Learning:** Pairing a hidden 'Skip to Content' link (`sr-only focus:not-sr-only focus:fixed z-[150] ...`) with a `<main id="main-content" tabindex="-1" class="focus:outline-none">` landmark allows keyboard users to bypass sticky nav headers smoothly while preventing persistent focus outlines on the main container upon target navigation.
**Action:** Always implement `<main id="main-content" tabindex="-1">` as the target when adding skip links in single-page applications to ensure robust focus management without visual outline artifacts.
