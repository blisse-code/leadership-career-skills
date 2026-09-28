# AI Governance and Evaluation Checklist

## When AI Is Applicable

Use this checklist for any case study involving AI/ML systems, automation, or algorithmic decision-making.

---

## AI Decision Rationale

### Why AI Was Considered

Document the problem fit, not technology enthusiasm.

| Question | Answer |
|----------|--------|
| What problem does AI solve that other approaches cannot? | |
| What is the cost/benefit of AI vs rule-based or manual approaches? | |
| What failure modes exist and how are they mitigated? | |
| What is the human fallback if AI fails? | |

**Anti-pattern**: "We used AI because it's cutting-edge"
**Good pattern**: "Task required processing [volume] with [latency] constraints. Rule-based approaches failed because [specific limitation]. AI enabled [specific capability] with [tradeoff]."

### Model/Approach Selection

| Option evaluated | Pros | Cons | Why selected/rejected |
|-----------------|------|------|----------------------|
| [Option 1] | | | |
| [Option 2] | | | |
| [Option 3] | | | |

**Required**: At least 2 options evaluated. Document why the chosen approach won.

---

## Risk Taxonomy

Assess each risk category. Mark N/A only with explicit justification.

### Privacy Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| PII exposure in training data | | | | |
| PII leakage in outputs | | | | |
| Re-identification risk | | | | |
| Data retention violations | | | | |

### Security Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| Prompt injection | | | | |
| Data exfiltration | | | | |
| Model extraction | | | | |
| Adversarial inputs | | | | |

### Safety Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| Harmful outputs | | | | |
| Misuse potential | | | | |
| Unintended actions (agentic) | | | | |
| Cascading failures | | | | |

### Reliability Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| Hallucination/confabulation | | | | |
| Performance degradation | | | | |
| Availability/latency failures | | | | |
| Edge case failures | | | | |

### Bias and Fairness Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| Demographic bias | | | | |
| Representation gaps | | | | |
| Disparate impact | | | | |
| Feedback loop amplification | | | | |

### Compliance Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| Regulatory violations | | | | |
| Audit trail gaps | | | | |
| Explainability requirements | | | | |
| Consent/disclosure gaps | | | | |

### IP Risk

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| Training data IP issues | | | | |
| Output IP ownership | | | | |
| Third-party model licensing | | | | |

---

## Evaluation Artifacts

### Evaluation Plan

| Element | Specification |
|---------|--------------|
| Success metrics | [Specific, measurable criteria] |
| Test methodology | [How validated: offline eval, A/B, shadow mode] |
| Evaluation dataset | [Size, composition, gold set methodology] |
| Failure criteria | [What triggers rollback or redesign] |
| Evaluation frequency | [One-time, periodic, continuous] |

### Required Evaluation Artifacts

- [ ] Gold set / evaluation dataset (documented methodology)
- [ ] Baseline performance benchmarks
- [ ] Test results with confidence intervals
- [ ] Failure case library (categorized)
- [ ] Red-team findings (if applicable)

### Red-Team Checklist (for high-risk systems)

- [ ] Adversarial input testing
- [ ] Edge case stress testing
- [ ] Prompt injection attempts (if LLM)
- [ ] Bias probing across demographics
- [ ] Failure mode enumeration

---

## Guardrails Implemented

Document each guardrail with its purpose and validation.

| Guardrail | Purpose | Implementation | Validation |
|-----------|---------|----------------|------------|
| Input validation | [What it prevents] | [How implemented] | [How tested] |
| Output filtering | [What it prevents] | [How implemented] | [How tested] |
| Rate limiting | [What it prevents] | [How implemented] | [How tested] |
| Confidence thresholds | [What it prevents] | [How implemented] | [How tested] |
| Human review triggers | [What it prevents] | [How implemented] | [How tested] |

---

## Human-in-the-Loop Design

### Review Triggers

| Condition | Review type | SLA | Escalation |
|-----------|-------------|-----|------------|
| Low confidence score | [Review level] | [Time] | [Path] |
| Flagged content | [Review level] | [Time] | [Path] |
| User dispute | [Review level] | [Time] | [Path] |
| High-stakes decision | [Review level] | [Time] | [Path] |

### Override Mechanisms

| Override type | Who can override | Audit trail | Feedback loop |
|--------------|-----------------|-------------|---------------|
| [Type 1] | [Role] | [How logged] | [How learned from] |
| [Type 2] | [Role] | [How logged] | [How learned from] |

---

## Monitoring and Rollback

### Runtime Monitoring

| Metric | Threshold | Alert | Response |
|--------|-----------|-------|----------|
| Accuracy/task completion | [Value] | [Type] | [Action] |
| Latency | [Value] | [Type] | [Action] |
| Error rate | [Value] | [Type] | [Action] |
| Drift indicators | [Value] | [Type] | [Action] |
| Hallucination rate (if LLM) | [Value] | [Type] | [Action] |

### Escalation Paths

```
Level 1: Automated alert → On-call review (15 min)
Level 2: Threshold breach → Feature flag disable (30 min)
Level 3: Critical failure → Full rollback (1 hour)
Level 4: Safety incident → Incident commander + exec notification
```

### Rollback Procedure

1. Trigger condition: [What initiates rollback]
2. Rollback mechanism: [Feature flag, deployment, manual]
3. Fallback behavior: [What users see during rollback]
4. Communication plan: [Who is notified, how]
5. Post-incident review: [Timeline, artifacts required]

### Incident Response Story (if applicable)

Document any incidents and how they were handled:

```markdown
**Incident**: [Brief description]
**Detection**: [How discovered, time to detection]
**Impact**: [Scope, users affected]
**Response**: [Actions taken, timeline]
**Resolution**: [How fixed]
**Prevention**: [What changed to prevent recurrence]
```

---

## When AI Is Not Applicable

If the case study does not involve AI, explicitly state:

```markdown
## AI Applicability

**AI involvement**: None

**Why AI was not used**:
[Explanation: problem did not require AI, simpler solutions sufficed, etc.]

**If AI were introduced, required guardrails would include**:
- [Guardrail 1]
- [Guardrail 2]
- [Evaluation requirement]
- [Human oversight requirement]
```

---

## AI Governance Summary Block

Use this block in the case study executive skim:

```markdown
**AI governance summary**:
- Approach: [Model type / technique]
- Evaluation: [Key validation method]
- Guardrails: [Top 2-3 controls]
- Human oversight: [Review mechanism]
- Monitoring: [Key runtime checks]
```
