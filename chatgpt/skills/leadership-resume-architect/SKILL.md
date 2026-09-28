---
name: leadership-resume-architect
description: Build or rewrite a leadership-level resume or CV (Lead, Principal, Staff, Manager, Director, Head, VP, or Chief of UX, Design, Experience, Product Design, or any leadership role) that proves scope, people leadership, business impact, and judgment instead of listing duties. Use whenever the user asks to write, rebuild, tailor, audit, or critique a resume or CV for a senior, lead, principal, manager, director, head, VP, or executive role, wants a master resume, wants to move from IC to leadership, says "make my resume look senior", or pastes a leadership job description with their background. Also use for LinkedIn About/Experience rewrites that must match a leadership resume. Enforces no invented metrics, ATS-safe format, country conventions, and outputs .docx plus an evidence log.
---

> **ChatGPT edition.** Same method as the Claude version. Where this file mentions companion skills, use them if they are installed in your workspace; otherwise continue with the rules stated here. Run bundled scripts in ChatGPT's code environment when available.

# Leadership Resume Architect

A leadership resume answers one question in the first 7 seconds: **what did this person make happen through other people, at what scale, and what changed for the business?** Everything in this skill serves that question. Duties, tool lists, and adjectives do not answer it. Scope lines, decisions, and outcomes do.

This skill exists because generic resume advice (one page, skills bars, "results-driven leader") actively hurts senior candidates. The rules below come from hiring data and design-leadership hiring managers; `references/research-basis.md` has the sources if the user asks why.

## Principles (read these, they drive every decision)

1. **Leverage over labour.** At leadership level the unit of value is what the team, org, or business achieved because you set direction, built the team, or changed how decisions were made. Keep one or two craft bullets per recent role to show you are still close to the work (player-coach is what 2026 hiring wants), but most bullets should show leverage.
2. **Mandate, move, measure.** Every role block reads as: what you walked into (mandate), what you did that others would not have (move), and what changed (measure). If a role has no visible mandate, the reader cannot judge the size of the win.
3. **Evidence or it did not happen, and never invent it.** Use only facts the user gave or that are in their files. If a number is missing, write the mechanism instead ("cut review cycles by moving sign-off to a weekly design council") and add the gap to the evidence log as `[Need number]`. Fabricated metrics get found in reference checks and in the interview; they end candidacies.
4. **Written for two readers.** A machine (ATS keyword and title filters) and a human who scans the left edge for titles in seconds. Single column, standard headings, exact target title in the headline, bold titles over short bullets. Both readers must win or neither does.
5. **Honest attribution.** "I" for what the user did, "led the team that" for what the team did under them, "partnered with" for shared wins. Leaders who claim everything read as either junior or untrustworthy.

## Workflow

### Step 1: Intake (fast, low burden)

Collect what exists before asking anything. Check, in order: files the user attached or pointed to (old resume, LinkedIn export, portfolio, performance reviews), any case studies produced earlier in the conversation, and saved context about the user. Then ask only what blocks the draft, max 6 questions in one message, each with an example answer so the user can reply in shorthand. Typical gaps:

- Target role(s), level, and country (drives length, photo, DOB conventions)
- Job description(s), or "master resume, no JD yet"
- For each of the last 2-3 roles: team size managed or influenced, budget or portfolio owned, the mandate on arrival, 2-3 wins with any numbers
- Confidentiality limits (client names, metrics that cannot be shown)

If the user wants speed, proceed with `[Need Human Review]` placeholders rather than stalling.

### Step 2: Deconstruct the target

If there is a JD (or several), build a **Target Map** before writing a word. Read `references/ats-and-format.md` section "Target Job Deconstruction" for the method. Output a compact table:

| Priority | Requirement (JD wording) | Keyword/phrase to mirror | User evidence | Gap? |

Priority 1 = explicitly required or repeated; 2 = stated as preferred; 3 = implied by company context. Also note the **exact job title** string and the leadership level the posting really wants (use the level calibration in `references/leadership-signals.md`, because "Head of Design" at a 40-person startup is a player-coach, and at a bank is an org builder).

With no JD, build the map from the user's target title and the level calibration, and label it "generic target, tailor before sending".

### Step 3: Mine evidence into a Leadership Evidence Bank

Before drafting, turn the raw material into an evidence bank grouped by leadership dimension (see `references/leadership-signals.md` for the eight dimensions and the questions that surface evidence). For each item record: claim, dimension, scope, number or mechanism, source, confidence (High = artifact exists, Med = user stated, Low = inferred). This is the raw ore; the resume is a selection from it. It also becomes the evidence log the user keeps for interviews.

### Step 4: Architect the document

Use the skeleton in `references/resume-template.md`. Key decisions:

- **Length.** 2 pages is the default for 10+ years or any manager-and-above role (hiring professionals preferred two-page resumes 2.9x for managerial roles). 1 page only if the user asks or has under ~8 years. 3 pages only for exec roles in markets that expect it (Germany, some public sector). Page 1 must stand alone.
- **Headline** = exact target title + scope signal, e.g. "Head of Experience Design | Design orgs of 20+ across telco, fintech, e-commerce | AI-integrated product design".
- **Summary** 3-4 lines, no adjectives about yourself. Formula: identity + scale + signature + proof. The **leadership signature** is the pattern others rely on the user for (see leadership-signals.md). Write it as a claim a stranger could verify.
- **Selected Impact** block (3-5 bullets) at the top of page 1 for Director and above: the best outcomes across the whole career, each a complete mandate-move-measure line. This is what the 7-second scan should catch.
- **Core Competencies**: one line or two short lines of keyword phrases mirrored from the Target Map. No skill bars, no self-ratings.
- **Experience**: reverse chronological. Each role gets a one-line **scope line** in italics under the title (team size, reports, budget, products, markets, stakeholders), then 3-6 bullets for recent roles, 1-3 for older ones. Roles older than ~15 years collapse into "Earlier career" with one line each.
- **Leadership extras** (only if real): hiring/team building, speaking, publications, advisory roles, patents, awards. These are strong signals at Head/VP level.

### Step 5: Write the bullets

Read `references/bullet-formulas.md` before writing. Core rules:

- Pattern: **Verb + what changed + measured how + by doing what** (Google's XYZ), with a leadership verb that shows the user's actual role.
- Aim for most bullets carrying a number, a scale marker, or a named mechanism. A number is best; a verifiable mechanism beats a vague number.
- Vary the dimension across bullets in a role: not five delivery bullets. Cover at least three of: business outcome, team/org building, operating model, cross-functional influence, craft/quality bar, strategy/vision, AI or innovation.
- One idea per bullet, one to two lines. Front-load the outcome or the scale.
- No em dashes (use commas or periods), no first person pronouns in bullets, no banned words (list in bullet-formulas.md).
- Mirror the JD's words where true. Keyword stuffing without context was one of the traits of the worst performers in eye-tracking research.

### Step 6: Quality gate

Run all checks in `references/quality-gate.md`: the 7-second scan test, the skeptical hiring manager test, the executive reader test (CEO/CPO/CFO), attribution check, ATS check, and consistency with LinkedIn/portfolio/cover letter. If `scripts/ats_check.py` can run, run it:

```bash
python scripts/ats_check.py --resume resume.md --jd jd.txt
```

It reports JD keyword coverage, exact title presence, bullet quantification ratio, banned words, em dashes, and first-person pronouns. Treat its output as a prompt for judgment, not a score to game.

**Final scrub (every deliverable, including notes and decks).** Em dashes (—) and en dashes used as dashes (–) are the most common thing that slips through, because they feel natural mid-draft. Before delivering, search every output file for them and replace with a comma, colon, period, or parentheses, e.g. `grep -c "—\|–" <file>` must return 0. Hyphens in compound words and date ranges written with a plain hyphen ("2022 - 2024") are fine.

### Step 7: Render and deliver

Default deliverable: an ATS-safe **.docx** (single column, Calibri or similar 10-11pt body, standard headings, no tables/text boxes/headers/footers for content) plus the same content as Markdown for copy-paste. Use the bundled renderer, which takes a JSON file matching the schema at the top of the script:

```bash
python scripts/render_resume_docx.py resume.json output.docx
```

If python-docx is unavailable, fall back to the `docx` skill if present, or deliver Markdown and say so. Offer a PDF copy for direct email (PDF preserves layout; .docx parses best in ATS; NN/g recommends keeping both).

Deliver alongside the resume:
1. **Evidence log**: every bullet mapped to its source and confidence, with all `[Need number]` / `[Need Human Review]` items listed at the top so the user knows exactly what to fill.
2. **Target Map** with remaining gaps and how the cover letter or interview should handle each.
3. **Three interview stories** the resume sets up (the bullets a panel will most likely probe), each with the STAR/CAR outline, so the resume and interview stay consistent.
4. **LinkedIn alignment notes**: headline and About opening lines matching the resume.
5. **Market conventions applied**: one line naming the target country and what that changed (e.g. "Germany: 2 pages; photo and date of birth are customary in German CVs, left out by default, add if you're comfortable; relocation line added"). Check the table in `references/ats-and-format.md` every time the target market differs from the user's current country; this is the step most often forgotten.

Keep the chat summary short: what the resume argues in one sentence, what needs the user's input.

## Variants

- **Master resume** (no JD): longest defensible version, 3 pages allowed as an internal source file. Tailored versions are cut from it.
- **Tailored resume** (JD given): reorder bullets by Target Map priority, swap competencies, retitle headline to the exact title. Never change facts between versions.
- **IC-to-leader transition**: lead with the leadership signature and leadership-without-title evidence (mentoring, running crits, setting standards, influencing roadmap, leading a workstream). See the transition section in leadership-signals.md.
- **Principal/Staff IC leadership**: scope is influence not headcount. Scope line = products, teams, and decisions influenced. See the IC archetypes in leadership-signals.md.
- **Agency or consultancy leaders**: accounts led, client portfolio size, multi-client operating model, pitches won, client retention; name clients only if public or cleared.
- **Country conventions**: apply the table in ats-and-format.md (e.g. Germany expects a photo and DOB, US and UK do not). Ask if unclear.

## Adjacent skills

- `tailored-resume-generator`: general job tailoring for non-leadership roles. This skill replaces it for leadership targets.
- `ux-leadership-case-study`: turns the strongest resume bullets into full leadership case studies; its outputs are excellent evidence input here.
- `bespoke-cover-letter`: write the letter after the resume so its proof points match.
- `principal-head-experience-ai-portfolio-architect`: whole-portfolio architecture.
- `docx`: advanced Word formatting if the renderer is not enough.

## Reference files

| File | Read when |
|---|---|
| `references/leadership-signals.md` | Step 2-3: level calibration, eight dimensions, evidence-mining questions, IC and transition cases |
| `references/bullet-formulas.md` | Step 5: formulas, verb bank by dimension, weak-to-strong rewrites, banned words |
| `references/resume-template.md` | Step 4: section skeleton and JSON schema for the renderer |
| `references/ats-and-format.md` | Steps 2 and 7: target deconstruction, ATS rules, length data, country conventions |
| `references/quality-gate.md` | Step 6: the checks |
| `references/research-basis.md` | When the user asks why, or rules seem to conflict |
