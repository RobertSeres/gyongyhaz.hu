## 2025-10-19 - Skip to Content Link and Main Landmark
**Learning:** Pairing a top-level "Skip to Content" link with a `<main id="main-content" tabindex="-1" class="focus:outline-none">` landmark drastically improves accessibility for screen reader and keyboard users without causing persistent focus rings on target jump.
**Action:** Always insert a Hungarian "Ugrás a tartalomra" link as the first child of `<body>` and wrap body content prior to `<footer>` in `<main id="main-content" tabindex="-1" class="focus:outline-none">`.
