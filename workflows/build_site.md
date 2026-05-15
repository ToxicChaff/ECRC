# Workflow: Build ECRC Website

## Objective
Assemble the ECRC website from modular component files into a single `index.html` that browsers can open directly.

## When to run
- After editing any file in `components/`
- After editing `css/styles.css`
- After adding a new section to the home page

## Required inputs
None — the script reads all component files automatically.

## Steps

1. Edit the relevant component file(s) in `components/`
2. Run the build tool:
   ```
   python tools/build_site.py
   ```
3. Open `index.html` in a browser to verify the change.

## File map

| What to edit | File |
|---|---|
| Navigation bar | `components/nav.html` |
| Hero section | `components/hero.html` |
| Stats bar | `components/stats.html` |
| News / Social feed | `components/news.html` |
| Upcoming Events | `components/events.html` |
| Regatta Results table | `components/results.html` |
| Member Clubs grid | `components/clubs.html` |
| CTA banner | `components/cta.html` |
| Footer | `components/footer.html` |
| All shared styles | `css/styles.css` |
| Rulebook page | `rulebook.html` |
| About Us page | `about.html` |
| Login page | `login.html` |

## Notes
- `index.html` is auto-generated — do not edit it directly. Your changes will be overwritten next time the build runs.
- The standalone pages (`rulebook.html`, `about.html`, `login.html`) are not assembled by the build tool — edit them directly.
- To add a new home page section: create `components/mysection.html`, add its path to the `COMPONENTS` list in `tools/build_site.py`, then re-run the build.
