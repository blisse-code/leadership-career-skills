---
name: ux-leadership-case-study
description: Write UX and design leadership case studies that prove how the user led (decisions, trade-offs, alignment, team and org building, business impact) rather than what screens they made. Use whenever the user wants a case study, portfolio project write-up, leadership proof file, decision map, or portfolio presentation for a Lead, Principal, Staff, Manager, Director, Head, VP, or CDO design/UX/experience role, or says "show my leadership", "turn this project into a case study", "I led this but it reads like IC work", "make this case study senior", or wants to present work to an interview panel of executives. Also use for agency/client work, design system, transformation, team-building, DesignOps, and AI-adoption stories. Outputs long-form case study, 30-second skim, deck outline, and evidence table; never invents metrics.
---

> **ChatGPT edition.** Same method as the Claude version. Where this file mentions companion skills, use them if they are installed in your workspace; otherwise continue with the rules stated here. Run bundled scripts in ChatGPT's code environment when available.

# UX Leadership Case Study

An IC case study proves "I can design". A leadership case study proves **"when I am in the room, the team makes better decisions, the work gets better, and the business moves"**. Hiring panels for design leadership are often not designers (CEO, CPO, CFO, engineering heads). They scan for mandate, judgment, leverage, and outcome in 30 seconds and go deep only if that lands.

Three failures sink most leadership case studies, so the whole workflow is built to prevent them:
1. **Process narration instead of proof of leverage.** "We did research, then wireframes, then testing" says nothing about leadership.
2. **The vanishing leader.** "We" everywhere, so nobody can tell what the user did; or "I" everywhere, which reads as untrustworthy.
3. **The clean story.** Leaders are hired to navigate mess. A story with no conflict, compromise, or failure is not believed (Adobe's design leaders: "tell a messy story").

## Principles

- **Decisions over deliverables.** The spine of the story is the 3-5 decisions that shaped the outcome: the tension, the options, who disagreed, what the user chose, why, and what it cost.
- **Answer first.** Open with the outcome and the mandate (Minto's pyramid). Depth on demand.
- **Balance** (DoorDash's Helena Seo): show team operations and product innovation, vision and execution, business and user, breadth and depth, leading from the front and from behind. A story that shows only one side of each pair reads as incomplete.
- **Credit the team, own your part.** Name team size and roles; use a responsibility map.
- **Evidence or placeholder, never invention.** Missing numbers become `[Need Human Review]` and move to the evidence table. Mechanism beats invented metric.
- **Plain language.** Test every paragraph on "would a smart person outside this company follow it?" Internal jargon and acronyms get cut or unpacked.

## Workflow

### Step 1: Intake

Gather what exists first: project notes, decks, PRDs, research, analytics, performance reviews, prior resume bullets, anything in the conversation. Then ask only blocking questions, max 7, each with an example answer. The ones that matter most:

1. Target role and level, and who will read or hear this (designers? execs? both?)
2. The mandate: what was broken or at stake when you started, and who asked you to fix it
3. Your role and team: title, team size and roles, who you reported to, key partners
4. The 3 hardest decisions and who disagreed
5. What changed: numbers, observable changes, adoption, team outcomes
6. What went wrong or what you'd do differently
7. Confidentiality limits

Proceed with placeholders if the user wants speed.

### Step 2: Choose the case type and the leadership lens

Read `references/case-types.md` and pick the type (org/team build, design system/platform, transformation/turnaround, product strategy led through a team, influence without authority, crisis/recovery, DesignOps/process, AI adoption, agency/client leadership). The type decides which sections carry weight and which evidence matters. Calibrate to level with the table in that file (Manager proves a team that ships; Director proves scale and alignment; VP proves executive influence and business outcome; Principal IC proves judgment beyond their team).

### Step 3: Build the Decision Map (before prose)

For each key decision fill one row. This is the raw material; it often reveals the story.

| # | Tension | Options considered | Who wanted what | My call and why | Cost / trade-off | Outcome signal |

Also draft the **responsibility map** (Owned / Led through others / Influenced / Consulted / Did not do) and the **evidence table** (Claim | Evidence type | Source | Confidence | Shareability). Details in `references/evidence-and-metrics.md`.

### Step 4: Write the long-form case study

Use the canvas in `references/case-study-canvas.md`. Write long first, then compress (Career Strategy Lab method: a 2,000-word draft is fine as source; every section then gets a tweet-length headline, and the headlines alone must tell the story). The sections:

1. **Descriptive title** (what, where, at what scale), e.g. "Rebuilding a regional telco's design practice while replatforming 3 apps", never just a client name.
2. **Signal strip**: role, team, timeline, scale, outcome type.
3. **30-second skim** (answer first): mandate, what I did, what changed, the hardest call.
4. **The mandate and the tension**: what was at stake, why it was hard (Situation, Complication).
5. **My role and team**: responsibility map, team composition, credits.
6. **Key decisions**: 3-5 decision blocks from the Decision Map, each with the options and the trade-off.
7. **How I led**: the leadership moves (up, across, down): alignment, operating model, team building, quality bar, coaching. Show artifacts (rituals, frameworks, decision records).
8. **The messy middle**: what broke, what was conceded, what changed my mind.
9. **Outcomes**: product, business, team/org, and at least one counter-metric or trade-off.
10. **What I'd do differently and what I reuse**: lessons and the reusable pattern.

Keep one or two craft moments visible (a flow the user personally designed, a critique that changed the work) so the reader sees a player-coach, not a manager who has drifted from the work.

### Step 5: Derive the formats

From the long form, produce the formats the user needs (default: skim + long form + deck outline):
- **30-second skim** (web portfolio card or top of page)
- **Web/Notion long form** with scannable headings (headings must carry the story on their own)
- **Deck outline** for a panel (slide by slide; 2-3 bullets and 1-2 visuals per slide) using `references/presentation-guide.md`
- **Talk tracks**: 60 seconds, 5 minutes, and the section-level notes for a 20-25 minute slot
- **Resume bullets** (2-3) and **cover letter proof sentence** harvested from the story, so all materials match
- **Likely panel questions** with answer outlines

If the user wants an actual deck, hand the outline to a slides/pptx or presentation-design skill. For interview delivery practice and cross-story narrative, use `leadership-storytelling` if available.

### Step 6: Ruthless review

Score against `references/quality-rubric.md` (seniority signals, balance, messy truth, business link, attribution, evidence, clarity). Then run the skeptic pass: list the 5 claims easiest to shoot down and repair each with evidence, softer wording, or removal. Report the score and the repairs briefly.

**Final scrub (every deliverable, including notes and decks).** Em dashes (—) and en dashes used as dashes (–) are the most common thing that slips through, because they feel natural mid-draft. Before delivering, search every output file for them and replace with a comma, colon, period, or parentheses, e.g. `grep -c "—\|–" <file>` must return 0. Hyphens in compound words and date ranges written with a plain hyphen ("2022 - 2024") are fine.

### Step 7: Deliver

Default: Markdown file(s) (portfolio-ready), plus the evidence table and open placeholders listed at the top. Offer .docx or a deck when useful. Chat summary: one sentence on what the story proves, plus what needs the user's input.

## Style rules

- No em dashes. Commas, colons, periods.
- No banned words: seamless, delighted users, game changer, significant improvement, leveraged, synergy, passion for, excited to, holistic, robust, empower, elevate, unlock, journey (metaphorical), world-class.
- "I" for the user's actions, "the team" or names/roles for others. Never "it's just".
- Numbers with baseline, timeframe, and attribution limits.
- Headings are informative sentences, not labels ("We cut the approval chain from 5 steps to 2", not "Process").

## Adjacent skills

- `principal-head-experience-ai-portfolio-architect`: whole-portfolio architecture, AI governance dossier, visual system. Use it for the portfolio; use this skill for each leadership case study inside it.
- `leadership-resume-architect`: case study outcomes become resume bullets; keep them consistent.
- `leadership-storytelling`: interview delivery, story bank across projects, walking deck, 30-60-90 plans.
- `bespoke-cover-letter`: harvest one proof sentence per case study.

## Reference files

| File | Read when |
|---|---|
| `references/case-types.md` | Step 2: case type, level calibration |
| `references/case-study-canvas.md` | Step 4: full template with section guidance and examples |
| `references/evidence-and-metrics.md` | Steps 3-4: leadership metrics catalog, evidence table, confidentiality patterns |
| `references/presentation-guide.md` | Step 5: panel deck structure, talk tracks, question bank |
| `references/quality-rubric.md` | Step 6: scoring and skeptic pass |
| `references/research-basis.md` | When the user asks why a rule exists |
