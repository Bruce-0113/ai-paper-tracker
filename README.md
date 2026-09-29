# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-09-29 06:36 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-28 · ✍️ Srinjay Sarkar, Prakhar Kaushik, Soumava Paul +1 more

Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets. Fur usually covers most of an animal's body, with large inter-species and intra-species variability. We present FurE, an efficient strand-based animal fur reconstruction method that recovers a per-s...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35770v1)

---

### 2. Telescopic Language Models

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-28 · ✍️ Zhilin Guo, Boqiao Zhang, Hakan Aktas +14 more

One deployed language model must often serve many compute budgets, yet serving each budget still means a separate training or compression run per point. We train a Telescopic Language Model (TLM) to be that continuum: a nested-capacity Transformer supervised by stochastic prefix supervision with a full anchor. At every step, one randomly truncated prefix of the capacity axis is trained against the...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35769v1)

---

### 3. PDMD: Projected Distribution Matching Distillation for Video Diffusion Models

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-28 · ✍️ Zimo Wang, Junkun Yuan, Angtian Wang +9 more

Modern video diffusion models require tens of denoising evaluations over long spatiotemporal token sequences. Distribution Matching Distillation (DMD) reduces the number of function evaluations (NFE) to just a few. However, DMD samples can degrade during training, exhibiting progressive oversaturation and artifacts. We trace this instability to critic errors, which enter successive student updates...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35768v1)

---

### 4. Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-28 · ✍️ Yijia Fan, Ziqi Huang, Zhongang Cai +5 more

Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose again. Whether a revision helps is known only after it is rendered, so the reflection text and the image generation must be learned jointly, over the whole loop. Supervised fine-tuning (SFT) on reflection...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35767v1)

---

### 5. Retrieving Biblical Intertextual References in Karen Blixen's Seven Gothic Tales

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-28 · ✍️ András Kovács, Alexander Conroy, Daniel Hershcovich +1 more

Identifying intertextual references is central to literary scholarship, but computationally difficult when source material is transformed through paraphrase, allusion, historical language, and translation. We investigate this problem through biblical intertextuality in Karen Blixen's Seven Gothic Tales. Drawing on the commentary to a critical edition, we construct a benchmark of 189 annotated refe...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35765v1)

---

### 6. Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-28 · ✍️ Zhilin Guo, Boqiao Zhang, Oszkár Urbán +8 more

Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth label...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35764v1)

---

### 7. Unifying Distributional Training for One-Step Visual Generation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-28 · ✍️ Chi Zhang, Haoyang Shi, Yueyi Liu +9 more

\emph{Distributional training} provides collective supervision for one-step visual generation by matching real and generated features in frozen representation spaces. We introduce \emph{a unified theoretical framework} that separates distribution modeling from matching discrepancy and connects global objectives to pointwise feature updates through Wasserstein gradient flow. Under this framework, F...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35763v1)

---

### 8. Scaling Long-Form Story Generation via Narrative State Tracking

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-28 · ✍️ Zhennan Wan, Jianfei Chen

LLMs have demonstrated strong capabilities in creative writing. However, scaling them to full-length novels remains challenging, as maintaining narrative consistency becomes increasingly difficult. Existing story-generation methods typically focus on stories of up to about ten thousand words, leaving their ability to scale to full-length novels underexplored. In this work, we introduce Narrative S...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35759v1)

---

### 9. TokenCast: Forecasting Token Consumption During LLM Agent Execution

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-28 · ✍️ Chaoqian Ouyang, Ling Yue, Libin Zheng +7 more

When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction mu...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35760v1)

---

### 10. Statistical Learning of Contractive Dynamical Representations for Composite Adaptive Control

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-28 · ✍️ Min Kim, José Leonardo Brenes, Fred Hadaegh +1 more

We present a representation-learning framework for composite adaptive tracking control under dynamically coupled disturbances. The framework connects classical disturbance-accommodating control (DAC) to recent last-layer adaptive disturbance-rejection methods. Specifically, we introduce a statistically principled hard expectation-maximization (hard-EM) procedure, with a Kalman smoother in the hard...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35758v1)

---

### 11. Neural Harmonic Measure Operator

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-28 · ✍️ Jinjin He, Sinan Wang, Yuchen Sun +1 more

We introduce Neural Harmonic Measure Operator (NHMO), a neural solver for elliptic PDE problems on variable-shape domains. The harmonic measure of a domain is the boundary probability distribution that, integrated against any boundary data, returns the Dirichlet Laplace solution. It depends only on the geometry, not on the boundary data. NHMO parameterizes the density of this measure as a transfor...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35752v1)

---

### 12. How to Loop MoE: Flatten the Experts, Untie the Attention

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-28 · ✍️ Shouren Wang, Chuang Ma, Mohsen Hariri +6 more

Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-experts (MoE) models activate only a few of many experts for each token. Looped MoE bridges these two design philosophies and gives MoE models new potential for better expert usage, but it raises a question...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35751v1)

---

### 13. KV-streams for Efficient Compaction in Agentic Reinforcement Learning

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-28 · ✍️ Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda +15 more

Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context many times over, hindering training throughput. To alleviate this bottleneck and en...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35750v1)

---

### 14. Towards Communication-Efficient Social Intelligence in Language Agents

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-28 · ✍️ Linxiao Gong, Yijie Xu, Tianfu Wang +7 more

Socially intelligent language agents must negotiate, coordinate, and resolve conflicting preferences while respecting the time and attention of both participants. Balancing these demands is challenging because agents must convey enough to address a partner's constraints and advance their goals without adding words that do not help the interaction. In this paper, we propose Teacher-Assisted Communi...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35749v1)

---

### 15. Improving Test-Time Scaling with Adaptive Looped Transformers

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-28 · ✍️ Yichen You, Tianyu Fu, Aosong Feng +4 more

Looped transformers have demonstrated promising parameter efficiency by reusing layers for latent computation. Prior studies compare looped and non-looped models at matched parameters or per-token FLOPs. However, to the best of our knowledge, whether looping improves test-time scaling as outputs grow longer remains underexplored. Through post-training looped transformers, we study the accuracy-com...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.35748v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
