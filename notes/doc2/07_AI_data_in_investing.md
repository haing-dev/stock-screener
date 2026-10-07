## AI & data in investing

Practitioners agree that AI is a powerful research accelerator and a way to encode an investor's judgment into repeatable workflows. Few believe it can independently find durable alpha: market data is scarce and unstable, the valuable signals sit in outliers where AI is least reliable, and judgment and execution stay human.

| Where AI clearly helps | Where it struggles |
| --- | --- |
| Data gathering (\~100% automatable) and processing (\~80%) (Ying) | Final judgment and asking the right question (\~0% automatable) (Ying) |
| Earnings previews and multi-step workflows: \~35M tokens replace \~1,000 hours, coverage 20 → 60–70 names (Akash) | Discovering stable alpha: \~2 seasonal data points a year, and anything stable gets arbitraged instantly (Gebhardt) |
| Risk management and portfolio optimization with explainable models (Chan) | Predicting returns directly from scarce, regime-shifting data (Chan) |
| Diffing 10-K risk factors and generating meeting questions (Pilecki) | Market-rule nuances: LLMs hallucinate and can be argued into agreeing with you (Paddock) |
| Scaling expert calls by generating the next good question (Matei) | Outliers, the exact moment you need reliable data (Matei) |
| Research plans and code in minutes (Gebhardt, Carver) | Code correctness (\~50% of chatbot answers wrong in Chan's experience) |
| Adding news context to simple causal models (Chan) | Generic LLMs lack domain context; BloombergGPT lost to a smaller generic model (Ying) |

### 1. Finance is a small-data problem

- Structural breaks leave maybe 20 usable years, against millennia of text for LLMs (Chan).
- Seasonal energy offers \~30–45 data points in 15 years. Language is stable, markets aren't. ML is "fancy regression" that can't extrapolate (Gebhardt).
- GenAI's real promise is pre-training on loosely related data and semi-supervised learning: hand-label a few Fed transcripts instead of buying vendor sentiment scores (Chan).

### 2. Alpha lives in outliers, where AI is least trustworthy

- You make money only when you're right and others are wrong, which happens at outliers. Outliers are also where data errors and hallucinations cluster (Matei).
- LLM memory can create a personal echo chamber that feeds you stories matching your playbook, the same way founders get surrounded by yes-men (Matei).
- "If you cannot put a number on it, you don't have a differentiated opinion" (Dan Loeb, via Akash). Analysts want facts with confidence intervals, not forecasts.

### 3. The real shift: encoding judgment into agents

- Tooling went from search to RAG (2024), then knowledge graphs, then agentic harnesses (2025). Model upgrades took accuracy from \~70% to \~90%. "Work's not going away; your judgment is being encoded" (Akash).
- PMs who want analysts to follow their process exactly find agents attractive for the same reason (Matei).
- Frontier models may beat the S&P risk-adjusted, but only inside well-engineered harnesses (ex-IMC trader).
- The path forward is ticker-level knowledge graphs, derived knowledge such as management-credibility scores, then reinforcement learning on market outcomes (Ying). Reinforcement learning is also being applied to turn fair values into trades (Lebron).

### 4. Edge still requires humans, and execution

- AI shortens the trial-and-error loop, but executing rules through losing streaks is a profession most people can't master (Yokokawa).
- The winning setup is human judgment on a robust system, like AI-augmented chess players (Gebhardt).
- Demand for investing talent *grows*: AI is a quant wave for words that collapses pattern-matchable alpha and raises payoffs for differentiated views (Ying).
- Curious investors find AI "a dream come true"; lazy ones who stop at the first answer fall behind (Matei).
- AI "is not going to change the research landscape." A 10-K that took weeks by post now takes seconds, but "just because the data is available doesn't mean the people know how to interpret it" (Stahl, Mar 2026).

### 5. What it does to markets

- Context becomes currency: as everyone runs the same models, edge shifts to proprietary data and context. Markets may become *noisier* because everyone processes faster but judges differently (Cedar).
- AI will make markets more efficient overall and shrink the gaps between large and small funds, but it creates new inefficiencies around AI-driven flows (Ying).
- LLMs will eventually let quants capture social-arbitrage signals, eroding retail's edge (Tom). Barriers to launching a fund fall: expect \~10x more hedge funds (Cedar) and more solo "AI hedge funds" (Yokokawa).

### 6. How firms are adopting AI

- **Bridgewater** has done machine learning since 2012, began building an "artificial investor" in 2022, and has run an AI-first fund generating alpha since 2024. Lesson: redesign processes around the technology instead of making it imitate humans (Jensen).
- **Temasek** trains associates to work "two levels above" because AI handles the base work (Pillay).
- **Quantedge** keeps generative AI out of production models because outputs are inconsistent, but uses it for research, data cleaning and execution.
- Fundamental PMs should redesign their process from scratch and keep someone who knows Python to audit convincingly wrong AI output (Ying).
- On the corporate side, Hoffman says record every meeting and let AI draft follow-ups. Bloisi had every executive learn to code in a 4-hour course.

### 7. NLP and alternative-data craft

- Dictionary sentiment is dead. Train a classifier per document type: a reporter praising a company is positive, a CEO saying the same about their own company isn't (Kantos).
- Match data to horizon: news alpha decays in days, while earnings-call forward-looking statements drift for \~1.5 months (Kantos). Train text models directly on risk-adjusted returns, over years not quarters, to avoid fads (Jha).
- Creative data wins: highway-patrol accident data for insurers, celebrity tweets mapping wildfire damage (Ying), hailstorm searches ahead of a roofing distributor's results (Camillo).
- Data infrastructure comes first: point-in-time storage and keeping copies of vendor data to catch revisions (Akash, Jha).
- Real-time KPIs from card data, web scraping and parking-lot images are now "table stakes". Use cohorts to test a multi-year thesis: Eminence compares Dave & Buster's 10 remodelled stores with the rest of its \~200 (Sandler).
