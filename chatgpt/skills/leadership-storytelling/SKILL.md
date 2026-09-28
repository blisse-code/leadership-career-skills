---
name: leadership-storytelling
description: Craft and rehearse the stories leaders tell, for career moments (interview story bank, "tell me about yourself", behavioral answers, portfolio panel talk tracks, career walking deck, 30-60-90 day plan, LinkedIn leadership POV posts) and for the job itself (vision story for a team, pitching design investment to executives, change or transformation narrative, delivering bad news, handling resistance). Use whenever the user is preparing for a leadership interview or panel, asks "how do I tell this story", wants STAR/CAR answers, a signature story, an elevator pitch, a keynote or all-hands narrative, a stakeholder pitch, or says their story "sounds flat", "rambles", or "doesn't land". Built on Ganz, Simmons, Denning, Duarte, Minto, and the Heath brothers. Strong fit for design and UX leaders; works for any leader. Never invents events or results.
---

> **ChatGPT edition.** Same method as the Claude version. Where this file mentions companion skills, use them if they are installed in your workspace; otherwise continue with the rules stated here. Run bundled scripts in ChatGPT's code environment when available.

# Leadership Storytelling

Leaders are judged by what others can repeat about them. A resume says where you worked; a story makes a panel, a CEO, or a team *remember* how you think and *repeat* it to someone else. This skill turns the user's real experience into stories that are short, specific, true, and built for a listener.

It works in two modes:
- **Career mode**: interviews, panels, walking deck, 30-60-90 plan, LinkedIn POV. The listener is deciding whether to trust you with a team.
- **On-the-job mode**: vision, pitch, change, bad news, resistance. The listener is deciding whether to follow you.

## Principles

1. **Challenge, choice, outcome** (Marshall Ganz). Every leadership story has a moment of challenge, a choice the leader made, and what followed. Without the choice there is no leader in the story. The choice is where values show.
2. **Listener first.** Decide what the listener should think, feel, and do afterwards before drafting. A panel wants evidence of judgment; a CFO wants risk and return; a team wants meaning and a path.
3. **Answer first for executives, tension first for teams.** Executives want the conclusion, then support (Minto). Teams and keynotes need the gap between "what is" and "what could be" (Duarte) to feel the stakes.
4. **One concrete detail beats three abstractions** (Heath, *Made to Stick*). "The CEO printed the churn report and put it on my chair" beats "leadership was concerned about retention".
5. **Show values in action, never announce them.** "I value transparency" is a claim. The time the user shared a failed test result with the exec team before being asked is a story.
6. **True or it doesn't get told.** Use only events the user lived. Composite or anonymized details are fine when labelled; invented results are not. Interviewers probe; invented detail collapses under the second follow-up.
7. **Spoken, not written.** Short sentences, one idea each, natural pauses. Stories are drafted to be *said*.

## Workflow

### Step 1: Define the moment
Ask (or infer) in one message, with example answers:
- The moment: interview, panel, walking deck, all-hands, exec pitch, LinkedIn post, other
- The listener(s) and what they care about
- The desired result: what should they think, feel, do
- Time available: 60 seconds, 2 minutes, 5, 20+
- Raw material: projects, case studies, resume, notes

### Step 2: Mine and select stories
If building for interviews, create a **Story Bank** (see `references/story-bank.md`): 8-12 stories from the user's career, each tagged to leadership competencies and likely questions, so one story can answer several questions. Use the evidence-mining prompts there; people forget their best stories until asked the right question ("when did you disagree with your boss and turn out to be right?").

For a single moment, pick the story type from `references/story-frameworks.md`: who-I-am, why-I'm-here, vision, values-in-action, teaching, I-know-what-you're-thinking (Simmons), or Denning's patterns (sparking action, sharing knowledge, leading into the future).

### Step 3: Structure
Choose the frame that fits the moment:

| Moment | Frame |
|---|---|
| Behavioral interview answer | STAR-L: Situation (1-2 lines), Task, Actions (the choices, 60% of time), Result, Learning |
| "Tell me about yourself" | Present, past, future + leadership signature (90 seconds) |
| Panel case presentation | Mandate, role, decisions, messy middle, outcome, lesson (use `ux-leadership-case-study` if present) |
| Exec pitch / design investment | SCQA (Situation, Complication, Question, Answer), then options, risk, ask |
| Team vision / all-hands | Story of Self, Us, Now (Ganz), ending in a concrete ask |
| Change / transformation | What is / what could be alternation (Duarte), with the resistance voiced early |
| Bad news | Fact first, impact, what we're doing, what I need, when you'll hear next |
| LinkedIn POV post | Specific moment, what I noticed, what I did, what changed, the belief it taught |

Details and examples for each frame are in `references/story-frameworks.md` and `references/on-the-job-narratives.md`.

### Step 4: Draft for the ear
- Open with a hook that is a *moment*, not a summary: "Three weeks into the job, our biggest client asked to pause the contract."
- Keep Situation short; spend the time on the choices and why.
- Include one sensory or human detail and one number.
- Name who disagreed and what they wanted. Tension is what makes listeners lean in.
- Say "I" for the user's actions, "the team" for theirs.
- Land on a one-line takeaway the listener can repeat.
- Write the length to the clock: ~130-150 spoken words per minute.

### Step 5: Pressure-test
Run the checks in `references/delivery-and-rehearsal.md`:
- **Repeatability test**: could the listener repeat the point in one sentence to someone else?
- **Follow-up test**: generate the 3 hardest follow-up questions and outline answers.
- **Specificity test**: remove every abstract noun that has no example behind it.
- **Time test**: word count to target minutes.
- **Values test**: what does this story say about the user without saying it? Is that the intended message?

**Final scrub (every deliverable, including notes and decks).** Em dashes (—) and en dashes used as dashes (–) are the most common thing that slips through, because they feel natural mid-draft. Before delivering, search every output file for them and replace with a comma, colon, period, or parentheses, e.g. `grep -c "—\|–" <file>` must return 0. Hyphens in compound words and date ranges written with a plain hyphen ("2022 - 2024") are fine. Spoken scripts suffer most here: a dash in a script becomes a stumble out loud, so use a period and a pause instead.

### Step 6: Deliver
Give the user: the story (spoken script), a bullet version (what they actually hold in their head), timing, the follow-up Q&A, and one line on what this story proves. For a story bank, deliver the full bank plus a competency-by-story matrix. For a walking deck or 30-60-90 plan, use `references/walking-deck-and-plans.md` and hand off to a slides skill if an actual deck is wanted.

## Style rules
- No em dashes; no banned words (seamless, passionate, visionary, synergy, game changer, journey as metaphor, delighted, leverage as "use", elevate, unlock, empower, world-class).
- No clichés as openers ("In today's fast-paced world", "I've always been passionate about").
- No invented quotes or dialogue attributed to real people; paraphrase what the user reports and mark it as paraphrase.
- Humor and self-deprecation are fine in small doses when they reveal judgment; never undercut the work ("it's just a small project").

## Adjacent skills
- `ux-leadership-case-study`: the written case study behind a panel story.
- `leadership-resume-architect`: every story in the bank should connect to a resume bullet, and vice versa.
- `bespoke-cover-letter`: the signature story often becomes the letter's opening.
- `elite-communication-codex`, `leverage-craft`, `headline-craft`: sentence-level sharpening, if installed.

## Reference files
| File | Read when |
|---|---|
| `references/story-frameworks.md` | Step 2-3: frameworks, story types, templates |
| `references/story-bank.md` | Interview prep: mining prompts, bank format, competency matrix, question list |
| `references/on-the-job-narratives.md` | Vision, pitch, change, bad news, resistance, all-hands |
| `references/walking-deck-and-plans.md` | Career walking deck, 30-60-90 plan, LinkedIn POV series |
| `references/delivery-and-rehearsal.md` | Step 5: tests, delivery, Q&A handling, remote panels |
| `references/research-basis.md` | Sources behind the rules |
