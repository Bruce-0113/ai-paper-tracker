# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-22 07:48 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Posterior Matching Distillation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-19 · ✍️ Hidir Yesiltepe, Julius Berner, Arash Vahdat +1 more

Diffusion distillation accelerates image and video generation by compressing a pretrained teacher's iterative sampling process into a few network evaluations. Distribution-based methods achieve this by matching the student's output distribution to the teacher's. This matching is often driven by reverse-KL objectives, whose mode-seeking bias favors dominant teacher modes at the expense of diversity...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26629v1)

---

### 2. RL Post-Training in Diffusion Transformers Is Activation Steering

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Tuna Han Salih Meral, Kaan Oktay, Alec Helbling +3 more

Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them requires learning complex, input-dependent transformations. To isolate how much of t...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26627v1)

---

### 3. PlayCraft: Designing Engaging Games from Agent Play Experience

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-19 · ✍️ Weihao Cheng

Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alter...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26624v1)

---

### 4. TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Jinbin Luo, Xiaozhe Yao, Shang Yang +3 more

Hybrid architectures have become mainstream among open-weight language models. Their global-attention and bounded-state layers maintain heterogeneous caches whose demands vary with context length and concurrency. We present TideCache, a serving system on CPU--GPU superchips with three components for allocating GPU memory among caches and managing their residency across GPU and host memory. The Tra...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26619v1)

---

### 5. One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Yuxin Jiang, Wenqiang Sun, Jiaqi Li +4 more

Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior,...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26617v1)

---

### 6. ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-19 · ✍️ Yansong Qu, Wesker Zheng, Quanjian Song +4 more

High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial computational and memory costs. We present ScaleWorld, a causal video model that unifies low-resolution world prediction and high-resolution refinement within a single shared backbone. By refining its own predictions, ScaleWorl...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26615v1)

---

### 7. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control

![CL](https://img.shields.io/badge/cs.CL-green) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-19 · ✍️ Yiyang Du, Yuxuan Kuang, Qitao Zhao +7 more

Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agen...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26613v1)

---

### 8. Bio-PM-Guided Synthetic IMU Generation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Deepali Singh, Deepesh Parpani, Aviral Gupta

Collecting and labeling inertial measurement unit (IMU) data for human activity recognition (HAR) is expensive, and models trained on one group of subjects often fail to generalize to unseen individuals. Even with balanced data, classifiers struggle to distinguish dynamically similar activity classes and benefit from targeted augmentation. We explore whether synthetic IMU data generated in the rep...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26607v1)

---

### 9. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Peiyun Hu, Marko Mihajlovic, Lyndon Duong +5 more

We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that pro...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26603v1)

---

### 10. SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-19 · ✍️ Amine Lbath, Manan Suri, Aurelien Delaitre +3 more

LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on a...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26601v1)

---

### 11. Active Feature Acquisition by Distilling an Oracle Teacher

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-19 · ✍️ Yang Meng, Zixin Ding, Robert L. Grossman +1 more

Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy that decides, per instance, which features to acquire under a budget. Existing AFA methods train this policy by optimizing a self-constructed utility target rather than distilling an explicit teacher....

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26598v1)

---

### 12. PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-19 · ✍️ Kai Lu, Chenyang Ma, Ioannis Havoutis

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free compon...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26596v1)

---

### 13. Coda-DaVinci: Reimagining Video Generation with Code2Video

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-19 · ✍️ Yiyan Ji, Qixun Wang, Yang Shi +20 more

Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompt...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26595v1)

---

### 14. Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Terence D. Agbeyegbe, Toneukarin G. Agbeyegbe

Self-consistency certification treats repeated sampling from a language model as sequential evidence accumulation and stops when an anytime-valid e-process crosses a threshold, guaranteeing finite-sample Type I error control by Ville's inequality. Prior constructions assume sampled rollouts are conditionally independent. We show this assumption fails in practice: reasoning streams are positively c...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26592v1)

---

### 15. Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-19 · ✍️ Jiahao Huang, Jun Wang

Vision-language models (VLMs) integrate visual and textual information, but their outputs do not reveal internal concept representations. Global workspace theory (GWT) proposes that information is selected from parallel brain processes, integrated in a shared workspace, and made available to specialised processes. We introduce the Multimodal Concept Lens (MC-Lens), a multimodal Jacobian lens, to s...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.26590v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
