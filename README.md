# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-08-29 07:40 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-27 · ✍️ Tianjie Ju, Zheng Wu, Yueqing Sun +15 more

Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a phys...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27456v1)

---

### 2. CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Yufan Wu, Yinghui He, Zhengyi Hu +4 more

Recent advances in inference-time scaling have significantly improved the reasoning performance of large language models (LLMs). However, these methods typically rely on repeated generation or external verification. To address this limitation, we introduce CritICL, a novel inference-time framework that improves reasoning while maintaining high efficiency. Our key insight is that LLM failure modes ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27455v1)

---

### 3. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng +3 more

Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27454v1)

---

### 4. SWE-Prime: Fewer Trajectories, Better Performance

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Dewu Zheng, Ruizhe Ye, Yanlin Wang +7 more

To improve large language models' ability to resolve real-world software issues, prior work has focused on constructing large-scale agent trajectory datasets and performing supervised fine-tuning (SFT) on successful trajectories. However, task success does not guarantee high-quality supervision: successful trajectories may still contain ineffective, redundant, or risky steps. Directly using such t...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27449v1)

---

### 5. TTPO: Test-Time Policy Optimization

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Aozhe Wang, Zhengxi Lu, Jianze Wang +8 more

Recent prominent post-training methods, such as Reinforcement Learning (RL) and On-Policy Self-Distillation (OPSD), have driven rapid progress in mathematical reasoning for large language models, yet their reliance on ground-truth labels precludes test-time training (TTT). Replacing ground truth with majority-vote pseudo-labels is a natural alternative, yet it is fragile: an incorrect vote corrupt...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27448v1)

---

### 6. From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Dewu Zheng, Yanlin Wang, Xiwen Wang +5 more

In real-world software development, code review typically involves iterative interactions between developers and reviewers to improve software quality, making the process costly and time-consuming. Although recent work explores large language models (LLMs) for automated code review, most approaches oversimplify code review into a single-round, static decision task, which fails to capture the multi...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27442v1)

---

### 7. RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-27 · ✍️ Junjie Zhang, Hui Liu, Kecheng Chen +3 more

LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-bas...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27439v1)

---

### 8. Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-27 · ✍️ Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong +1 more

Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.   We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), w...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27429v1)

---

### 9. Stochastic Estimation of Transduced Language Models

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Vésteinn Snæbjarnarson, Samuel Kiegeland, Manuel de Prada Corral +2 more

Transduced language models (TLMs) compose a pretrained \emph{source} language model with a functional finite-state transducer to induce a language model over \emph{target} strings. Computing the probability of a target prefix under a TLM amounts to summing the source-model probabilities of all source strings that the transducer maps to target strings beginning with that prefix. This set can be exp...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27428v1)

---

### 10. Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-27 · ✍️ Yisen Xi

Large language model (LLM) agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely, while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply. We present Persona-Execution Separation (PES): persona and execution reside in different trust domains, connected by a governed contract bridge. The pe...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27427v1)

---

### 11. Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-27 · ✍️ Qianlong Lan, Vinothini Pandurangan, Anuj Kaul +1 more

Static scanners are increasingly used to identify executable or otherwise unsafe content in machine- learning artifacts, yet conventional evaluation metrics characterize only cases where a scanner yields a usable security judgment. We evaluate ModelScan, ModelAudit, and Fickling using a controlled, artifact-backed benchmark on a synthetic corpus of 170 Pickle and PyTorch focused artifacts across 1...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27424v1)

---

### 12. Learning a Continuous Sepsis Severity Score Without Hour-by-Hour Supervision: A Two-Site Retrospective Study

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-27 · ✍️ Kevin Zhu, Ryan Zhang, Baraa Abed +18 more

Currently used sepsis severity indices rely on fixed variables and weights established decades ago, which are coarsely discretized and calibrated to a cohort that no longer reflects contemporary critical care. No alternative learned directly from patient trajectories is in routine use. We conducted a retrospective two-cohort study on a total of 29,116 and 7,691 adult patients meeting Sepsis-3 crit...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27421v1)

---

### 13. Boosting LLM Exploration via Weak-Model Guidance in RLVR

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-27 · ✍️ Xingyu Shen, Huishuai Zhang, Peng Li +2 more

Reinforcement Learning with Verifiable Rewards (RLVR) significantly improves LLM reasoning but often causes a drop in policy entropy, leading to narrowed reasoning coverage and degraded pass@$k$ for large $k$. While existing methods mitigate this entropy collapse through algorithmic regularizations, cross-model non-parametric perturbation is also neglected. In this work, we propose a simple yet ef...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27420v1)

---

### 14. Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-27 · ✍️ Chanho Park, Daehyeon Choi, Jihyun Lee +1 more

Vision-language models (VLMs) can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism behind this behavior is not understood. Inspired by retrieval heads in large language models, we ask whether VLMs contain an analogous mechanism for visual retrieval. We answer affirmatively by introducing Visual Retrieval Heads...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27417v1)

---

### 15. Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings and Temporal Neighbor Sampling

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-27 · ✍️ Maksim Utushkin, Andrei Ovsiannikov, Alexander D'yakonov

Friend recommendation is inherently graph-structured: the relevance of a potential connection depends on multi-hop social context rather than user attributes alone. However, deploying message-passing GNNs on a production-scale social graph with hundreds of millions of users and tens of billions of edges requires addressing numerous modeling and systems challenges. We present a scalable end-to-end ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.27413v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
