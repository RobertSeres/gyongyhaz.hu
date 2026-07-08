# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2025-05-15 - Structural Landmark Pattern
**Learning:** For static, long-scroll landing pages with fixed navigation, the "Skip to Content" link paired with a `<main>` landmark is the single most impactful accessibility win. Adding `tabindex="-1"` and `focus:outline-none` to the `<main>` element ensures that when the link is activated, the focus shifts correctly without a persistent focus ring, providing a smooth experience for keyboard users.
**Action:** Always implement a "Skip to Content" link as the first child of `<body>` and wrap core content in a `<main>` landmark with a corresponding ID and `tabindex="-1"`.
