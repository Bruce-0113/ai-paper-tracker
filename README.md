# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-15 03:57 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-14 · ✍️ Junjie Yin, Xinyu Feng

Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estima...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13034v1)

---

### 2. The Seriality Gap in Video Diffusion Models

![LG](https://img.shields.io/badge/cs.LG-purple) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-14 · ✍️ Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu +1 more

When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13031v1)

---

### 3. TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-14 · ✍️ Zhouchonghao Wu, Akshay Rangesh, Weixin Li +4 more

Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13028v1)

---

### 4. PalmClaw: A Native On-Device Agent Framework for Mobile Phones

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-14 · ✍️ Hongru Cai, Yongqi Li, Ran Wei +1 more

Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, a...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13027v1)

---

### 5. A Shortcut to Statistically Steady-State Turbulence with Flow Matching

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-14 · ✍️ Gianluca Galletti, Gerald Gutenbrunner, William Hornsby +5 more

Many nonlinear physical systems exhibit an initial transient phase in which perturbations grow before nonlinear interactions lead to a statistically steady state. While this saturated regime is of primary interest, direct numerical simulations must resolve the full transient dynamics before reaching it, incurring significant computational cost. In Computational Fluid Dynamics, reduced-order approa...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13022v1)

---

### 6. FlowWAM: Optical Flow as a Unified Action Representation for World Action Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-14 · ✍️ Yixiang Chen, Peiyan Li, Yuan Xu +13 more

World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. Existing numerical actions fail to satisfy th...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13017v1)

---

### 7. Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-14 · ✍️ Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani +1 more

Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. We train an audio-native interface for DiffusionGemma, a 26B mixture-of-experts model that generates text by uniform, random-token discret...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13013v1)

---

### 8. DermDepth: Toward Monocular Metric Scale 3D Reconstruction Models for Dermatology

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-14 · ✍️ Héctor Carrión, Narges Norouzi

Dermatological practice routinely involves measuring and tracking lesion size, morphology and texture, as critical components of wound or skin cancer screening, monitoring and diagnosis. To accomplish this task, practitioners often image the skin surface with commonly available off-the-shelf camera sensors. This has led to an overwhelming research focus on 2D methods while these objectives natural...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13010v1)

---

### 9. Dynamic Resource Allocation for Ensemble Determinization MCTS

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-14 · ✍️ Jakub Kowalski, Adam Ciężkowski, Artur Krzyżyński +1 more

Simulation-based algorithms are especially suited for high-uncertainty environments such as adversarial board games with significant elements of randomness and hidden information. In particular, several Monte Carlo Tree Search (MCTS) variants are commonly used in such domains. In this paper, we propose a series of enhancements for Ensemble Determinization MCTS, introducing two axes for dynamic res...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13007v1)

---

### 10. The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-14 · ✍️ Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban

A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from t...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13006v1)

---

### 11. Watermark Forensics for Generative Models: An Information-Theoretic Perspective

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-14 · ✍️ Xiaoyu Li, Zheng Gao, Xiaoyan Feng +3 more

A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$.   One object organizes the answers. Let $S$ be the secret the mark carries (...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.13003v1)

---

### 12. X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-14 · ✍️ Heng Zhou, Shuhong Liu, Yonghao He +6 more

We present X-lens, a compact feed-forward model for metric depth estimation from a variable number of calibrated fisheye and pinhole views. To support real-time downstream perception, X-lens is built around a geometry-aware heterogeneous camera formulation with two key components. Learnable calibration tokens provide a coarse alignment between fisheye and pinhole projective spaces, while a Jacobia...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.12993v1)

---

### 13. Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-14 · ✍️ Héctor Carrión, Narges Norouzi

Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tones and rare diseases, impedes progress toward measurably fair methods. We introduce cgDDI (Controllable Generation of Diverse Dermatological Imagery), a hybrid framework that (1) synthesizes realistic ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.12987v1)

---

### 14. Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-14 · ✍️ Aleh Manchuliantsau

Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i<k} p_i)[c_k + (1 - p_k)R_{k+1}]. On a frozen 26-route cohort, all 57 ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.12986v1)

---

### 15. Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-14 · ✍️ Sen Yang, Yuen-Hei Yeung

Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this as a failure of internal incentive-compatibility (IC) and present a method for learning and certifying counterfactual report mediators that hold a model's reports to a causal contract: invariant to fo...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.12985v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
