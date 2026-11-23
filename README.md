# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-23 08:36 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Optimal Linear Regression Without a Variance

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-20 · ✍️ Artin Tajdini, Jasper C. H. Lee, Jonathan Scarlett +1 more

We study high-probability linear regression in the infinite variance regime, wherecthe regression noise has only a finite conditional $α$-moment $ν$ for some unknown $α\in(1,2)$, and the covariates may only have finite moments up to a given order (e.g., 4th moment). We give a black-box reduction that converts finite-variance regression procedures into weak-moment procedures. The reduction is based...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27983v1)

---

### 2. A Methodologically Rigorous Benchmark of Linear Regression,RNN, and LSTM for S&P 500 Forecasting:Identifying Sources of Performance Inflation in Financial DeepLearning

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-20 · ✍️ Hari Sitaula, Joseph Opitz

This study examines one-day-ahead forecasting of the S&P 500 closing level using a 2006-2025 dataset that includes fundamental price data, macroeconomic indicators, and engineered technical features. We benchmark three model families, namely linear regression, vanilla recurrent neural networks (RNN), and long short-term memory networks (LSTM), within a unified preprocessing and chronological evalu...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27978v1)

---

### 3. MemOnce: A Scalable Memory Architecture for Large Language Models

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-20 · ✍️ Chang Nie, Chaoyou Fu, Songlin Liu +2 more

Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures c...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27973v1)

---

### 4. On the Complete Feature Set for ADHD Classification in Children and Adolescents Based on EEG Signals

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-20 · ✍️ Javier Sanchis, Álvaro Navarro, Jorge García-Carrasco +2 more

Attention-deficit/hyperactivity disorder is a neurodevelopmental condition that can affect attention, activity and impulse control. Electroencephalography (EEG) records brain activity as children and adolescents perform cognitive tasks. However, comparing features derived from these recordings requires consistent signal preparation, shared analysis windows and documented quality decisions. We cura...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27970v1)

---

### 5. Non-penetrating World Models

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-20 · ✍️ Yuhang Dai, Yinwei Wu, Ziyue Lin +2 more

We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information n...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27963v1)

---

### 6. Model Carving: Training Transformers That Optimize Their Own Topology

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-20 · ✍️ Kaden Zheng, Pratyusha Sharma

Machine learning has largely kept separate the choice of architecture and the process of training. A classic Transformer, for instance, trains a fixed set of attention and MLP sublayers at every layer, in the same order, and optimizes the weights within. This uniformity is a convention rather than a principled design choice, and it is likely suboptimal: the best architecture for a given task may b...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27962v1)

---

### 7. Ranking-Preserving Coreset Selection for Efficient Evolutionary Hyperparameter Optimization

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-20 · ✍️ Mamoona Tasadduq, Maryam Bashir

Hyperparameter optimization (HPO) is essential for high predictive performance, but its computational cost becomes prohibitive when candidate configurations require repeated training on large datasets. This paper proposes a ranking-preserving coreset (RPC) selection framework for accelerating evolutionary HPO. The method constructs a compact coreset that preserves the relative ranking of hyperpara...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27959v1)

---

### 8. Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash Speed

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-20 · ✍️ Dylan Forde

Long-context models use sparse or structured attention to avoid quadratic cost, yet retrieving a small set of relevant facts embedded among hundreds of thousands of distractors degrades as normalization mass disperses with length. Hub-and-spoke optimal transport (OT) replaces the dense $L \times L$ matrix with a linear-size graph over local windows and $K$ shared hubs balanced by Sinkhorn scaling....

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27951v1)

---

### 9. The Optimal Sample Complexity of Agnostic PAC Learning for Partial Concept Classes

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-20 · ✍️ Liang-Yu Zou

Let $\mathcal H\subseteq\{-1,+1,\star\}^{\mathcal X}$ be a partial concept class of finite VC dimension $d$. We construct a deterministic agnostic PAC learner that, for every $\varepsilon,δ\in(0,1)$, uses $O((d+\log(1/δ))/\varepsilon^2)$ i.i.d. examples from an arbitrary distribution $\mathcal D$ over $\mathcal X\times\{-1,+1\}$ and returns a total concept $\hat h:\mathcal X\to\{-1,+1\}$ satisfyin...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27946v1)

---

### 10. DiTraR: Diverse Scorers and Transcript-Guided Re-ranking for Video Corpus Moment Retrieval

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-20 · ✍️ Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Ali Amini

Video corpus moment retrieval asks a system to find, in a large collection of untrimmed videos with subtitles, the video and the time interval that a natural-language query describes. We find that most top-ranked errors of a strong corpus-level scorer come from choosing the wrong video, not from imprecise boundaries, and that re-weighting the evidence the scorer already uses does not fix them. We ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27931v1)

---

### 11. BioEmu2: Scalable Emulation of Biomolecular Dynamics

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-20 · ✍️ Michael Gastegger, Adam E. Foster, José Jiménez-Luna +27 more

Despite major advances in structure prediction, modelling the motions and interactions that drive biomolecular function at scale remains a central challenge. We introduce BioEmu2, a generative model for atomically resolved biomolecular structures combining static structure prediction, equilibrium sampling and time evolution, that samples orders of magnitude faster than molecular dynamics (MD). Tra...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27924v1)

---

### 12. ESSI: Computationally Efficient Semantic Search for Sparse Autoencoder Concepts

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-20 · ✍️ James Baker

Sparse autoencoders (SAEs) decompose diffusion model activations into interpretable features, but steering a model with them requires identifying which features map to a given semantic concept, if any. Existing methods for this concept to feature task are expensive, relying on grid searches or repeated passes through the frozen UNet. We propose Efficient Semantic Sparse Identification (ESSI). Usin...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27921v1)

---

### 13. SUAF: Spectral Universal Advantage Features for Zero-Shot Policy Improvement

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-20 · ✍️ Huaze Tang, Runqing Miao, Tianren Peng +4 more

Reward-independent representations enable reinforcement learning agents to reuse knowledge across tasks, but limited representation capacity raises three fundamental questions: what statistical dependence should these representations capture, which components of that dependence should be retained for policy improvement, and how does discarding the remaining components affect decision-making? We ad...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27919v1)

---

### 14. Augmentation of cardiovascular flow measurements with generative diffusion models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-20 · ✍️ Fabio Guglietta, Tianyi Li, Francesco Viola +1 more

Cardiovascular imaging offers several ways to measure blood flow, but each provides an incomplete, resolution-limited, or noisy view of the underlying dynamics. Reconstructing the missing information is inherently ambiguous because several flow fields may be compatible with the same observation. Here, we investigate generative diffusion models as tools for cardiovascular-flow generation and recons...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27917v1)

---

### 15. StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-20 · ✍️ Chi Yan, Guoyang Zhao, Wentao Yuan +3 more

Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints. This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial pr...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.27915v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
