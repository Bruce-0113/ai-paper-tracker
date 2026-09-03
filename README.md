# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-09-03 05:29 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. A Common Measure of Communication for Speech Brain-Computer Interfaces

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones

Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natural human-computer interaction. Despite this promise, the field lacks a common measure of progress because systems use different datasets, recording methods, types of speech, and vocabularies, so thei...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02887v1)

---

### 2. SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-02 · ✍️ Junchao Huang, Guian Fang, Shengju Qian +15 more

We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive d...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02886v1)

---

### 3. Discriminative World Models for Web Agents

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ Kelvin Li, Dhruv Pendharkar, Anish Pahilajani +6 more

Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PRM). These world models are typically trained via supervised next-state prediction to generate fixed representations like HTML or AXTree snapshots. However, this objective is misaligned with the downst...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02885v1)

---

### 4. Graph Machine: Towards Better Pretraining via Edges

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ Lintai Hou

We introduce the Graph Machine (GM), an architecture that maintains an $O(n)$-sized state and accesses it through sparse, dynamic routing. Unlike methods with fixed-size states or sparse but static routing, GM preserves $O(n)$ complexity in its sparse layers without restricting the potentially accessible state size to $O(1)$. Instead, GM uses edges - pointer-like objects updated differentiably by ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02881v1)

---

### 5. GRADSOLVE: fast exact gradients for ODE ensembles on GPUs

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ Alessio Spurio Mancini

Ordinary differential equations (ODEs) underlie models in science and engineering, and many applications need derivatives of their solutions with respect to parameters. Ensembles of independent trajectories suit graphics processing units (GPUs), but current GPU software forces a trade-off: the fastest ensemble solvers cannot be differentiated in reverse mode at the speed they solve, and the solver...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02876v1)

---

### 6. Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-02 · ✍️ Yutong Liu, Nan Huang, Xu Cao +1 more

Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from vis...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02864v1)

---

### 7. Towards Trustworthy Autonomous Robots: An Explainable AI-Based Decision Framework

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-02 · ✍️ Cagri Temel

Autonomous robots powered by deep learning face a fundamental auditability challenge: when incidents occur, investigators cannot reconstruct why the system made specific decisions. This paper presents TRACE (Transparent Reasoning Architecture for Credible Execution), a decision framework that ensures every autonomous action can be traced back to sensor evidence through documented causal chains. Th...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02861v1)

---

### 8. PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-02 · ✍️ Yu Tian, Xintong Jiang, Jan Franklin Adamowski +2 more

Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches rely heavily on densely annotated datasets that are labor-intensive to acquire. Unified PPCS adaptation from distribution-shifted examples with minimal additional training remains challenging. To addr...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02860v1)

---

### 9. User Feedback Provides a Unique Signal that LLMs Can not Detect

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-02 · ✍️ Shachar Don-Yehiya, Leshem Choshen, Omri Abend

Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy and difficult to leverage effectively. We challenge this conception by demonstrating that user feedback is a highly actionable signal for improvement, and that its perceived ineffectiveness stems from a...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02859v1)

---

### 10. Improved Gradient Descent Lower Bounds Beyond Nesterov

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ Yuhan Ye, Kaizhao Liu

We study how far gradient descent (GD) can be accelerated by predetermined stepsizes in smooth convex optimization. Going beyond the classical $Ω(n^{-2})$ first-order oracle lower bound of Nemirovsky and Yudin, we prove an $Ω(n^{-1.6342})$ non-anytime lower bound and an $Ω(n^{-1.2408})$ anytime lower bound. These improve the recent $Ω(n^{-1.932})$ non-anytime lower bound of Ma and Chen and the $Ω(...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02855v1)

---

### 11. MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video via Sparse Fusion

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-02 · ✍️ Aidan Bradshaw, Marco Giordano, David Rode +8 more

The 3D center of mass (CoM) is a primary quantity in the biomechanical analysis of sport, rehabilitation, and clinical movement, yet existing 3D pose tracking, mesh recovery, and multi-view triangulation methods either optimize 3D keypoint accuracy without anatomical constraints or carry compute and capture infrastructure too heavy to deploy where CoM tracking is most useful. As a result, the metr...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02854v1)

---

### 12. The Implications of Linguistic Illegibility for LLM Security

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ James Mickens

LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model computation. We introduce the term ``linguistic illegibility'' to broadly refer to scenarios in which an LLM's externalized or mechanistically-probed la...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02852v1)

---

### 13. Post-Training Language Models for Gold-Medal Performance in Coding Competitions

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-02 · ✍️ Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi +2 more

Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, we train Ne...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02849v1)

---

### 14. RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-02 · ✍️ Xiaolei Lang, Ze Kang, Zehao Huang +1 more

Novel view synthesis from sparse inputs requires both geometric grounding from the observed views and generative priors of unobserved regions, motivating recent hybrid methods that combine reconstruction and generation. However, existing methods bridge the two with rendered images or explicit 3D representations such as point maps or 3D Gaussians. Generation is thus conditioned on a lossy and imper...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02847v1)

---

### 15. UE5M3 FP4 Block Scaling for Stable Language Model Pretraining

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-02 · ✍️ Robert Hu, Carlo Luschi, Paul Balanca

Stable 4-bit floating-point (FP4) pretraining is difficult because the E2M1 payload represents only a narrow range of magnitudes. NVIDIA's Transformer Engine \nv{} recipe addresses this with current-tensor scaling, a randomized Hadamard transform (RHT), and bfloat16 (BF16) final layers, adding work outside the FP4 matrix multiplications. We instead pair E2M1 payloads with unsigned E5M3 (\ue{}) blo...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.02846v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
