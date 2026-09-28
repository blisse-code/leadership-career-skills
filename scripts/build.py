#!/usr/bin/env python3
"""Build installable packages into dist/.

  dist/claude/<skill>.skill          zip for the Claude app (Customize > Skills > upload)
  dist/chatgpt/<skill>-chatgpt.zip   zip for ChatGPT Skills upload
  dist/custom-gpts-fallback.zip      Custom GPT instructions + knowledge files (ChatGPT Plus/Pro)
  dist/leadership-career-skills-all.zip  everything above

Standard library only. Run from anywhere: python scripts/build.py
"""
import pathlib
import shutil
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLAUDE = ROOT / "plugins/leadership-career-skills/skills"
CHATGPT = ROOT / "chatgpt/skills"
GPTS = ROOT / "chatgpt/custom-gpts"
DIST = ROOT / "dist"
SKIP = {"__pycache__", ".DS_Store"}


def zip_dir(src: pathlib.Path, out: pathlib.Path, arc_root: str):
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob("*")):
            if f.is_file() and not (SKIP & set(f.parts)):
                z.write(f, f"{arc_root}/{f.relative_to(src)}")
    return out


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    built = []
    for s in sorted(p for p in CLAUDE.iterdir() if p.is_dir()):
        built.append(zip_dir(s, DIST / "claude" / f"{s.name}.skill", s.name))
    for s in sorted(p for p in CHATGPT.iterdir() if p.is_dir()):
        built.append(zip_dir(s, DIST / "chatgpt" / f"{s.name}-chatgpt.zip", s.name))

    # Custom GPT fallback: instructions + knowledge copied from the Claude edition
    stage = DIST / "_gpts"
    for g in sorted(p for p in GPTS.iterdir() if p.is_dir()):
        dst = stage / g.name
        (dst / "knowledge").mkdir(parents=True)
        shutil.copy(g / "instructions.txt", dst / "instructions.txt")
        skill = CLAUDE / g.name
        for f in list((skill / "references").glob("*.md")) + list((skill / "scripts").glob("*.py")):
            shutil.copy(f, dst / "knowledge" / f.name)
    built.append(zip_dir(stage, DIST / "custom-gpts-fallback.zip", "custom-gpts"))
    shutil.rmtree(stage)

    with zipfile.ZipFile(DIST / "leadership-career-skills-all.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in built:
            z.write(f, f"leadership-career-skills/{f.relative_to(DIST)}")
        z.write(ROOT / "README.md", "leadership-career-skills/README.md")
    for f in built:
        print("built", f.relative_to(ROOT))
    print("built", (DIST / "leadership-career-skills-all.zip").relative_to(ROOT))


if __name__ == "__main__":
    main()
