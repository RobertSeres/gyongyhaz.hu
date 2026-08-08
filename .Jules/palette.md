# Palette's Journal - Gyöngy Ház

## 2026-03-06 - Structural Landmark Pattern
**Learning:** Monolithic landing pages often lack proper HTML structural landmarks, causing screen readers and keyboard users to navigate repetitive layout elements on every interaction. Applying the 'Structural Landmark Pattern' provides a quick and highly accessible mechanism (Ugrás a tartalomra / Skip to Content) to bypass redundant navigation, satisfying WCAG 2.1 Success Criterion 2.4.1.
**Action:** Always wrap the main interactive content of a monolithic single-page application in a `<main id="main-content" tabindex="-1" class="focus:outline-none">` landmark and pair it with a pill-shaped, focus-visible Skip-to-Content link as the very first child of the `<body>` element.
