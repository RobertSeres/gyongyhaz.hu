# Palette's Journal

## 2025-05-14 - Mobile Menu Accessibility Pattern
**Learning:** For mobile menu implementations in this repository, follow the established pattern of toggling `aria-expanded`, updating `aria-label`, and swapping Font Awesome icon classes (e.g., `fa-bars` to `fa-xmark`) via JavaScript.
**Action:** Always implement this pattern when modifying or creating mobile menus to ensure consistency and accessibility.

## 2025-05-14 - Avoiding Global Reformatting
**Learning:** Running automated formatting tools like Prettier on a legacy or large file without a project-wide configuration can lead to massive diffs that violate the "Keep changes under 50 lines" rule and hinder code review.
**Action:** Prefer targeted edits and match existing code style manually, or only format the modified blocks of code.
