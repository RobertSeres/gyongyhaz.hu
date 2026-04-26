## 2025-05-14 - Accessible Mobile Menu Synchronization
**Learning:** In a single-page architecture with multiple menu trigger points (toggle button and navigation links), centralizing state management in a `toggleMenu` function ensures that ARIA attributes (`aria-expanded`, `aria-label`) and visual states (Font Awesome icons) remain synchronized, preventing accessibility mismatches.
**Action:** Always use a unified state management function for UI components with multiple interaction points to maintain consistent accessibility states.
