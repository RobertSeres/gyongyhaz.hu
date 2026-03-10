# Palette's Journal - Critical Learnings

## 2025-05-14 - Unified Mobile Menu Toggle Pattern
**Learning:** Mobile menus with multiple trigger points (toggle button and internal links) benefit from a unified `toggleMenu` function to ensure synchronization of visual state (icon classes), accessibility attributes (`aria-expanded`, `aria-label`), and visibility.
**Action:** Use a `toggleMenu(forceClose)` pattern that centralizes all state updates for mobile navigation.
