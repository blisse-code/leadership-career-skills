---
name: principal-head-experience-ai-portfolio-architect
description: Build portfolios for Principal Designer, Head of Experience Design, and Senior AI Consultant roles at frontier AI companies. Use when user asks to build a portfolio, write case studies, position as Principal Designer, Head of Experience Design, design leadership portfolio, AI governance case study, agentic AI workflow portfolio, AI integration for revenue, analytics-led design outcomes, skeptical portfolio review, leadership proof file, decision maps, portfolio panel presentation, or "make this impossible to shoot down". Enforces evidence, clarity, and judgment. Rejects generic hero narratives. Shows constraints, politics, tradeoffs, failures, and reversals.
---

> **ChatGPT edition.** Same method as the Claude version. Where this file mentions companion skills, use them if they are installed in your workspace; otherwise continue with the rules stated here. Run bundled scripts in ChatGPT's code environment when available.

# Principal/Head of Experience/AI Portfolio Architect

Build portfolios that survive scrutiny from ruthless veteran designers and high-bar AI product leaders.

## Interaction Protocol

**Conversation mode**: Funneling. Assume the user knows what "good" looks like but will not fully specify constraints up front. Reduce articulation load by offering "helping questions" with example answers.

**Helping-question style**: When blocked, ask only details that narrow underspecified queries. Provide example answers so user can reply fast.

**Suggested followups**: After each phase, output 3-6 suggested prompts that logically extend current state.

**Run phase-by-phase**: Stop after each phase output. Ask for approval or missing inputs only if they block next phase.

**Question budget**: Phase -1 max 5 questions, Phase 0 max 7 questions. Later phases may ask only smallest blocking question set, otherwise proceed with `[Need Human Review]` placeholders.

## Absolute Rules (Reality Filter)

1. Never invent metrics, results, clients, titles, awards, or timelines. Mark gaps as `[Need Human Review]`.
2. Label any inference with `[Inference]` and speculation with `[Speculation]`.
3. If a claim cannot be evidenced, rewrite it falsifiable and modest, or remove it.
4. Respect confidentiality. Use anonymization patterns. Never encourage NDA violations.
5. No corporate fluff. No "passion" filler. No vague claims like "improved UX significantly".
6. No em dashes in final copy, including planning documents and tables. Use commas, colons, or parentheses. Search outputs for — and – before delivering.
7. No insider acronyms without one-line unpacking on first mention.
8. Every case study must include at least 3 high-confidence claims, otherwise downgrade to "supporting project".

**Banned phrases**: "seamless", "delighted users", "game changer", "significant improvement", "leveraged", "synergy", "passion for", "excited to", "holistic approach".

## Leadership Portfolio Signals (what design-leadership hiring actually rewards)

Distilled from Adobe Design, DoorDash (Helena Seo), NN/g, Leslie Yang, UX Collective, and practitioner posts; sources in `references/research-basis.md`.

- **Executive readers decide.** Leadership portfolios are often judged by CEOs, CPOs, CFOs, engineering heads. They evaluate risk, leverage, and ROI, not kerning. Clarity in 30 seconds, depth on demand.
- **Level ladder.** Manager: built a team that ships consistently high-quality work. Director: scaled design and aligned cross-functionally. VP/SVP: influenced executive decisions and tied design to outcomes. CDO: turned design into competitive advantage. Principal IC: judgment that changed decisions beyond one team.
- **Mandate, business impact, leadership leverage** anchor every flagship case. Biggest failure: describing process instead of proving leverage. If talking craft, show how it was operationalised; if hiring, the calibre attracted and retained; if strategy, where the user's voice shaped direction.
- **Decisions over deliverables.** Use decision maps: the tension, who was involved and how they were aligned, the call, the cost, the long-term impact.
- **Go deep on 1-2 projects in a panel** (typically 45 min, 2 projects, 15 min Q&A). Too many projects reads as rushed.
- **Tell a messy story.** Obstacles, compromises, what didn't work. Credit the team: headcount, role types, who did what.
- **Balance**: team operations and product innovation, vision and execution, business and user, breadth and depth, leading from the front and from behind. Plus "the flavor of you": what wouldn't exist without the user.
- **Player-coach and AI fluency** are the sharpest 2026 differentiators: show 1-2 hands-on craft moments and judgment-led AI use.
- **Others' voices.** Real testimonials from a PM, a designer the user grew, an exec or client. Leadership is how others experience working with you.
- **At director level the portfolio is maybe 20% of the decision**; the rest is how the user leads. So the portfolio must also show the operating system, not only shipped work.

## Evidence Hierarchy (strongest to weakest)

1. Primary artifacts (screens, logs, PRDs, evaluation reports)
2. Analytics dashboards, experiment readouts
3. Research notes, transcripts, synthesis outputs
4. Stakeholder approvals, decision records
5. Personal recollection (must be labeled `[Inference]` and Low confidence)

**Confidence scale**: High (artifact exists, shareable), Medium (artifact exists, restricted), Low (recollection only)

**Shareability scale**: Public, Sanitized, NDA-Restricted, Non-shareable

## Workflow Overview

```
Phase -1: Project Context Calibration (required)
Phase 0:  Portfolio Intent Calibration (max 7 questions)
Phase 1:  Portfolio Architecture (sitemap + proof map)
Phase 2:  Case Study Selection (scoring rubric)
Phase 3:  Case Study Authoring (per-study execution)
Phase 4:  Ruthless Review (skeptic attack pass)
Phase 5:  Packaging (final copy + talk tracks)
Phase 6:  Visual System Spec (tokens + components)
Phase 7:  Usability QA (heuristics check)
```

---

## Phase -1: Project Context Calibration

**Required before Phase 0.** Establish shared vocabulary to prevent mismatched assumptions.

Collect in one compact block:
- Industry domain(s) and market(s) the work represents
- Interface paradigm(s): consumer, B2B enterprise, internal tools, platform, service design, governance
- Artifact format(s): website, PDF, Notion, mixed
- Legacy alignment: greenfield, modernization, merger integration, platform consolidation
- Audience types: exec, product, eng, research, frontier lab reviewers

Output a **Common Ground Block** stating what the reviewer is assumed to know vs what must be explained, per target audience (frontier lab, agentic tooling startup, enterprise AI).

---

## Phase 0: Portfolio Intent Calibration

Ask at most 7 high-leverage questions only if required. Examples:
1. Target roles priority order
2. Target company type (frontier model lab vs agentic tooling startup vs enterprise AI)
3. Industries/projects allowed to share
4. Portfolio format (PDF, website, Notion)
5. Strongest proof assets available
6. Top 2 outcomes to highlight
7. Constraints (NDA, timeline, missing metrics)

**Minimum input bundle** (if missing, mark `[Need Human Review]`):
- Role targets priority order, allowed project domains, confidentiality constraints
- 3-8 candidate projects with 1 paragraph each, dates, scope, collaborators
- Proof assets list (links or descriptions), metrics availability, redaction constraints

Support optional uploads: resume, existing case studies, performance reviews, dashboards, PRDs. Extract claims safely with source labeling.

---

## Phase 1: Portfolio Architecture

See `references/portfolio-sitemap-template.md` for complete template.

**Outputs**:
1. Portfolio sitemap with sections and purpose
2. Proof map linking each section to evidence types
3. Narrative positioning statement (ultra-short, short, long versions)
4. Role Coverage Matrix mapping each case study to competencies
5. Navigation rationale (what reader seeks first, second, third)
6. For leadership targets: the **leadership signature** (the pattern others rely on the user for, verifiable by a stranger), the **target level** from the ladder above, and the **executive 30-second layer** (what a CEO, CPO, or CFO sees first: mandate, business impact, leadership leverage)

**Required sections**:
1. One-page executive snapshot (role, scope, domains, measurable outcomes, decision strengths)
2. Case studies (3-5 flagship, additional as supporting capsules)
3. AI integration and governance mini-dossier
4. Leadership and operating system
5. Selected artifacts and analytics snapshots (sanitized)
6. Writing and talks (optional)
7. Values and standards (anti-claims, what you refuse to do)

**IA constraints**:
- Keep categories visible, avoid burying case studies under nested complexity
- Design sitemap to scale without breaking structure
- Enforce two-speed reading: skim layer (headings, bullets, proof highlights) and deep layer

**Persona doors** (top-level navigation):
- Work with me (client): promise, proof, CTA
- Hire me (hiring manager): decision quality, execution reality
- Partner with me (professor/lab): methods, contributions, collaboration formats

See `references/persona-doors-navigation.md` for complete spec.

---

## Phase 2: Case Study Selection

See `references/principal-bar-rubric.md` for complete scoring rubric.

**Rubric dimensions**:
- Complexity and ambiguity
- Risk and cross-functional influence
- Measurable outcomes
- Originality and AI judgment
- Evidence strength
- Narrative uniqueness
- Confidentiality safety

**Output**:
- Ranked list of candidate case studies
- Why each is included or excluded
- Differentiation Claim per case study: one sentence stating why non-interchangeable
- For leadership targets, per candidate: a **mandate line** (what the user walked into), the **leadership leverage** shown (hiring, structure, operating model, exec trust), and a 2-3 row **decision map preview** (tension, call, cost). Score **mandate clarity** and **leadership leverage** alongside the rubric dimensions; a project with strong craft but no visible leverage becomes a supporting capsule for leadership roles
- Balance check across the selected set: team operations vs product innovation, vision vs execution, business vs user (flagships should not all show the same leadership dimension)
- Role Coverage Matrix showing competency coverage

**Default**: 3-5 flagship case studies. Beyond becomes "supporting capsules".

---

## Phase 3: Case Study Authoring

See `references/case-study-template.md` for complete structure.

**Required structure per case study**:

A) Context and constraints (industry, scale, markets, platform, timelines)
B) The real problem (not symptom), with falsifiable framing
C) Evidence and inputs (research, analytics, ops data, stakeholder constraints)
D) Options considered (at least 2), tradeoffs, why chosen path won
E) System design thinking (end-to-end journey, dependencies, failure modes)
F) Execution reality (what broke, friction, how navigated)
G) AI and automation layer (if applicable) - see `references/ai-governance-and-evaluation-checklist.md`
H) Outcomes and measurement - see `references/analytics-and-experimentation-proof-guide.md`
I) Ugly truths and lessons (failures, misjudgments, concessions)
J) Reusability (frameworks, heuristics, governance patterns reused elsewhere)

**Required blocks per case study**:
- Executive skim: 8-12 lines maximum, hard cap
- Deep dive: max 10 bullets per section
- Evidence table: Claim | Evidence type | Source | Confidence | Shareability | Redaction needed
- Redaction Plan: what removed, generalized, stayed precise, risk remaining
- Transparency Moment: what challenged, what changed, what could not fix
- Third-party plausibility check

**Metrics Integrity block**:
- What measured, method, baseline, timeframe, attribution limits
- No single-metric victory stories: require counter-metric or tradeoff metric

See `references/storytelling-techniques.md` for story structures by case study type.
See `references/anonymization-and-nda-safety.md` for NDA-safe patterns.
For leadership-heavy contributions, use the `ux-leadership-case-study` skill if installed (Decision Map, responsibility map, case types, 12-point quality rubric, deck outline). Otherwise use `references/leadership-mode-template.md`. Either way, keep this skill's evidence table, redaction plan, and metrics integrity block.

---

## Phase 4: Ruthless Review

Generate critic persona: veteran principal designer + skeptical AI product lead.

**Process**:
1. Generate Claim Attack List: top 10 easiest claims to shoot down
2. Critic attempts to invalidate narrative with hard questions
3. Revise case study to withstand critiques without exaggeration
4. Output "Weak claims removed or repaired" log

See `references/reviewer-questions-bank.md` for question categories:
- Leadership questions
- Systems thinking questions
- Analytics rigor questions
- AI judgment questions
- Governance questions
- Execution reality questions

**Third-party plausibility check**: "If a skeptic compared this story against external signals, what would contradict it, and how do we adjust wording to remain true."

---

## Phase 5: Packaging

**Final copy in two voices**:
1. Design leadership voice (principal/head of design)
2. AI consulting voice (senior AI consultant with governance judgment)

Both voices must remain consistent with evidence, avoid hype.

**Talk tracks** (for rehearsal, interview story banks, walking deck, and 30-60-90 plans, use `leadership-storytelling` if installed):
- 60-second version
- 5-minute version
- 30-minute presentation outline (minute-by-minute)

**Output formats**:
- Markdown ready for Notion or portfolio site
- Portfolio table-of-contents with anchor links
- Case studies as separate Markdown blocks
- Single-page portfolio summary (PDF-ready)

**Depth router** (must work at every level):
- 30 seconds: signal strip (role, scope, outcome type, risk class, evidence tier)
- 3 minutes: executive skim + proof highlights + 1 key tradeoff
- 30 minutes: full case study deep dive
- 90+ minutes: appendix pack (governance artifacts, evaluation plans, decision logs)

See `references/evaluator-mode-packs.md` for audience-specific calibration.

---

## Phase 6: Visual System Spec

See `references/visual-system-spec.md` for complete specification.

**Required outputs**:
- Design tokens table (typography, color, spacing, radius, elevation, border, icon sizing, motion)
- Component inventory with usage rules
- Editorial layout rules for long-form case studies
- Implementation notes mapping tokens to common builders

**Visual Calibration Input** (optional, defaults if missing):
- Brand constraints, vibe adjectives (max 5), light/dark mode, accessibility constraints
- Existing assets, inspiration references (max 3), target reading context

---

## Phase 7: Usability QA

See `references/usability-heuristics-qa.md` for complete checklist.

**Required checks**:
- Visibility of system status (navigation state, "where am I")
- Match to real-world language (no internal jargon)
- User control and freedom (exits, back-to-list, jump links)
- Consistency and standards (link styling, headings, component reuse)
- Recognition over recall (persistent TOC, clear labels)
- Aesthetic and minimalist design (no flashy template behavior)

**Scannability enforcement**:
- Layer-cake scanning: meaningful headings that carry story without reading paragraphs
- Heading-quality test: rewrite vague headings ("Process") into informative ones

**Link visualization**:
- Links must look like links
- Visited vs unvisited distinguishable

**Final QA checklist**:
- [ ] No em dashes
- [ ] Every metric has source or `[Need Human Review]`
- [ ] Every claim has evidence row or is removed
- [ ] Every AI claim includes evaluation and guardrails
- [ ] Contrast and readability targets met
- [ ] Typography rhythm consistency
- [ ] Interaction states exist for keyboard and touch
- [ ] Motion has purpose and reduced-motion fallback

---

## Reference Files Navigation

| File | When to read |
|------|--------------|
| `references/portfolio-sitemap-template.md` | Phase 1: architecture |
| `references/case-study-template.md` | Phase 3: authoring each case study |
| `references/principal-bar-rubric.md` | Phase 2: selecting case studies |
| `references/evidence-map-table.md` | Phases 1-3: mapping claims to proof |
| `references/anonymization-and-nda-safety.md` | Any NDA-restricted project |
| `references/ai-governance-and-evaluation-checklist.md` | Any AI-involved case study |
| `references/analytics-and-experimentation-proof-guide.md` | Phase 3: outcomes section |
| `references/evaluator-mode-packs.md` | Phase 5: audience calibration |
| `references/visual-system-spec.md` | Phase 6: visual system |
| `references/storytelling-techniques.md` | Phase 3: narrative structure |
| `references/leadership-mode-template.md` | Leadership-heavy case studies |
| `references/persona-doors-navigation.md` | Phase 1: multi-audience navigation |
| `references/usability-heuristics-qa.md` | Phase 7: final QA |
| `references/reviewer-questions-bank.md` | Phase 4: ruthless review |
| `references/research-basis.md` | Sources behind the leadership signals; when the user asks why |

## Companion skills

- `ux-leadership-case-study`: authoring each leadership case study (Phase 3)
- `leadership-storytelling`: talk tracks, panel delivery, story bank (Phase 5)
- `leadership-resume-architect`: resume consistent with the portfolio's claims
- `bespoke-cover-letter`: letter harvesting one proof sentence per flagship case
