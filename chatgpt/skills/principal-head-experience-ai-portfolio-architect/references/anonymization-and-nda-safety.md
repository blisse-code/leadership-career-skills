# Anonymization and NDA Safety

## Redaction Token Standard

Use consistent tokens throughout the portfolio. Never mix token styles.

| Token | Replaces | Example usage |
|-------|----------|---------------|
| `[Client]` | Company/client name | "Working with [Client], a Fortune 500 retailer..." |
| `[Industry]` | Specific industry when identifying | "In the [Industry] sector..." |
| `[Product]` | Product or service name | "The [Product] platform serves..." |
| `[Region]` | Geographic location when identifying | "Launched across [Region]..." |
| `[Metric]` | Exact numbers when NDA-restricted | "Improved conversion by [Metric]%" |
| `[Vendor]` | Third-party vendor names | "Integrated with [Vendor] for payments..." |
| `[Model]` | AI model names/versions | "Evaluated [Model] against alternatives..." |
| `[DateRange]` | Specific dates when identifying | "During [DateRange], the team..." |
| `[TeamSize]` | Exact team size | "Led a team of [TeamSize] designers..." |
| `[RevenueBand]` | Revenue figures | "Platform processing [RevenueBand] annually..." |

---

## Redaction Plan Template

Every NDA-restricted case study requires this block:

```markdown
## Redaction Plan

### What was removed
- Client name and all identifying brand elements
- Exact revenue and user count figures
- Specific product names and feature names
- Internal team member names
- Proprietary algorithm details

### What was generalized
- Industry: "enterprise B2B SaaS" instead of specific vertical
- Scale: "millions of users" instead of exact count
- Metrics: "15-25% improvement" range instead of exact
- Timeline: "Q3-Q4 2023" instead of specific dates
- Team: "team of 8-12" instead of exact count

### What stayed precise
- Decision logic and tradeoffs
- Evaluation methodology
- Failure modes and how handled
- Governance patterns implemented
- Role and responsibilities

### Remaining risk
- Combination of industry + scale + timeline could narrow identification
- Mitigation: reviewed with legal, approved for portfolio use

### Verification pathway
- "Reference available on request"
- "Can discuss deeper under mutual NDA"
- "Sanitized evidence pack available in interview"
```

---

## NDA-Safe Storytelling Techniques

### Mechanism-First Narrative

Emphasize the decision mechanism and governance pattern, not proprietary details.

**Before (risky)**:
"We implemented [Client]'s proprietary fraud detection algorithm with 94.7% accuracy on their 12M transaction dataset."

**After (safe)**:
"Implemented a fraud detection system requiring evaluation against production-scale data. Accuracy targets were set based on operational cost thresholds, with monitoring for drift over time."

### Reconstructed Timelines

Describe sequence and decision points using generic labels.

**Before (risky)**:
"In January 2024, we launched the checkout redesign for MegaCorp's European markets."

**After (safe)**:
"During [DateRange], launched checkout redesign across [Region] markets, navigating localization and compliance requirements."

### Synthetic Examples

When concrete examples help but real ones are protected, create illustrative micro-scenarios.

**Labeling requirement**: Always mark as `[Illustrative]`

```markdown
**Example flow** `[Illustrative]`:
User encounters error → System classifies severity → Low severity: self-service recovery
→ High severity: routes to human review → Resolution logged for pattern analysis
```

**Rule**: Never present illustrative examples as the actual system.

### Pattern Abstraction

Describe the reusable pattern rather than the specific implementation.

**Before (risky)**:
"MegaCorp's dashboard used a 3-column layout with real-time inventory counts, supplier alerts, and fulfillment status."

**After (safe)**:
"Dashboard design balanced information density with scanability using a modular layout pattern. Primary metrics visible without scrolling, secondary details progressive-disclosed."

---

## Disclosure Tier Labels

Mark every case study with its disclosure tier:

| Tier | Label | What can be shared | Where |
|------|-------|-------------------|-------|
| 1 | **Public** | Full detail, named client (with permission) | Portfolio, talks, LinkedIn |
| 2 | **Sanitized** | Redacted narrative, patterns, ranges | Portfolio, recruiter conversations |
| 3 | **Interview-only** | Verbal discussion, no written artifacts | Live interviews only |
| 4 | **Reference-gated** | Verification via reference call | Reference check only |

### Tier Labeling Template

```markdown
**Disclosure tier**: Sanitized
**What's shareable**: Decision logic, evaluation approach, outcome ranges
**What requires interview**: Exact metrics, specific failure incidents
**What requires reference**: Client validation, peer testimony
```

---

## Proprietary Content Rules

### Never describe:
- Proprietary model architectures or training data
- Security controls beyond safe abstractions
- Internal data sources or pipelines
- Unreleased product features
- Confidential business strategy

### Safe abstractions for AI systems:

**Risky**: "We fine-tuned GPT-4 on 50K customer support transcripts with custom loss function targeting resolution time."

**Safe**: "Evaluated multiple LLM approaches for customer support automation. Selected approach based on resolution accuracy, response latency, and operational cost. Custom evaluation dataset developed to measure task completion."

### Safe abstractions for security:

**Risky**: "Implemented OAuth 2.0 with PKCE flow and 256-bit AES encryption for PII storage."

**Safe**: "Authentication and data protection designed to meet enterprise security requirements and compliance standards."

---

## Verification Pathways

Provide ways for reviewers to validate claims without NDA violation:

### Reference available on request
- Prepare reference contacts who can speak to your work
- Brief references on what they can and cannot discuss
- Provide context for the reviewer's questions

### Sanitized evidence pack (interview-only)
- Prepare redacted artifacts for live screen-share
- Practice walking through without revealing protected info
- Have clear boundaries on what questions you can answer

### Mutual NDA discussion
- For very restricted work, offer to discuss under mutual NDA
- Prepare what additional detail this would unlock
- Know your company's policy on this

---

## Legal Checkpoint

Before publishing any case study:

- [ ] Reviewed against employment agreement
- [ ] Confirmed no trade secrets disclosed
- [ ] Verified client permission (if naming)
- [ ] Checked with legal/compliance if uncertain
- [ ] Confirmed no third-party IP issues
- [ ] Verified no security vulnerabilities exposed

**When in doubt**: Err on the side of more redaction. You can always reveal more in conversation.
