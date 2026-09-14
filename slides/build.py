#!/usr/bin/env python3
"""Build the session decks.

    python3 slides/build.py

Content lives in content_day1.py / content_day2.py / content_day3.py as
DECKS = [(filename, deck_label, title, [slide_html, ...]), ...]

Edit the content files, re-run this, done. Shared look lives in deck.css.
"""
from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="deck.css">
</head>
<body>
{slides}
<div id="bar"></div><div id="num"></div>
<div id="deck">{label}</div>
<div id="hint">← → or space · F fullscreen</div>
<script src="deck.js"></script>
</body>
</html>
"""


def build() -> list[tuple[str, int]]:
    import content_day1, content_day2, content_day3

    built = []
    for mod in (content_day1, content_day2, content_day3):
        for fname, label, title, slides in mod.DECKS:
            body = "\n".join(
                f'<div class="slide{" on" if n == 0 else ""}">{s}</div>'
                for n, s in enumerate(slides)
            )
            (HERE / fname).write_text(
                PAGE.format(title=title, slides=body, label=label)
            )
            built.append((fname, len(slides)))
    return built


def index(built: list[tuple[str, int]]) -> None:
    rows = []
    for day in (1, 2, 3):
        theme = {1: "UNDERSTAND", 2: "DELEGATE", 3: "DELIVER"}[day]
        items = [b for b in built if b[0].startswith(f"day{day}-")]
        links = "".join(
            f'<li><a href="{f}">{f.replace(".html", "")}</a>'
            f'<span class="n">{n} slides</span></li>'
            for f, n in items
        )
        rows.append(
            f'<section><h2>Day {day} — {theme}</h2><ol>{links}</ol></section>'
        )
    (HERE / "index.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Workshop decks</title>
<style>
 body{{background:#0f1115;color:#f2f4f8;font:16px/1.6 system-ui,sans-serif;
       max-width:46rem;margin:0 auto;padding:3rem 1.5rem}}
 h1{{font-size:2.2rem;margin:0 0 .2em}} h2{{font-size:1.15rem;color:#4ade80;
       margin:2rem 0 .5rem;font-family:ui-monospace,monospace;letter-spacing:.1em}}
 ol{{list-style:none;padding:0;margin:0}}
 li{{display:flex;justify-content:space-between;align-items:center;gap:1rem;
     border-bottom:1px solid #2a2f3a;padding:.65rem 0}}
 a{{color:#f2f4f8;text-decoration:none;font-weight:600}}
 a:hover{{color:#4ade80}}
 .n{{color:#98a2b3;font:600 .8rem/1 ui-monospace,monospace;white-space:nowrap}}
 .tip{{color:#98a2b3;font-size:.9rem;margin-top:2.5rem;border-top:1px solid #2a2f3a;
       padding-top:1rem}}
</style></head><body>
<h1>Workshop decks</h1>
<p style="color:#98a2b3">One deck per 90-minute session. Open, press
<b style="color:#4ade80">F</b> for fullscreen, arrows or space to advance.</p>
{"".join(rows)}
<p class="tip">Works offline — no internet needed. Sessions run
09:30–11:00, 11:30–13:00, 13:45–15:15, 15:30–17:00.</p>
</body></html>""")


if __name__ == "__main__":
    b = build()
    index(b)
    total = sum(n for _, n in b)
    for f, n in b:
        print(f"  {f:<18} {n:>3} slides")
    print(f"\n  {len(b)} decks, {total} slides total")
