# ChatGPT editions

## Option A: ChatGPT Skills (Business, Enterprise, Edu)
ChatGPT skills use the same open format as Claude skills: a folder with `SKILL.md` (name + description frontmatter), plus optional `references/` and `scripts/`.
1. Download `*-chatgpt.zip` from the [latest release](https://github.com/blisse-code/leadership-career-skills/releases/latest), or zip a folder from `chatgpt/skills/`.
2. In ChatGPT, open Skills, choose upload, and select the zip. ChatGPT scans it before it becomes available.

What differs from the Claude edition: a short note at the top of each SKILL.md, plus in `bespoke-cover-letter` the memory, .docx build, and delivery steps use ChatGPT equivalents. Companion skills are used if installed; otherwise each skill carries the rules it needs.

## Option B: Custom GPTs (Plus, Pro, or any plan without Skills)
Available for the three new skills in `custom-gpts/`:
1. Create a GPT, then paste `custom-gpts/<skill>/instructions.txt` into **Instructions**. Each file is under the 8,000-character limit.
2. Under **Knowledge**, upload every file from `plugins/leadership-career-skills/skills/<skill>/references/`, and `scripts/*.py` if present. The release asset `custom-gpts-fallback.zip` bundles these for you.
3. Turn on **Code Interpreter** so the resume renderer and ATS checker can run.
