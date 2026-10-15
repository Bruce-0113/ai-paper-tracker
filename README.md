# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-15 05:36 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Can Learning to Answer Spatial Questions Improve Novel-View Generation?

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Jahyeok Koo, Hyeonseo Yu, Seungho Jang +4 more

Generating novel views from limited observations requires preserving both the appearance and spatial structure of a scene. Although recent approaches exploit fine-grained geometric cues, they do not explicitly model high-level semantic and spatial properties such as object identity, attributes, and inter-object relationships. In this work, we investigate whether 3D language understanding can provi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20610v1)

---

### 2. Modeling and Understanding Neural Weights of Humanoid Policies with Diffusion

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-14 · ✍️ Huixuan Cheng, Bike Zhang, Shankar Sastry +1 more

Recent advances in robot learning have driven rapid progress in humanoid control, enabling increasingly agile behaviors in the real world. However, humanoid control networks are typically obtained through conventional training procedures, while comparatively little attention has been given to directly modeling the distribution of their learned weights and generating functional networks in weight s...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20606v1)

---

### 3. Representation Conditioning for Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Saeed Razavi, Xingjian Leng, Liang Zheng

Representation-alignment methods effectively accelerate the diffusion transformer training. REPA, for example, uses a pretrained vision encoder to supervise an intermediate layer through an MLP projection head which is discarded after training. It aims to import semantics from the vision encoder to the diffusion backbone. While this objective is achieved at early layers by back-propagating the ali...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20608v1)

---

### 4. Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-14 · ✍️ Zhefei Gong, Hefeifei Jiang, Zehao Wang +1 more

Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a systematic framework for stable and sample-efficient real-world fine-tuning of complex M...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20607v1)

---

### 5. VITAL: From Visual Motion to Precise Action

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Ao Liang, Youquan Liu, Mingxiao Li +7 more

World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual motion. We first examine a simpler setting in which trajectories are reconstructed from recorded future images. Even without the need for future prediction, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20604v1)

---

### 6. CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Xiaoli Xu, Zhengtao Wu, Zhengze Xu +8 more

We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists throug...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20603v1)

---

### 7. DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Qihang Cao, Haoyuan Li, Zihan Guo +8 more

Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. Our analysis reveals that this spatial--dynamic interference is highly non-uniform across parameter groups, wit...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20598v1)

---

### 8. Co-Evolving Acting and Forecasting for Language Agents

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-14 · ✍️ Haofei Yu, Yixing Chen, Yining Zhao +6 more

Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20597v1)

---

### 9. GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Haoyuan Li, Qihang Cao, Huanyuan Zhou +10 more

Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference introduces substantial latency and computational overhead. We propose GeoThinker-$F$, an efficient framework that internalizes spatiotemporal perception by transforming causal MLLM hidden states into predi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20592v1)

---

### 10. Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo +2 more

Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, existing feed-forward scene-coding pipelines first generate a complete Gaussian representation and then encode its geometry and appearance attributes separately, often involving non-differentiable operat...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20590v1)

---

### 11. Your Transformer Is Secretly Elastic

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-14 · ✍️ Walter Simoncini, Dheeraj Varghese, Gertjan J. Burghouts +1 more

Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints. This rigidity is often suboptimal under varying query loads. We introduce a retraining-free method that elastifies pre-tr...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20588v1)

---

### 12. Price of Anarchy of First-Price Auctions in Agentic Markets

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-14 · ✍️ Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal +3 more

An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt. An agent's bid is based on its expected value for the prompt, which is the expectation of the reward for its response minus its inference costs. First-price auctions (FPAs), in which the highest bidder pays its bid and receives the prompt, are a natural way to allocate prompts in such a market, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20587v1)

---

### 13. Continuum Attention

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-14 · ✍️ Afshin Khadangi

We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half token ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20586v1)

---

### 14. Learnable Hodge-Laplacian Driven Mixture of Experts for Steady-PDE Surrogates on Coarse Unstructured Meshes

![LG](https://img.shields.io/badge/cs.LG-purple) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-14 · ✍️ Stavros Nousias, Akis Nousias, Konstantinos Gkrispanis

Current approaches for steady partial differential equations surrogate models on unstructured meshes apply a single mixing mechanism to the whole solution. This paper proposes an architecture that partitions the solution among vanilla transformer experts, each focused on a different spectral scale. The partition is built from a discrete Hodge Laplacian $L_0=\star_0^{-1} d_0^{\top}\star_1 d_0$, tha...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20585v1)

---

### 15. Player-1: Learning to Play from Synthetic Experience

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-14 · ✍️ Mingyu Ouyang, Yiran Wang, Siyuan Hu +9 more

Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game state...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.20584v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
