# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-29 04:12 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Pass the Baton: Trajectory-Relayed On-Policy Distillation

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-28 · ✍️ Haolei Xu, Xiaowen Xu, Haiwen Hong +5 more

On-policy distillation (OPD) grounds token-level supervision in the student's own trajectory, yet suffers from prefix failure: once the student commits to a wrong reasoning direction, all subsequent generation builds on this deviation, producing misdirected continuations that elicit unreliable supervision and waste compute. We identify a teacher-student continuation asymmetry on failed prefixes, w...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26057v1)

---

### 2. $π\mathbf{R}^2$: Reactive Real-time Flow Policies

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-28 · ✍️ Sungjae Park, Shubham Tulsiani

Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones. Such chunks run open-loop, so the policy cannot react to sensory input arriving mid-execution, sacrificing \emph{reactivity}. Replanning more often would restore it, but the perception-to-action pipeline (a large backbone plus multiple denoising steps) is too slow: this...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26055v1)

---

### 3. Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-28 · ✍️ Tom Saliencro, Rohan Desai, Priya Nair +2 more

Mixture-of-Experts (MoE) variants of Low-Rank Adaptation (LoRA) route every token to a fixed number of experts $k$. Tokens differ in how uncertain the model is about them, so a single k over-spends on easy tokens and under-serves hard ones. We observe that the router's output distribution is already a per-token uncertainty signal: peaked mass indicates confidence, while a flat distribution indicat...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26052v1)

---

### 4. Re-thinking Mammography Transfer Learning: The Dataset-Informed Transfer Learning (DITL) Framework for Breast Cancer Screening and Lesion Diagnosis

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-28 · ✍️ Adarsh Bhandary Panambur, Siming Bayer, Andreas Maier

Enhancing classification performance in mammography remains a persistent challenge across both small curated datasets and large-scale clinical cohorts. Conventional transfer learning approaches often neglect dataset-specific characteristics, while recent neighborhood-informed methods have been restricted to narrow tasks with rigid formulations, limiting their scalability to population-level datase...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26043v1)

---

### 5. VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-28 · ✍️ Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti +1 more

We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduli...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26042v1)

---

### 6. Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-28 · ✍️ Abhishek Pillai, Samir Kumar Nayak, Yuan Chen

Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult beca...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26041v1)

---

### 7. Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-28 · ✍️ Gaspard Lambrechts, Adrien Bolland, Daniel Ebi +1 more

Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state informat...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26040v1)

---

### 8. Wonder: Video World Model Done Better

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-28 · ✍️ Jiacong Xu, Hanwen Jiang, Zhixin Shu +3 more

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26037v1)

---

### 9. Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-28 · ✍️ Elias Fernández Domingos, The Anh Han

Technological races create tension between speed and safety: actors may gain by moving faster than competitors, even when risky development is harmful. This is prominent in debates about artificial intelligence (AI), where competitive pressure is often argued to incentivise riskier, less safety-conscious development. We study this using a framed behavioural experiment based on an idealised AI race...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26034v1)

---

### 10. CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-28 · ✍️ Ankang Yang, Jitao Zhao, Di Jin +2 more

Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivat...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26023v1)

---

### 11. UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-28 · ✍️ Siyu Xia, Chenheng Zhang, Yanting Wu +8 more

Memory is essential for LLM agents to accumulate task experience and reuse task-specific execution strategies. However, real-world deployment over boundary-agnostic and evolving task streams exposes a fundamental stability-plasticity dilemma. External retrieval-based memory can rapidly absorb new evidence, but it often fails to internalize recurring execution patterns and incurs inference-time ret...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26017v1)

---

### 12. MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-28 · ✍️ Solomon Micheal Serunjogi, Rachmad Vidya Wicaksana Putra, Ayat Taha +2 more

Recently, photonic transformer accelerators (PTAs) have successfully achieved significant speedup and energy efficiency improvements over electronic accelerators for expediting Transformer inference. However, state-of-the-art rely on expensive multi-wavelength light generation and large dot-product units due to active phase-shifter components, thus making their approach inefficient and impractical...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26016v1)

---

### 13. Instruction-Tuned Models Locally Reuse Human Syntax More Than Humans Do

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-28 · ✍️ Zandi Eberstadt

Syntactic convergence (the tendency of speakers to adapt in language towards the grammatical profiles of their interlocutors) is a well-documented feature of human dialogue widely considered to operate below conscious awareness. Whether large language models exhibit analogous syntactic convergence toward human users relative to human baselines and across a broad range of syntactic constructions re...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26015v1)

---

### 14. Pictura: Perspective-View Self-Play at Scale for Driving

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-28 · ✍️ Yuan Yin, Elias Ramzi, Marc Lafon +8 more

Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26005v1)

---

### 15. Parallel Decoding Distillation for Fast Image and Video Generation

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-28 · ✍️ Neta Shaul, Chao Liu, Arash Vahdat +1 more

Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. Albeit achieving high-quality video generation, these training losses are notoriously hard to o...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.26004v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
