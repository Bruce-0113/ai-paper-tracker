# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-08 07:01 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Tetris3D: 3D Scene Generation With Objects That Fit Together

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-07 · ✍️ Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee +2 more

We propose Tetris3D, a generative framework for single-image 3D scene reconstruction that recovers objects which are physically and geometrically coherent as a scene. Existing methods often generate objects independently or couple them implicitly, providing limited guidance for ensuring fine-grained spatial compatibility between neighboring objects that interact with one another. To address this, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10539v1)

---

### 2. Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-07 · ✍️ Shravan Chaudhari, William Paul, Suchi Saria +2 more

As we move through the world and carry out everyday tasks, we encounter objects that may become relevant only later. We are capable of recalling where we left something or what was inside a container, even without knowing we would need it later. Here, we study how an embodied assistant can build a similar memory from egocentric videos, by observing a person's day-to-day activities. We present Ledg...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10538v1)

---

### 3. Decoupling Exploration from Optimization in RLVR

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-07 · ✍️ Saif Punjwani, Micah Goldblum

Modern language models undergo reinforcement learning with verifiable rewards (RLVR) on top of already-trained checkpoints. A key promise of RLVR is the discovery of new reasoning strategies. In principle, a model can sample novel ideas absent from its prior training data. In practice, however, augmenting RLVR with strong novelty incentives has seen limited success and can degrade model quality. B...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10536v1)

---

### 4. EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-07 · ✍️ Hongru Cai, Ran Wei, Wenjie Wang +4 more

Conditional memory architectures such as DeepSeek Engram use input n-grams to look up learned embeddings, expanding the capacity of large language models (LLMs) with limited additional computation. Beyond model scaling, this architecture has demonstrated the potential to decouple factual knowledge storage from general-purpose computation, offering a promising route to updating factual knowledge wh...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10533v1)

---

### 5. Long-WAM: Scaling the Context of World-Action Models

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-07 · ✍️ Wei Huang, Bohan Zhang, Chenzhi Liu +13 more

Real-time robot control demands enough visual history to infer motion and task progress, but processing that history can delay action. We present Long-WAM, a model-system framework for scaling the context of causal world-action models under real-time control constraints. Our central finding is that access to history is not the same as using it: longer histories pay off far more when the video foun...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10528v1)

---

### 6. Decentralized SGD under Heavy-Tailed Noise: Optimal Convergence Rates and the Role of Gradient Clipping

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-07 · ✍️ Aleksandar Armacki, Haoyuan Cai, Ali H. Sayed

Heavy-tailed noise has been widely observed in modern machine learning, motivating the use of methods like gradient clipping and normalization. While these methods are well understood in centralized settings, much less is known in decentralized ones, where applying a nonlinearity to local gradients affects both optimization and consensus. Recent works on decentralized non-convex optimization have ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10527v1)

---

### 7. Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-07 · ✍️ Mikey Watts, Yuchen Cui

Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ checkpoint finetuned with rephrase augmenta...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10526v1)

---

### 8. GRACE: Generation-aware latent compression for efficient video generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-07 · ✍️ Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam +5 more

Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10524v1)

---

### 9. Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-07 · ✍️ Zhewei Chen, Hao Zhu, Jiaojiao Jiang +1 more

GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference. Existing methods mainly transfer node-wise predictions or use confidence-based reweighting, but they do not specify where the student should preserve the teacher's graph-induced geometry. We show that this omission leads to two spectral failure modes in the stu...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10520v1)

---

### 10. Why Forget-Only Unlearning Needs Memorization

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-07 · ✍️ Luka Radić, Vikrant Singhal, Amartya Sanyal

Machine unlearning asks for a deletion algorithm whose output is close to retraining from scratch without the selected forget examples. In this work, we study forget-only unlearning, where the deletion algorithm receives only the trained model and the examples to forget, with no retained data or extra training information. We ask whether forget-only unlearning is always possible. We first show tha...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10519v1)

---

### 11. RoboJEPA: Scaling Robotic Latent World Models

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-07 · ✍️ Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan +9 more

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and traine...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10515v1)

---

### 12. SciExam for ENSO: Can AI Agents Build Climate Models?

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-07 · ✍️ Yinling Zhang, Langchen Liu, Dongbin Xiu +4 more

Language-model agents are increasingly asked to carry out open-ended scientific research, yet their results are usually graded against a known answer, a rubric, or a language-model reviewer, none of which can tell whether a new scientific model is valid. The AI Science Exam for El Nino-Southern Oscillation (SciExam for ENSO) is a benchmark in which agents build low-order stochastic models of ENSO,...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10513v1)

---

### 13. Video-Conditioned Generative Joint 2D-3D Hand Motion Recovery

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-07 · ✍️ Chen Xu, Yunqi Li, Binbin Huang +3 more

Recovering faithful 3D hand motion from video remains challenging due to frequent occlusions and incomplete visual observations, which make frame-wise pose estimates unreliable and temporally inconsistent. To address this problem, we propose JoHan, a unified generative framework that recovers hand motion directly from video sequences without relying on intermediate per-frame pose predictions. Trai...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10512v1)

---

### 14. Your Prompt Should Do More: Effects of Retrieval Instructions in Embedding Models

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-07 · ✍️ Amanda Myntti, Jenna Kanerva, Veronika Laippala +1 more

Prompted embedding models have recently received increasing attention, particularly for retrieval, where detailed retrieval instructions are provided as part of the retrieval prompt. Several new datasets and studies have examined this setting, showing that the current embedding models often struggle to follow such instructions reliably. In this paper, we study the mechanism of how instructions act...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10508v1)

---

### 15. RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-07 · ✍️ Yilun Hao, Krishna Sayana, Isabella Ye +4 more

Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic variants adapt queries and tool use but remain largely retrieval-centric. However, in many tasks, the evidence required for a solution is not explicitly present in any single source i...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.10507v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
