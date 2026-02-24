# Template renderer

Small Flask app to upload a `_stare` file (or `.docx`) and render `template_olivin.md` with variables.

Usage:

- Create virtualenv and install:

```
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

- Open http://127.0.0.1:5000 and upload a `_stare.md` or `.docx` file.

Notes:
- The app performs a simple `{{KEY}}` placeholder replacement. Complex array handling (gallery slides, JSON arrays) is not implemented yet.
- By default the app looks for `PRODUCT_NAME` in the form fields to name the generated file.
