# Visual System Spec

## Visual Calibration Input (Optional)

Collect from user. If absent, use safe defaults.

| Input | Default if missing |
|-------|-------------------|
| Brand constraints | None (start fresh) |
| Vibe adjectives (max 5) | "Clear, credible, technical, calm, precise" |
| Light/dark mode | Light primary, dark optional |
| Accessibility constraints | WCAG AA minimum |
| Existing assets | None |
| Inspiration references (max 3) | None |
| Target reading context | Desktop-first, recruiter skim + deep review |

---

## Design Tokens Table

### Typography Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `font-display` | Inter, system-ui, sans-serif | H1, H2, hero text |
| `font-text` | Inter, system-ui, sans-serif | Body, bullets, captions |
| `font-mono` | JetBrains Mono, monospace | Code, technical labels |
| `size-h1` | 2.5rem / 40px | Page titles |
| `size-h2` | 1.75rem / 28px | Section headers |
| `size-h3` | 1.25rem / 20px | Subsection headers |
| `size-body` | 1rem / 16px | Body text |
| `size-small` | 0.875rem / 14px | Captions, metadata |
| `size-caption` | 0.75rem / 12px | Labels, tags |
| `line-height-tight` | 1.2 | Headlines |
| `line-height-normal` | 1.5 | Body text |
| `line-height-relaxed` | 1.75 | Long-form reading |
| `letter-spacing-tight` | -0.02em | Large headlines |
| `letter-spacing-normal` | 0 | Body text |

**Line length target**: 65-75 characters for long-form to reduce fatigue.

**Fallback stack**: Inter → -apple-system → BlinkMacSystemFont → Segoe UI → Roboto → sans-serif

### Color Tokens (Semantic Mapping)

| Token | Light mode | Dark mode | Usage |
|-------|-----------|-----------|-------|
| `color-background` | #FFFFFF | #1A1A1A | Page background |
| `color-surface` | #F8F9FA | #2D2D2D | Cards, containers |
| `color-surface-elevated` | #FFFFFF | #3D3D3D | Modals, dropdowns |
| `color-text-primary` | #1A1A1A | #F0F0F0 | Headings, body |
| `color-text-secondary` | #6B7280 | #A0A0A0 | Captions, metadata |
| `color-text-muted` | #9CA3AF | #707070 | Placeholders |
| `color-border` | #E5E7EB | #404040 | Dividers, outlines |
| `color-border-strong` | #D1D5DB | #505050 | Emphasis borders |
| `color-accent` | #2563EB | #3B82F6 | Links, CTAs |
| `color-accent-hover` | #1D4ED8 | #60A5FA | Interactive states |
| `color-success` | #059669 | #10B981 | Positive signals |
| `color-warning` | #D97706 | #F59E0B | Caution signals |
| `color-error` | #DC2626 | #EF4444 | Error states |
| `color-focus-ring` | #3B82F6 | #60A5FA | Keyboard focus |

**Credibility constraint**: Avoid palettes that read as "consumer playful" unless requested. Prioritize trust, clarity, technical precision.

**No decoration color rule**: Color must encode hierarchy, status, or interaction, not vibe-only.

### Spacing Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Tight gaps |
| `space-2` | 8px | Component internal |
| `space-3` | 12px | Related elements |
| `space-4` | 16px | Standard gap |
| `space-6` | 24px | Section gap |
| `space-8` | 32px | Major sections |
| `space-12` | 48px | Page sections |
| `space-16` | 64px | Hero spacing |

### Border and Radius Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 4px | Small elements, chips |
| `radius-md` | 8px | Cards, buttons |
| `radius-lg` | 12px | Large containers |
| `radius-full` | 9999px | Pills, avatars |
| `border-width-default` | 1px | Standard borders |
| `border-width-strong` | 2px | Emphasis, focus |

### Elevation Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | 0 1px 2px rgba(0,0,0,0.05) | Subtle lift |
| `shadow-md` | 0 4px 6px rgba(0,0,0,0.1) | Cards |
| `shadow-lg` | 0 10px 15px rgba(0,0,0,0.1) | Modals, dropdowns |

---

## Component Inventory

### Navigation Components

| Component | Variants | Usage | Avoid when |
|-----------|----------|-------|------------|
| Header | Minimal, Full | Page top | Content-dense pages |
| Sidebar TOC | Sticky, Collapsible | Case studies | Short pages |
| Breadcrumb | Standard | Deep navigation | Top-level pages |
| Jump links | Inline, Floating | Long pages | Short pages |

### Content Components

| Component | Variants | Usage | Avoid when |
|-----------|----------|-------|------------|
| Section header | H2, H3, with metadata | All sections | Never avoid |
| Evidence chip | Confidence, Shareability | Claims | Non-claim content |
| Role chip | Owned, Led, Influenced | Attribution | Solo work |
| Metric card | Single, Comparison | Outcomes | No metrics |
| Quote block | Stakeholder, User | Testimony | Unattributed quotes |
| Callout | Info, Warning, NDA | Alerts | Overuse |
| Evidence table | Standard | Claims mapping | Simple claims |
| Artifact frame | Image, Redacted, Diagram | Visuals | Text-only |

### Interactive Components

| Component | States | Usage |
|-----------|--------|-------|
| Link | Default, Hover, Visited, Focus | Navigation |
| Button | Default, Hover, Active, Disabled, Focus | CTAs |
| Accordion | Closed, Open, Focus | Progressive disclosure |
| Tab | Inactive, Active, Focus | View switching |
| Tooltip | Hidden, Visible | Contextual help |

---

## Layout and Grid Spec

### Grid System

| Token | Value | Usage |
|-------|-------|-------|
| `max-content-width` | 1200px | Page container |
| `max-text-width` | 720px | Long-form reading |
| `gutter` | 24px | Column gaps |
| `margin-mobile` | 16px | Mobile edges |
| `margin-desktop` | 48px+ | Desktop edges |

### Section Templates

**Homepage/Landing**:
- Hero: Signal strip + positioning
- Case study grid: 2-3 columns
- Quick-nav sections
- CTA block

**Case Study List**:
- Filterable index
- Card grid or list view
- Metadata chips visible

**Case Study Page**:
- Sticky TOC sidebar (desktop)
- Executive skim block (prominent)
- Deep dive sections (collapsible optional)
- Evidence table (expandable)
- Related artifacts

**Governance Dossier**:
- Philosophy statement
- Evaluation approach
- Guardrails grid
- Case study cross-links

### Responsive Behavior

| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| TOC | Sticky sidebar | Collapsible top | Accordion |
| Case study grid | 3 columns | 2 columns | 1 column |
| Evidence table | Full width | Horizontal scroll | Stacked |
| Navigation | Full header | Hamburger | Hamburger |

---

## Graphic Design Style

### Diagram Style

| Element | Specification |
|---------|--------------|
| Line weight | 1-2px |
| Corner radius | Consistent with `radius-md` |
| Arrow style | Simple, single-headed |
| Connector rules | Right angles or smooth curves, not mixed |
| Labeling | Clear, outside shapes when possible |
| Color | Minimal, functional only |

### Data Visualization Rules

| Rule | Specification |
|------|--------------|
| Chart palette | Max 4 colors from semantic tokens |
| Annotation style | Clear labels, outside data when possible |
| Axis labeling | Always visible, clear units |
| Ranges | Show confidence intervals when available |
| Grid lines | Minimal, light |

### Iconography

| Element | Specification |
|---------|--------------|
| Style | Outline, consistent stroke weight |
| Stroke weight | 1.5-2px |
| Grid size | 24x24px base |
| Rounding | Match `radius-sm` |
| Where allowed | Navigation, metadata chips, callouts |

---

## Photography and Imagery Policy

### Stance

Prefer diagrams and artifacts over photography. Photography only when:
- Workshop/collaboration documentation (with permission)
- Artifact screenshots
- System diagrams

### Rules

| Rule | Specification |
|------|--------------|
| Aspect ratios | 16:9, 4:3, 1:1 (consistent per context) |
| Cropping | Content-aware, no awkward cuts |
| Treatment | No heavy filters, minimal adjustment |
| Captioning | Required for all images |
| Alt text | Required for accessibility |
| Licensing | User-owned or properly licensed only |

---

## Motion System

### Motion Grammar

| Motion type | Duration | Easing | Usage |
|-------------|----------|--------|-------|
| Micro-feedback | 100-150ms | ease-out | Hover, focus |
| State change | 200-250ms | ease-in-out | Accordion, tabs |
| Page transition | 300-400ms | ease-in-out | Navigation |
| Attention | 400-600ms | ease-in-out | Notifications |

### Microinteraction Patterns

| Interaction | Behavior | Purpose |
|-------------|----------|---------|
| Link hover | Underline + color shift | Affordance |
| Button hover | Background shift | Feedback |
| Accordion open | Smooth expand | Orientation |
| Evidence reveal | Fade in | Progressive disclosure |
| Copy-to-clipboard | Checkmark flash | Confirmation |
| Artifact zoom | Scale + overlay | Detail access |

### Reduced Motion Mode

All motion must have reduced-motion alternatives:

| Full motion | Reduced motion |
|-------------|---------------|
| Slide transitions | Instant cut |
| Fade in | Instant appear |
| Expand/collapse | Instant toggle |
| Hover animations | Static state change |

**Rule**: Motion must clarify structure or state change, never decoration.

---

## Visual Disclosure Patterns (NDA-Safe)

### Redacted Artifact Frames

| Pattern | Usage | Implementation |
|---------|-------|----------------|
| Blur regions | Hide specific text/data | Gaussian blur overlay |
| Masked tables | Hide column values | Solid color blocks |
| Cropped UI | Show partial interface | Strategic crop with border |
| Placeholder blocks | Indicate omitted content | Labeled empty state |

### Restaged Visuals

When showing reconstructed examples:
- Use generic UI skins
- Label clearly as `[Reconstructed]` or `[Illustrative]`
- Match fidelity to original intent, not original brand

### Evidence Signaling Without Exposure

"Proof chips" pattern:

```
[Artifact: Production dashboard] [Confidence: High] [Shareability: Interview-only]
```

---

## Leadership-Forward Patterns

### Role Chips

| Chip | Usage |
|------|-------|
| `Set direction` | Strategic decisions |
| `Established quality bar` | Standards setting |
| `Unblocked delivery` | Obstacle removal |
| `Decision owner` | Final call authority |
| `Coached team` | Development role |
| `Aligned execs` | Stakeholder management |

### Decision Log Cards

```
┌─────────────────────────────────────┐
│ Decision: [What was decided]        │
│ Options: [A, B, C]                  │
│ Tradeoff: [Key consideration]       │
│ Owner: [Role]                       │
│ Date: [When]                        │
│ Downstream: [What it affected]      │
└─────────────────────────────────────┘
```

---

## Builder-Agnostic Output

### CSS Variables Snippet

```css
:root {
  --color-background: #FFFFFF;
  --color-surface: #F8F9FA;
  --color-text-primary: #1A1A1A;
  --color-text-secondary: #6B7280;
  --color-accent: #2563EB;
  --font-display: Inter, system-ui, sans-serif;
  --font-text: Inter, system-ui, sans-serif;
  --space-4: 16px;
  --radius-md: 8px;
  /* ... */
}
```

### Implementation Mapping

| Token category | Webflow | Framer | Figma | CSS |
|---------------|---------|--------|-------|-----|
| Colors | Color variables | Tokens | Styles | CSS vars |
| Typography | Text styles | Text styles | Text styles | Font classes |
| Spacing | Spacing classes | Spacing tokens | Auto layout | Margin/padding |
| Components | Symbols | Components | Components | Classes |

---

## Visual QA Checklist

- [ ] Contrast meets WCAG AA (4.5:1 text, 3:1 large text)
- [ ] Links distinguishable from body text
- [ ] Focus states visible for all interactive elements
- [ ] Typography scale consistent throughout
- [ ] Spacing rhythm consistent
- [ ] All interaction states defined (hover, focus, active)
- [ ] Keyboard navigation functional
- [ ] Touch targets minimum 44x44px
- [ ] Motion has purpose and reduced-motion fallback
- [ ] Images have captions and alt text
- [ ] Color not sole indicator of meaning
