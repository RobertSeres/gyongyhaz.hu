## 2025-05-22 - Semantic Landmarks and Navigation Shortcuts

**Learning:** In monolithic single-page HTML sites lacking a standard framework, the absence of basic navigation landmarks (like `<main>`) and skip links creates a major barrier for keyboard-reliant users. Even localized sites must prioritize these structural elements over visual-only improvements to ensure actual usability for assistive technology.

**Action:** Always implement a localized "Skip to Content" link and a corresponding `<main>` landmark as the first step in auditing legacy single-file projects. This provides the highest accessibility ROI with minimal code impact.
