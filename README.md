# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-05 06:34 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-02 · ✍️ Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan +5 more

This paper examines the role of Novel View Synthesis (NVS) in geometric representation learning. In principle, NVS should reason about 3D scene structure, thereby enabling transferable multi-view geometric representations. Yet, existing encoder-based NVS methods yield poor representations. This is not because of a lack of supervisory signal, but rather due to inconspicuous architectural choices: \...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03717v1)

---

### 2. MoSE3: Learning World-Space SE(3) at Every Pixel

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-02 · ✍️ Jiahuan Cheng, Zhiyi Li, Tian Xia +3 more

Dense 3D point tracking has been a prominent paradigm for modeling motion in dynamic scenes, but a point track is just a 3-DoF translation curve per pixel: it captures where pixels go, not the rotation of the underlying part, nor which pixels move together as one body. We propose MoSE3, the first feed-forward model that predicts dense SE(3) motion from monocular RGB video, producing full 6-DoF rig...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03716v1)

---

### 3. 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-02 · ✍️ Ruihong Shen, Žiga Kovačič, Peter Kulits +6 more

We introduce 4DCodeBench, a benchmark for 4D inverse graphics through code generation, in which agents reconstruct dynamic scenes from video as executable graphics programs. To accomplish this, agents must translate visual observations into compact representations of scene structure and dynamics, by implementing abstractions such as physical simulations to reproduce complex behavior. To evaluate t...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03715v1)

---

### 4. What Should World Models Forget? Stratified Retention for Continual Adaptation

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-02 · ✍️ Nishit Anand, Ramani Duraiswami, Dinesh Manocha

Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely. World models do not satisfy this condition. Their prediction target is the environment, which changes, so knowledge that was accurate when acquired may later become false, and discarding i...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03713v1)

---

### 5. RNADyn: A Benchmark for Generating and Understanding RNA Dynamics

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-02 · ✍️ Yiming Huang, Lennart Bastian, Hanqun Cao +2 more

Ribonucleic acid (RNA) functions through conformational changes that are not fully captured by static structures. However, large-scale standardized RNA dynamics data remain limited, and existing approaches typically treat trajectory generation and dynamics understanding as separate objectives. Here, we introduce RNADynBench, a standardized RNA molecular dynamics (MD) benchmark with 2585 quality-co...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03712v1)

---

### 6. EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-02 · ✍️ Kush Hari, Justin Kerr, Nidhya Shivakumar +7 more

Inspired by human vision, we introduce a framework using active gaze to enable fine-grained bimanual manipulation with only a single stereo camera. EyeRobot 2.0 physically attends to a 3D fixation point in the scene by swiveling two eye viewpoints to center their gaze on it. The resulting images are processed foveally by allocating more visual tokens to the image centers, focusing computation on t...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03710v1)

---

### 7. From Mixing to Tearing: Graph Decomposition in Decentralized Optimization via Message Passing

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-02 · ✍️ Kuangyu Ding, Gesualdo Scutari

We study the minimization of sums of smooth strongly convex functions over undirected graphs, with each function held by one agent and communication restricted to neighbors in the graph. Existing decentralized methods, whether based on gossip or on routing over spanning trees, typically   use the network to mix or aggregate information to enable   {\it prescribed} local optimization   updates. Wha...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03709v1)

---

### 8. LESSER: Post-Training Data Selection with Output-Layer Gradients

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-02 · ✍️ Lyuxin David Zhang, Eric Wong, Surbhi Goel +1 more

The choice of post-training data for large language models substantially affects downstream performance. Gradient-based data selection is a popular approach that ranks training data by how well their gradients align with those of a small validation set. However, ranking with full-parameter gradients requires an expensive backward pass on every sample, making computation intractable for large candi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03702v1)

---

### 9. Decoding the Functional Roles of Register and High-Norm Patch Tokens in Vision Transformers

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-02 · ✍️ Neel Varma, Andrew Rufail, Dipika Khullar +1 more

Self-supervised Vision Transformers (ViTs), such as DINOv2, learn rich visual representations, but the functions of their internal tokens remain poorly understood. Recent architectures introduce dedicated register tokens to reduce high-norm out- lier patch tokens that emerge in background re- gions, yet the semantic and functional roles of both token types have not been fully established. In this ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03698v1)

---

### 10. Language Models that Play Chess and Explain Their Moves

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-02 · ✍️ Adithya Bhaskar, Jeffrey Cheng, Danqi Chen

Modern chess engines are silent experts: they play at a superhuman level, but do not offer explanations for their play. On the other hand, language models (LMs) can generate plausible-sounding explanations, but their weak playing strength limits the utility of their explanations. We introduce Queen, a 4B-parameter chess-language model that can explain its moves and plans while playing at the level...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03695v1)

---

### 11. Transcriptome-informed multi-modal AI for predicting neoadjuvant therapy response from breast cancer biopsies

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-02 · ✍️ Jungkyu Park, Dhruva Biswas, Joseph Cappadona +22 more

Scarcity of labeled data limits development of deep learning biomarkers in oncology. We develop a two-stage AI model predicting pathological complete response (pCR) to neoadjuvant therapy in breast cancer. The first stage learns the transcriptome from histopathology using 8,742 patients across 32 cancer types, corroborated by pathologist review and spatial agreement with measured expression. This ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03693v1)

---

### 12. FlowHMR: Physically Plausible Motion Capture from Video

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-02 · ✍️ Zhanke Wang, Chengfeng Zhao, Qing Shuai +8 more

We present FlowHMR, a framework for recovering physically plausible global 3D human motion from monocular video. Previous learning-based methods typically regress human motion directly from video and train the network with geometric supervision. However, recovering human motion from monocular video is inherently ambiguous in depth, and direct regression tends to collapse toward an averaged solutio...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03691v1)

---

### 13. SigLIP2 for aerial fire risk classification

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-02 · ✍️ Yunus Serhat Bıçakçı

We examine the transfer of a pretrained SigLIP2 image encoder to seven class fire risk classification from aerial imagery. We introduce a reproducible partition of the public FireRisk training mirror and an implementation that records data provenance, preprocessing and model selection. Two initial runs compare a frozen encoder probe with full model adaptation. On the validation partition, full ada...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03689v1)

---

### 14. Simulation-Free Learning of Population Dynamics with Wasserstein Lagrangian Residuals

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-02 · ✍️ Fedor Sergeev, Markus Heinonen, Daniel Waxman +4 more

The dynamics of cells, organisms, and fluids are often modeled as probability distributions evolving over time. Reconstructing and extrapolating this evolution from unpaired snapshots requires assumptions about the underlying process. Wasserstein gradient flows are a common choice, but they cannot describe conservative or periodic dynamics. Lagrangian mechanics in Wasserstein space covers both, bu...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03679v1)

---

### 15. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-02 · ✍️ Hui Chen, Xuan Qi, James Xu Zhao +5 more

LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framewo...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.03675v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
