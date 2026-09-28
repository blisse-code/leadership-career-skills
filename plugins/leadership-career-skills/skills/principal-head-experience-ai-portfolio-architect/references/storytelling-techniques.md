# Storytelling Techniques

## Universal Storytelling Techniques

Apply these to all case studies regardless of type.

### Audience-First Framing

Before writing, identify what the audience cares about:

| Audience | Cares about | Frame the story to show |
|----------|-------------|------------------------|
| Exec | Business impact, risk, speed | Outcomes, decision quality, unblocking |
| Product | Tradeoffs, collaboration, shipping | Options considered, cross-functional work |
| Engineering | Feasibility, technical respect, quality | Constraints respected, edge cases handled |
| Research | Rigor, methodology, validity | Evidence quality, research integration |
| Frontier lab | Evaluation, safety, transparency | Guardrails, failure handling, honesty |

### Big Picture Hook

Connect the work to a larger trend or risk that matters, then narrow to the project.

**Template**:
```markdown
[Industry/domain] faces [macro trend or risk]. [Specific company/context] encountered this as [specific manifestation]. This case study shows [what the work addressed].
```

**Anti-pattern**: "I redesigned the checkout flow."
**Good pattern**: "Enterprise SaaS buyers increasingly expect consumer-grade UX, but compliance requirements create friction. This case study shows how we reduced checkout abandonment while maintaining audit requirements."

### Hook in 30-60 Seconds

Open with a surprising constraint, failure mode, decision dilemma, or quantified risk. Not a project overview.

**Anti-pattern**: "This project was a redesign of the onboarding experience for [Company]'s enterprise product."

**Good patterns**:
- "47% of trial users never completed setup. Not because the product was bad, but because the onboarding assumed expertise users didn't have."
- "We had 6 weeks to ship something that would take 6 months, for a client who had already fired two agencies."
- "The obvious solution would have increased support costs by $2M annually. We found a different path."

### Hero Is the User (or the System)

Narrate as a journey with obstacles and decision points. The user or system is the protagonist, not you.

**Anti-pattern**: "I identified the problem and designed an innovative solution."
**Good pattern**: "Users attempting to complete [task] encountered [obstacle]. The existing system failed them because [reason]. The redesigned flow addressed this by [mechanism]."

### Limit the Premises

One main premise per case study. Support it with evidence. Avoid "everything we did."

**Premise examples**:
- "Complex workflows need progressive disclosure, not simplification"
- "Enterprise trust requires visible governance, not hidden automation"
- "Conversion and compliance can coexist with the right interaction model"

### Kill Complexity

Use analogies for abstract AI and technical topics. Avoid jargon when explaining evaluation, safety, and tradeoffs.

**Before**: "We implemented a retrieval-augmented generation pipeline with semantic chunking and hybrid reranking."

**After**: "The system retrieves relevant documents before generating responses, using a two-stage ranking process to surface the most relevant information first."

---

## Case Study Type Specific Structures

### Type 1: 0-to-1 Product Build

**Anchor**: The first irreversible decision, then show option tradeoffs.

**Structure**:
1. **Why build this**: Market gap, strategic bet, user need
2. **First irreversible decision**: What locked the direction (platform, architecture, go-to-market)
3. **Options and tradeoffs**: What was considered, why chosen path won
4. **Build reality**: What changed, what was descoped, what surprised
5. **Launch and learn**: Initial outcomes, what validation showed

**Story arc**: Constraint-led invention

**Hook example**: "The brief said 'build a dashboard.' But dashboards assume users know what to look for. Our users didn't."

### Type 2: Turnaround / Recovery

**Anchor**: What broke, what was triaged, what governance prevented repeat failure.

**Structure**:
1. **The incident**: What went wrong, impact, detection
2. **Triage**: What was done immediately, decision hierarchy
3. **Root cause**: What actually caused it (not symptoms)
4. **Recovery design**: How the fix was approached
5. **Prevention**: What governance changed to prevent recurrence

**Story arc**: Incident narrative

**Hook example**: "The feature launched to 50% of users before anyone noticed it was broken. By the time we rolled back, 12,000 users had seen error states."

### Type 3: Platform / Systems Design

**Anchor**: Downstream teams, failure modes, and long-tail operational cost.

**Structure**:
1. **System scope**: What the platform enables, who depends on it
2. **Dependency map**: Upstream/downstream relationships
3. **Design constraints**: What couldn't change, what was negotiable
4. **Failure mode analysis**: What could break, edge cases
5. **Operational model**: How it's maintained, monitored, evolved

**Story arc**: Dependency map story

**Hook example**: "17 teams depended on this component. A breaking change would cascade across the entire product suite."

### Type 4: AI Integration Feature

**Anchor**: Why AI, how validated, where it failed, and how guardrails shaped UX.

**Structure**:
1. **Why AI**: Problem fit, alternatives considered
2. **Approach selection**: What was evaluated, selection rationale
3. **Validation**: How tested, what failed, what succeeded
4. **Guardrails**: What controls were implemented, why
5. **UX implications**: How guardrails shaped the experience
6. **Monitoring**: How it's observed in production

**Story arc**: Evaluation story

**Hook example**: "The AI could answer 80% of questions correctly. But the 20% it got wrong were the questions users cared about most."

### Type 5: AI Governance / Risk Program

**Anchor**: Policy friction, auditability, monitoring and rollback.

**Structure**:
1. **Governance need**: Why governance was required
2. **Policy landscape**: Regulatory, compliance, internal policy constraints
3. **Framework design**: What governance structure was created
4. **Friction points**: Where governance conflicted with speed/experience
5. **Auditability**: How decisions are tracked and reviewed
6. **Incident response**: Rollback and escalation paths

**Story arc**: Risk register story

**Hook example**: "Legal said no. Product said ship. We built a framework that satisfied both."

### Type 6: Design Ops / Org Transformation

**Anchor**: How quality gates and decision logs changed throughput and outcomes.

**Structure**:
1. **Before state**: How the org operated, pain points
2. **Transformation thesis**: What change was hypothesized to help
3. **Operating system design**: Cadence, rituals, quality gates
4. **Implementation**: How it was rolled out, resistance encountered
5. **After state**: Measurable changes in throughput, quality, satisfaction

**Story arc**: Operating system story

**Hook example**: "Design reviews happened, but nothing changed afterward. We redesigned the review system itself."

### Type 7: Multi-Market / International Complexity

**Anchor**: What could not be standardized and why.

**Structure**:
1. **Market scope**: Which markets, what diversity
2. **Standardization attempt**: What was hoped to be shared
3. **Localization reality**: What couldn't be standardized
4. **Variant management**: How differences were handled
5. **Governance**: How variants were maintained, quality assured

**Story arc**: Variant management story

**Hook example**: "We designed one checkout flow for 12 countries. It worked in 3. Here's what we learned about the other 9."

---

## NDA-Safe Storytelling (Cross-Cutting)

Use these techniques when specifics are restricted.

### Mechanism-First Narrative

Emphasize the decision mechanism and governance pattern, not proprietary details.

**Pattern**: "We implemented [pattern type] to address [problem class]. The approach required [tradeoffs]. Validation showed [outcome type]."

### Reconstructed Timelines

Describe sequence and decision points using generic labels.

**Pattern**: "During [DateRange], the team faced [decision type]. Options included [generalized options]. Selection was based on [criteria type]."

### Synthetic Examples

Create illustrative micro-scenarios labeled clearly.

**Pattern**: "`[Illustrative]` A user encountering [situation type] would see [experience description]. The system responds by [mechanism]."

---

## Authenticity Signals

### Transparency Moment (Required per case study)

Include at least one of:
- What stakeholders or users challenged
- What you changed based on feedback
- What you could not fix and why

### Third-Party Plausibility Check

Ask: "If a skeptic compared this story against external signals, what would contradict it?"

Adjust wording to remain true while acknowledging complexity.

### Realistic Artifact Policy

Prefer real, sanitized artifacts over "portfolio-polished" diagrams:
- Actual screenshots (redacted) over mockups
- Real decision logs over reconstructed ones
- Actual research outputs over idealized syntheses

---

## Design the Meeting Framing

Treat each case study as a stakeholder meeting that reduces cognitive load.

### Set Context First

```markdown
**Project goal**: [What success looks like]
**Where we are**: [Current stage in the narrative]
**Evaluation mode**: [What kind of assessment is appropriate]
```

### Summarize Prior Decision Context

```markdown
**Previously decided**: [What was already locked]
**Constraints**: [What couldn't change]
```

### Timeline Visual Concept

Place the story on a timeline from research to ship-ready:

```
[Research] → [Define] → [Options] → [Build] → [Validate] → [Ship] → [Measure]
                                      ↑
                           (This case study focuses here)
```

### Anticipate Reactions

```markdown
**Likely objections**:
1. [Objection]: [Preemptive clarification]
2. [Objection]: [Preemptive clarification]
```
