import sys
import os
import re
import json
import yaml
from jinja2 import Environment
from markdownify import markdownify as md

ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_VARS_FILE = os.path.join(ROOT, 'vars_template_products.yaml')
TEMPLATE_PATH = os.path.join(ROOT, 'template_olivin.md')


def load_template_keys():
    if not os.path.exists(TEMPLATE_VARS_FILE):
        return {}
    with open(TEMPLATE_VARS_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def extract_vars_from_markdown(md_text: str):
    out = {}
    m = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if m:
        out['product_name'] = m.group(1).strip()
    else:
        first = md_text.strip().splitlines()
        out['product_name'] = first[0].strip() if first else ''

    m = re.search(r'ARAT\d{2,4}', md_text)
    if m:
        out['product_code'] = m.group(0)

    m = re.search(r'\b(\d{2,6})(?:[.,]\d{2})?\b\s*(?:CZK|Kč)?', md_text)
    if m:
        try:
            out['price'] = int(m.group(1))
        except Exception:
            out['price'] = m.group(1)

    imgs = re.findall(r'(/[^\s\)"\']+\.(?:jpg|jpeg|png|webp))', md_text)
    if imgs:
        out['hero_image'] = imgs[0]
        out['json_images'] = imgs[:6]
        slides = []
        for im in imgs[:6]:
            slides.append({'image': im, 'caption': ''})
        out['gallery_collection_slides'] = slides
        out['gallery_detail_slides'] = slides

    out['STORY_HTML'] = md(md_text)
    return out


def build_gallery_html(slides):
    if not slides:
        return ''
    parts = []
    for s in slides:
        img = s.get('image') if isinstance(s, dict) else s
        caption = s.get('caption','') if isinstance(s, dict) else ''
        link = s.get('link','') if isinstance(s, dict) else ''
        part = f'<div class="slide"><a href="{link}"><img src="{img}" alt="{caption}"/></a>'
        if caption:
            part += f'<div class="caption">{caption}</div>'
        part += '</div>'
        parts.append(part)
    return '\n'.join(parts)


def main(md_fname):
    md_path = os.path.join(ROOT, md_fname)
    if not os.path.exists(md_path):
        print('File not found:', md_path)
        return 2

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    template_keys = load_template_keys()
    defaults = {k: template_keys.get(k, '') for k in template_keys}
    extracted = extract_vars_from_markdown(md_text)

    # attempt existing vars file
    product_key = os.path.basename(md_fname).replace('_stare.md','').replace('.md','')
    vars_path = os.path.join(ROOT, f"{product_key}.vars.yaml")
    vars_file = {}
    if os.path.exists(vars_path):
        with open(vars_path, 'r', encoding='utf-8') as f:
            vars_file = yaml.safe_load(f) or {}

    merged = defaults.copy()
    merged.update(extracted)
    merged.update(vars_file)

    # prepare context for template
    gallery_coll = merged.get('gallery_collection_slides') or []
    gallery_detail = merged.get('gallery_detail_slides') or []
    json_images = merged.get('json_images') or []

    merged['GALLERY_COLLECTION_SLIDES'] = build_gallery_html(gallery_coll)
    merged['GALLERY_DETAIL_SLIDES'] = build_gallery_html(gallery_detail)
    merged['JSON_IMAGES'] = json.dumps(json_images, ensure_ascii=False)

    for k, v in list(merged.items()):
        merged[k.upper()] = v

    if not os.path.exists(TEMPLATE_PATH):
        print('Missing template_olivin.md')
        return 3

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as tf:
        tpl_text = tf.read()

    env = Environment()
    template = env.from_string(tpl_text)
    rendered = template.render(**merged)

    safe_name = (merged.get('product_code') or merged.get('PRODUCT_CODE') or merged.get('product_name') or 'output')
    safe_name = str(safe_name)
    # sanitize for Windows filenames: keep letters, numbers, dot, underscore, hyphen
    safe_name = re.sub(r'[^A-Za-z0-9_.-]', '_', safe_name)
    out_name = f"{safe_name}.generated.md"
    out_path = os.path.join(ROOT, out_name)
    with open(out_path, 'w', encoding='utf-8') as wf:
        wf.write(rendered)

    print('Generated:', out_path)
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: generate_from_md.py <file.md>')
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
