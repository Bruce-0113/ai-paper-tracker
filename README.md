# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-11 04:12 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Wat3R: Underwater 3D Geometry Learning without Annotations

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Jiangwei Ren, Xingyu Jiang, Zijie Song +4 more

Estimating 3D geometry in underwater environments presents unique challenges due to light attenuation, scattering, and the absence of large-scale, high-quality 3D annotations. Pioneering methods rely on massive dense annotations that are impractical in underwater settings. In this paper, we propose Wat3R, a cross-domain semi-supervised learning framework designed to adapt feed-forward 3D reconstru...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08772v1)

---

### 2. ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Fabio Tosi, Luca Bartolomei, Matteo Poggi +1 more

Monocular depth estimation has seen remarkable progress through foundation models achieving robust zero-shot generalization, yet their computational demands place them far beyond the reach of embedded and mobile platforms. Lightweight alternatives exist, but have been developed almost exclusively within single-domain, self-supervised paradigms, failing silently under domain shift. We present ZipDe...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08771v1)

---

### 3. LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang +4 more

Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video m...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08770v1)

---

### 4. Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Weijian Chen, Weibo Yao, Yuhang Zhang +7 more

Scaling 3D Gaussian Splatting (3DGS) to large outdoor scenes is costly in both data acquisition and computation. Adopting panoramic images with equirectangular projection (ERP) can reduce capture effort via their full $360^{\circ}$ field of view, yet the resulting omnipresent visibility invalidates existing partitioning strategies that rely on local camera frustums, causing block-wise optimization...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08769v1)

---

### 5. UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-09 · ✍️ Zhekai Chen, Chengqi Duan, Kaiyue Sun +4 more

The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08768v1)

---

### 6. OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Hongyu Liu, Chun Wang, Feng Gao +6 more

We propose OPSD-V, an on-policy self-distillation paradigm for post-training few-step autoregressive (AR) video diffusion models. Existing few-step AR video generators can produce long videos with low latency, but still suffer from error accumulation and weakened motion dynamics during long autoregressive rollout. OPSD-V reduces long-horizon degradation while preserving the original few-step infer...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08766v1)

---

### 7. Enhancing In-context Panoramic Generation via Geometric-aware Pretraining

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Haoran Feng, Ruiyang Zhang, Longyi Zhang +2 more

In this work, we present Canvas360, a two-stage framework for in-context panoramic generation that combines geometry-aware pretraining with downstream task-specific fine-tuning. To address the lack of large-scale, high-quality training data tailored to in-context panoramic tasks, we propose Canvas360Dataset, a collection of 1M high-quality paired panoramic samples for style transfer, inpainting, o...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08765v1)

---

### 8. OpenCoF: Learning to Reason Through Video Generation

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-09 · ✍️ Xinyan Chen, Ziyu Guo, Renrui Zhang +2 more

Reasoning has become a core capability for large models, especially when reliable decisions require understanding logical consequences. Recent video generation models offer a reasoning path distinct from previous Chain-of-Thought (CoT): reasoning can unfold through temporally connected frames, known as Chain-of-Frame (CoF) reasoning. However, existing video generators are primarily trained on gene...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08763v1)

---

### 9. Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-09 · ✍️ Yifan Zhou, Qihao Yang, Yan Li +14 more

Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Bench), a benchmark for scientific lineage reasoning and lineage-grounded idea generation. IG-Bench is...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08758v1)

---

### 10. Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability in Diffusion Sampling

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-09 · ✍️ Yiwei Zhou

Score matching controls average error under the forward marginals, but a discretized reverse-time sampler evaluates the learned score along its own trajectory. We show that small forward-marginal error does not guarantee numerical stability. We construct a single smooth score field with arbitrarily small forward-marginal $L^2$ error. The learned reverse-time process is nonexplosive, has moments of...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08757v1)

---

### 11. MulTTiPop: A Multitrack Transcription Dataset for Pop Music

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-09 · ✍️ Nathan Pruyne, Benjamin Stoler, William Chen +3 more

We present MulTTiPop, a dataset of pop music segments and their associated multitrack MIDI recordings for the evaluation of automatic music transcription models. MulTTiPop contains 572 segments of popular music totaling 3.5 hours of audio, and contains songs from diverse genres and decades from the 1930s to 2000s. To collect this dataset, we perform metadata-based matching on song segments from th...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08756v1)

---

### 12. SLORR: Simple and Efficient In-Training Low-Rank Regularization

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-09 · ✍️ David González-Martínez, Shiwei Liu

Low-rank factorization is widely used to compress neural networks, but modern models are often not naturally amenable to aggressive factorization without significant accuracy loss. Existing training-time low-rank regularizers can improve compressibility, but they often require SVDs of large weight matrices, modify the model architecture (introducing additional trainable parameters), or rely on sta...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08754v1)

---

### 13. Using AI-based Learning Assistants in Higher Education: A Large-Scale Descriptive Analysis

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-09 · ✍️ Kristina Schaaff, Quintus Stierstorfer, Valerie Heckel

In this study, we present a large-scale descriptive analysis of the use of an AI-based learning assistant (Syntea) in higher education. Based on objective log data from 77,543 students enrolled in distance studies, we examine usage patterns across gender, age group, study cluster, degree, and study mode. To date, existing research on educational chatbots has largely relied on comparatively small s...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08748v1)

---

### 14. Dimensionality Reduction Meets Network Science: Sensemaking on UMAP's kNN Graph

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-09 · ✍️ Duen Horng Chau, Donghao Ren, Fred Hohman +1 more

While UMAP is widely used for exploring high-dimensional data, typical workflows focus on its lower-dimensional embedding, largely overlooking the rich k-nearest-neighbor (kNN) graph that UMAP constructs internally. This graph encodes the data manifold in its original high-dimensional space, before the distortion that UMAP's 2D projection introduces. We demonstrate the untapped potential of this i...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08746v1)

---

### 15. AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-09 · ✍️ Siddharth Damodharan, Radhika Gupta, Ali Alshami +2 more

Recent advances in Vision-Language Models, Large Language Models, and Multimodal Large Language Models have improved autonomous driving tasks such as scene understanding, decision making, trajectory prediction, and visual question answering. However, evaluating whether these models can reliably reason about safety-critical incidents remains challenging. To address this gap, we present AUTOPILOT-VQ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.08745v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
