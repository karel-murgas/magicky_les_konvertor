import os
import sys
import mammoth
from markdownify import markdownify as md

INPUT_DIR = os.path.dirname(__file__)

def convert_file(path):
    try:
        with open(path, "rb") as f:
            html = mammoth.convert_to_html(f).value
        markdown = md(html, heading_style="ATX")
        out = os.path.splitext(path)[0] + ".md"
        with open(out, "w", encoding="utf-8") as w:
            w.write(markdown)
        return True, out
    except Exception as e:
        return False, str(e)

def main():
    root = INPUT_DIR
    converted = []
    errors = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".docx"):
                path = os.path.join(dirpath, name)
                ok, info = convert_file(path)
                if ok:
                    print(f"Wrote {info}")
                    converted.append(info)
                else:
                    print(f"Error converting {path}: {info}")
                    errors.append((path, info))
    print(f"Done. Converted: {len(converted)}, Errors: {len(errors)}")

if __name__ == "__main__":
    main()
