# S Saitheja — Portfolio

A responsive personal portfolio built with **Python + Flask**, HTML, CSS and JavaScript.

## Run locally

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start the site:

```bash
python app.py
```

6. Open **http://127.0.0.1:5000** in your browser.

## Important notes

- The resume from the supplied PDF is included as `static/Saitheja.pdf`.
- The contact form validates submissions but does not send/store email because no mail provider was supplied. Visitors can use the displayed email address.
- The LinkedIn URL was not present in the supplied resume, so no invented link was added.

## GitHub Pages note

GitHub Pages serves static files and does **not** run a Flask/Python server. To publish this exact Flask version publicly, deploy it to a Python-capable host (for example Render, Railway, or PythonAnywhere). If you specifically want GitHub Pages, the Flask app can be converted to a static HTML version while keeping the same design.

## Customize

- Main page: `templates/index.html`
- Styling: `static/css/style.css`
- Browser behavior: `static/js/main.js`
- Flask server: `app.py`
