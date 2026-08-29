from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
TEMPLATE = ROOT / "templates" / "index.html"

# Ensure output directory exists
DOCS.mkdir(parents=True, exist_ok=True)

html = TEMPLATE.read_text(encoding="utf-8")
html = html.replace("{{ url_for('static', filename='css/style.css') }}", "static/css/style.css")
html = html.replace("{{ url_for('static', filename='js/main.js') }}", "static/js/main-static.js")
html = html.replace("{{ url_for('static', filename='Saitheja.pdf') }}", "static/Saitheja.pdf")
(DOCS / "index.html").write_text(html, encoding="utf-8")

for folder in ["css", "js"]:
    src = ROOT / "static" / folder
    dst = DOCS / "static" / folder
    dst.mkdir(parents=True, exist_ok=True)
    for f in src.iterdir():
        if f.is_file():
            shutil.copy2(f, dst / f.name)

pdf_src = ROOT / "static" / "Saitheja.pdf"
if pdf_src.exists():
    (DOCS / "static").mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf_src, DOCS / "static" / "Saitheja.pdf")

print(f"Built static portfolio at: {DOCS}")

