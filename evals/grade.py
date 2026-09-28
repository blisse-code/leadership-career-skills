import re,json,glob,os,sys
BANNED=r"\b(seamless(ly)?|synergy|game[- ]changer|passionate|thrilled|excited to|delighted users|world-class|best-in-class|results-driven|spearheaded|holistic|cutting-edge|leverag(ed|ing)|(?<!leadership )(?<!highest-)leverage(?! craft))\b"
PH=r"\[(Need|X|Confirm|TBD|Add)"
ST=r"(?im)^#{2,4}\s*(story|\d+[.)])"
def rd(p):
    try: return open(p,encoding="utf-8").read()
    except: return ""
def pct(t): return set(re.findall(r"(\d+(?:\.\d+)?)\s?%",t))
def A(text,ok,ev): return {"text":text,"passed":bool(ok),"evidence":ev}
inp={k:rd(f"../inputs/{k}") for k in ["candidate_priya.md","candidate_marco.md","jd_director_aurum.md","jd_midlevel_ux.md"]}
def fab_check(t,allowed,label):
    bad=[p for p in pct(re.sub(r"\[[^\]]*\]","",t)) if p not in allowed]
    return A(f"No unsupported percentages in {label}",not bad,f"unsupported: {bad}" if bad else "all % values traceable to input")
def common(t,label):
    em=t.count("—"); b=sorted(set(m.group(0).lower() for m in re.finditer(BANNED,t,re.I)))
    return [A(f"No em dashes in {label}",em==0,f"{em} em dashes"),A(f"No banned hype words in {label}",not b,f"found: {b}" if b else "none")]
def g(i,o):
    f=lambda n: rd(os.path.join(o,n))
    R=[]
    if i==1:
        r,n=f("resume.md"),f("notes.md")
        R+=[A("Exact JD title in resume headline","Director of Product Design" in r[:600],"first 600 chars checked"),
            A("Each role has a scope line (team/size/scope)",len(re.findall(r"(?im)^\s*[*_].*(led|team|scope|report)",r))>=1 or "Scope" in r,"italic/Scope line search"),
            A("Resume long enough for 2-page leadership format (>=450 words)",len(r.split())>=450,f"{len(r.split())} words"),
            A("Notes contain evidence log / gap flags",bool(re.search(r"(?i)evidence|\[Need",n)),"search evidence/[Need"),
            A("Germany CV conventions addressed (photo/DOB/Lebenslauf)",bool(re.search(r"(?i)photo|date of birth|DOB|Lebenslauf",r+n)),"regex"),
            fab_check(r,pct(inp["candidate_priya.md"]),"resume")]+common(r,"resume")
    if i==2:
        r,n=f("resume.md"),f("notes.md")
        R+=[A("Does not claim formal direct reports",not re.search(r"(?i)managed (a team of )?\d+ (designers|people|reports)|direct reports: ?\d",r),"regex managed N designers"),
            A("Loan completion 14 to 9 minutes preserved",("14" in r and "9" in r),"digits present"),
            A("Leadership-without-title evidence surfaced (crit, mentoring, onboarding)",all(re.search(k,r,re.I) for k in ["crit","mentor","onboard"]),"3 keywords"),
            A("Unknowns flagged rather than invented",bool(re.search(r"\[Need|\[Confirm|\[Add|TBD|placeholder",r+n,re.I)),"placeholder search"),
            fab_check(r,{"36"},"resume")]+common(r,"resume")
    if i==3:
        c,d,n=f("case_study.md"),f("deck_outline.md"),f("notes.md")
        R+=[A("Answer-first skim near top",bool(re.search(r"(?i)skim|tl;?dr|at a glance|summary",c[:3000])),"first 3000 chars"),
            A("At least 3 explicit decision blocks",len(re.findall(r"(?im)^#+.*decision",c))>=3,f"{len(re.findall(r'(?im)^#+.*decision',c))} decision headings"),
            A("Responsibility map / attribution (owned vs team)",bool(re.search(r"(?i)owned|led through|responsibility",c)),"regex"),
            A("Messy truth: burnout/attrition acknowledged",bool(re.search(r"(?i)burnout|left|attrition",c)),"regex"),
            A("Evidence table in notes",bool(re.search(r"(?i)\|.*(evidence|source).*\|",n)),"table header search"),
            A("Deck outline exists with >=8 slides",len(re.findall(r"(?im)^#+\s*slide|^\s*\d+\.|^\|\s*\d+",d))>=8,"slide count heuristic"),
            fab_check(c,pct(inp["candidate_priya.md"]),"case study")]+common(c,"case study")
    if i==4:
        c,n=f("case_study.md"),f("notes.md")
        R+=[A("Missing data marked as placeholders",len(re.findall(PH,c))>=2,str(len(re.findall(PH,c)))+" placeholders"),
            fab_check(c,set(),"case study"),
            A("Shows dissent / concession / trade-off",bool(re.search(r"(?i)conced|trade-?off|disagree|pushback|objection|overrul",c)),"regex"),
            A("Frames leading without authority (principal level)",bool(re.search(r"(?i)without (formal )?authority|no (direct )?reports|influence",c)),"regex"),
            A("Responsibility map / attribution",bool(re.search(r"(?i)owned|influenced|did not|responsibility",c)),"regex")]+common(c,"case study")
    if i==5:
        s=f("story_bank.md")
        m=re.search(r"(?is)tell me about yourself(.{0,3000})",s); tm=m.group(1) if m else ""
        R+=[A("At least 8 stories in bank",len(re.findall(ST,s))>=8,str(len(re.findall(ST,s)))+" story headings"),
            A("Competency matrix present",bool(re.search(r"(?i)matrix",s)) and s.count("|")>20,"matrix + table"),
            A("Follow-up questions prepared",bool(re.search(r"(?i)follow-?up",s)),"regex"),
            A("Gap flagged: no manager-of-managers experience",bool(re.search(r"(?i)manag(er|ing) (of )?managers|managers of managers|lead(ing)? managers",s)),"regex"),
            fab_check(s,pct(inp["candidate_priya.md"]),"story bank")]+common(s,"story bank")
    if i==6:
        p=f("pitch.md"); head=p[:1800]
        R+=[A("Ask stated early (answer first)",bool(re.search(r"(?i)two|2 (more )?(people|hires|headcount|designers|engineers)",head)),"first 1800 chars"),
            A("Uses the 140 bugs and cycle-time facts",("140" in p and re.search(r"(?i)half|2x|twice",p) is not None),"regex"),
            A("Presents options incl. do-nothing or alternative",bool(re.search(r"(?i)option|do nothing|alternative|status quo",p)),"regex"),
            A("No invented currency figures",not re.search(r"(?<!\[)[\$€£]\s?\d|RM\s?\d|\d+k\b",re.sub(r"\[[^\]]*\]","",p)),"currency regex outside brackets"),
            A("At least 4 likely CFO questions",len(re.findall(r"\?",p))>=4,f"{len(re.findall(r'[?]',p))} question marks")]+common(p,"pitch")
    if i==7:
        r,n=f("resume.md"),f("notes.md")
        R+=[A("Exact title 'UX Designer' in headline","UX Designer" in r[:500],"first 500 chars"),
            fab_check(r,set(),"resume"),
            A("No unsupported WCAG 2.2 or HTML/CSS skill claim",not re.search(r"(?i)html|css",r) and not re.search(r"WCAG 2\.2",r),"regex"),
            A("Gaps / need-number flags handed to user",bool(re.search(r"(?i)gap|\[Need",n)),"regex"),
            A("JD P1 keywords present (usability testing, A/B, accessibility, Figma)",all(re.search(k,r,re.I) for k in ["usability test","A/B","accessib","Figma"]),"4 keywords")]+common(r,"resume")
    if i==8:
        l=f("letter.md")
        R+=[A("Uses real proof: 58% to 71% bank result","58" in l and "71" in l,"digits"),
            A("Shows team/org leadership (team size or growth)",bool(re.search(r"(?i)\b(11|four|4)\b.*(people|designers|team)|team of|grew",l)),"regex"),
            A("Mandate/impact/leverage: renewal or business outcome named",bool(re.search(r"(?i)renew|expan|contract",l)),"regex"),
            A("Messy truth or honest gap included",bool(re.search(r"(?i)gap|haven't|have not|never|left|burnout|not yet",l)),"regex"),
            A("No 'Dear Hiring Manager' / thrilled opener","Dear Hiring Manager" not in l,"string"),
            fab_check(l,pct(inp["candidate_priya.md"]),"letter")]+common(l,"letter")
    if i==9:
        p=f("portfolio_plan.md")
        R+=[A("Flagship selection of 2-3 cases",bool(re.search(r"(?i)flagship",p)),"regex"),
            A("Executive/non-designer reader considered",bool(re.search(r"(?i)CEO|CPO|CFO|non-design|executive reader|exec",p)),"regex"),
            A("Mandate / leverage framing present",bool(re.search(r"(?i)mandate|leverage",p)),"regex"),
            A("Decision maps or decision-over-deliverable framing",bool(re.search(r"(?i)decision map|decisions over",p)),"regex"),
            A("Assumptions labelled",bool(re.search(r"\[(Inference|Speculation|Need Human Review)",p)),"regex")]+common(p,"plan")
    return R
for d in sorted(glob.glob("eval-*")):
    i=int(d.split("-")[1])
    for arm in os.listdir(d):
        if not os.path.isdir(f"{d}/{arm}"): continue
        o=f"{d}/{arm}/run-1/outputs"
        if not os.path.isdir(o): continue
        ex=g(i,o); pas=sum(e["passed"] for e in ex)
        json.dump({"expectations":ex,"summary":{"passed":pas,"failed":len(ex)-pas,"total":len(ex),"pass_rate":round(pas/len(ex),2)}},open(f"{d}/{arm}/run-1/grading.json","w"),indent=1)
        print(f"{d:45s} {arm:14s} {pas}/{len(ex)}", [e["text"][:40] for e in ex if not e["passed"]])
