---
name: tailored-resume-generator
description: Analyzes a job description and tailors the user's resume or CV to it, maximizing ATS match and human-scan impact without inventing experience or metrics. Use whenever the user pastes or links a job posting and wants their resume customized, asks to "tailor", "optimize", "match", or "ATS-proof" a resume, wants multiple versions for different roles, is changing careers, or asks why their resume isn't getting callbacks. For Lead, Principal, Manager, Director, Head, VP, or executive targets, hand off to leadership-resume-architect if installed (it carries the leadership-specific rules); this skill covers everything else and the tailoring mechanics.
---

# Tailored Resume Generator

Tailoring is **reprioritizing true evidence around what one employer asked for**, in their words, so that both the applicant tracking system (ATS) and a human scanning for a few seconds see the match. It is never inventing new facts. Most candidates send one generic resume; a truthful, targeted one is the cheapest advantage in a job search (NN/g).

## Routing

- **Leadership target** (Lead, Principal, Staff, Manager, Director, Head, VP, C-level, or the JD mentions reports, budget, org building): use `leadership-resume-architect` if it is available and follow it; its rules on scope lines, leadership dimensions, and two-page length override the defaults below. If it is not installed, apply the "Senior and leadership roles" section here.
- **Everything else**: follow this skill.

## Principles

1. **Never fabricate.** No invented metrics, titles, tools, employers, or dates. When the user gives no number, write the mechanism or scale instead and flag `[Need number]` so they can supply it. (A fabricated "improved ROI by 35%" collapses at the first interview follow-up and can cost an offer after a reference check.)
2. **Mirror, don't stuff.** Use the JD's exact phrases where they are true for the candidate, inside real bullets. Keyword stuffing out of context was a trait of the worst-performing resumes in TheLadders eye-tracking study.
3. **Exact title matters.** Put the posting's exact job title in the headline when truthful (Jobscan found 10.6x more interviews when the title appears; vendor data, direction consistent across sources).
4. **Scan-first layout.** Recruiters' first pass is about 7 seconds, scanning left-edge titles. Bold titles, short bullets, clear headings, white space, single column.

## Workflow

### 1. Gather
- Full JD (fetch the URL if given), company, title.
- The user's resume or background. If missing, ask for work history, education, skills, achievements with any numbers, and certifications, with example answers to reduce effort.
- Target country (conventions differ; see step 6).

### 2. Deconstruct the job (Target Map)
Extract in the JD's words and prioritize:
- **P1 must-haves**: required, repeated, or in the title/first bullets.
- **P2 strongly desired**: "preferred", "nice to have" but emphasized.
- **P3 bonus**: implied by company context, values, product.
Capture: hard skills, methods, tools, domain, soft skills, scope indicators, culture phrases, exact title. If the user is applying to many similar roles, deconstruct 3-6 postings together and treat terms that recur as P1 (Martin Yate's Target Job Deconstruction).

Output a table: Priority | Requirement | Keyword to mirror | Candidate evidence | Gap.

### 3. Map evidence and gaps
For each requirement: direct match, transferable match (reframe honestly), or gap. Gaps get a plan: address in cover letter, bridge in summary, prepare for interview, or accept. Never paper over a P1 gap with invented content.

### 4. Structure
- **Header**: name, target title as headline, city/country, email, phone, LinkedIn, portfolio. No full address.
- **Summary** (3-4 lines): years + field, top P1 skills, domain, one proof point. No adjectives about the self ("results-driven", "passionate").
- **Skills / Core Competencies**: grouped keyword phrases from the Target Map that the candidate can substantiate. No skill bars or self-ratings (NN/g: "arbitrary, you made them up").
- **Experience**: reverse chronological; title, company, location, dates; 3-6 bullets for recent roles, fewer for older; reorder bullets by Target Map priority.
- **Education / Certifications**: one line each unless early-career.
- **Optional**: projects (technical roles), portfolio link (creative roles), publications, awards. Skip objective statements, references, photos (unless the market expects them), hobbies.

### 5. Write bullets
Pattern (Google's XYZ): **Accomplished [X] as measured by [Y], by doing [Z]**. UX variant (NN/g): [Verb] [quantitative outcome] [context] using [skill/method].
- Strong action verb, one idea, 1-2 lines, outcome or scale up front.
- Numbers where the user has them; otherwise scale (users, markets, team size, frequency) or mechanism.
- Remove: "responsible for", "helped", "worked on", first-person pronouns, em dashes, banned hype words (synergy, leverage as "use", seamless, game changer, passionate, dynamic, world-class).

### 6. Format, length, and market conventions
- Single column; standard headings; no tables, text boxes, columns, icons, or header/footer content; 10-12pt readable font; one accent color at most.
- **Length**: 1 page for under ~8-10 years or career changers (NN/g); 2 pages is fine and often better for mid-level and senior candidates (ResumeGo, 482 hiring professionals: two-page resumes preferred 2.6x for mid-level and 2.9x for managerial roles).
- **Markets**: US/Canada: resume, no photo or DOB. UK/Ireland: CV, 2 pages, personal statement. Germany/Austria/Swiss: 2-3 pages, photo and DOB customary. Nordics/Netherlands: 2 pages, modest tone. Singapore/Malaysia/India/Gulf: 2-3 pages; nationality, work-pass status, and notice period often stated. Verify with the employer when unsure.
- **Files**: .docx for ATS portals (parses best), text-based PDF for email. Offer both. If the `leadership-resume-architect` renderer (`leadership-resume-architect/scripts/render_resume_docx.py`) or the `docx` skill is available, use it for the .docx; otherwise deliver Markdown.

### 7. Quality check
- Exact title present; P1 keywords present in context.
- Every number traced to the user or flagged.
- 7-second test: headline + summary line 1 + job titles tell the match.
- Consistency with LinkedIn and portfolio (titles, dates).
- Proofread; tense consistent (present for current role).

**Final scrub (every deliverable, including notes and decks).** Em dashes (—) and en dashes used as dashes (–) are the most common thing that slips through, because they feel natural mid-draft. Before delivering, search every output file for them and replace with a comma, colon, period, or parentheses, e.g. `grep -c "—\|–" <file>` must return 0. Hyphens in compound words and date ranges written with a plain hyphen ("2022 - 2024") are fine.

### 8. Deliver
1. The tailored resume (.docx + Markdown).
2. The Target Map with remaining gaps and how to handle each.
3. `[Need number]` list for the user to fill.
4. 2-3 cover letter hooks and 3 interview stories the resume sets up.
Offer: alternate versions for other roles (facts identical, emphasis different).

## Special cases

**Career changers**: lead with relevant experience and training, reframe prior roles through the new field's lens (interviewing, data analysis, presentations, project leadership), keep older unrelated detail short. Avoid purely functional formats; hybrid (summary + relevant skills + chronological) is safer with ATS and recruiters.

**Recent graduates**: education first, projects and internships, relevant coursework; GPA if strong and recent.

**Senior and leadership roles** (fallback when `leadership-resume-architect` is unavailable): add an italic scope line under each title (team size, budget, products, markets); show leverage (what the team or business achieved through the user's direction) as well as personal craft; add a Selected Impact block of 3-5 top outcomes for Director and above; default to two pages; use honest attribution ("led the team that...").

**Technical roles**: prominent skills section, links to GitHub or work samples, methods.

**Creative and UX roles**: portfolio link in the header; outcomes over visuals in the resume itself; keep the resume ATS-plain and let the portfolio carry the design.

**Employment gaps**: state briefly and factually if asked; focus on achievements. Don't fabricate bridging roles.

## Example (bullet rewrite with limited data)

User said: "Worked with marketing on campaign analysis using SQL and Tableau."

- Weak: "Worked with marketing team on campaign analysis."
- Fabricated (never do this): "Improved campaign ROI by 35% through A/B testing."
- Honest and strong: "Built SQL + Tableau campaign dashboards used by the marketing team for weekly budget decisions `[Need number: campaigns or spend covered]`."

## Privacy
The resume contains personal data. Don't add personal details the user did not provide. Remind the user to review before sending.
