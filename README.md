# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-24 10:41 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Seongchan Kim, Soowon Son, Sangoh Kim +9 more

Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study structured pruning for these models, focusing on preserving both scene understanding and trajectory prediction. Our analysis of Taylor importance in Alpamayo-1.5-10B shows that reasoning and trajectory o...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31240v1)

---

### 2. Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-23 · ✍️ Chen Wang, Jiahui Huang, Riccardo de Lutio +7 more

Exploring a scene from as little as a single photo requires generating a long, camera-controlled walkthrough that extends far beyond what was captured, yet remains consistent upon return. Memory-based video generation methods preserve what they have already seen, but have no anchor beyond it, where the camera drifts from its path and a text prompt can name objects but not place them. Layout-condit...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31239v1)

---

### 3. Modern Self-Supervised Vision Transformers Are Pareidolic

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-23 · ✍️ Zihang Lin, Huaiyuan Qin, Liangli Zhen +4 more

In human perception, pareidolia is the tendency to perceive a meaningful pattern, such as a face, in a random or ambiguous stimulus.We find a similar phenomenon in modern self-supervised Vision Transformers (ViTs): on white noise, which contains neither objects nor spatial structure, a few directions of their features still form spatially coherent patterns across the patches, imposed by the featur...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31238v1)

---

### 4. Let Vision-Language Models Generate Images through Their Representations

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ JB Kim, Byungwoo Jeon, Kyungmin Lee +5 more

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central ch...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31237v1)

---

### 5. TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Hani Alomari, Md Atabuzzaman, Chris Thomas

CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the usual suspect. Yet removing it post hoc degrades retrieval on every CLIP checkpoint we test. We introduce a paired stat...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31233v1)

---

### 6. Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-23 · ✍️ Daniel Theron

Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does confidence drop when an error occurs?) and (2) downstream steering control (does an uncertainty token causally steer the mod...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31228v1)

---

### 7. How Far Can Linear Go? BiPert, a Unified Framework for Single-Cell Perturbation Modelling

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Abhishek Sharma, Aleksej Zelezniak

Understanding how genetic perturbations affect cellular behaviour is essential for studying gene function and regulatory mechanisms. Large-scale CRISPR screens measure these effects across thousands of genes, but cover relatively few cellular contexts. Predicting perturbation responses in unseen cell types and identifying perturbed genes from their transcriptional effects therefore remain challeng...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31227v1)

---

### 8. Self-Supervised Dataset Distillation via Mutual Information Maximization

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Mohammad Hossein Moslemi, Mahdi Beitollahi, Zhimin Mei +3 more

Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains underexplored in self-supervised learning (SSL), where distilled data must preserve the information needed to learn representations that remain consistent across augmentations. To bridge this gap, we introd...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31225v1)

---

### 9. Agentic AI for Intent Management and Control in Autonomous Communication Networks

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Burak Demirel, Yu Wang, Pablo Soldati

Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches often focus on intent management and orchestration, leaving the adaptation of underlying network optimization and control functions largely unaddressed. This article proposes a triadic agentic AI fra...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31223v1)

---

### 10. CTLink: A Text-Prompted Segmentation Model for Linking Radiology Report Findings to 3D Chest CT Scans

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-23 · ✍️ Mohammed Baharoon, Sung Eun Kim, Mahmoud Hussain Alabbad +33 more

Radiology reports describe findings in text only, without visually marking them on the scan, so readers cannot directly see which abnormality each reported finding refers to. We introduce CTLink, a text-prompted 3D segmentation model that segments findings described in a chest CT report. CTLink was trained on 4123 noncontrast chest CT scans with 9547 segmented report findings, including ReXGroundi...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31222v1)

---

### 11. LeJEPA Features Are Not Isotropic, and Should Not Be

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Richeek Das, Pratik Chaudhari

The SIGReg term in LeJEPA regularizes features to have an isotropic Gaussian distribution. Our first result is to show that this regularizer, in practice, cannot achieve its goal. We design a modified regularizer to enforce the objective better. This leads to slightly improved performance. For example, on ImageNet-100, our modified regularizer reaches the final accuracy of SIGReg in 1.3$\times$ fe...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31216v1)

---

### 12. Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-23 · ✍️ Xiwei Liu, Yulong Li, Xuhui Li +7 more

Humans explore unfamiliar spaces with purpose, deciding where to look until they have gathered the evidence a spatial question requires. However, can vision-language models (VLMs), which reason increasingly well over curated images and videos, also seek in space when the evidence is not handed to them? We present ActSpace-Bench, a benchmark of 994 questions across 234 exploration episodes in 72 re...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31215v1)

---

### 13. Flood forecasting using a physics-guided conditional denoising diffusion probabilistic model

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Omar Sallam, David Coe, Jeremy Feinstein +3 more

High-resolution flood forecasting with full two-dimensional shallow water equation (SWE) solvers remains computationally expensive, even on GPUs. We develop a conditional denoising diffusion probabilistic model (DDPM) that forecasts the evolution of 30 m water-depth fields over a four-day horizon for the Des Plaines River watershed, Illinois. The model is trained on SynxFlow SWE simulations of 113...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31212v1)

---

### 14. Verifying the Outputs of PDE Solvers: From Finite Elements to Neural Surrogates

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-23 · ✍️ Konstantinos Dovelos

Physics simulation outputs increasingly come from solvers that no expert inspects, such as third-party packages in automated pipelines, programs written by large language models (LLMs), and learned surrogates. In earlier work on cardiac pulsed field ablation, we proposed that solvers return a certificate with their answers. The certificate consists of an admissible potential and an exactly charge-...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31211v1)

---

### 15. WorldLatent: A Unified 4D Latent Space for World Perception and Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-23 · ✍️ Jingxi Chen, Yujia Chen, Cornelia Fermuller +3 more

Generative Pre-Training (GPT) represents a profound milestone in natural language processing, serving as the foundation for most of today's state-of-the-art large language models. By casting diverse understanding and generation problems into a shared token representation, GPT enables a single architecture and unified optimization loop to master heterogeneous tasks across massive corpora, giving ri...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.31209v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
