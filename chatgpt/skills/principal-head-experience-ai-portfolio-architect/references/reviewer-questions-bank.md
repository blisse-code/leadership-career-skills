# Reviewer Questions Bank

## Purpose

Use this question bank during Phase 4 (Ruthless Review) to stress-test case studies. Generate critic personas and use these questions to identify weak claims.

---

## Leadership Questions

### For Hiring Manager Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What decisions did YOU make vs the team?" | Attribution clarity | Vague "we" without specifics |
| "How did you handle disagreement with your manager?" | Influence skills | "There was none" or no specifics |
| "What did you delegate and why?" | Judgment about what to own | Did everything or delegated nothing |
| "How did you know when to escalate?" | Judgment about scope | No escalation framework |
| "What would your reports say was your weakness?" | Self-awareness | "Nothing" or deflection |
| "Tell me about someone you coached who improved." | Development skills | No specific example |
| "How did you handle underperformance?" | Difficult conversations | Avoided or no specifics |

### For Executive Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What was the business case for this work?" | Business acumen | Design-only framing |
| "How did you align stakeholders with competing priorities?" | Political skill | "Everyone agreed" |
| "What was the cost of delay?" | Prioritization thinking | No understanding |
| "What would you cut if given half the timeline?" | Tradeoff judgment | "Nothing" or everything equally |
| "How did this connect to company strategy?" | Strategic thinking | No clear connection |

---

## Systems Thinking Questions

### For Principal Designer Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What were the upstream and downstream dependencies?" | Systems awareness | Only focused on own component |
| "What edge cases did you identify?" | Thoroughness | "We didn't find any" or <5 |
| "How does this scale to 10x users?" | Scale thinking | Never considered |
| "What breaks if [dependency] fails?" | Failure mode awareness | "It won't fail" |
| "How did you handle the long-tail operational costs?" | Operational thinking | Only considered launch |
| "What cross-team coordination was required?" | Influence scope | Solo narrative |

### For Systems Architect Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What were the failure modes you designed for?" | Defensive design | "None identified" |
| "How did you handle state across touchpoints?" | Technical understanding | No answer or handwave |
| "What monitoring did you implement?" | Production awareness | "That was engineering's job" |
| "What would break this system?" | Vulnerability awareness | "Nothing" |

---

## Analytics Rigor Questions

### For Data-Minded PM Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "How do you know this metric change was caused by your work?" | Attribution discipline | "It went up after we launched" |
| "What was the statistical significance?" | Rigor | "We didn't measure that" |
| "What counter-metrics did you monitor?" | Tradeoff awareness | "None" or didn't consider |
| "What was the baseline and how was it measured?" | Measurement validity | "I don't remember" |
| "What confounding factors existed?" | Critical thinking | "None" |
| "How long did you measure post-launch?" | Durability awareness | Only launch week |

### For Skeptical Analyst Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "Can I see the dashboard?" | Evidence existence | "It's gone" or "I don't have access" |
| "How was the cohort defined?" | Methodology rigor | Vague or post-hoc |
| "What would make this metric go up that wasn't your work?" | Attribution humility | Can't name anything |
| "Why this metric and not [alternative]?" | Metric selection | "That's what we always use" |

---

## AI Judgment Questions

### For AI Product Lead Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "Why AI for this problem?" | Problem fit | "Because AI is powerful" |
| "What did you evaluate the model against?" | Evaluation rigor | "We trusted the vendor" |
| "What happens when the model is wrong?" | Failure handling | "It's accurate enough" |
| "How do you monitor for drift?" | Production awareness | "We don't" or "engineering handles it" |
| "What would make you roll back?" | Judgment criteria | No clear answer |
| "What guardrails did you implement?" | Safety thinking | None or generic |

### For AI Safety Researcher Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What's the failure mode library?" | Thoroughness | None exists |
| "How did you red-team this?" | Adversarial thinking | "We didn't" |
| "What biases did you test for?" | Fairness awareness | "None found" without testing |
| "What's the human escalation path?" | Human oversight | Fully automated with no escape |
| "What data was the model trained on?" | Data awareness | "I don't know" |
| "What privacy controls are in place?" | Privacy awareness | None or generic |

---

## Governance Questions

### For Compliance/Legal Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "How did you handle [relevant regulation]?" | Compliance awareness | "That wasn't my area" |
| "What's the audit trail?" | Accountability | None or unclear |
| "How are decisions documented?" | Governance | Not documented |
| "Who approved this approach?" | Decision authority | "I just did it" |
| "What would happen in an audit?" | Risk awareness | Never considered |

### For Risk Manager Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What's the worst case scenario?" | Risk awareness | "It won't happen" |
| "What's the rollback plan?" | Recovery planning | None or "we'd figure it out" |
| "What incidents have occurred?" | Operational reality | "None" (suspicious) |
| "How do you handle escalations?" | Process maturity | Ad hoc only |

---

## Execution Reality Questions

### For Experienced IC Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "What went wrong?" | Honesty | "Nothing" |
| "What did you have to descope?" | Prioritization reality | "Nothing, we shipped everything" |
| "What would you do differently?" | Self-awareness | "Nothing" or superficial |
| "Where did you compromise?" | Realism | "We didn't compromise on quality" |
| "What took longer than expected?" | Estimation honesty | "Nothing" |
| "What surprised you during execution?" | Learning orientation | "Nothing surprised me" |

### For Hiring Manager (BS Detector) Persona

| Question | What it tests | Red flag answers |
|----------|--------------|------------------|
| "Walk me through a specific decision point." | Detail availability | Vague or generic |
| "What did you personally do on day [X]?" | Hands-on reality | Can't answer specifically |
| "Show me an artifact you created." | Work evidence | None available |
| "What feedback did you get and how did it change your work?" | Iteration evidence | "Everyone loved it" |

---

## Claim Attack List Template

Generate this for each case study during ruthless review:

| # | Claim | Attack vector | Evidence gap | Resolution |
|---|-------|---------------|--------------|------------|
| 1 | [Claim] | [How to shoot it down] | [What's missing] | [Remove/Rewrite/Evidence] |
| 2 | | | | |
| 3 | | | | |
| ... | | | | |
| 10 | | | | |

### Common Attack Vectors

| Attack type | Example | Defense |
|-------------|---------|---------|
| Attribution inflation | "You didn't cause that outcome" | Specific evidence + attribution limits |
| Vague metrics | "What does 'improved' mean?" | Specific numbers with methodology |
| Hero narrative | "Where's the team?" | Clear responsibility map |
| No failure | "Nothing went wrong?" | Honest transparency moment |
| Unsubstantiated AI claims | "How do you know it works?" | Evaluation artifacts |
| Missing governance | "What controls existed?" | Documented guardrails |

---

## Critic Persona Generation

For Phase 4, generate a composite critic with these attributes:

### Veteran Principal Designer

- 15+ years experience
- Has seen hundreds of portfolios
- Skeptical of hero narratives
- Values craft and systems thinking
- Asks "what actually happened?" not "what do you claim?"

### Skeptical AI Product Lead

- Deep AI/ML background
- Has shipped AI products
- Knows evaluation is hard
- Skeptical of vendor claims
- Asks about guardrails, failures, monitoring

### Combined Critic Prompt

"You are reviewing this case study as a 15-year veteran principal designer who has also shipped AI products and seen hundreds of portfolios. You are skeptical of hero narratives and unsubstantiated claims. Your job is to find the weakest claims and ask the hardest questions. Be specific."

---

## Weak Claims Log Template

Document claims that were removed or repaired during ruthless review:

| Original claim | Attack | Resolution | Final version |
|----------------|--------|------------|---------------|
| "Significantly improved UX" | Vague, no metric | Rewrite | "Task completion improved from 34% to 72%" |
| "Led the redesign" | Attribution unclear | Add responsibility map | "Set direction and quality bar for redesign; team executed across 6 sprints" |
| "Users loved it" | No evidence | Remove | [Removed, replaced with CSAT data] |

---

## Question Strategy Pack (for interviews)

Prepare questions that demonstrate independent thinking:

### Template for Target Company Research

| Company | Their challenges (public info) | Thoughtful questions |
|---------|-------------------------------|---------------------|
| [Company] | [Challenge 1] | [Non-obvious question] |
| [Company] | [Challenge 2] | [Non-obvious question] |

### Question Quality Filter

**Reject**: Questions answerable by reading their website
**Accept**: Questions that show you've thought about their specific problems

### Examples

**Bad**: "What's your design process?"
**Good**: "I noticed [specific product decision]. What tradeoffs did that involve?"

**Bad**: "How do you use AI?"
**Good**: "Given [specific constraint in their domain], how do you think about evaluation for [specific use case]?"
