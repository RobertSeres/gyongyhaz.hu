## 2025-05-15 - Skip to Content link visibility vs. high z-index overlays
**Learning:** In projects with a fixed navigation bar and high-z-index components (like the newsletter modal at `z-[100]`), a 'Skip to Content' link requires explicit `focus:fixed` positioning and a higher `z-index` (e.g., `z-[150]`) to ensure it remains visible and accessible above all other overlays when focused.
**Action:** Always check for high-z-index modals/popups when implementing skip links and set the link's focus state z-index accordingly.
