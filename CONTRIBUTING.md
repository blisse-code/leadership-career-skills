# Contributing

Thanks for helping make career advice for design leaders more honest and better evidenced.

## Ground rules
1. **Evidence first.** New rules need a source: a study with a method, a named hiring leader's practice, or an established book. Add it to `docs/research-basis.md` and to the skill's own `references/research-basis.md`, labelled Data, Practitioner, Book, or Vendor.
2. **Never teach fabrication.** No examples that invent metrics, titles, or quotes. Placeholders (`[Need number]`, `[Need Human Review]`) are the pattern.
3. **Explain the why.** Skills work better when they give reasons than when they shout MUST. Keep each `SKILL.md` under ~500 lines and push detail into `references/`.
4. **Keep editions in sync.** Changes to `plugins/leadership-career-skills/skills/<skill>` should be mirrored in `chatgpt/skills/<skill>`. The only differences there are the ChatGPT note and platform-specific delivery steps. If a Custom GPT's `instructions.txt` is affected, keep it under 8,000 characters.
5. **House style for outputs:** no em dashes, no hype vocabulary (see each skill's banned list).

## Before opening a PR
```bash
python scripts/validate.py      # frontmatter, name, description length, referenced files
python scripts/build.py         # confirms everything packages
claude plugin validate .        # if you have Claude Code
```
If you change behaviour, add or update a case in `evals/evals.json` and describe what you expect in the PR.

## Useful contributions
- Country CV conventions (`leadership-resume-architect/references/ats-and-format.md`)
- Eval prompts that break a skill
- Better sources, or corrections where a source was overstated
- Translations of the Custom GPT instructions
