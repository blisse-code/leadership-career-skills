# Resume Template

## Section order (leadership default)

```
NAME
Target Title | Scope signal | Signature domain          <- headline, exact JD title first
City, Country | email | phone | linkedin | portfolio      <- one line, no full address

SUMMARY (3-4 lines)
Identity + scale + signature + proof. No adjectives about self.

SELECTED IMPACT (Director+; 3-5 bullets)
Best career outcomes, each mandate > move > measure.

CORE COMPETENCIES (1-2 lines of keyword phrases mirrored from JD)
Design org leadership · Experience strategy · Design systems governance · ...

PROFESSIONAL EXPERIENCE
Title | Company | City | Mon YYYY - Present
Scope: team size, reports, budget, products, markets, stakeholders (italic, one line)
- 3-6 bullets for recent roles (1-2 craft/player-coach bullets allowed)
- 1-3 bullets for older roles

Earlier career: Title, Company (years) · Title, Company (years)

LEADERSHIP & RECOGNITION (only if real)
Speaking, publications, awards, advisory, teaching, patents

EDUCATION & CERTIFICATIONS (one line each)
```

Summary formula example (fictional):
> Head of Experience Design with 13 years across telco, banking, and e-commerce in Southeast Asia. Builds multi-disciplinary design practices and turns fragmented multi-market products into one system teams can ship on. Recent: led a 12-person team through a regional telco replatform serving 9M customers `[Need number check]`.

## JSON schema for scripts/render_resume_docx.py

```json
{
  "name": "Full Name",
  "headline": "Head of Experience Design | Design orgs of 20+ | AI-integrated product design",
  "contact": ["Kuala Lumpur, Malaysia", "name@email.com", "+60 ...", "linkedin.com/in/...", "portfolio.com"],
  "summary": "3-4 line paragraph",
  "selected_impact": ["bullet", "bullet"],
  "competencies": ["phrase", "phrase"],
  "experience": [
    {
      "title": "Head of Experience Design",
      "company": "Company",
      "location": "City",
      "dates": "Jan 2022 - Present",
      "scope": "Led 12 designers and researchers; 3 enterprise accounts; reported to MD",
      "bullets": ["bullet", "bullet"]
    }
  ],
  "earlier_career": "Title, Company (2010-2013) · Title, Company (2008-2010)",
  "extras": {"Leadership & Recognition": ["item"], "Education": ["item"]},
  "style": {"font": "Calibri", "body_pt": 10.5, "accent": "1F3A5F"}
}
```

Omit any key you don't need; the renderer skips empty sections.
