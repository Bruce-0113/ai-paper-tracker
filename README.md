# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-05 07:43 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. From Pixels to Actions - Towards Native Vision-Language-Action Policies

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-04 · ✍️ Weichen Fan, Haiwen Diao, Penghao Wu +14 more

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06918v1)

---

### 2. A Framework for Context Enrichment and Selective Robustness in LLM Social Agents

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-04 · ✍️ Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel

Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt variations, creating a validation problem for social simulation. One plausible hypothesis is that this brittleness reflects...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06914v1)

---

### 3. FlowReconBench: Accuracy, calibration and cost of learned and classical flow reconstruction from sparse sensors

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-04 · ✍️ Nicolas Tricard, Linzheng Wang, Jason Chen +1 more

Reconstructing full flow fields from sparse sensors requires prior assumptions about unmeasured regions and physical variables. Yet it remains unclear when learned models outperform classical estimators and which aspects of their predictions can be trusted. FlowReconBench evaluates ten learned and five classical methods on three regimes: a laminar cylinder wake across Reynolds numbers, two-dimensi...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06912v1)

---

### 4. BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-04 · ✍️ Fei Lin, Tengchao Zhang, Ziyang Gong +15 more

Self-Driving Chemical Laboratories (SDCLs) are moving chemical experimentation toward embodied automation, where machines must perceive laboratory scenes, reason about experimental states, and act under physical, procedural, and safety constraints. Although Multimodal Large Language Models (MLLMs) are increasingly considered as embodied brains for such systems, existing laboratory benchmarks mainl...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06911v1)

---

### 5. FrontierPhysics: Evaluating Agents for End-to-End Physics Research

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-04 · ✍️ Bingran You, Wenjun Ke, Ria Rosenauer +69 more

AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine doma...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06910v1)

---

### 6. Perceptive Humanoid Motion from Simulation

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-04 · ✍️ Siyuan Hu, Abulikemu Abuduweili, Yue Meng +5 more

Humanoid robots have the potential to automate a wide range of physical tasks. Progress toward generalist humanoid autonomy, however, remains constrained by a data bottleneck: mapping pixels and free-form language to low-level joint commands requires paired supervision, and no corpus of such data exists at sufficiently large scale. Some approaches rely on human teleoperation and wearable capture d...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06908v1)

---

### 7. Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-04 · ✍️ Michal Korniak, Marco Bagatella, Ralf Römer +21 more

The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in deployment. Iterated self-improvement via reinforcement learning (RL) has demonstrated ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06905v1)

---

### 8. Motion-guided Contrastive Regularization For Latent World Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-04 · ✍️ Yiwen Chen, Qiqi Hou, Jisoo Jeong +3 more

JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for control. We identify static collapse, a failure mode in which the encoder preserves episode-specific static content while suppressing manipulation-relevant state changes. Because stat...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06901v1)

---

### 9. Occlusion for Free: Detecting Occlusion from the Disagreement Between Two Monocular Distance Cues

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-04 · ✍️ Chibueze Praise Onyenweaku, Toyibat Adele, Sikirulahi Opeyemi Abdulkareem +1 more

Knowing that a pedestrian is occluded is useful to a robot even when the detector cannot recover the hidden pixels, but occlusion estimators are normally trained on occlusion annotations that deployment settings rarely have. We show that occlusion can be read off two distance estimates a camera-only pipeline already computes. Apparent height is largely unchanged by occlusion, because the detected ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06899v1)

---

### 10. Procedural Adversarial Learning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-04 · ✍️ Jack Nugent, Jia Deng

For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires first finding them, but they may not be in a fixed dataset. We study procedural adversarial learning (PAL), a framework of minimax training and adversarial evaluation which searches the input space of a procedural generator ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06890v1)

---

### 11. Dull, Dirty, Dangerous? Working Conditions and the Limits of Occupational AI Exposure

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-04 · ✍️ Siyi Yu

Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using 21 O*NET items across 754 US occupations. Higher exposure is associated with lower condition scores under a large language model (LLM) measure and AI Occupational Exposure (AIOE), with equal occupation weights and employment weights. Adjustment for p...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06888v1)

---

### 12. Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-04 · ✍️ Benjamin Jacob Bodner

The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one benchmark, and few test an optimizer's implicit assumptions online. AMM (Adaptive Multi Mode) routes a known budget among quasi-Newton, trust-region, coordinate, multistart and evolution-strategy optim...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06879v1)

---

### 13. SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative Verification

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-04 · ✍️ Yulu An, Yifei Feng, Xiangyang Yin

LLM agents use context compaction to manage growing interaction histories, but summarizing long histories with large models can introduce substantial delays. Compaction therefore requires balancing information retention against latency. We observe that structured summary slots can retain information when generated independently. Based on this observation, we present SpecCompact, a framework that a...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06876v1)

---

### 14. Learning to Decode Linear Codes with Generalized Belief Propagation Network

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-04 · ✍️ Samira Malek

Error correcting codes are a fundamental component of communication systems, enabling reliable data transmission over noisy channels. Recently, neural decoders have demonstrated notable performance gains over classical iterative algorithms. In this paper, we propose a Generalized Belief Propagation Network (GBPNet) that preserves message-passing symmetry while enhancing the decoder's learning capa...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06874v1)

---

### 15. PixelSpline: Continuous Space-Time Video Super-Resolution via Endpoint-Anchored Shared Pixel Trajectories

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-04 · ✍️ Wanqi Yuan, Nianyi Li

Existing continuous space-time video super-resolution methods often infer motion from only two endpoint frames and model the two motion directions independently, making them vulnerable to ambiguous correspondence and inconsistent trajectories. We introduce a continuous STVSR framework that combines long-context encoding, continuous HR feature lifting, and an endpoint-anchored PixelSpline. Long-ran...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.06870v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
