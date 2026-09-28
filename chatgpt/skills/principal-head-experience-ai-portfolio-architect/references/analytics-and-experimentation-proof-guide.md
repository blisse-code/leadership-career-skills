# Analytics and Experimentation Proof Guide

## Metrics Integrity Framework

Every outcome claim requires a Metrics Integrity Block documenting measurement validity.

### Metrics Integrity Block Template

```markdown
## Metrics Integrity

| Metric | What measured | Method | Baseline | Result | Timeframe | Attribution limits |
|--------|--------------|--------|----------|--------|-----------|-------------------|
| [Metric 1] | [Definition] | [How] | [Before] | [After] | [Period] | [Confounds] |

**Measurement notes**:
- Instrumentation: [How data was collected]
- Sample: [Population, any exclusions]
- Statistical validity: [Significance, confidence intervals if applicable]

**Attribution caveats**:
- Other factors: [What else could have contributed]
- Isolation: [How we attempted to isolate effect]
- Confidence: [High/Medium/Low in causal attribution]
```

---

## Metric Categories

### Business Metrics

| Metric type | Examples | Measurement considerations |
|-------------|----------|---------------------------|
| Conversion | Sign-up rate, purchase rate, upgrade rate | Define funnel precisely, track cohorts |
| Retention | D1/D7/D30 retention, churn rate | Cohort definition, time window consistency |
| Revenue | ARPU, LTV, revenue per session | Attribution window, multi-touch complexity |
| Cost | CAC, support cost per user, operational cost | Include all relevant cost components |
| Efficiency | Cycle time, throughput, automation rate | Define start/end points clearly |

### Experience Metrics

| Metric type | Examples | Measurement considerations |
|-------------|----------|---------------------------|
| Task success | Completion rate, error rate, time-on-task | Define task boundaries, success criteria |
| Satisfaction | CSAT, NPS, SUS score | Survey timing, response bias |
| Effort | CES, clicks-to-complete, support contacts | Define effort boundaries |
| Engagement | Session duration, feature adoption, DAU/MAU | Define meaningful engagement |

### Operational Metrics

| Metric type | Examples | Measurement considerations |
|-------------|----------|---------------------------|
| Quality | Bug rate, defect density, rework rate | Define quality criteria |
| Speed | Lead time, deployment frequency, MTTR | Define process boundaries |
| Scale | Throughput, capacity utilization | Define constraints |

---

## Counter-Metric Requirement

**Rule**: No single-metric victory stories. Every outcome section must include at least one counter-metric or tradeoff metric.

### Counter-Metric Template

```markdown
**Primary outcome**: Conversion increased 23%

**Counter-metrics monitored**:
- Support ticket volume: Increased 8% (acceptable given conversion lift)
- Time-on-task: Increased 12 seconds (tradeoff for additional validation)
- Drop-off at step 3: Flat (no degradation)

**Tradeoff assessment**: Net positive. Conversion gain outweighs support cost increase. Time-on-task increase is acceptable for fraud prevention benefits.
```

### Common Counter-Metrics by Primary Metric

| Primary metric | Common counter-metrics |
|---------------|----------------------|
| Conversion | Support volume, error rate, fraud rate, satisfaction |
| Speed | Quality/error rate, cost, satisfaction |
| Engagement | Retention, satisfaction, support contacts |
| Cost reduction | Quality, speed, satisfaction |
| Automation rate | Error rate, escalation rate, satisfaction |

---

## Experimentation Evidence

### A/B Test Documentation

```markdown
## Experiment: [Name]

**Hypothesis**: [If we change X, we expect Y to improve by Z because...]

**Design**:
- Control: [What control saw]
- Treatment: [What treatment saw]
- Randomization: [How assigned]
- Sample size: [N per variant]
- Duration: [Runtime]
- Primary metric: [What we optimized for]
- Guardrail metrics: [What we monitored for harm]

**Results**:
| Metric | Control | Treatment | Lift | p-value | CI |
|--------|---------|-----------|------|---------|-----|
| Primary | [Value] | [Value] | [%] | [p] | [range] |
| Guardrail 1 | [Value] | [Value] | [%] | [p] | [range] |

**Decision**: [Ship / Iterate / Kill] because [reasoning]

**Learnings**: [What we learned beyond the metrics]
```

### When A/B Testing Wasn't Possible

Document why and what alternative evidence exists:

| Reason | Alternative evidence | Confidence |
|--------|---------------------|------------|
| Insufficient traffic | Pre/post comparison with controls | Medium |
| Technical constraints | Qualitative validation + proxy metrics | Medium |
| Time pressure | Staged rollout with monitoring | Medium |
| Ethical concerns | Expert review + limited pilot | Medium-Low |

---

## Handling Missing or Restricted Metrics

### When Exact Numbers Are Confidential

**Safe ranges**:
- "Conversion improved by 15-25%"
- "Retention moved from bottom quartile to top quartile"
- "Cost reduced by more than 30%"

**Directional statements**:
- "Statistically significant improvement in conversion"
- "Measurable reduction in support contacts"
- "Notable increase in task completion"

**Labeling requirement**: Always mark restricted metrics clearly:
- `[Range due to NDA]`
- `[Directional due to confidentiality]`
- `[Exact value available in interview]`

### When Metrics Don't Exist

**Reconstruct with smallest viable evidence**:

1. **Proxy metrics**: What related, measurable signal indicates the outcome?
2. **Process evidence**: What methodological rigor suggests the outcome?
3. **Stakeholder testimony**: Who can validate the outcome qualitatively?
4. **Before/after artifacts**: What artifacts show the change?

**Documentation**:
```markdown
**Outcome**: Reduced user confusion in onboarding

**Direct metric**: Not instrumented at the time

**Proxy evidence**:
- Support tickets tagged "onboarding": -34% (instrumented)
- Qualitative feedback: "Much clearer" theme in 8/12 interviews
- Time to first value action: -2 days (estimated from cohort analysis)

**Confidence**: Medium (proxy + qualitative convergence)
```

---

## Attribution Discipline

### Attribution Limits Documentation

For every metric, document what limits causal attribution:

| Attribution factor | Impact | Mitigation |
|-------------------|--------|------------|
| Concurrent changes | [Other things that changed] | [How isolated or acknowledged] |
| Seasonality | [Relevant seasonal effects] | [How controlled] |
| External factors | [Market, competitor, macro] | [How acknowledged] |
| Selection bias | [Non-random exposure] | [How addressed] |
| Measurement artifacts | [Instrumentation changes] | [How controlled] |

### Honest Attribution Language

**Avoid**:
- "I increased conversion by 23%"
- "My design drove $2M in revenue"
- "Responsible for 50% reduction in churn"

**Use**:
- "Conversion increased 23% following the redesign"
- "Redesign contributed to $2M revenue lift (multi-factor attribution)"
- "Churn reduced 50% in the quarter of launch; design was one of several contributing factors"

---

## Instrumentation and Methodology Documentation

### Instrumentation Block

```markdown
## Instrumentation

**Data source**: [Analytics platform, database, logs]
**Collection method**: [Event tracking, surveys, logs]
**Sample definition**: [Who was included/excluded]
**Time window**: [When data was collected]
**Known limitations**: [Gaps, biases, quality issues]
```

### Methodology Block (for research-based evidence)

```markdown
## Research Methodology

**Method**: [Usability testing, interviews, surveys, etc.]
**Sample**: [N, recruitment criteria, representation]
**Protocol**: [What was done]
**Analysis**: [How findings were derived]
**Limitations**: [Generalizability, bias, validity concerns]
```

---

## Evidence Presentation Standards

### Table Format for Metrics

Always present metrics in tables, not prose:

| Metric | Before | After | Change | Timeframe | Confidence |
|--------|--------|-------|--------|-----------|------------|
| [Metric] | [Value] | [Value] | [+/-X%] | [Period] | High/Med/Low |

### Visualization Standards

If including charts or graphs:
- Label axes clearly
- Include sample size
- Show confidence intervals where applicable
- Date-stamp the data
- Anonymize if needed
