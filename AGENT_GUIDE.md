# Agent Guide for Copilot / AI contributors

Purpose
- This project converts `.docx` product drafts into a rendered product page using a single full-page template (`template_olivin.md`) and a set of per-product variables (YAML). The web tool (`app.py`) accepts an uploaded `_stare` file (or `.docx`), extracts candidate variables, lets a human edit all template variables, then renders and returns a generated markdown page.

Quick runtime files (what must remain in the repo)
- `app.py` — Flask app that powers upload → extract → review → render flow.
- `template_olivin.md` — canonical full-page template containing fixed scaffolding and placeholders (Jinja-style `{{KEY}}`).
- `vars_template_products.yaml` — product-level variable keys (minimal set used by templates).
- `vars_template.yaml` — extended YAML template with comments/example values.
- `requirements.txt` — Python dependencies.
- `templates/` — Jinja templates used by the web UI (`index.html`, `review.html`).
- `README.md` — basic user instructions.

How the app works (high level)
1. Upload: `app.py` `/upload` accepts `.docx` or `.md`. `.docx` is converted to HTML (mammoth) and then to Markdown.
2. Extract: heuristics in `extract_vars_from_markdown()` find product title, product code (`ARATxxx`), a price-like number, image URLs, and place content into keys like `product_name`, `product_code`, `hero_image`, `json_images`, `gallery_collection_slides`, and `STORY_HTML`.
3. Merge: merged variables come from three sources (priority): existing per-product `.vars.yaml` (if present) > extracted values > `vars_template_products.yaml` defaults.
4. Review: the `/review` page shows every key from `vars_template_products.yaml` as an editable form field; lists/dicts are rendered as JSON strings in textareas for editing.
5. Render: `/render` parses edited values (attempting YAML parsing when applicable), derives gallery HTML and `JSON_IMAGES`, renders `template_olivin.md` using Jinja2, and returns the generated `.generated.md` file.

Key code locations and quick dev notes
- Parsing heuristics: `extract_vars_from_markdown()` in `app.py` and `tools/generate_from_md.py`. Improve here to pull more structured values (regex, front-matter, or image captions).
- Template rendering: Jinja2 is used to render `template_olivin.md`. Template contains placeholders in both HTML and JSON-LD blocks — keep fixed scaffolding in template and expose only variables as keys.
- Preview: review page now shows the rendered preview (HTML) built from merged variables — ensure any changes to template keys are mirrored in `vars_template_products.yaml`.
- Form serialization: lists/dicts are serialized to JSON strings for editing and parsed back on render; avoid using Jinja `tojson()` with unsupported kwargs.

Running locally (quick commands)
1. Create venv and install:
```
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```
2. Run app:
```
.venv\Scripts\python.exe app.py
```
3. Open: `http://127.0.0.1:5000` → Upload a `_stare.md` or `.docx` file.

If you change dependencies, update `requirements.txt` and test in the venv.

Extending or modifying the template
- Add or remove placeholder keys in `template_olivin.md` only after updating `vars_template_products.yaml` (so the UI shows all editable keys).
- For arrays/complex keys (galleries, json_images), the app expects JSON/YAML in the textarea; implement better editors later (repeatable fields) if needed.

Tests & manual checks
- Use `tools/generate_from_md.py <file.md>` for quick CLI generation without running the web UI. This replicates the app's extract+render flow.
- After edits, open the generated `.generated.md` to verify that JSON-LD blocks and gallery HTML are correct.

Security and repo hygiene
- Do not commit secrets or large binaries. If old `.docx` files exist in history and you want them removed, run BFG or git-filter-repo (note: rewrites history; collaborators must re-clone).

Troubleshooting
- If preview fails to render: check `template_olivin.md` for missing placeholders or invalid Jinja syntax. The app renders with Jinja2 directly.
- If upload conversion fails: verify `mammoth` and `markdownify` are installed in the venv.
- If pushing changes to GitHub fails (remote non-fast-forward), pull/rebase or force-push only after confirming it's safe.

Helpful shortcuts for Copilot assistance
- When asked to add a new variable, update `vars_template_products.yaml` first, then update `templates/review.html` and `app.py` extraction/merging logic.
- When asked to improve galleries or JSON-LD, keep the fixed JSON-LD scaffolding in `template_olivin.md` and expose only the data arrays as variables.

Contact
- For project-specific quirks (naming rules or file conventions), refer to `README.md` for user-facing expectations or ask the repository owner for naming preferences (e.g., use `product_code` for filenames).

End of guide.
