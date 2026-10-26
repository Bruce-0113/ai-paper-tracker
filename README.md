# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-26 05:47 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. The Language of Instruction: Genre and Generative AI

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-23 · ✍️ James E. Dobson

This article argues that instruction-fine-tuned language models should be understood as implementing a genre, what is proposed as the instructional-conversational genre. This genre is an amalgamation of discursive language from prior conversations between generative models and humans recursively run through these massive neural networks. It is instantiated in applications through instruction fine-...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32982v1)

---

### 2. SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-23 · ✍️ Yuhan Liu, Lianhui Qin, Shenji Wan

Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrangements, yet their outputs require geometric reasoning to become physically valid 3D scenes. We intro...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32978v1)

---

### 3. UniAction: Unified Action Conditioning for World Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-23 · ✍️ Bowen Xue, Zizhang Li, Hong-Xing Yu +1 more

Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across separate models. We introduce UniAction, a unified action-conditioning framework that represents any action as a sparse set of action elements, each with a discrete semantic identity...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32977v1)

---

### 4. FlexGlue: Sparse-to-Dense Feature Matching and Visual Disambiguation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-23 · ✍️ Philipp Lindenberger, Paul-Edouard Sarlin, Ondrej Miksik +1 more

To estimate correspondences across images, existing approaches match either sparse interest points, which is highly efficient but limited by repeatability, or dense pixel grids, which is robust but expensive. Furthermore, these approaches are trained with only matching pairs and thus often fail to reject unrelated pairs that exhibit visual symmetries, which is equally important in applications lik...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32976v1)

---

### 5. RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-23 · ✍️ Xi Chen, Fengqi Hu, Zeyu Shen +5 more

Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusability and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric l...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32971v1)

---

### 6. DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-23 · ✍️ Amber Xie, Jiawei Fu, Xiaofeng Guo +3 more

Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargeted to the robot, and they do not directly ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32969v1)

---

### 7. MiD-VLM: Detecting and Grounding Global Semantic Misinformation in Image-Caption Pairs

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-23 · ✍️ Tarunya Prasad, Bharatesh Chakravarthi

Semantic misinformation can arise when an authentic image is paired with a caption that changes or distorts its narrative. Because the image itself may contain no visible signs of manipulation, methods designed to detect pixel-level artifacts can miss these misleading image-caption pairs. We study this problem using DGM4+, a dataset designed to evaluate the detection of global scene and semantic i...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32967v1)

---

### 8. ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-23 · ✍️ Zimo He, Tianyi Bian, Zizhong Yang +7 more

Learning humanoid control from monocular human videos offers a scalable way to acquire diverse whole-body behaviors. Yet, existing reconstruction-retargeting-tracking pipelines are limited in system-level scalability by separately optimized intermediate stages and cannot directly optimize reference motion executability using downstream tracking feedback. We present ViT-H, a video-to-humanoid contr...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32966v1)

---

### 9. Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-23 · ✍️ Bernardo Perrone Ribeiro, Erkut Akdag, Egor Bondarev

Few-shot industrial anomaly detection requires modeling category-specific normality from only a handful of defect-free images. Common approaches tie inference to stored exemplars, impose rigid linear structure, or risk reproducing anomalous content. Flownomaly instead casts the problem as normal-counterpart recovery in frozen DINOv2 feature space. Given normal supports, a velocity field is learned...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32964v1)

---

### 10. Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-23 · ✍️ Federico Lucca

Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent in daily use, and a measurement protocol (stratified sampling, frozen snapshots, thread-grouped splits, pre-registered ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32955v1)

---

### 11. Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-23 · ✍️ Yijing Ke, Tianle Cai, Ruosong Wang

Reinforcement learning for large language models often uses separate systems for inference and training. Even with identical weights and BF16 tensors, implementation differences can make an intended on-policy update off-policy and destabilize training. Existing remedies align the entire inference and training stacks, change global precision, or modify the learning algorithm. We ask whether alignin...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32951v1)

---

### 12. Beyond Discrete Tokens: Preserving Numerical Continuity in Medical Vision-Language Models

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-23 · ✍️ Dianye Huang, Jiamei Guo, Yue Zhou +5 more

Objective: To develop a unified vision-language model for prompt-conditioned quantitative ultrasound measurement that addresses the mismatch between continuous measurement targets and discrete token-based numerical prediction. Methods: This article presents HAD-VLM, a hybrid autoregressive-diffusion framework that combines autoregressive text generation with continuous measurement prediction withi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32948v1)

---

### 13. Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-23 · ✍️ Yuhang Ji, Fasheng Xu, Tianjun Feng

Large language model (LLM) platforms introducing advertising must decide how much capability ad revenue should fund and what consumers should pay to avoid ads. We study a monopolistic platform that jointly chooses costly response quality, advertising intensity, and subscription prices when advertising reduces user value but better service raises advertising returns. Three findings follow. First, w...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32945v1)

---

### 14. Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-23 · ✍️ Yixuan Xu, Hailin Liu, Linxiang Peng +1 more

Generative recommendation with semantic IDs represents each item as a sequence of discrete codes derived from its semantic representation and predicts these codes to generate recommendations. Existing semantic-ID recommenders are typically trained with hard labels for the observed next item. Although such supervision identifies the target, it provides no explicit distributional information about a...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32943v1)

---

### 15. If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-23 · ✍️ Thomas Landeg, Thierry Tambe

Vision-Language-Action (VLA) models perform well on robotic manipulation, yet remain brittle once their own actions carry them into states their training data barely covers. Recovering from such failures usually requires recovery demonstrations, policy retraining, or a separate model at inference time. We introduce Backtrack, a lightweight failure detection and recovery mechanism for frozen VLAs t...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.32941v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
