# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-30 06:49 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Elucidating the Design Space of LM Data Attribution

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-29 · ✍️ Steven Yu, Sheng-Yu Wang, Kimia Hamidieh +2 more

Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introd...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40655v1)

---

### 2. Propose-Filter-Release: Scaling Noise to Typical Sensitivity via Private Filtering

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-29 · ✍️ Moshe Shenfeld, Eliad Tsfadia, Katrina Ligett

An estimator can be accurate and stable on typical data, yet sensitive to a few possible records. Differentially private mechanisms commonly scale their noise to the worst-case influence of a single record, which lets these records dictate the noise even when the remaining data would allow far less. Removing them first would restore the smaller scale, but the removal must itself be private.   We i...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40654v1)

---

### 3. Micro-Edits: Computational Support for Fine-Scale Edits in Film

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-29 · ✍️ Nhan Tran, Hijung Valentina Shin, Abe Davis +1 more

In film editing, every frame matters. While macro, content-level edits shape the high-level narrative of a film, small local edits often control timing and direct visual attention. For example, editors can adjust the precise timing of clips to control the length of a meaningful silence, or cut to shots that highlight a specific character's reactions to important moments. These small, detailed edit...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40653v1)

---

### 4. Rethinking Neural Thickets Without Weight Perturbations

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-29 · ✍️ Nicolas Dufour, Elouan Gardès, Amil Dravid +2 more

The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen a...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40649v1)

---

### 5. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-29 · ✍️ Jiongfan Yang, Weichen Fan, Haiwen Diao +2 more

Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introdu...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40647v1)

---

### 6. Adaptive Scenario Generation for KL-DRO Around a Learned Density Model

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-29 · ✍️ Aron Brenner, Saurabh Amin

Distributionally robust optimization (DRO) hedges data-driven two-stage stochastic programs against error in the distribution estimated from a finite record, and standard ambiguity sets differ in how they treat realizations absent from that record. A divergence ball around the empirical distribution contains only reweightings of the record, whereas a transport ball also contains distributions supp...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40644v1)

---

### 7. Luggage re-identification: A study of strategies towards a real-world application

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-29 · ✍️ Quentin Dhôte, Romaric Audigier

Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (lost luggage recovery). It enables the association of observations of the same luggage across disjoint camera views in complex environments such as airports, train stations and border crossing. While exi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40643v1)

---

### 8. From extreme weather to agricultural consequences with agentic AI

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-29 · ✍️ Minghan Yu, Mengyu Dai, Yixin Wen +1 more

Extreme weather is forecast days ahead, yet its consequences for agriculture remain hard to predict: a forecast says where a storm will strike, not which crops will suffer or how much is at risk, and the records that could tell span many sources. We present WxCrop, the first agent that judges agricultural hazards from physically interpretable weather indices examined by causal analysis, and the fi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40641v1)

---

### 9. SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-29 · ✍️ Derong Jin, Xiyi Chen, Ming C. Lin +1 more

Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce Video-to-4DAVScene, a new task that turns a video into an explorable, time-varying 4D audio-v...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40640v1)

---

### 10. world2vec: Mechanistic world models through latent dynamics learning

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-29 · ✍️ Tobias Schmidt, Rodrigo Gonzalez Laiz, Krisztián Szuppinger +1 more

World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. Here, we introduce world2vec to learn mechanistic world models without reward information directly from observations and actions. World2vec learns latent dynamics that faithfully reproduce the true sy...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40637v1)

---

### 11. Probing Spatial State Representations in Visual Foundation Models

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-29 · ✍️ Baiqiao Yin, Zhongang Cai, Ruisi Wang +3 more

An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual foundation models provide representations that support such a state? We study this question through ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40636v1)

---

### 12. SymAnt: Grounding Long-Horizon Action Anticipation with Adaptable Symbolic Priors

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-29 · ✍️ Fnu Aryan, Yaqi Xie, Joseph Campbell +6 more

As robots and intelligent systems increasingly interact with humans, they must anticipate long sequences of future actions from only brief observations. While purely neural models typically require extensive observations to predict future actions and remain difficult to interpret and adjust, symbolic priors offer a structured alternative. To this end, we introduce SymAnt, a novel neuro-symbolic ap...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40632v1)

---

### 13. ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-29 · ✍️ Qiyao Ma, Xiaodong Liu, Weiwei Yang +9 more

Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model's first few output tokens, and existing defenses inherit the weakness, supervising the surface form...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40627v1)

---

### 14. Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-29 · ✍️ Chengyang He, Wenlong Zhang, Koduvayur Subbalakshmi +1 more

Ask a language model whether sales tend to dip after a product recall, or whether one side effect tends to follow another after a vaccine, and it answers in a fluent sentence that reads like a finding, with no test behind it. Assertions about how events unfold across many cases fill the Web, and each is a temporal hypothesis that only a significance test over the right records can settle. The veri...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40619v1)

---

### 15. An ODE-based Sampler for Discrete Diffusion Models

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-29 · ✍️ Samson Gourevitch, Yazid Janati, Eric Moulines +3 more

The marginals of a continuous diffusion model can be reproduced by a deterministic ordinary differential equation (ODE), known as the probability flow ODE, which provides a foundation for accelerated sampling and consistency distillation. In this paper we address the question whether an analogous formulation exists for discrete diffusion models and answer it affirmatively by introducing exponentia...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.40618v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
