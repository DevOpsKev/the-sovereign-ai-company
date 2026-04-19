# The Sovereign AI Company — Writing Outline

*Working document. This is the distilled source of truth for what the book is arguing, how it's
structured, and what each chapter needs to do. Use this as the context
primer when starting a new writing session.*

---

## The argument in one paragraph

AI has become load-bearing infrastructure for every serious company, and the
post-1945 rules-based order that made it safe for European businesses to
rent that infrastructure from American vendors is failing. This book is not
an argument that EU companies should stop using OpenAI, Anthropic, AWS, or
Azure. It is an argument that they need a Plan B — a managed set of
dependencies across compute, models, data, talent, and regulation that can
keep the lights on if access is cut or terms turn hostile, while Europe
builds competitive alternatives. The posture is cold-eyed continuity
planning, not ideology. "We depend on each other, and that is the starting
position, not the conclusion."

## The tagline

*"Have a Plan B that can keep your lights on — while Europe builds
competitive alternatives."*

## Audience

- **Primary:** C-level executives and senior technology leaders at European
  (incl. UK) mid-cap and enterprise firms
- **Secondary:** founders, board members, strategy and transformation
  consultants serving the above
- **Also useful for:** policy readers, journalists covering EU tech, and
  American executives who want to understand what their European customers
  are increasingly worried about

## Positioning and voice

- **Confident but not anti-American.** The book is about continuity,
  hedging, and negotiating leverage. "We depend on each other."
- **Cold-eyed and operational in the middle 85%.** Values language belongs
  in the opening chapter and the epilogue; the body of the book is
  execution analysis.
- **Honest about the capability gap.** Mistral is not as good as frontier
  US/Chinese models on reasoning. The argument is that for enterprise
  workloads, this matters less than readers assume — not that the gap
  doesn't exist.
- **Names names.** European companies making good and bad calls. US
  hyperscalers and their "sovereign cloud" theatre. Palantir as a litmus
  test European governments keep failing.
- **UK treated as a de facto EU member for AI strategy purposes.**
  Post-Brexit politically, aligning closer in practice. Defence will be
  the healing driver — "those wounds will heal stronger than before."

## Format

- ~80,000 words
- 7 parts, 17 chapters, plus epilogue
- Trade paperback (5.25 × 8 in), EPUB, screen PDF
- Published via Distributed Equity Press (self-published)

---

## Structural logic of the book

**Why this structure works.** The signature chapter is Chapter 4 (The
Hyperscale Myth), not the geopolitical opener. The geopolitical framing
earns the pickup; the contrarian operational argument is what gets readers
recommending the book to colleagues. Part I sets up the world. Parts II–V
work dependency-by-dependency (compute → models → data → talent). Part VI
proposes the affirmative vision. Part VII converts it into a playbook.
Epilogue carries the values close.

**Why 7 parts and 17 chapters.** Dependency-stack structure ages best —
specific vendors and regulations shift; the underlying dependencies
(compute, models, data, talent, regulatory reach) are durable. Seventeen
chapters is substantial without being intimidating for an executive
audience.

---

## Part I — The Reckoning

*~13,000 words. Sets up the world the rest of the book operates in.
Geopolitical framing, "load-bearing" thesis, and the bipolar model
landscape as the single most important geopolitical fact European
executives have not fully processed.*

### Chapter 1 — The End of the Assumption

**Core argument.** The post-1945 rules-based order was the operating system
European business ran on. It is failing — not as prediction, as present
description. This chapter establishes the Plan B framing as the book's
thesis and anchors every subsequent argument.

**Key content.**

- Trump II-era tariff threats (300% tariff on AI as stress-test scenario)
- Project Glass Wing and tiered access to frontier models
- The CLOUD Act as extraterritorial leverage
- Canadian, Arab state, and Chinese divestment flows from US assets
- EU post-NATO defence thinking and the nascent EU army conversation
- Why this concentrates risk differently than previous tech dependencies
- The Plan B frame introduced and owned: "We are not saying don't use
  Anthropic or OpenAI. We are saying have a Plan B."

**Tone note.** Do not assume the post-rules-based-order shift as settled
fact — walk the reader through the evidence. Half the audience is
American-aligned in instincts; lose them here and the book fails.

### Chapter 2 — AI as Load-Bearing Infrastructure

**Core argument.** AI is no longer SaaS. It writes the software, handles
the customer service, processes the contracts. Compete with AI or die —
and you cannot compete if the infrastructure is rented from a jurisdiction
that can cut you off.

**Key content.**

- The shadow economy of ChatGPT and Claude inside enterprises (employees
  using them regardless of official policy)
- Measuring actual AI dependency: how to audit what your company actually
  cannot function without
- Why SaaS dependencies were tolerable and AI dependencies aren't —
  velocity, depth, and substitutability
- The "critical infrastructure" framing as the right mental model for
  regulators, boards, and CFOs

### Chapter 3 — The Bipolar Model Landscape

**Core argument.** Every frontier model in production today is US-owned
or Chinese-owned. Mistral is the only serious EU-origin effort; Cohere is
Canadian. This bipolarity is the geopolitical fact that structures every
decision in the book.

**Key content.**

- Roster: OpenAI, Anthropic, Google/Gemini, Meta (US) vs. Qwen (Alibaba),
  DeepSeek, Kimi, GLM/Zhipu, Yi (China)
- Mistral and Cohere as statistical outliers
- The open-weight shift and why Chinese models have become the most
  capable open-weight options available — a strategic fact with
  uncomfortable implications
- Xi Jinping's stated AI priority, the Chinese education pipeline,
  projected GDP crossover
- Why Europe has not been pricing this correctly
- What "sovereignty" means in a bipolar world: not autarky, but managed
  dependency across more than one pole

---

## Part II — The Compute Question

*~13,000 words. The physical substrate. Contains the book's signature
contrarian chapter (Ch. 4) and the Taiwan stress test that every later
recommendation has to survive (Ch. 6).*

### Chapter 4 — The Hyperscale Myth *(signature chapter)*

**Core argument.** Most EU enterprise AI workloads do not need hyperscale.
Hyperscale is overhead sold to European CFOs at Silicon Valley margins for
capability they never use. Hetzner, OVH, Scaleway, and StackIT can absorb
the vast majority of real workloads at a fraction of the cost.

**Key content.**

- Total-cost-of-ownership reality checks: named comparisons of AWS/Azure/
  GCP vs. Hetzner/OVH/Scaleway/StackIT for representative workload
  profiles
- The "sovereign cloud" offerings from the hyperscalers — Azure for
  Sovereignty, AWS European Sovereign Cloud, GCP sovereign controls —
  examined honestly: real, or theatre?
- Workload segmentation: when hyperscale genuinely matters (global
  latency, extreme burst, specific managed services) and when it doesn't
- The Schwarz Group / StackIT story as evidence Europeans can run this at
  scale
- "You have been overpaying for capability you do not use" — the single
  most quotable argument in the book

**Interview targets.** A CTO who moved off hyperscale. A Hetzner or OVH
executive on the mid-market story. A European CFO who has done the
economic analysis.

**Why this chapter matters most.** If the rest of the book is correct but
this chapter is wrong, readers conclude sovereignty requires sacrifice. If
this chapter lands, sovereignty becomes the *cheaper* option for most
workloads — and everything else in the book flows from there.

### Chapter 5 — Building on European Rails

**Core argument.** Practical transition patterns from hyperscaler lock-in
to European compute. Energy, land, and data centre geography as strategic
assets. Defence-driven investment as the tailwind finally making this
viable.

**Key content.**

- Migration patterns: lift-and-shift vs. workload-by-workload
- Kubernetes, open-source orchestration, and why portable architectures
  make the transition feasible
- The Gaia-X autopsy — what went wrong and what to learn
- Where European data centres are being built, who is funding them, where
  the energy is coming from
- Defence, AI Factories, and IPCEI investment as the funding engine
  Europe has been missing
- The critical-raw-materials and grid-capacity questions honestly
  addressed

### Chapter 6 — The Taiwan Question

**Core argument.** TSMC is the single point of failure for the entire
Western AI stack. Any sovereignty strategy that doesn't survive a Taiwan
contingency is a PR exercise. This chapter is the stress test every later
recommendation must pass.

**Key content.**

- The TSMC chokepoint explained for a non-technical executive audience
- ASML's indispensable role and why it is Europe's crown jewel
- Samsung Foundry, Intel Foundry, and SMIC progress — realistic timeline
  for non-Taiwan leading-edge capacity
- What "if Taiwan goes hot" actually looks like for enterprise AI —
  timeline, price, availability
- How to stress-test a sovereignty plan against this scenario
- Why this is in Part II (compute) rather than Part I (geopolitics): it
  is a physical substrate problem, not an abstract one

---

## Part III — The Model Layer

*~10,000 words. The model stack, the honest gap, and how to architect
around it.*

### Chapter 7 — Enterprise Good Enough

**Core argument.** Frontier reasoning benchmarks are a poor proxy for
enterprise value. Most production workloads are document extraction,
classification, summarisation, structured generation, RAG over internal
data, and agentic orchestration — where reliability, cost, and latency
matter more than whether the model can solve IMO problems. Mistral and
the open-weight ecosystem are already good enough for most of this.

**Key content.**

- Workload taxonomy: which tasks demand frontier reasoning and which
  don't (the 80/20 split)
- Benchmarks vs. production reality — MMLU and the reasoning benchmarks
  are not the job description
- Mistral's actual capability envelope, honestly assessed
- The open-weight ecosystem: Llama, Qwen, DeepSeek, GLM — what they do
  well, where they fail
- Fine-tuning and distillation as force multipliers that make "good
  enough" actually *better* than frontier-via-API for specific domains
- The honest caveat: there are workloads where frontier reasoning
  genuinely matters (novel research, hard code generation, certain
  agentic tasks). Acknowledge this clearly.

**Interview targets.** An enterprise running significant production
workload on Mistral or open-weight. A head of AI at a mid-cap.

### Chapter 8 — The Hedged Model Strategy

**Core argument.** The answer is not "dump Anthropic, use only Mistral."
It is a multi-model architecture with routing, fallbacks, and
jurisdictional hedging. Capture resistance by design.

**Key content.**

- Multi-model architectures as the engineering pattern: model routers,
  fallback chains, per-workload provider selection
- When to use Anthropic or OpenAI and how to do it without becoming
  captured — data handling, contractual terms, exit plans
- The specific question of Chinese open-weight models: when they are the
  right Plan B and when they introduce their own dependencies (supply
  chain, licensing, trust)
- Jurisdictional hedging: why production model calls should be routable
  by jurisdiction, not just by capability
- Costs, latency, and operational complexity of a hedged strategy —
  honest accounting, not salesmanship

---

## Part IV — Data and Jurisdiction

*~9,000 words. The legal collision and the one asset American vendors
cannot replicate.*

### Chapter 9 — The CLOUD Act vs. the AI Act

**Core argument.** The US CLOUD Act and the EU AI Act are on a legal
collision course. Schrems II is not a one-off. Extraterritoriality flows
in both directions, and your general counsel needs to understand it
before your CTO signs anything.

**Key content.**

- The CLOUD Act explained: what it actually obliges US providers to do
  with data held abroad
- Schrems II and why it still shapes transatlantic data flow
- The AI Act's extraterritorial reach — non-EU providers serving EU
  users are in scope
- Real enforcement cases and what they tell us about direction of travel
- "Sovereign cloud" marketing claims tested against the actual text of
  the CLOUD Act
- What your GC needs on the first slide

### Chapter 10 — Data as Strategic Asset

**Core argument.** Your proprietary data is the one thing US hyperscalers
and their models cannot give you. Data residency is not a compliance
cost — it is competitive advantage.

**Key content.**

- Why the GDPR fight set the template for the AI fight — Europe learned
  to win on data law
- Proprietary data as the moat that matters: fine-tuning, RAG, domain
  specialisation
- Data as a negotiating asset — why giving it to a frontier lab gives
  them more than they give you
- The defence and health data question: Palantir as the most uncomfortable
  case study. How European governments keep buying Palantir for health
  and defence despite it being the clearest possible sovereignty
  contradiction. Own this; don't dodge it.

---

## Part V — Talent and Capability

*~9,000 words. The people problem. The talent exists; the question is
whether Europe can keep it and grow it.*

### Chapter 11 — The European AI Corridor

**Core argument.** Serious European AI talent exists, and it clusters on
a corridor: London, Paris, Munich, Amsterdam, Zürich. The talent is not
the missing ingredient. The retention is.

**Key content.**

- DeepMind's London origin story and the structural fact that Google-
  owned does not equal Mountain View-controlled
- Mistral as the Paris gravitational centre
- ASML, Siemens, SAP as engineering-talent engines
- The UK's AISI as a credible institution and what it means for
  regulatory leadership
- Where Zürich (ETH), Amsterdam, and Munich fit
- Why the talent leaks to San Francisco — honest diagnosis, not
  hand-wringing
- The long-term competitive threat Europe is not yet pricing in: China's
  university pipeline and the sheer scale of new AI PhDs per year

### Chapter 12 — Retaining and Building

**Core argument.** Compensation reality, equity structures, visa policy,
and the mission-vs-ARR pitch. What European firms that are winning this
are actually doing.

**Key content.**

- Compensation reality — stop pretending you don't need to pay
  competitively; start pretending less
- Equity structures in Europe: the structural barriers and the firms
  that have worked around them
- The Blue Card and national equivalents — what works, what doesn't
- The mission pitch: "work on something that matters for your
  continent" is underpriced. Firms that have used it well.
- Public-private pipelines: defence-adjacent work, national lab
  partnerships, university-industry programs
- What your company does Monday morning to stop the leak

**Interview targets.** A European founder who has retained serious AI
talent against US offers. An HR leader at a national champion.

---

## Part VI — The Affirmative Vision

*~10,000 words. The book's constructive proposal and its synthesising
geopolitical argument. This is the part that gets the book cited, not just
sold.*

### Chapter 13 — The Linux of AI Models *(book's affirmative proposal)*

**Core argument.** Europe's strongest move is an open-weight,
transparently-trained, consortium-governed model ecosystem. Linux is the
analogy: it emerged when the industry was captured by proprietary Unix
vendors and a dominant platform player, it was built through distributed
contribution with clear governance, and it eventually became the
substrate for nearly all serious computing — including, ironically, the
cloud platforms now selling sovereignty theatre back to Europe.

**Key content.**

- The Linux analogy worked out in detail: governance, licensing,
  contribution, eventual ubiquity
- Why transparent training data and reproducible training matter for
  sovereignty in a way they don't for commercial products
- Honest pricing of the gap: compute capacity, talent density,
  coordination capability. This is a 5–10 year project, not a
  next-budget-cycle one.
- The coalition that could plausibly build it — **conceptual, not
  prescriptive**: ASML, SAP, Siemens, Mistral, national AI labs,
  defence primes, and whatever consortium structure evolves
- Why this is not Gaia-X — the specific failures of Gaia-X and how a
  model-layer consortium would need to be structured differently
- The UK's role as a de facto contributor

**Note on framing.** Stay conceptual with a nod to today's plausible
coalitions. Avoid naming a specific institutional vehicle (no "EuroStack
AI Foundation" etc.) — the landscape will shift and overspecificity
dates the book. But the *shape* of the coalition should be clear enough
that readers can recognise it forming.

**Interview targets.** Someone at Mistral, ASML, or a European AI lab
with views on the Linux-of-AI path.

### Chapter 14 — The Third Pole

**Core argument.** Europe as neither vassal to Washington nor client of
Beijing. What strategic autonomy looks like when executed across the full
stack — compute, models, data, talent, regulation. This is where the
book's threads finally converge.

**Key content.**

- The three-pole model world: US, China, Europe-plus-UK-plus-aligned
  democracies
- What "strategic autonomy" means operationally, not rhetorically
- NATO-adjacent defence AI as the honest home of Europe's hard-capability
  investment
- The UK's role: de facto member, closer to EU on AI governance than to
  US, defence-driven realignment
- Relationship with Canada, Australia, Japan, South Korea — the
  democratic-aligned periphery
- Where the "bastion for democracy" frame finally earns its place in
  the book, having been held back through the operational chapters

---

## Part VII — The Executive Playbook

*~11,000 words. The tactical close. Steelman the objection first; then the
diagnostic framework; then Monday morning.*

### Chapter 15 — The Steelman for Staying

**Core argument.** The honest case for "just keep using US
infrastructure" — fairly made, then dismantled. Engaging the strongest
version of the counter-argument is what makes everything else in the book
credible.

**Key content.**

- The strongest steelman: ecosystem maturity, integration cost, the
  political risk of being wrong, the operational risk of spreading thin
- When the steelman is actually right — specific company profiles where
  staying all-in on US infrastructure is the correct call
- Why it's wrong for most readers — the dependency stress tests from the
  earlier chapters now land with weight
- How to have this conversation with a board member or CEO who opens
  with the steelman

### Chapter 16 — The Four Postures in Practice

**Core argument.** There is no single right answer. There are four
postures — Full Sovereign, Hedged, Compliant Dependent, Exit — and the
executive's job is to diagnose which fits their company and execute it
deliberately.

**Key content.**

- **Full Sovereign:** rare, typically state-adjacent or defence-adjacent.
  Named companies as examples.
- **Hedged:** the realistic best-in-class posture for most serious
  European enterprises. Multi-jurisdiction, multi-provider,
  portfolio-managed.
- **Compliant Dependent:** accept the US stack, manage the risk, document
  the exposure. When this is honest and when it is denial.
- **Exit:** for businesses where AI is not core-differentiated, the
  honest answer may be to stay small and stay simple.
- Diagnostic framework: a short set of questions that map a reader's
  company to the right posture
- Named examples for each posture

**Interview targets.** A named executive for each of the four postures —
four interviews total. If you land these, this chapter becomes the book's
centre of gravity.

### Chapter 17 — Monday Morning

**Core argument.** What the reader does tomorrow morning. 12-, 24-, and
36-month roadmaps. Board conversations. Vendor negotiations.

**Key content.**

- The 12-month roadmap: audit, map dependencies, stress-test a scenario,
  identify the first workload to migrate
- The 24-month roadmap: the first migration completed, second pole
  (models or compute) established, procurement language updated
- The 36-month roadmap: multi-model, multi-jurisdiction architecture in
  production, sovereignty posture documented and board-approved
- Board conversations: the questions to put on the agenda
- Vendor negotiations using sovereignty as leverage — "we are prepared
  to move to [X]" is a real position now, and US vendors know it
- The Plan B frame restated as the book closes

---

## Epilogue — A Bastion for Democracy

**Core argument.** The operational case has been made. This short close
earns the democratic-values frame the book opened with. Why getting AI
sovereignty right matters beyond the balance sheet.

**Content.**

- Short (~2,000 words), values-forward
- Europe as the testing ground for whether democratic AI is possible
- The UK and the wider democratic periphery
- A direct line from technical architecture to political sovereignty to
  the world the reader's children will live in
- Closes on hope, not dread — the argument has been made; now it is
  time to act

---

## Through-lines (threads woven through multiple chapters)

### China

Not a dedicated chapter; present throughout. The bipolarity of the model
landscape (Ch. 3), Chinese open-weight models as hedge options (Ch. 8),
Taiwan as stress test (Ch. 6), the talent pipeline threat (Ch. 11), the
three-pole synthesis (Ch. 14). China is not the antagonist; the capture
of European capability by *either* pole is.

### Palantir

Not a dedicated chapter; woven through. Appears in Ch. 10 (defence and
health data sovereignty contradictions), Ch. 15 (steelman chapter — why
some governments choose it anyway), and Ch. 16 (as an example of
compliant-dependent posture taken to an uncomfortable extreme). The book
does not treat Palantir as simply bad — it treats it as the hardest
sovereignty question European governments have kept dodging.

### The UK

Treated as a de facto EU member for AI strategy purposes throughout.
London-Paris-Munich-Amsterdam-Zürich corridor framing (Ch. 11). AISI
credibility (Ch. 11, 14). Defence-driven realignment (Ch. 5, Ch. 14).
"The wounds will heal stronger than before" is the implicit editorial
stance; do not argue for it explicitly, just proceed as if it's true.

### The Plan B framing

Not a chapter; the spine of the book. Introduced in Ch. 1, restated at
the close of Ch. 17. Every strategic recommendation should cash out as:
*"we are not saying stop using X; we are saying have a Plan B that can
keep your lights on if X becomes unavailable or hostile."*

---

## Named companies and institutions

*Reference list. Every name below should appear at least once, most should
appear multiple times across different chapters. If a reader finishes the
book and can't recall where each showed up, the book was too abstract.*

**US hyperscalers and model providers**
Microsoft, OpenAI, Anthropic, Amazon/AWS, Google/DeepMind, Meta, Nvidia,
Palantir

**European infrastructure and industry**
Hetzner, OVH, Scaleway, Schwarz Group/StackIT, Deutsche Telekom/T-Systems,
Gaia-X, EuroStack, IPCEI-CIS, ASML, SAP, Siemens

**European AI/model providers**
Mistral, Aleph Alpha, Stability (UK), Wayve (UK), DeepMind (UK-origin),
ARM (UK), Cohere (Canada, honourable mention)

**Chinese model providers**
Qwen (Alibaba), DeepSeek, Kimi (Moonshot), GLM (Zhipu), Yi, SMIC
(foundry)

**Taiwan / semiconductor layer**
TSMC, Samsung Foundry, Intel Foundry

**Regulatory and governance**
CLOUD Act, EU AI Act, GDPR, Schrems II, AISI (UK), Project Glass Wing

---

## Interview strategy

**Lead time.** Start outreach now; C-level interviews are 4–8 week lead
times. A shared tracking doc (target / outlet / warm intro path / status /
date locked) is worth setting up before writing begins.

**Priority targets by chapter.**

- **Ch. 4 (Hyperscale Myth):** a CTO who has moved serious workload off a
  hyperscaler; a Hetzner/OVH/Scaleway executive on the mid-market story;
  a CFO who has done the TCO analysis
- **Ch. 7 (Enterprise Good Enough):** a head of AI at a mid-cap running
  production workload on Mistral or open-weight models
- **Ch. 13 (Linux of AI):** someone at Mistral, ASML, or a European
  national AI lab with a view on the consortium path
- **Ch. 16 (Four Postures):** one named executive per posture. Four
  interviews. These land → this chapter becomes the book's centre of
  gravity.

**Secondary targets.** General counsel or CISO for Ch. 9. A European HR
leader at a national champion for Ch. 12. A defence or intelligence
figure (on background if necessary) for Ch. 6.

**Publishing strategy integration.** Interviews are a networking strategy
as much as a research strategy. Every interview is a future reviewer,
reader, and distribution node.

---

## Things to avoid

- **Assuming the reader agrees on the post-rules-based-order thesis in
  paragraph one.** Earn it with evidence in Ch. 1.
- **Sounding anti-American.** The book is pro-continuity, pro-negotiating
  position, pro-optionality. Not a screed.
- **Treating frontier-model benchmarks as the job description.** Most
  enterprise workloads don't need them. Be honest about where they do.
- **Overclaiming Mistral's capabilities.** Honesty about the gap builds
  credibility for the larger claim.
- **Dismissing hyperscaler sovereign cloud offerings without scrutiny.**
  Engage them seriously; then show why they fall short.
- **Ideological language in the operational middle chapters.** Values
  language belongs in Ch. 1 and the epilogue, not throughout.
- **Anchoring to current news specifics that will date quickly.** Tariff
  numbers, who divested this quarter, the specific name of this year's
  executive order — these are illustrative evidence for durable arguments
  about dependencies. Write the durable argument; use the news as
  illustration.
- **Proposing specific institutional vehicles for the Linux of AI.**
  Stay conceptual. Name the coalition shape, not the logo.
- **Walking through an article or report point-by-point.** Synthesise.
  Cite. Move on.

---

## Writing order

**Write Ch. 4 first.** The Hyperscale Myth is the signature chapter. If
you can land it against your own best steelman, the rest of the book's
arguments hold up. If it wobbles, adjust the thesis before committing to
the full structure.

**Then Ch. 7 (Enterprise Good Enough).** Same logic — second-most-load-
bearing contrarian argument. If this lands alongside Ch. 4, the book has
a spine.

**Then Ch. 1.** Not first. Opening chapters get rewritten three times
anyway, and you will write a better Ch. 1 knowing how Ch. 4 and Ch. 7
actually landed.

**Then Ch. 13 (Linux of AI).** The affirmative vision. Worth writing
early because it's the book's constructive core and shapes how the
preceding chapters need to set it up.

**Then the rest, roughly in order,** with Ch. 15 (steelman) and Ch. 16
(four postures) benefiting from having the interviews in hand.

**Epilogue last.** It should feel like the book earned it.

---

## Research-to-writing ratio by chapter

**Argument-heavy (write from your own head first, research to verify):**
Ch. 1, Ch. 2, Ch. 14, Epilogue

**Evidence-heavy (research before writing):**
Ch. 4 (TCO numbers), Ch. 6 (Taiwan analysis), Ch. 7 (workload benchmarks),
Ch. 9 (legal texts and cases), Ch. 11 (talent data)

**Interview-heavy (land the interviews before writing):**
Ch. 4, Ch. 7, Ch. 13, Ch. 16

Batch research for the evidence-heavy chapters together, before writing,
rather than serially.

---

## Repo and tooling notes

- Book structure lives in `structure.yaml` at the repo root. To reorder
  or rename, edit that file and the corresponding chapter file.
- Each chapter file lives at
  `content/parts/part-N-slug/NN-chapter-slug.md` with H1 heading
  `# Chapter N: Title`.
- Epilogue at `content/epilogue.md`.
- References collected in `content/back-matter/references-sources.md`
  under matching H2 chapter headings.
- Build with `python3 scripts/build-epub.py` and
  `python3 scripts/build-pdf.py --variant both`.
- Part title pages render automatically — no manual page-break
  management needed.

---

*End of outline. Prompt future sessions with this file as context, plus
the specific chapter you are working on.*
