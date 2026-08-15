## 2026-08-15 - Hungarian Locale ARIA Labeling for Icon-Only Interactive Controls
**Learning:** Icon-only close buttons (`&times;`, FontAwesome `fa-times`) and social media links (`fa-facebook`, `fa-instagram`) lack default text accessible names. Adding generic English labels in a Hungarian application creates a jarring localized experience for screen reader users.
**Action:** Always provide explicit Hungarian `aria-label` attributes (e.g., `aria-label="Bezárás"`, `aria-label="Facebook oldalunk"`) for all icon-only buttons and anchor tags in Hungarian sites.
