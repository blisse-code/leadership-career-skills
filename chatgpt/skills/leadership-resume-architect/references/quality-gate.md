# Quality Gate

Run every check. Fix, then re-run the ones that failed. Report the results briefly to the user in the evidence log, not in chat.

## 1. The 7-second scan test
Read only: name, headline, first line of summary, Selected Impact, job titles and companies. Can a stranger answer "what level, what scale, what changed"? If not, the headline or Selected Impact is wrong.

## 2. Skeptical hiring manager test
For each bullet ask: What was the user's role? Compared to what baseline? Over what time? Could this be checked in a reference call? Rewrite or cut any bullet that fails two of these.

## 3. Executive reader test (Director+)
Would a CEO, CFO, or CPO see mandate, business impact, and leadership leverage in each recent role? If a role only shows process, add the "so what".

## 4. Dimension coverage
Each recent role shows at least three of the eight dimensions (leadership-signals.md). Whole resume shows all of: business outcome, team/org building, cross-functional influence, and at least one hands-on craft signal.

## 5. Attribution check
Verbs match reality. No team outcome claimed as solo. No role hidden behind "we".

## 6. Integrity check
- Every number traced to a user-provided source, or marked `[Need number]`.
- No invented clients, titles, awards, dates.
- Titles match what the employer would confirm. If the internal title differs from the functional role, use "Official Title (functional: Head of UX)" or explain in scope line.
- Confidential client names removed or cleared.

## 7. ATS check
Exact title in headline. Priority 1 keywords present in context. Single column, standard headings, no tables or header/footer content. Run `scripts/ats_check.py` when possible.

## 8. Language check
No banned words, no em dashes, no first-person pronouns in bullets, no adjective-only summary, no bullet over 2 lines, tense consistent.

## 9. Consistency check
Titles, dates, and headline numbers match LinkedIn, portfolio, and any cover letter in the conversation. Mismatches are the most common reference-check failure.

## 10. Length and page-1 check
2 pages default for leaders; page 1 stands alone; no orphan lines on page 2.
