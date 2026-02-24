from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
import yaml
import mammoth
from markdownify import markdownify as md
import json
from jinja2 import Environment

ROOT = os.path.dirname(__file__)
VARS_EXT = '.vars.yaml'
TEMPLATE_VARS_FILE = os.path.join(ROOT, 'vars_template_products.yaml')

app = Flask(__name__)


def convert_docx_to_md(file_path):
    with open(file_path, 'rb') as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
        markdown = md(html)
    return markdown


def load_vars_for_product(name):
    path = os.path.join(ROOT, f"{name}{VARS_EXT}")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {}


def load_template_keys():
    if not os.path.exists(TEMPLATE_VARS_FILE):
        return {}
    with open(TEMPLATE_VARS_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def extract_vars_from_markdown(md_text: str):
    # Heuristic extraction from markdown-like `_stare` files
    out = {}
    # product name: first H1 or first line
    import re
    m = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if m:
        out['product_name'] = m.group(1).strip()
    else:
        first = md_text.strip().splitlines()
        out['product_name'] = first[0].strip() if first else ''

    # product code ARAT###
    m = re.search(r'ARAT\d{2,4}', md_text)
    if m:
        out['product_code'] = m.group(0)

    # price: find first number that looks like a price
    m = re.search(r'\b(\d{2,6})(?:[.,]\d{2})?\b\s*(?:CZK|Kč)?', md_text)
    if m:
        out['price'] = int(m.group(1))

    # images: collect common image paths
    imgs = re.findall(r'(/[^\s\)"\']+\.(?:jpg|jpeg|png|webp))', md_text)
    if imgs:
        out['hero_image'] = imgs[0]
        out['json_images'] = imgs[:6]
        # small gallery heuristics
        slides = []
        for im in imgs[:6]:
            slides.append({'image': im, 'caption': ''})
        out['gallery_collection_slides'] = slides
        out['gallery_detail_slides'] = slides

    # STORY_HTML: keep the main body (as markdown)
    out['STORY_HTML'] = md_text

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


@app.route('/')
def index():
    files = [f for f in os.listdir(ROOT) if f.endswith('_stare.md') or f.endswith('_stare.docx')]
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f:
        return redirect(url_for('index'))
    filename = f.filename
    save_path = os.path.join(ROOT, filename)
    f.save(save_path)

    if filename.lower().endswith('.docx'):
        md_text = convert_docx_to_md(save_path)
        md_name = filename.rsplit('.', 1)[0] + '.md'
        md_path = os.path.join(ROOT, md_name)
        with open(md_path, 'w', encoding='utf-8') as out:
            out.write(md_text)
    else:
        md_path = save_path

    basename = os.path.basename(md_path)
    product_key = basename.replace('_stare.md', '').replace('.md', '')

    # load defaults from template keys
    template_keys = load_template_keys()
    defaults = {k: template_keys.get(k, '') for k in template_keys}

    # try to load existing vars.yaml for product
    vars_file = load_vars_for_product(product_key)

    with open(md_path, 'r', encoding='utf-8') as rf:
        md_content = rf.read()

    extracted = extract_vars_from_markdown(md_content)

    # merge priority: existing vars_file > extracted > template defaults
    merged = defaults.copy()
    merged.update(extracted)
    if vars_file:
        merged.update(vars_file)

    # For list/dict values, serialize them to JSON strings for safe editing in the form
    merged_serialized = {}
    for k, v in merged.items():
        if isinstance(v, (list, dict)):
            try:
                merged_serialized[k] = json.dumps(v, ensure_ascii=False, indent=2)
            except Exception:
                merged_serialized[k] = str(v)
        else:
            merged_serialized[k] = v

    # Build a rendering context from merged_serialized for preview
    ctx = {}
    for k, v in merged_serialized.items():
        # attempt to parse JSON strings back into Python
        if isinstance(v, str) and (v.startswith('[') or v.startswith('{')):
            try:
                ctx[k] = json.loads(v)
                continue
            except Exception:
                pass
        ctx[k] = v

    # Derived preview fields
    gallery_coll = ctx.get('gallery_collection_slides') or []
    gallery_detail = ctx.get('gallery_detail_slides') or []
    json_images = ctx.get('json_images') or []
    ctx['GALLERY_COLLECTION_SLIDES'] = build_gallery_html(gallery_coll)
    ctx['GALLERY_DETAIL_SLIDES'] = build_gallery_html(gallery_detail)
    ctx['JSON_IMAGES'] = json.dumps(json_images, ensure_ascii=False)
    for k, v in list(ctx.items()):
        ctx[k.upper()] = v
    if 'STORY_HTML' not in ctx and 'story_html' in ctx:
        ctx['STORY_HTML'] = ctx['story_html']

    # Render preview using the template
    preview_html = ''
    template_path = os.path.join(ROOT, 'template_olivin.md')
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as tf:
            tpl_text = tf.read()
        env = Environment()
        template = env.from_string(tpl_text)
        try:
            preview_html = template.render(**ctx)
        except Exception:
            preview_html = '<pre>Error rendering preview</pre>'

    return render_template('review.html', keys=list(defaults.keys()), vars=merged_serialized, preview=preview_html, product=product_key)


@app.route('/render', methods=['POST'])
def render_template_route():
    template_path = os.path.join(ROOT, 'template_olivin.md')
    if not os.path.exists(template_path):
        return 'Missing template_olivin.md', 500

    # load template keys to know which fields to expect
    template_keys = load_template_keys()
    ctx = {}
    form = request.form
    for k in template_keys:
        v = form.get(k)
        if v is None:
            ctx[k] = template_keys.get(k)
            continue
        # if looks like YAML list or dict, try to parse
        try:
            parsed = yaml.safe_load(v)
            # keep parsed when it's list/dict, else keep string
            if isinstance(parsed, (list, dict)):
                ctx[k] = parsed
            else:
                ctx[k] = v
        except Exception:
            ctx[k] = v

    # create derived strings expected by template
    gallery_coll = ctx.get('gallery_collection_slides') or []
    gallery_detail = ctx.get('gallery_detail_slides') or []
    json_images = ctx.get('json_images') or []

    ctx['GALLERY_COLLECTION_SLIDES'] = build_gallery_html(gallery_coll)
    ctx['GALLERY_DETAIL_SLIDES'] = build_gallery_html(gallery_detail)
    ctx['JSON_IMAGES'] = json.dumps(json_images, ensure_ascii=False)

    # mirror uppercase keys used in some templates
    for k, v in list(ctx.items()):
        up = k.upper()
        ctx[up] = v

    # Also ensure STORY_HTML present
    if 'STORY_HTML' not in ctx and 'story_html' in ctx:
        ctx['STORY_HTML'] = ctx['story_html']

    # render template via Jinja2 to allow HTML injection
    with open(template_path, 'r', encoding='utf-8') as tf:
        tpl_text = tf.read()

    env = Environment()
    template = env.from_string(tpl_text)
    rendered = template.render(**ctx)

    # determine output filename
    product_code = ctx.get('product_code') or ctx.get('PRODUCT_CODE') or ctx.get('product_name','output')
    safe_name = str(product_code).replace('/', '_').replace(' ', '_')
    out_name = f"{safe_name}.generated.md"
    out_path = os.path.join(ROOT, out_name)
    with open(out_path, 'w', encoding='utf-8') as wf:
        wf.write(rendered)

    return send_from_directory(ROOT, out_name, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
