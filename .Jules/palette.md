# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2025-05-14 - Testing "sr-only" elements for accessibility
**Learning:** Automated visibility checks (like Playwright's `is_visible()`) correctly identify elements with Tailwind's `sr-only` class as hidden from sighted users, which can cause test failures if checking for interaction. However, these elements are still part of the tab order if they are focusable.
**Action:** When verifying "Skip to Content" links or similar accessibility features, use `page.focus()` and then verify the element's visibility state changes (e.g., via `focus:not-sr-only`) or check for the presence of specific accessibility attributes rather than just global visibility.
