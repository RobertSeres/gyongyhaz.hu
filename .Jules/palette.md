# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-05-15 - Surgical Accessibility Implementation
**Learning:** In monolithic HTML projects, automated tools for modifying DOM (like BeautifulSoup) can cause excessive reformatting (indentation, attribute ordering), leading to "diff noise" that violates line-count constraints and complicates reviews.
**Action:** Prioritize manual, surgical edits using specific search-and-replace patterns to implement accessibility landmarks and ARIA labels without altering the surrounding code structure.
