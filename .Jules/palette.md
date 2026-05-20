# Palette's Journal - Gyöngy Ház

## 2025-05-14 - [A11y/UX] Conflict between sr-only and fixed positioning
**Learning:** Tailwind's `not-sr-only` utility sets `position: static`, which can conflict with `fixed` or `absolute` positioning when trying to make a "Skip to Content" link visible on focus.
**Action:** Instead of `focus:not-sr-only`, use a combination of `focus:fixed`, `focus:w-auto`, `focus:h-auto`, `focus:clip-auto`, and `focus:whitespace-normal` to reliably reveal accessible-only elements without disrupting their intended layout.
