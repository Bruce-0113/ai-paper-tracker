# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-01 06:54 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-30 · ✍️ Hongyuan Tao, Xinggang Wang, Lianghui Zhu +7 more

We present Multimodal Flow, a fully continuous generative model of language and vision. Most unified multimodal models either model both language and quantized images as discrete tokens or combine discrete language prediction with continuous image generation. The former introduces a visual quantization bottleneck. The latter requires modality-dependent objectives and sampling procedures. Fully con...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40362v1)

---

### 2. Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-30 · ✍️ Tian Xia, Minghao Liu, Yiqing Liang +2 more

Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanced: a constant-majority predictor can score above 90% accuracy while being clinically useless. We therefore evaluate and optimize for AUROC, a threshold-free score that ranks positives above negatives...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40361v1)

---

### 3. Semifactual Credit-Augmented Policy Optimization

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-30 · ✍️ Junshu Pan, Zhizhang Fu, Shulin Huang +5 more

Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity an...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40360v1)

---

### 4. Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-30 · ✍️ Dulhan Jayalath, Oiwi Parker Jones

We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40359v1)

---

### 5. Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-30 · ✍️ Liming Lu, Xianzheng Ma, Wenkun He +14 more

Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40358v1)

---

### 6. ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-30 · ✍️ Xinghao Chen, Xiangbo Gao, Jiongze Yu +2 more

Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video scene text editing replaces text on scene surfaces, such as storefront signs, whiteboards, and product labels, while preserving the surrounding content, motion, and camera dynamics. Although scene te...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40356v1)

---

### 7. AssemblyWorld: Rethinking 3D Assembly with General-Purpose Agents

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-30 · ✍️ Jiahao Zhang, Yeying Fan, Moitreya Chatterjee +5 more

The task of 3D assembly requires translating an understanding of parts and their relationships into precise spatial arrangements. Can pretrained general-purpose agents assemble objects through visual interaction without additional assembly-specific fine-tuning? To investigate this question, we introduce AssemblyWorld, an interactive 3D environment in which agents inspect rendered views and manipul...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40353v1)

---

### 8. Image Classifiers are Efficient Self-Supervised Video Representation Learners

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-30 · ✍️ Owais Iqbal, Sudipta Sarkar, Shyam Marjit +3 more

We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstruction-based autoencoders for learning with unlabeled data, we repurpose standard image Vision Transformers by representing videos as super images which are grids composed of frames sampled from videos. Fr...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40347v1)

---

### 9. Ego4WAM: What Matters When Scaling Egocentric Human Data for Robot Learning?

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-30 · ✍️ Zhihao Sun, Liu Liu, Xinjiang Wang +6 more

Egocentric human data provides a scalable source of experience for robot learning, but varies substantially in human-robot alignment, behavioral coverage, and available supervision. Existing work shows favorable scaling with increasing human data, but it remains unclear which data properties drive downstream robot gains and how to use such data throughout the training pipeline. We present a system...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40341v1)

---

### 10. EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-30 · ✍️ Young-Jun Lee, Jinheon Baek, Soyeong Jeong +5 more

Evolutionary search with large language models (LLMs) can stall when progress requires external knowledge the model lacks. Supplying relevant documents helps, but simply adding web search tool can keep returning the same pages as solutions change. We introduce EvoDuet, a bi-level optimization method that co-evolves solutions and search queries with fixed model parameters. At each iteration, a retr...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40340v1)

---

### 11. Is Weight Tying Still Beneficial for Decoder-Only LLMs in Private Settings Under DP-SGD?

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-30 · ✍️ Razan El Mais, Ali Chehab, Ibrahim Issa +1 more

Differentially Private Stochastic Gradient Descent (DP-SGD) is a leading approach for privacy-preserving fine-tuning of large language models (LLMs). Many decoder-only LLMs employ weight tying between input and output embeddings, a design choice originally introduced for parameter efficiency and improved language modeling performance in the non-private setting. However, the impact of weight tying ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40335v1)

---

### 12. I Have a Stream: Making Self-Supervised Learning Work on Continuous Video

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-30 · ✍️ Ivan Martinović, Lukas Knobel, Yuki M. Asano

Self-supervised learning draws inspiration from infant visual development, yet standard training pipelines bear little resemblance to it: images are independently sampled and globally shuffled across epochs. We study self-supervised learning from continuous video streams, where frames are consumed in temporal order using strict sliding-window batches, without global reshuffling or multi-epoch repl...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40333v1)

---

### 13. Turbo Harness: Instance-Adaptive Harness Optimization

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-30 · ✍️ Tunyu Zhang, Hao Wang, Kai Xu +1 more

Automating the search for effective harnesses is an important step toward enabling agents to recursively self-improve. Existing harness optimizations typically produce a single global harness that is applied uniformly across task instances. However, a harness that works well on average may not be optimal for every instance. We introduce Turbo Harness, a framework that can adapt a globally optimize...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40330v1)

---

### 14. WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-30 · ✍️ Ziyan Jiang, Jingbo Yang, Jiabao Ji +5 more

As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have show...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40325v1)

---

### 15. Cogentic: Multi-Agent Orchestration for Automated Proof Discovery

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-30 · ✍️ Yang Cai, Vineet Gupta, Yanchen Jiang +4 more

We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot generation is often insufficient for open problems that require exploring multiple competing conjectures, overcoming subtle technical obstructions, and retaining intermediate progress over a long hori...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.40324v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
