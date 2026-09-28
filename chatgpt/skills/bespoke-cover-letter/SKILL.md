---
name: bespoke-cover-letter
description: "Write a bespoke cover letter for a specific job posting, synthesizing 8 writing and positioning skills against the user's profile, resume, and case studies. Trigger on requests to write a cover letter, application letter, motivation letter, letter of interest, or job application, including Lead, Principal, Manager, Director, Head, VP, and executive design or UX leadership roles, where it proves mandate, business impact, and leadership leverage instead of listing duties. Also trigger when a job URL is paired with any writing request. Output as .docx."
---

> **ChatGPT edition.** Same method as the Claude version. Where this file mentions companion skills, use them if they are installed in your workspace; otherwise continue with the rules stated here. Run bundled scripts in ChatGPT's code environment when available.

# Bespoke Cover Letter

Orchestrates 8 skills into a single cover letter that reads like a human wrote it at the top of their ability. Not a template. Not a merge-field exercise. A bespoke argument for one person at one company for one role.

## When to use

Any time the user asks to write a cover letter, application letter, or letter of interest for a specific role. Also trigger on "write my application", "cover letter for [company]", "apply to this role", or any job URL paired with a writing request.

## Prerequisite skills (load all 8 before drafting)

These skills compose in a specific order. Load the ones that are installed; the synthesis rules below restate each one's essentials, so if a skill is missing (or you are running outside Claude), apply its rules from this file and carry on.

| Skill | Role in the letter |
|---|---|
| `leverage-craft` | **Structural spine.** The 7 moves (cold open, factual ground, specific receipt, quiet virtue reveal, surgical understatement, forced binary/landing line, cold close) define the letter's skeleton |
| `writing-constitution` | **Voice rules.** No em dashes, burstiness, grade 6-7 readability, banned vocabulary, authority implied never claimed, no engagement bait, acid test |
| `fable-writing-standard` | **Prose quality gate.** Every claim needs evidence/example/mechanism. Banned AI-marker vocabulary. Rhythm monotony check. No hedging |
| `elite-communication-codex` | **Density and authority.** SPEAR framework (Point, Picture, Proof, Push). Kill qualifiers. Lexicon engineering. Atomic wording |
| `headline-craft` | **Opening line.** Observant + Strong Opinion technique for the cold open. Anti-patterns enforced (no "Introducing", no "Unlock/Unleash/Elevate") |
| `cognitive-bias-index` | **Persuasion layer.** Halo Effect (hero credential first), Von Restorff (distinctive opener), Loss Aversion (cast hesitation as loss), Peak-End Rule (end on strongest beat). Cap at 3 biases per letter |
| `principal-head-experience-ai-portfolio-architect` | **Reality filter.** No invented metrics. No corporate fluff. Honest domain gap acknowledgment. Banned phrases enforced. Evidence hierarchy applied |
| `design:ux-copy` | **Sentence-level clarity.** Clear, concise, consistent, useful, human. Every sentence does one job |

## Workflow (strict order)

### Phase 1: Gather inputs

1. **Job description.** Read the full posting. If the user provides a URL, fetch it. Extract: company, role title, team, reporting line, key responsibilities, stated principles, required experience, preferred experience, company mission phrases, and any distinctive language the posting uses.
2. **User profile.** Use what the user has shared: uploaded resume or notes, earlier messages in this chat, and anything ChatGPT memory holds about their work history, skills, location, and job search context. Extract: current role and title, years of experience, industries and markets, notable projects with specifics (numbers, outcomes, methods), design philosophy, location and relocation posture, citizenship/visa status if relevant.
3. **Sibling artifacts.** If the conversation or the user's files contain a tailored resume, leadership case studies, or an interview story bank (from `leadership-resume-architect`, `ux-leadership-case-study`, `leadership-storytelling`), read them. Harvest proof points from them rather than re-deriving, so every claim in the letter matches the resume word for word on titles, dates, and numbers. Mismatches are the most common reference-check failure.
4. **Level calibration.** Decide whether the role is a leadership role (reports, budget, org building, "Head", "Director", "Principal", "VP") and at what level. If yes, apply "Leadership-role calibration" below.
5. **Gap analysis.** Map the job's requirements against the user's profile. Identify: direct matches (proof exists), adjacent matches (proof exists in a neighboring domain), honest gaps (no proof, acknowledge openly), and unique strengths the posting did not ask for but the user brings.

### Phase 2: Architect the argument

Build the letter skeleton using **Leverage Craft's 7 moves** mapped to cover letter format:

| Move | Cover letter function |
|---|---|
| 1. Cold Open | Lead with THEIR problem, not your excitement. Open with the company's design tension or the hardest unsolved problem the role exists to fix. No "Dear Hiring Manager", no "I am thrilled to apply" |
| 2. Factual Ground | One verifiable observation about the company, product, or market (from the posting or public sources). No adjective, no adverb. Never guess at the company's internal history ("each was likely built by a different team"): a wrong guess about their org reads as presumptuous |
| 3. Specific Receipt | Your concrete proof. Number, date, count, named project. Specificity kills plausible deniability |
| 4. Quiet Virtue Reveal | Show what you have been doing right. Do not claim virtue. Let the reader supply the moral verdict |
| 5. Surgical Understatement | Clinical vocabulary for charged moments. Especially for domain gaps: state them cold, then bridge them |
| 6. Forced Binary / Landing Line | One bold sentence that forces a decision or sticks in the head. This is the letter's climax |
| 7. Cold Close | First name only. No "I look forward to hearing from you". No "Thank you for your consideration" |

**Paragraph plan (typical 7-8 paragraphs, single page):**

1. **Cold open paragraph.** Their problem. The design tension the role exists to resolve. Written as if you already understand the product at a user level. (Moves 1+2)
2. **Bridge sentence.** Connect their problem to your career arc in one sentence. (Move 2)
3. **Primary proof paragraph.** Your most directly relevant project. Specific, named, with outcome data if available. Show the same design discipline the role demands. (Move 3)
4. **System-level proof.** A second proof point showing you think in systems, not screens. Design system work, cross-product governance, or platform-scale decisions. (Move 4)
5. **Player-coach proof.** Show you still do the work AND lead people. Prototyping, writing copy, running sessions, mentoring. (Move 4)
6. **Domain honesty paragraph.** If there is a gap, name it. Do not pretend. Then bridge: show why the adjacent experience transfers, why you close gaps fast, and what mental model you start from. (Move 5)
7. **Mission alignment.** Connect to the company's stated mission using their own language. If relocation is relevant, state it as a fact, not a plea, but only if the user has confirmed it; otherwise insert `[Need Human Review: relocation/work authorisation line]` rather than asserting it. (Move 2)
8. **Landing line.** One bold, specific, time-bound sentence. Bold formatting. (Move 6)
9. **Sign-off.** First name only. (Move 7)

Adjust paragraph count based on how much proof the user has. Never pad. If 6 paragraphs say everything, use 6.

### Leadership-role calibration

For leadership roles the reader is often not a designer (CEO, CPO, CFO, engineering heads). They evaluate risk, leverage, and return. Adjust the proof paragraphs:

| Level | The letter must make obvious |
|---|---|
| Lead / Principal / Staff | Judgment that changed decisions beyond one team; standards others adopted; still hands-on |
| Manager | Built a team that ships consistently high-quality work |
| Director | Scaled design and aligned cross-functionally |
| Head / VP | Influenced executive decisions and tied design to business outcomes; built the capability |
| CDO | Turned design into competitive advantage |

- **Primary proof paragraph** becomes **mandate, move, measure**: what the user walked into, the leadership move others would not have made, what changed for the business.
- **System-level proof** shows leadership leverage: who they hired, how they structured the team or operating model, how they raised the bar, how they earned exec trust.
- **Player-coach proof** stays: 2026 hiring favours leaders who inspire through the work. One concrete craft moment.
- **Messy truth beats a clean story** (Adobe design leaders): one line on a real trade-off or concession reads as judgment. Pairs naturally with Surgical Understatement.
- **Credit the team.** "I led the 12-person team that..." rather than "I built...". Attribution honesty is itself a leadership signal.
- **Balance** (DoorDash): across the letter show both business and user, vision and execution, team operations and product.
- For first-time leaders: lead with the leadership signature, the pattern others already rely on them for without the title, and one story of leading without authority.
- If a 30-60-90 view helps, one sentence of "what I'd do first" can replace the mission paragraph. Keep it humble: listen first.

### Phase 3: Draft

Write the letter applying all 8 skills simultaneously. The synthesis rules:

**Voice (from writing-constitution + fable-writing-standard):**
- No em dashes. Period, comma, or line break instead
- Burstiness: vary sentence length wildly. Two-word fragments next to 20-word compounds
- Grade 6-7 readability. Anglo-Saxon vocabulary. No "thus", "moreover", "consequently"
- Authority implied, never claimed. Never write "in my X years of experience"
- No exclamation marks. No hype scaffolding

**Banned vocabulary (merged from all skills):**
delve, tapestry, seamlessly, elevate, unlock, unleash, harness, robust, holistic, synergy, game-changer, paradigm, journey (metaphorical), landscape (metaphorical), passionate, excited to, thrilled, honored, humbled, proud to, incredibly, amazing, transformative, cutting-edge, leverage (as verb in marketing sense), innovative, disruptive, empower, foster, curate, utilize, deep dive, thought leadership, circle back, move the needle, ecosystem (metaphorical), double down, lean in, learnings, impactful, scalable (unless literally about systems), world-class, best-in-class, holistic approach, significant improvement, game changer, delighted users

**Density (from elite-communication-codex):**
- Kill every qualifier. "Very", "really", "quite", "somewhat", "fairly" are dead on arrival
- One idea per sentence. Atomic wording
- If a sentence can be split, split it

**Persuasion (from cognitive-bias-index, max 3 per letter):**
- Halo Effect: lead with the strongest credential. Everything after benefits from its glow
- Von Restorff Effect: make the opener distinctive from every other cover letter they will read that day
- Loss Aversion: frame the landing line so NOT responding feels like a miss
- Peak-End Rule: the last thing they read (landing line + cold close) shapes their memory of the whole letter

**Reality filter (from portfolio-architect):**
- Every claim must be evidenced or acknowledged as inference
- No invented metrics. If the user does not have a number, describe the mechanism instead
- Honest domain gaps stated openly. The honesty itself is the credibility signal
- Banned phrases from portfolio-architect enforced

**Clarity (from ux-copy):**
- Every sentence does one job: inform, prove, or move
- If a sentence does not do one of these three things, cut it

### Phase 4: Format as .docx

Build the document programmatically in the code environment using Python and `python-docx` (or Node.js with the `docx` package if that is what is available).

**Document specs (single page, no overflow):**
- Font: Calibri throughout
- Body text: 10.5pt, color #2D2D2D
- Name header: 17pt bold, color #1A1A1A
- Subtitle (current title): 8.5pt, color #666666
- Contact line: 8.5pt, color #666666
- Line spacing: 1.1x (264 in docx units)
- Paragraph spacing after: 140 DXA
- Margins: top 960, bottom 720, left/right 1380 DXA
- Separator: thin bottom border (#D0D0D0) after contact block
- Date: body size, color #666666
- Addressee: body size, bold
- Re: line: body size, italic, color #666666
- Landing line: body size, bold, color #2D2D2D
- Sign-off: body size, bold, color #1A1A1A

**Structure in the .docx:**
```
Name (17pt bold)
Title (8.5pt gray)
Contact info (8.5pt gray)
--- separator ---
Date
Addressee (bold)
Re: Role Title

[Body paragraphs]

Landing line (bold)

First name (bold)
```

**Single-page enforcement:** If the letter overflows to a second page, tighten in this order: reduce paragraph-after spacing, reduce line spacing, shorten the weakest paragraph, reduce margins slightly. Never go below 10pt body text or 240 line spacing.

### Phase 5: Verify

1. **Visual check.** Convert .docx to PDF (LibreOffice), render to image, and visually inspect that it fits on one page with clean whitespace at the bottom
2. **Banned vocabulary scrub.** Search the final text for every word in the banned list. Remove any that survived
3. **Em dash check.** Search for em dashes and en dashes. Replace with period or comma
4. **Acid test (from writing-constitution).** Audit every named entity. No current employer named unless cleared. No identifiable client details unless public
5. **Leverage self-check (from leverage-craft):**
   - Could a fifth-grader follow it?
   - One verifiable fact stated?
   - One specific receipt shown?
   - Virtue revealed, not claimed?
   - Binary or landing line forced?
   - Every "just", "really", "hope", "sorry" removed?
   - First sentence stands alone if rest is cut?
   - Last sentence stays in the head?
6. **Reality filter (from portfolio-architect).** Every claim has evidence or is marked as inference. No corporate fluff survived
7. **Consistency check.** Titles, dates, team sizes, and numbers match the resume and case studies in the conversation. Fix the letter, not the facts
8. **Leadership check (leadership roles only).** Mandate, business impact, and leadership leverage each appear at least once. Team credited. At least one hands-on moment

### Phase 6: Deliver

1. Write the .docx to the outputs directory
2. Give the user a download link to the .docx
3. Also paste the letter text in the chat so they can copy it
4. Provide a one-line summary of the letter's argument, not a recap of its contents

## Adaptation notes

- **Different industries.** The 7-move skeleton works for any industry. The proof paragraphs change. The domain-honesty paragraph appears only when there is a real gap
- **Non-design roles.** Replace design-specific proof types (design systems, IA, prototyping) with the equivalent in the target domain. The structural mechanics are domain-agnostic
- **When the user has no job URL.** Ask for the job description text, or the company name and role title, then search for the posting
- **When the user has limited proof.** Reduce to 5-6 paragraphs. Never pad with generic claims. A shorter, honest letter outperforms a longer, hollow one
- **Multiple letters in batch.** Run the full workflow per letter. Do not reuse body paragraphs across companies. The cold open must be company-specific every time

## What this skill does NOT do

- Resume writing (use `leadership-resume-architect` for leadership roles, `tailored-resume-generator` otherwise)
- Leadership case studies (use `ux-leadership-case-study`); whole portfolios (use `principal-head-experience-ai-portfolio-architect`)
- Interview stories and panel talk tracks (use `leadership-storytelling`)
- LinkedIn profile optimization (different medium, different constraints)
- Follow-up emails after application (different tone, different structure)

## Adjacent skills that compose well

- `leverage-craft`: the structural foundation this skill builds on
- `writing-constitution`: the voice this skill writes in
- `fable-writing-standard`: the quality bar this skill enforces
- `principal-head-experience-ai-portfolio-architect`: when the cover letter is part of a larger portfolio effort
- `headline-craft`: when the opening line needs extra work
- `cognitive-bias-index`: when the persuasion layer needs tuning for a specific audience
- `leadership-resume-architect`: write the resume first; the letter harvests its strongest proof
- `ux-leadership-case-study`: each flagship case study yields one letter-ready proof sentence
- `leadership-storytelling`: the signature story often becomes the cold open