#!/usr/bin/env python3
"""Turn a resume.md into resume.pdf and resume.docx, next to it.

usage: python3 scripts/export.py companies/google-backend/resume.md

No packages to install. PDF is printed by Chrome / Chromium / Edge (headless).
DOCX is written directly with Python's standard library.

Supported markdown (keep resumes to this):
  # Name                      -> big name line
  plain line after the name   -> contact line
  ## SECTION                  -> section heading
  ### Role | Company | Dates  -> job / project line
  - bullet                    -> bullet
  plain paragraph             -> paragraph
  **bold**                    -> bold text
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile


def parse(md):
    blocks = []
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("### "):
            blocks.append(("h3", line[4:].strip()))
        elif line.startswith("## "):
            blocks.append(("h2", line[3:].strip()))
        elif line.startswith("# "):
            blocks.append(("h1", line[2:].strip()))
        elif re.match(r"^\s*[-*] ", line):
            blocks.append(("li", re.sub(r"^\s*[-*] ", "", line).strip()))
        elif blocks and blocks[-1][0] == "h1":
            blocks.append(("contact", line.strip()))
        else:
            blocks.append(("p", line.strip()))
    return blocks


def runs(text):
    """Split '**bold** rest' into [(text, bold)]."""
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if part:
            out.append((part, i % 2 == 1))
    return out


# ---------- PDF (HTML printed by headless Chrome) ----------

CSS = """
@page { size: A4; margin: 14mm 16mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; color: #111; line-height: 1.35; }
h1 { font-size: 20pt; margin: 0 0 2pt; }
.contact { font-size: 9.5pt; color: #333; margin-bottom: 8pt; }
h2 { font-size: 11pt; letter-spacing: 0.06em; text-transform: uppercase; border-bottom: 1px solid #999; margin: 12pt 0 4pt; padding-bottom: 2pt; }
h3 { font-size: 10.5pt; margin: 7pt 0 2pt; }
ul { margin: 0 0 2pt 16pt; padding: 0; }
li { margin: 0 0 2pt; }
p { margin: 0 0 4pt; }
"""


def inline_html(text):
    return "".join(f"<b>{html.escape(t)}</b>" if b else html.escape(t) for t, b in runs(text))


def to_html(blocks):
    body, in_list = [], False
    for kind, text in blocks:
        if kind == "li" and not in_list:
            body.append("<ul>")
            in_list = True
        if kind != "li" and in_list:
            body.append("</ul>")
            in_list = False
        tag = {"h1": "h1", "h2": "h2", "h3": "h3", "li": "li", "p": "p"}.get(kind)
        if kind == "contact":
            body.append(f'<div class="contact">{inline_html(text)}</div>')
        else:
            body.append(f"<{tag}>{inline_html(text)}</{tag}>")
    if in_list:
        body.append("</ul>")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(body)}</body></html>"


def find_chrome():
    names = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "chrome", "msedge"]
    for n in names:
        p = shutil.which(n)
        if p:
            return p
    paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    return next((p for p in paths if os.path.exists(p)), None)


def write_pdf(blocks, out):
    chrome = find_chrome()
    if not chrome:
        print("  ! no Chrome/Chromium/Edge found: skipped PDF (open the .docx and Save as PDF)")
        return False
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "resume.html")
        with open(page, "w", encoding="utf-8") as f:
            f.write(to_html(blocks))
        subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf-no-header",
                        f"--print-to-pdf={os.path.abspath(out)}", "file://" + page],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return True


# ---------- DOCX (plain OOXML, standard library only) ----------

def x(t):
    return html.escape(t, quote=False)


def w_runs(text, size=None, color=None):
    out = []
    for t, b in runs(text):
        props = ("<w:b/>" if b else "") + (f'<w:color w:val="{color}"/>' if color else "") + (f'<w:sz w:val="{size}"/>' if size else "")
        out.append(f'<w:r><w:rPr>{props}</w:rPr><w:t xml:space="preserve">{x(t)}</w:t></w:r>')
    return "".join(out)


def w_para(kind, text):
    if kind == "h1":
        return f'<w:p><w:pPr><w:spacing w:after="40"/></w:pPr>{w_runs("**" + text + "**", size=40)}</w:p>'
    if kind == "contact":
        return f'<w:p><w:pPr><w:spacing w:after="160"/></w:pPr>{w_runs(text, size=19, color="333333")}</w:p>'
    if kind == "h2":
        return ('<w:p><w:pPr><w:spacing w:before="240" w:after="80"/><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="999999"/></w:pBdr></w:pPr>'
                f'{w_runs("**" + text.upper() + "**", size=22)}</w:p>')
    if kind == "h3":
        return f'<w:p><w:pPr><w:spacing w:before="140" w:after="40"/></w:pPr>{w_runs("**" + text + "**", size=21)}</w:p>'
    if kind == "li":
        return f'<w:p><w:pPr><w:spacing w:after="40"/><w:ind w:left="360" w:hanging="220"/></w:pPr><w:r><w:t xml:space="preserve">• </w:t></w:r>{w_runs(text, size=21)}</w:p>'
    return f'<w:p><w:pPr><w:spacing w:after="80"/></w:pPr>{w_runs(text, size=21)}</w:p>'


def write_docx(blocks, out):
    body = "".join(w_para(k, t) for k, t in blocks)
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
           f'{body}<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="800" w:right="900" w:bottom="800" w:left="900" w:header="0" w:footer="0" w:gutter="0"/></w:sectPr>'
           '</w:body></w:document>')
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:docDefaults><w:rPrDefault><w:rPr>'
              '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="21"/></w:rPr></w:rPrDefault></w:docDefaults></w:styles>')
    types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
             '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", styles)
        z.writestr("word/_rels/document.xml.rels", doc_rels)


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".md"):
        sys.exit("usage: python3 scripts/export.py <folder>/resume.md")
    src = sys.argv[1]
    with open(src, encoding="utf-8") as f:
        blocks = parse(f.read())
    base = src[:-3]
    write_docx(blocks, base + ".docx")
    print("  ✓", base + ".docx")
    if write_pdf(blocks, base + ".pdf"):
        print("  ✓", base + ".pdf")


if __name__ == "__main__":
    main()
