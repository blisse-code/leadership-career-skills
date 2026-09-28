# Evidence Map Table

## Evidence Hierarchy

Use this hierarchy to classify evidence strength. Higher tiers are more credible and harder to dispute.

### Tier 1: Primary Artifacts (Highest)
Direct, tangible outputs from the work.

| Evidence type | Examples | Confidence | Notes |
|--------------|----------|------------|-------|
| Production screens | Live product screenshots, archived versions | High | Date-stamp if possible |
| System logs | Error rates, latency logs, uptime records | High | Anonymize user data |
| PRDs and specs | Approved requirements, design specs | High | Show decision points |
| Evaluation reports | A/B test results, usability findings | High | Include methodology |
| Code or config | Shipped code, feature flags, guardrail configs | High | Sanitize secrets |
| Decision records | ADRs, design decision logs, meeting notes | High | Show rationale |

### Tier 2: Analytics and Experiments
Quantitative data from instrumented systems.

| Evidence type | Examples | Confidence | Notes |
|--------------|----------|------------|-------|
| Dashboard exports | Conversion funnels, retention cohorts | High | Include date range |
| Experiment readouts | A/B results with statistical significance | High | Include confidence intervals |
| Operational metrics | Support ticket volume, error rates | Medium-High | Show before/after |
| Business metrics | Revenue impact, cost reduction | Medium-High | Note attribution limits |

### Tier 3: Research and Synthesis
Qualitative evidence from research activities.

| Evidence type | Examples | Confidence | Notes |
|--------------|----------|------------|-------|
| Research transcripts | User interview recordings, notes | Medium | Anonymize participants |
| Synthesis artifacts | Affinity maps, journey maps, personas | Medium | Show source data |
| Survey results | Quantified user feedback | Medium | Include sample size, methodology |
| Competitive analysis | Feature comparisons, benchmarks | Medium | Date-stamp, note methodology |

### Tier 4: Stakeholder Records
Evidence of alignment and approval.

| Evidence type | Examples | Confidence | Notes |
|--------------|----------|------------|-------|
| Approval records | Sign-off emails, Slack threads | Medium | Anonymize if needed |
| Review feedback | Critique notes, executive feedback | Medium | Show how it shaped decisions |
| Partnership agreements | Cross-team commitments | Medium | Note what was delivered |

### Tier 5: Personal Recollection (Lowest)
Must be labeled `[Inference]` and Low confidence.

| Evidence type | Examples | Confidence | Notes |
|--------------|----------|------------|-------|
| Memory of events | "I recall that we decided..." | Low | Always label `[Inference]` |
| Unrecorded conversations | Verbal agreements, hallway decisions | Low | Note uncertainty |
| Estimated metrics | "Approximately 20% improvement" | Low | Clearly mark as estimate |

---

## Evidence Table Template

Use this table for every case study to map claims to evidence.

| # | Claim | Evidence type | Tier | Source | Confidence | Shareability | Redaction needed | Status |
|---|-------|--------------|------|--------|------------|--------------|------------------|--------|
| 1 | [Claim text] | [Type] | [1-5] | [Specific source] | High/Med/Low | Public/Sanitized/NDA/Non-shareable | Yes/No | Verified/Pending/Remove |
| 2 | | | | | | | | |

### Confidence Criteria

**High confidence**:
- Artifact exists and is accessible
- Multiple corroborating sources
- Can be verified independently
- Methodology is documented

**Medium confidence**:
- Artifact exists but restricted
- Single source with some corroboration
- Methodology is partially documented
- Time gap between event and documentation

**Low confidence**:
- No artifact, recollection only
- No corroboration
- Methodology unclear
- Significant time gap

### Shareability Definitions

**Public**: Can be shared openly (portfolio, LinkedIn, public talks)
**Sanitized**: Can be shared with redactions (client name, exact metrics removed)
**NDA-Restricted**: Can be discussed verbally in interviews, not published
**Non-shareable**: Cannot be shared outside the company, even verbally

---

## Proof Map by Portfolio Section

| Portfolio section | Required evidence types | Minimum evidence count | Notes |
|------------------|------------------------|----------------------|-------|
| Executive snapshot | Scope metrics, outcome signals | 3 | At least 1 Tier 1-2 |
| Case study: Context | Constraints documentation | 2 | Can be Tier 3-4 |
| Case study: Problem | Research or analytics showing problem | 2 | At least 1 Tier 2-3 |
| Case study: Options | Decision records, analysis docs | 2 | Tier 1 preferred |
| Case study: Outcomes | Metrics, experiment results | 3 | At least 2 Tier 1-2 |
| AI governance dossier | Evaluation plans, guardrail docs | 3 | Tier 1-2 required |
| Leadership operating system | Process docs, decision logs | 2 | Can be Tier 1-4 |
| Artifacts gallery | Sanitized screens, diagrams | 6-12 | Tier 1 only |

---

## Evidence Gap Analysis

When evidence is missing, document gaps and mitigation:

| Claim | Gap | Mitigation strategy | Risk |
|-------|-----|---------------------|------|
| [Claim] | No artifact exists | Reconstruct from memory with `[Inference]` label | Low credibility |
| [Claim] | Artifact exists but NDA | Describe pattern/approach without specifics | May seem vague |
| [Claim] | Metric exists but unattributable | Provide range, note attribution limits | May be challenged |

### Smallest Reconstruction Options

When metrics are missing, propose the smallest way to reconstruct:

1. **Proxy metrics**: What related metric could demonstrate the outcome?
2. **Directional evidence**: Can you show before/after qualitatively?
3. **Process evidence**: Can you show the methodology that would produce the outcome?
4. **Third-party validation**: Is there stakeholder testimony that corroborates?

---

## Three High-Confidence Claim Rule

Every flagship case study must include at least 3 claims with:
- High confidence rating
- Tier 1-2 evidence
- Shareability of Public or Sanitized

If a case study cannot meet this bar, downgrade to "supporting capsule" or exclude.

### Audit Checklist

| Case study | High-confidence claims | Tier 1-2 evidence | Shareable evidence | Status |
|------------|----------------------|-------------------|-------------------|--------|
| [Study 1] | [Count] | [Count] | [Count] | Flagship/Capsule/Exclude |
| [Study 2] | | | | |
