# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-02 04:57 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Measuring the Gap Between Human and LLM Research Ideas

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-01 · ✍️ Ziyu Chen, Yilun Zhao, Arman Cohan

LLMs are increasingly used to brainstorm research ideas, but existing evaluations mostly judge individual ideas by novelty, feasibility, or expert preference. We instead ask: how far are current LLM-generated ideas from human researchers? To characterize this gap, we build a large-scale evaluation framework for ideation from high-quality human research papers. For each paper, we reverse-engineer a...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01233v1)

---

### 2. Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-01 · ✍️ Zijian Zhang, Rizhen Hu, Athanasios Glentis +4 more

Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge t...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01232v1)

---

### 3. Language-Critique Imitation Learning from Suboptimal Demonstrations

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-01 · ✍️ Chih-Han Yang, Dai-Jie Wu, Yun-Ping Huang +3 more

Prior work on imitation learning from suboptimal demonstrations typically relies on compressed supervision signals such as confidence estimates, discriminator scores, or importance weights. These scalar signals are inherently limited, as they cannot explicitly express intermediate reasoning about task progress, failure modes, or corrective actions. We propose a language-critique framework for imit...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01225v1)

---

### 4. AutoMem: Automated Learning of Memory as a Cognitive Skill

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-01 · ✍️ Shengguang Wu, Hao Zhu, Yuhui Zhang +2 more

Memory expertise is a learned skill: knowing what to encode, when to retrieve, and how to organize knowledge--a capacity known in cognitive science as metamemory. We bring this perspective to LLMs by treating memory management as a trainable skill. We promote file-system operations to first-class memory actions alongside task actions, letting the model itself decide how to manage its memory. This ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01224v1)

---

### 5. Theoria: Rewrite-Acceptability Verification over Informal Reasoning States

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-01 · ✍️ Ben Slivinski, Michael Saldivar

When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01223v1)

---

### 6. Ink3D: Sculpting 3D Assets with Extremely Complex Textures via Video Generative Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-01 · ✍️ Yue Han, Chong Li, Zhening Liu +5 more

Recent 3D generative models can synthesize high-quality geometry but often struggle to reproduce intricate textures from reference images, largely due to the scarcity of large-scale 3D training data with rich surface appearance. In contrast, visual generative models are trained on datasets several orders of magnitude larger and excel at modeling complex visual patterns. Motivated by this gap, we i...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01222v1)

---

### 7. The State-Prediction Separation Hypothesis

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-01 · ✍️ Giovanni Monea, Nathan Godey, Kianté Brantley +1 more

Transformers use the same forward computation stream to both predict the next token and store useful state for future token predictions. We formulate the \emph{state-prediction separation hypothesis}: disentangling the two roles yields better language modeling performance. We design a Transformer variant that uses two computation streams to separate the two functions, and conduct pretraining exper...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01218v1)

---

### 8. FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-01 · ✍️ Chenyang Ma, Yue Yang, Radu Corcodel +4 more

Current work on robot furniture assembly mostly focuses on toy-scale settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for expert data generation and evaluation, and build a VR teleoperation system for single-op...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01212v1)

---

### 9. Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-01 · ✍️ Zhi Chen, Zhensu Sun, Yuling Shi +2 more

Repository-level performance-optimization benchmarks such as GSO, SWE-Perf and SWE-fficiency evaluate coding agents by applying patches to real repositories and comparing runtime against unoptimized baselines and official reference patches. Their leaderboard scores are increasingly used as evidence of coding-agent progress, but those scores can conflate runtime instability, benchmark-specific scor...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01211v1)

---

### 10. Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-01 · ✍️ Shayan Talaei, Abhinav Chinta, Devvrit Khatri +3 more

Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work ha...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01208v1)

---

### 11. Linkify: Learning from Interface-Augmented Assembly Graphs

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-01 · ✍️ Anushrut Jignasu, Daniele Grandi

We present Linkify, a framework for learning from interface-augmented assembly graphs to enable context-aware part retrieval in mechanical assemblies. While recent generative AI methods for CAD have focused largely on isolated parts or monolithic assemblies, the rich geometric information at the interfaces between parts, where function is realized, remains underexplored. We address this gap by rec...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01205v1)

---

### 12. TiRex-2: Generalizing TiRex to Multivariate Data and Streaming

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-01 · ✍️ Patrick Podest, Marco Pichler, Elias Bürger +7 more

We introduce TiRex-2, a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates. Real-world forecasting is inherently sequential: observations arrive continuously, variables evolve jointly, and a subset of covariates is known ahead of time. Existing Transformer-based time series foundation models capt...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01204v1)

---

### 13. GPU-Parallel Linearization Error Bounds for Real-Time Robust Optimal Control of Nonlinear and Neural Network Dynamics

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-01 · ✍️ Jeffrey Fang, Keyi Shen, Anutam Srinivasan +1 more

This paper studies real-time robust optimal control for uncertain nonlinear systems, where linear time-varying (LTV) approximations make planning tractable but require sound linearization error bounds (LEBs) to guarantee robust constraint satisfaction. We develop tight, differentiable, GPU-parallel LEBs for LTV approximations of nonlinear and neural network (NN) dynamics. For analytic dynamics, we...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01203v1)

---

### 14. World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-01 · ✍️ Liyuan Zhu, Shengyu Huang, Amrita Mazumdar +6 more

We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01202v1)

---

### 15. Quantum vs. Classical Machine Learning: A Unified Empirical Comparison

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-01 · ✍️ Chuanming Yu, Jiaming Liu, Zihao Ge +4 more

Quantum computing has emerged as a promising computational paradigm for machine learning (ML), with the potential to offer computational advantages over classical approaches. At this stage, the evidence supporting the performance and advantages of quantum machine learning (QML) models relative to classical models is insufficient.To address this gap, this paper presents an empirical study on the pe...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.01197v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
