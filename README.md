# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-24 05:25 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. A Unified Framework for Image-to-3D Part Generation via Variable Granularity

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-22 · ✍️ Qiwen Gu, Xin Zhou, Xiwu Chen +3 more

Controllable 3D part generation is pivotal for digital asset creation, yet existing methods lack the flexibility to accommodate diverse user workflows requiring varying levels of control. In this paper, we introduce FlexPart, a unified image-to-3D part generation framework that supports variable-granularity geometric conditions within a single model. By seamlessly integrating heterogeneous inputs,...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31671v1)

---

### 2. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-22 · ✍️ Yunfei Xie, Howard H. Qian, Shiyi Lan +2 more

Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality:...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31670v1)

---

### 3. Reading, Writing, Sharing, and Interacting with the World through Video

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-22 · ✍️ Shengqiong Wu, Meng Luo, Bobo Li +5 more

Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving world. This survey adopts world modeling as a unifying lens for examining these developments. Viewing an...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31668v1)

---

### 4. Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-22 · ✍️ Mahdi Salmani, Adel Javanmard, Devansh Gupta +1 more

Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the su...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31667v1)

---

### 5. Phase Transition from Random Features to Fully Trainable Networks

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-22 · ✍️ Xin He, Huan Lao, Xiliang Lu +1 more

Constructing accurate and computationally tractable approximation spaces is a fundamental task in scientific computing. Partially trainable neural networks bridge fixed random features and fully adaptive representations. This paper quantifies a phase transition pattern in approximation bounds and observes analogous behavior in training errors: a rapid but smooth initial improvement followed by dim...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31663v1)

---

### 6. Reliable AI-Assisted Decisions via Selective Auditing

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-22 · ✍️ Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani +1 more

We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31662v1)

---

### 7. SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-22 · ✍️ Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe +4 more

Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often tr...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31659v1)

---

### 8. Cost-Aware Abstention for LLM-Based IT Ticket Classification

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-22 · ✍️ Sachin Gupta

Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four lar...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31657v1)

---

### 9. METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-22 · ✍️ Ali Najar, Hosein Hasani, Amir Kooshan Fattah +2 more

Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31656v1)

---

### 10. BrickWright: Agentic Creation of Physically Feasible Brick Builds

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-22 · ✍️ Ava Pun, Kevin Dai, Sally Chen +7 more

Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for assembling builds and verifying their physical feasibility is sufficient for them to produce physical...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31651v1)

---

### 11. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-22 · ✍️ Qijin Zhang, Hanzhen Wang, Yuehan Zhao +4 more

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LL...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31650v1)

---

### 12. Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-22 · ✍️ Xiaolin Li, Zihao Huang, Fanpeng Meng +5 more

Single-image 3D generation has achieved high fidelity on curated benchmarks, yet degrades sharply on real-world images with uneven illumination, blur, and occlusions. Purifying such inputs requires deciding when to intervene and preserving the visual cues needed for 3D generation, while leaving clean inputs unchanged. We introduce Gate3DGen, a selective pre-processing model that gates image inputs...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31649v1)

---

### 13. Low-Bit N-Gram Embeddings for Language Models

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-22 · ✍️ Stephen Chung, Wenyu Du

Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Flash, for example, allocates 196 billion parameters to its Engram n-gram memory. We t...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31646v1)

---

### 14. OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-22 · ✍️ Namitha Guruprasad, Abhay Yadav, Cheng Peng +2 more

Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses. Camera-aware models remove this assumption by predicting a per-pixel ray field. However, they represent different camera geometries using a single fixed basis to capture both the overall camera proj...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31645v1)

---

### 15. GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-22 · ✍️ Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez +1 more

Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the other hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultur...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.31644v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
