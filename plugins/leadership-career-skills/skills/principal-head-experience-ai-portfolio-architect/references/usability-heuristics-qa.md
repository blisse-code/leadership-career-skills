# Usability Heuristics QA

## Portfolio Interface Heuristics

Review the portfolio interface itself using NN/g heuristics. This is separate from content quality.

---

## Heuristic 1: Visibility of System Status

### Checks

- [ ] Navigation state is always visible (where am I?)
- [ ] Progress within long content is indicated (reading position)
- [ ] Current section is highlighted in TOC/nav
- [ ] Loading states exist for any async content
- [ ] Filter/sort state is visible when applied

### Fixes

| Issue | Fix |
|-------|-----|
| No nav highlighting | Add active state to current nav item |
| Lost in long page | Add sticky TOC or progress indicator |
| No filter feedback | Show active filters as chips/badges |

---

## Heuristic 2: Match Between System and Real World

### Checks

- [ ] Section labels use plain language, not internal jargon
- [ ] Technical terms are defined on first use
- [ ] Navigation labels match reader mental models
- [ ] Evidence tier labels are self-explanatory
- [ ] Role chips have intuitive meanings

### Fixes

| Issue | Fix |
|-------|-----|
| Jargon in headings | Replace with plain language equivalents |
| Unexplained acronyms | Add inline definition or tooltip |
| Confusing labels | User test labels with non-designers |

### No Insider Acronyms Rule

On first mention, unpack any acronym:
- "SCQA (Situation, Complication, Question, Answer)"
- "MECE (Mutually Exclusive, Collectively Exhaustive)"
- "ACI (Agent-Computer Interface)"

---

## Heuristic 3: User Control and Freedom

### Checks

- [ ] Clear exits from any state (back, close, home)
- [ ] Back-to-list always accessible from case study pages
- [ ] Jump links allow skipping sections
- [ ] Undo available for any filter/sort actions
- [ ] No forced sequential reading

### Fixes

| Issue | Fix |
|-------|-----|
| No back button | Add persistent back-to-list link |
| Trapped in long content | Add section jump links |
| Forced linear path | Allow random access to any section |

---

## Heuristic 4: Consistency and Standards

### Checks

- [ ] Link styling is consistent throughout
- [ ] Heading hierarchy is consistent (H1 > H2 > H3)
- [ ] Button styling is consistent
- [ ] Evidence chips use consistent format
- [ ] Component reuse is systematic

### Link Styling Requirements

- [ ] Links look like links (underline or distinct color)
- [ ] Visited vs unvisited distinguishable
- [ ] Hover state provides feedback
- [ ] Focus state visible for keyboard users

### Heading Consistency

| Level | Usage | Max per page |
|-------|-------|--------------|
| H1 | Page title | 1 |
| H2 | Major sections | 5-8 |
| H3 | Subsections | As needed |

---

## Heuristic 5: Error Prevention

### Checks

- [ ] No broken links
- [ ] No missing images
- [ ] No dead-end pages
- [ ] Form validation (if contact form exists)
- [ ] No confusing navigation paths

### Link Audit Process

1. Crawl all internal links
2. Verify external links work
3. Check image sources load
4. Test all nav paths

---

## Heuristic 6: Recognition Rather Than Recall

### Checks

- [ ] Persistent TOC visible on long pages
- [ ] Labels are clear without requiring context
- [ ] Evidence is inline, not hidden
- [ ] No hidden navigation

### Fixes

| Issue | Fix |
|-------|-----|
| TOC not visible | Make TOC sticky |
| Vague labels | Add descriptive text |
| Evidence hidden | Show evidence inline or one click away |

---

## Heuristic 7: Flexibility and Efficiency

### Checks

- [ ] Quick access to key content (shortcuts)
- [ ] Filterable case study index
- [ ] Jump links for power users
- [ ] Both skim and deep reading supported

---

## Heuristic 8: Aesthetic and Minimalist Design

### Checks

- [ ] No flashy template behavior competing with content
- [ ] Visual design serves content, not vice versa
- [ ] No decorative elements without purpose
- [ ] Whitespace used appropriately
- [ ] Information density is balanced

### Anti-Patterns to Avoid

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| Heavy hero animations | Delays content access | Reduce or remove |
| Experimental scrolling | Disorienting | Use standard scroll |
| Novelty interactions | Increases effort | Use conventional patterns |
| Dense text walls | Unreadable | Add structure, whitespace |

### Time-to-First-Case-Study Rule

User can reach a case study from landing within one obvious action.

---

## Scannability Enforcement

### Layer-Cake Scanning Test

Read only the headings. Do they tell the story?

**Fail**: "Background", "Process", "Solution", "Impact"
**Pass**: "47% of trial users never completed setup", "Progressive disclosure solved the expertise assumption", "Completion rate doubled within 6 weeks"

### Heading Quality Checklist

- [ ] Headings carry meaning without reading paragraphs
- [ ] No generic headings ("Process", "Solution", "Impact")
- [ ] Headings are specific to this case study
- [ ] Subheadings support scanning

### Heading Rewrite Examples

| Before (vague) | After (informative) |
|----------------|---------------------|
| "Background" | "Enterprise SSO with compliance requirements" |
| "Process" | "Why we rejected the obvious redesign" |
| "Solution" | "Progressive disclosure for expert-novice split" |
| "Impact" | "Completion doubled, support tickets dropped 40%" |

---

## Legibility and Readability

### Checks

- [ ] Minimum default font size (16px body)
- [ ] No tiny text anywhere
- [ ] Text not embedded as images
- [ ] Sufficient contrast (WCAG AA minimum)
- [ ] Line length 65-75 characters for long-form

### Contrast Requirements

| Element | Minimum contrast ratio |
|---------|----------------------|
| Body text | 4.5:1 |
| Large text (18px+ or 14px bold) | 3:1 |
| Links | Distinguishable from body + 4.5:1 |
| Focus indicators | 3:1 against adjacent colors |

---

## Motion Rules

### Checks

- [ ] Motion communicates state change or provides feedback
- [ ] No auto-playing motion competing with reading
- [ ] Reduced-motion mode available
- [ ] Motion has clear purpose (not decoration)

### Motion Purpose Requirement

Every animation must have a labeled purpose:

| Motion | Purpose |
|--------|---------|
| Accordion expand | Orientation (shows content relationship) |
| Hover state | Feedback (confirms interactivity) |
| Page transition | Orientation (shows navigation) |

---

## Portfolio Format Restraint

### Checks

- [ ] Content-first design
- [ ] No visual design obstructing consumption
- [ ] Case studies accessible quickly
- [ ] No forced sequential experience

### Format Audit

| Question | Answer |
|----------|--------|
| Can I reach a case study in one click from home? | |
| Is the navigation immediately clear? | |
| Does visual design compete with content? | |
| Are there any "wow" moments that delay content? | |

---

## Portfolio Usability Test Protocol

### 5-Reader Comprehension Test

Test with 5 readers across archetypes:
1. Recruiter (skim perspective)
2. Designer peer (craft perspective)
3. PM (collaboration perspective)
4. Engineer (technical respect perspective)
5. Exec (business perspective)

### Standardized Feedback Form

| Question | Response |
|----------|----------|
| What is this person's main strength? | |
| What questions remain after reading? | |
| What was confusing? | |
| What was missing? | |
| Where did you get lost or stuck? | |
| How credible does this feel? | |
| Would you want to interview this person? | |

### Revision Rule

Fix the top 3 confusion points before final packaging.

---

## Final QA Checklist

### Content QA

- [ ] No em dashes (use commas or parentheses)
- [ ] Every metric has source or `[Need Human Review]`
- [ ] Every claim has evidence row or is removed
- [ ] Every AI claim includes evaluation and guardrails
- [ ] No banned phrases
- [ ] No insider acronyms without definition

### Visual QA

- [ ] Contrast meets WCAG AA
- [ ] Links distinguishable from body text
- [ ] Focus states visible for all interactive elements
- [ ] Typography scale consistent
- [ ] Spacing rhythm consistent
- [ ] All interaction states defined

### Navigation QA

- [ ] No broken links
- [ ] No dead-end pages
- [ ] Back/home always accessible
- [ ] TOC visible on long pages
- [ ] Time-to-first-case-study is one click

### Motion QA

- [ ] Motion has purpose
- [ ] Reduced-motion fallback exists
- [ ] No auto-playing animations competing with content

---

## Iteration and Maintenance Protocol

### Feedback Loop

1. Use skill to build initial portfolio
2. Test with 5 readers using protocol above
3. Identify top 3 confusion points
4. Fix and retest specific issues
5. Repeat until no major confusion points

### Maintenance Protocol

| Cadence | Action |
|---------|--------|
| Monthly | Check for broken links |
| Quarterly | Review metrics for accuracy |
| Annually | Full content refresh |
| Per project | Add new case studies, archive old ones |

### Continuous Capture

- Document artifacts and outcomes as projects complete
- Save decision logs and evidence immediately
- Don't wait to reconstruct from memory
