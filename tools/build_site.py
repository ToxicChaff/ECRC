#!/usr/bin/env python3
"""
Assembles the ECRC website from component files into index.html.

Usage:
    python tools/build_site.py

How it works:
    - Reads each file listed in COMPONENTS in order
    - Wraps them in the HTML shell (head linking to css/styles.css)
    - Writes the result to index.html

To edit a section, open the relevant file in components/ and then re-run this script.
"""

from pathlib import Path

ROOT = Path(__file__).parent.parent

COMPONENTS = [
    "components/nav.html",
    "components/hero.html",
    # "components/stats.html",   # hidden — uncomment to restore
    "components/news.html",
    "components/events.html",
    "components/results.html",
    "components/clubs.html",
    # "components/cta.html",     # hidden — uncomment to restore
    "components/footer.html",
]

HTML_SHELL = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>East Coast Rowing Council</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>

{body}

  <script>
    function toggleMenu() {{
      const menu = document.getElementById('mobile-menu');
      menu.classList.toggle('open');
    }}

    document.querySelectorAll('.mobile-menu a').forEach(link => {{
      link.addEventListener('click', () => {{
        document.getElementById('mobile-menu').classList.remove('open');
      }});
    }});

    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');
    window.addEventListener('scroll', () => {{
      let current = '';
      sections.forEach(section => {{
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) current = section.getAttribute('id');
      }});
      navLinks.forEach(a => {{
        a.classList.remove('active');
        if (a.getAttribute('href') === '#' + current) a.classList.add('active');
      }});
    }}, {{ passive: true }});
  </script>

</body>
</html>
"""


def build():
    parts = []
    for rel_path in COMPONENTS:
        path = ROOT / rel_path
        if not path.exists():
            print(f"  WARNING: {rel_path} not found — skipping")
            continue
        parts.append(f"  <!-- ── {path.stem} ── -->")
        parts.append(path.read_text(encoding="utf-8").strip())

    body = "\n\n".join(parts)
    output = HTML_SHELL.format(body=body)

    out_path = ROOT / "index.html"
    out_path.write_text(output, encoding="utf-8")
    print(f"Built {out_path.name} from {len(COMPONENTS)} components.")
    for c in COMPONENTS:
        print(f"  + {c}")


if __name__ == "__main__":
    build()
