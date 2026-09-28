#!/usr/bin/env python3
"""Render an ATS-safe, single-column resume .docx from JSON.

Usage:
    python render_resume_docx.py resume.json output.docx

Schema (all keys optional except name):
{
  "name": str,
  "headline": str,
  "contact": [str, ...],
  "summary": str,
  "selected_impact": [str, ...],
  "competencies": [str, ...],
  "experience": [{"title", "company", "location", "dates", "scope", "bullets": [str]}],
  "earlier_career": str,
  "extras": {"Section Heading": [str, ...]},
  "style": {"font": "Calibri", "body_pt": 10.5, "accent": "1F3A5F"}
}

Design choices (why): single column, no tables, no text boxes, nothing in
headers/footers, standard headings, real bullet characters. These parse
reliably in ATS portals and match eye-tracking findings (bold titles over
short bullets, clear section headers, white space).
Requires: pip install python-docx
"""
import json
import sys

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor, Inches
except ImportError:  # pragma: no cover
    sys.exit("python-docx is not installed. Run: pip install python-docx")


def _rgb(hexstr):
    hexstr = hexstr.lstrip("#")
    return RGBColor(int(hexstr[0:2], 16), int(hexstr[2:4], 16), int(hexstr[4:6], 16))


def _spacing(p, before=0, after=2, line=1.08):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line


def _bottom_border(p, color="BFBFBF"):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pbdr.append(bottom)
    pPr.append(pbdr)


def render(data, out_path):
    style = data.get("style", {})
    font = style.get("font", "Calibri")
    body = float(style.get("body_pt", 10.5))
    accent = _rgb(style.get("accent", "1F3A5F"))
    dark = _rgb("1A1A1A")
    grey = _rgb("555555")

    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.6)
        s.left_margin = s.right_margin = Inches(0.7)

    normal = doc.styles["Normal"]
    normal.font.name = font
    normal.font.size = Pt(body)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), font)

    def para(text="", size=None, bold=False, italic=False, color=None, align=None, after=2, before=0):
        p = doc.add_paragraph()
        if text:
            r = p.add_run(text)
            r.bold = bold
            r.italic = italic
            r.font.size = Pt(size or body)
            if color is not None:
                r.font.color.rgb = color
        if align is not None:
            p.alignment = align
        _spacing(p, before=before, after=after)
        return p

    def heading(text):
        p = para(text.upper(), size=body + 0.5, bold=True, color=accent, before=8, after=3)
        _bottom_border(p)
        return p

    def bullet(text):
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(text)
        r.font.size = Pt(body)
        _spacing(p, after=1.5)
        p.paragraph_format.left_indent = Inches(0.22)
        return p

    para(data["name"], size=body + 9, bold=True, color=dark, after=1)
    if data.get("headline"):
        para(data["headline"], size=body + 1, bold=True, color=accent, after=1)
    if data.get("contact"):
        para("  |  ".join(data["contact"]), size=body - 1, color=grey, after=4)

    if data.get("summary"):
        heading("Summary")
        para(data["summary"], after=2)

    if data.get("selected_impact"):
        heading("Selected Impact")
        for b in data["selected_impact"]:
            bullet(b)

    if data.get("competencies"):
        heading("Core Competencies")
        para("  ·  ".join(data["competencies"]), after=2)

    if data.get("experience"):
        heading("Professional Experience")
        for i, job in enumerate(data["experience"]):
            p = doc.add_paragraph()
            _spacing(p, before=6 if i else 2, after=0)
            r = p.add_run(job.get("title", ""))
            r.bold = True
            r.font.color.rgb = dark
            r.font.size = Pt(body + 0.5)
            tail = [x for x in (job.get("company"), job.get("location")) if x]
            if tail:
                r2 = p.add_run("  |  " + ", ".join(tail))
                r2.font.size = Pt(body + 0.5)
            if job.get("dates"):
                r3 = p.add_run("  |  " + job["dates"])
                r3.font.color.rgb = grey
                r3.font.size = Pt(body)
            if job.get("scope"):
                para(job["scope"], italic=True, color=grey, after=2)
            for b in job.get("bullets", []):
                bullet(b)

    if data.get("earlier_career"):
        heading("Earlier Career")
        para(data["earlier_career"], after=2)

    for title, items in (data.get("extras") or {}).items():
        if not items:
            continue
        heading(title)
        for it in items:
            bullet(it)

    doc.save(out_path)
    return out_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as fh:
        payload = json.load(fh)
    print("Wrote", render(payload, sys.argv[2]))
