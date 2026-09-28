# Evals

Built with Anthropic's `skill-creator` loop: realistic prompts, each run by an independent agent **with** the skill and with a **baseline** (no skill for new skills, the previous version for updated ones), then graded and reviewed by a human.

- `evals.json`: the 9 prompts and what each run had to produce
- `inputs/`: fictional candidate notes and job descriptions (no real people)
- `grade.py`: programmatic assertions (exact title, scope lines, unsupported percentages or currency, decision blocks, responsibility maps, placeholders, em dashes, banned words). It expects the skill-creator workspace layout `iteration-N/eval-*/<config>/run-1/outputs/`.
- `results/`: benchmark for each iteration plus `review-viewer.html`, a standalone page with every output side by side. Download it and open it in a browser.

| Iteration | Baseline pass rate | With skills |
|---|---|---|
| 1 | 72% | 88% |
| 2 (after fixes: dash scrub, market-conventions line, relocation placeholder, portfolio leadership scoring) | 72% | 95% |

Honest limits: one run per configuration (no variance estimate), test agents ran on a smaller model, and round 2 re-ran only the affected evals. Automated checks cover the parts that can be checked mechanically; quality of judgment still needs a human read.
