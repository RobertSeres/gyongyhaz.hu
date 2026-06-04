## 2025-05-14 - Skip Link Visibility in Fixed Navigation
**Learning:** In projects with a `fixed` navigation bar, a "Skip to Content" link using Tailwind's `sr-only focus:not-sr-only` pattern may remain invisible or obscured if it inherits standard flow positioning.
**Action:** Always apply `focus:fixed` and a high `z-index` (e.g., `z-[100]`) to the skip link to ensure it overlays fixed headers and is immediately visible to keyboard users upon the first Tab press.
