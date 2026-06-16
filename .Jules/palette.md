## 2025-05-14 - Structural Landmarks and Icon Noise Reduction

**Learning:** In monolithic legacy HTML projects, decorative icons often create significant noise for screen reader users. Silencing them en masse (70+ instances) while adding a "Skip to Content" link and semantic landmarks (<main>, <nav> labels) provides the highest accessibility ROI with minimal visual impact.

**Action:** When auditing a single-page site, prioritize the "Structural Landmark Pattern": pair a high-z-index "Skip to Content" link with a <main> landmark and perform a regex-based sweep to add `aria-hidden="true"` to all decorative <i> tags.
