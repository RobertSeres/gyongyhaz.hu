## 2026-01-09 - Accessibility Landmark Hierarchy
**Learning:** Site-wide landmarks such as `<main>` and `<footer>` must be implemented as sibling elements; nesting `<footer>` inside `<main>` is a semantic error that negatively impacts accessibility. A "Skip to Content" link targeting the `<main>` element should be the first interactive element in the `<body>` to allow keyboard users to bypass navigation.
**Action:** Always verify that `<main>` and `<footer>` are siblings and implement a skip link using `sr-only focus:not-sr-only` classes.
