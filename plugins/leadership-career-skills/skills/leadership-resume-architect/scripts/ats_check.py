#!/usr/bin/env python3
"""Heuristic ATS and quality check for a resume against a job description.

Usage:
    python ats_check.py --resume resume.md [--jd jd.txt] [--title "Head of Design"]

Accepts .md, .txt, or .docx for the resume. Reports:
  - exact job title presence (from --title or first line of the JD)
  - JD keyword/phrase coverage (unigrams + bigrams, stopwords removed)
  - share of bullets carrying a number or scale marker
  - banned words, em/en dashes, first-person pronouns in bullets
  - unresolved placeholders ([Need ...])
This is a prompt for judgment, not a score to game. Keyword stuffing hurts
with human readers (TheLadders eye-tracking).
"""
import argparse
import re
from collections import Counter

STOP = set("""a an the and or of to in for on with by at from as is are be been being this that these those
our your their we you they it its will can may must should would could into over under across within
about per via than then also including include includes such other more most any all each both etc
role team work working need needs looking seeking join experience years year strong ability skills skill who what how using use new
""".split())

BANNED = ["results-driven", "dynamic", "passionate", "visionary", "synergy", "seamless", "delighted users",
          "game changer", "game-changer", "cutting-edge", "best-in-class", "world-class", "spearheaded",
          "orchestrated", "holistic", "robust", "thought leader", "rockstar", "ninja", "guru", "go-getter",
          "detail-oriented", "team player", "significant improvement", "delve", "tapestry", "elevate",
          "unlock", "empower", "responsible for", "helped", "leveraged", "leverage"]

NUM = re.compile(r"(\d|%|\bone\b|\btwo\b|\bthree\b|\bfour\b|\bfive\b|\bsix\b|\bdouble|\bhalf\b|\bthird\b)", re.I)
PRON = re.compile(r"\b(I|me|my|mine|we|our)\b")


def read(path):
    if path.lower().endswith(".docx"):
        from docx import Document
        return "\n".join(("- " + p.text) if "List" in p.style.name else p.text for p in Document(path).paragraphs)
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def tokens(text):
    words = [w for w in re.findall(r"[a-z][a-z+#./-]*", text.lower()) if w not in STOP and len(w) > 2]
    bigrams = [f"{a} {b}" for a, b in zip(words, words[1:])]
    return words, bigrams


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resume", required=True)
    ap.add_argument("--jd")
    ap.add_argument("--title")
    a = ap.parse_args()

    res = read(a.resume)
    low = res.lower()
    lines = [l.strip() for l in res.splitlines()]
    bullets = [l.lstrip("-•* ").strip() for l in lines if re.match(r"^[-•*]\s+", l)]

    print("=== ATS / QUALITY CHECK ===")
    title = a.title
    if a.jd:
        jd = read(a.jd)
        if not title:
            title = next((l.strip() for l in jd.splitlines() if l.strip()), "")
        jw, jb = tokens(jd)
        cand = [w for w, c in Counter(jb).most_common(40) if c >= 2] + [w for w, c in Counter(jw).most_common(40)]
        seen, terms = set(), []
        for t in cand:
            if t not in seen:
                seen.add(t)
                terms.append(t)
        terms = terms[:50]
        hit = [t for t in terms if t in low]
        miss = [t for t in terms if t not in low]
        print(f"JD term coverage: {len(hit)}/{len(terms)} ({100*len(hit)//max(1,len(terms))}%)")
        print("Missing (check which are true for the candidate before adding):", ", ".join(miss[:25]))
    if title:
        print(f"Exact title '{title}' present:", "YES" if title.lower() in low else "NO")

    if bullets:
        q = sum(1 for b in bullets if NUM.search(b))
        print(f"Bullets with number/scale: {q}/{len(bullets)} ({100*q//len(bullets)}%)")
        long_b = [b for b in bullets if len(b) > 220]
        if long_b:
            print(f"Bullets likely over 2 lines: {len(long_b)}")
        pron = [b[:70] for b in bullets if PRON.search(b)]
        if pron:
            print("First-person pronouns in bullets:", *pron, sep="\n  - ")

    found = [w for w in BANNED if re.search(r"\b" + re.escape(w) + r"\b", low)]
    print("Banned/discouraged words:", ", ".join(found) if found else "none")
    dashes = res.count("—") + res.count("–")
    print("Em/en dashes:", dashes)
    ph = re.findall(r"\[Need[^\]]*\]", res)
    print("Open placeholders:", len(ph))


if __name__ == "__main__":
    main()
