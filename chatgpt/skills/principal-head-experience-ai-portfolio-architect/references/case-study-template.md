# Case Study Template

## Required Structure

Every flagship case study must include all sections A-J. Supporting capsules may abbreviate.

---

### Header Block

```markdown
# [Case Study Title: Informative, Not Generic]

**Role**: [Your specific role and scope]
**Timeline**: [DateRange]
**Scale**: [Users, markets, team size]
**Outcome type**: [Turnaround | 0-1 Build | Platform | AI Integration | Governance]
**Evidence tier**: [High | Medium | Low]
**Shareability**: [Public | Sanitized | Interview-only]
```

**Responsibility Map** (required):
- Owned: [list]
- Led through others: [list]
- Influenced: [list]
- Consulted: [list]
- What I did NOT do: [list]

---

### Executive Skim Block (8-12 lines, hard cap)

```markdown
## Executive Skim

**Context**: [1-2 lines: industry, scale, constraint]
**Problem**: [1-2 lines: the real problem, falsifiable]
**Approach**: [2-3 lines: what you chose and why]
**Outcome**: [2-3 lines: measurable results with attribution limits]
**Judgment signal**: [1-2 lines: the hardest tradeoff or decision]
```

---

### Section A: Context and Constraints

- Industry and market position
- Platform and technical constraints
- Timeline and resource constraints
- Organizational constraints (politics, legacy, compliance)
- What was already locked vs what was negotiable

**Length**: 4-8 bullets max

---

### Section B: The Real Problem

State the problem in falsifiable terms. Not symptoms, not solutions.

**Template**:
```markdown
## The Real Problem

**Surface symptom**: [What stakeholders initially described]
**Underlying problem**: [What actually needed solving]
**Falsifiable framing**: [If we do X, we expect Y to change by Z]
**Why it mattered**: [Business or user impact if unsolved]
```

**Anti-pattern**: "Users were frustrated" (not falsifiable)
**Good pattern**: "Task completion for [workflow] was 34% with 6+ clicks average, causing [downstream effect]"

---

### Section C: Evidence and Inputs

What informed your decisions. Must cite evidence type and source.

| Input type | What it showed | Confidence | Source |
|-----------|----------------|------------|--------|
| Analytics | [Finding] | High/Med/Low | [Dashboard/Export] |
| Research | [Finding] | High/Med/Low | [Study/Transcript] |
| Stakeholder constraint | [Constraint] | High/Med/Low | [Meeting/Doc] |
| Ops data | [Finding] | High/Med/Low | [System/Report] |

**Length**: 4-8 rows

---

### Section D: Options Considered

At least 2 options. Show why chosen path won.

| Option | Tradeoffs | Why it lost or won |
|--------|-----------|-------------------|
| Option A (chosen) | [Pros/cons] | [Why selected] |
| Option B | [Pros/cons] | [Why rejected] |
| Option C (if applicable) | [Pros/cons] | [Why rejected] |

**Required**: Explicit "opposing idea" and why it lost.

---

### Section E: System Design Thinking

Show end-to-end understanding beyond the screen.

- Journey scope (which touchpoints, which channels)
- Dependencies (upstream/downstream systems, teams, data)
- Failure modes (what could break, edge cases identified)
- Operational considerations (support load, maintenance, monitoring)

**Include**: Mini edge-case library (minimum 8 edge cases for flagship studies)

| Edge case | How detected | How handled | Human escalation? |
|-----------|-------------|-------------|-------------------|
| [Case 1] | [Signal] | [Resolution] | Yes/No |
| ... | ... | ... | ... |

---

### Section F: Execution Reality

What actually happened. No hero narrative.

- What broke or went wrong
- Where friction happened (technical, political, resource)
- How you navigated (not "overcame")
- What was descoped or compromised
- Timeline reality vs plan

**Length**: 6-10 bullets max

---

### Section G: AI and Automation Layer

**If AI not applicable**: State why and what guardrails you would require if introduced.

**If AI applicable**, include all of:

```markdown
## AI and Automation Layer

**Why AI was considered**: [Problem fit, not technology enthusiasm]

**Model/approach selection**:
- Options evaluated: [List]
- Selection rationale: [Why this approach]
- What was rejected and why: [Anti-patterns avoided]

**Evaluation plan**:
- Success metrics: [Specific, measurable]
- Test methodology: [How validated]
- Failure criteria: [What would cause rollback]

**Risk taxonomy**:
| Risk type | Specific risk | Mitigation |
|-----------|--------------|------------|
| Privacy | [Risk] | [Control] |
| Safety | [Risk] | [Control] |
| Reliability | [Risk] | [Control] |
| Bias | [Risk] | [Control] |
| Compliance | [Risk] | [Control] |

**Guardrails implemented**:
- [Guardrail 1]
- [Guardrail 2]

**Human-in-the-loop design**:
- When human review required
- Escalation paths
- Override mechanisms

**Monitoring and rollback**:
- What is monitored (drift, hallucination rates, error rates)
- Escalation thresholds
- Rollback procedure
- Incident response story (if applicable)
```

See `ai-governance-and-evaluation-checklist.md` for complete checklist.

---

### Section H: Outcomes and Measurement

See `analytics-and-experimentation-proof-guide.md` for detailed guidance.

**Metrics Integrity Block** (required):

| Metric | Measurement method | Baseline | Result | Timeframe | Attribution limits |
|--------|-------------------|----------|--------|-----------|-------------------|
| [Metric 1] | [How measured] | [Before] | [After] | [Period] | [What else contributed] |
| [Metric 2] | ... | ... | ... | ... | ... |

**Required**: At least one counter-metric or tradeoff metric. No single-metric victory stories.

**If exact numbers confidential**: Use safe ranges or directional metrics, labeled clearly.
- Example: "Conversion improved by 15-25% [range due to NDA]"
- Example: "Retention moved from bottom quartile to top quartile [directional]"

---

### Section I: Ugly Truths and Lessons

**Required**: At least one transparency moment per case study.

- What failed or was misjudged
- What you fought for and conceded, and why
- What changed your mind during the project
- What you would redo differently
- What you could not fix and why

**Frame**: Reality navigation and judgment, not complaining.

---

### Section J: Reusability

What frameworks, heuristics, or governance patterns you reused elsewhere.

- Pattern name and when to apply
- Where else it was used (with evidence if available)
- Limitations and when not to apply

---

## Evidence Table (Required)

| Claim | Evidence type | Source | Confidence | Shareability | Redaction needed |
|-------|--------------|--------|------------|--------------|------------------|
| [Claim 1] | [Type from hierarchy] | [Specific source] | High/Med/Low | Public/Sanitized/NDA/Non-shareable | Yes/No |
| [Claim 2] | ... | ... | ... | ... | ... |

**Rule**: Every claim in the case study must have a row. If no evidence, remove the claim.

---

## Redaction Plan Block (Required for NDA-restricted)

```markdown
## Redaction Plan

**What was removed**: [Client name, product name, specific metrics]
**What was generalized**: [Industry descriptor, metric ranges, team size bands]
**What stayed precise**: [Decision logic, tradeoffs, evaluation approach]
**Remaining risk**: [What could still identify the client if combined with other signals]
**Verification pathway**: [How a reviewer could validate claims without NDA violation]
```

---

## Common Ground Block (Required)

```markdown
## Common Ground

**Assumed knowledge**: [What the reader is expected to already know]
**Terms defined**:
- [Term 1]: [Definition]
- [Term 2]: [Definition]

**In-scope**: [What this case study covers]
**Out-of-scope**: [What it does not cover]
```

---

## Microinteraction Proof Bundle (for flagship studies)

| State | Behavior | Why it exists |
|-------|----------|---------------|
| Default | [Description] | [Purpose] |
| Hover | [Description] | [Feedback type] |
| Focus | [Description] | [Accessibility] |
| Active | [Description] | [Confirmation] |
| Loading | [Description] | [Status communication] |
| Empty | [Description] | [Guidance] |
| Error | [Description] | [Recovery path] |
| Offline | [Description] | [Graceful degradation] |

**Include**: 10-30 second capture or state storyboard if shareable.
