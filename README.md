# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-30 03:56 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-29 · ✍️ Hengyi Xie, Chenfei Yao, Xianjin Wu +7 more

Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27205v1)

---

### 2. Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-29 · ✍️ Perry Dong, Ron Polonsky, Dorsa Sadigh +1 more

Pre-training followed by fine-tuning has become the dominant recipe for learning performant policies, and in value-based reinforcement learning (RL) this raises a natural question: given a pretrained policy, should the Q-function be pretrained on offline data too? Conventional wisdom suggests it should, but recent results show that online RL with a randomly-initialized Q-function can result in hig...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27203v1)

---

### 3. Mental World Modeling

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-29 · ✍️ Hao Fei, Yiran Zhao

World models enable a predictive substrate for planning and action, yet existing formulations merely answer a physical question: what/where it is, and how will it evolve. Human behavior, however, is driven by hidden mental state (what a person believes, wants, intends, feels, and considers socially permissible), so a model that tracks the physical scene but not what each agent knows and believes a...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27201v1)

---

### 4. From Classification to Regression: Using a Fruitfly to Solve Equations

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-29 · ✍️ Shady E. Ahmed, Panos Stinis

We present a novel approach to regression tasks using classification which is motivated by the mechanism used by fruitflies to sense their environment. Specifically, we formulate a general framework for learning nonlinear input-output relationships by replacing complex global surrogate models with a finite library of representative local patterns. Since scientific data often occupy limited and rec...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27196v1)

---

### 5. VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-29 · ✍️ Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys

Accurately recovering the camera's calibration and metric poses for any unconstrained video would unlock large-scale training data for navigation and scene understanding. The dominant approaches to this problem are severely limited: Simultaneous Localization and Mapping (SLAM) is sensitive to initialization and transient failures due to its causal, incremental nature; it is often over-optimized fo...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27194v1)

---

### 6. Can AI agents conduct open-ended AI research? Early evidence from two case studies

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-29 · ✍️ Peter Kirgis, Sayash Kapoor, Andrew Schwartz +21 more

Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27191v1)

---

### 7. APEX-Accounting

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-29 · ✍️ Julien Benchek, Austin Bennett, Jasmin Kern +8 more

We introduce APEX-Accounting, a benchmark built by Mercor in partnership with Ramp, to assess whether frontier models can do the real work of accountants. Tasks include reconciling accounts, accruing expenses, posting transactions, and producing reports. The private eval set comprises 160 tasks, split across 10 worlds. Each world contains an accounting system, as well as spreadsheets, PDFs, and ot...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27189v1)

---

### 8. Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-29 · ✍️ Lennon J. Shikhman, Michael Galarnyk, Aadi Dash +1 more

Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary benchmarks. A controlled benchmark exposes simulator-truth densities for latent evaluation, while a chronological NIFTY benchmark tests only held-out market prices. A two-component lognormal mixture has the lowest aggregate price, $L^1$, Wasserstein, and fixed-...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27188v1)

---

### 9. Pangram 4 Technical Report

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-29 · ✍️ Ben Glickenhaus, Katherine Thai, Jenna Russell +4 more

We present Pangram 4, the latest deep-learning-based AI-text classification model from Pangram Labs. We achieve an AUROC of 0.9916 with a false positive rate of 0.0041% and a false negative rate of 0.3396%. In addition to its increased overall accuracy compared with Pangram 3, Pangram 4 exhibits superior out-of-distribution generalization and robustness to adversarial attacks. Another novel contri...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27183v1)

---

### 10. HumanCLAW: Can Vision-Language Models Act Through a Body?

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-29 · ✍️ Siyao Li, Jiawei Gu, Shuai Liu +15 more

Evaluating whether a vision-language model (VLM) can act through a physical body is challenging. The outcome of an action couples the VLM's decision with motor control. When a task fails, it is hard to tell whether the VLM made a bad choice or the motor controller simply failed to execute it, e.g., losing balance and falling. In this work, we introduce HumanCLAW, an evaluation framework that decou...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27180v1)

---

### 11. The Social Cost of an AI Teammate: How an Artificial Teammate Reshapes Human-Human Communication in Small-Team Decision-Making

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-29 · ✍️ Nia Nixon, Jaeyoon Choi, Pedro Martins De Bastos +4 more

Conversational AI is increasingly positioned as a teammate rather than a tool, yet we know little about how its presence reshapes communication among the humans on the team. We examined sociocognitive communication dynamics in team decision-making using Group Communication Analysis (GCA), team surveys, and lexical analyses of team discourse. Teams completed a high-stakes moral-dilemma decision tas...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27179v1)

---

### 12. DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-29 · ✍️ Raphaël Sourty, Antoine Chaffin, Paulo Roberto Moura Junior +1 more

State-of-the-art retrieval models increasingly rely on closed training data, creating a reproducibility gap. We present an open end-to-end recipe for training retrieval models and study how English supervision transfers to multilingual retrieval through translate-train. We first reconstruct and curate 665M English contrastive pre-training pairs from 1.4B pairs across 34 public sources and build 1....

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27178v1)

---

### 13. Partner Capability Estimation for Task-Agnostic Adaptation in Ad-Hoc Teamwork

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-29 · ✍️ Peter Tisnikar, Maja Swieczkowska, Benteng Ma +2 more

Effective collaboration with novel and diverse partners is a crucial skill for autonomous agents. Most current ad-hoc teamwork (AHT) approaches assume that agents will collaborate on a single, fixed task and that the partner's capabilities, their ability to successfully execute the desired action, are already known. In reality, a partner's true capabilities are often hidden, and human collaborator...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27177v1)

---

### 14. Improving Item Discoverability in e-Commerce Search via Related Intent Generation

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-29 · ✍️ Ji Xin, Xiao Xiao, Ishan Bhatt +6 more

Traditional search systems are optimized to retrieve items that strictly match a query, often prioritizing precision over recall. In e-commerce marketplaces and particularly grocery, this paradigm is limiting, as user satisfaction and commercial outcomes depend heavily on the discoverability of substitute, complementary, and thematically related items. In this paper, we present a scalable system f...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27172v1)

---

### 15. When Do Learned Diffusion Proposals Help Constraint Solving? A Controlled Study on Continuous Algebraic Systems

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-29 · ✍️ Quang Bui, Sparsh Roy, Akash Gundimeda +1 more

Solving a continuous algebraic constraint system requires two decisions: which values satisfy the constraints, and which structural augmentation renders an unsolvable system solvable. Classical solvers answer the first well and the second only by enumeration. On that discrete decision, a candidate-conditioned repair ranker choosing among K augmentations reaches the exhaustive-search ceiling at a f...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.27169v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
