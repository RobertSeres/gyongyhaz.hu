# Palette's Journal - UX & Accessibility Learnings

## 2025-05-10 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `class="focus:outline-none"` ensures keyboard users can bypass repetitive navigation directly to main content without leaving a visible outline box after focus shift.
**Action:** Implement `<a href="#main-content">` as the first child in `<body>` and wrap primary page sections in `<main id="main-content" tabindex="-1" class="focus:outline-none">` as a sibling to `<footer>`.
