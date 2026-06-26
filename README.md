# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-06-26 08:30 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. DanceOPD: On-Policy Generative Field Distillation

![CV](https://img.shields.io/badge/cs.CV-blue) ![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-06-25 · ✍️ Wei Zhou, Xiongwei Zhu, Zelin Xu +8 more

Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has be...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27377v1)

---

### 2. Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar +5 more

Most unified large multimodal models (LMMs) that support both visual understanding and image generation still rely on curated post-training supervision, such as human annotations, preference labels, or external reward models. We ask whether a unified LMM can improve both abilities autonomously using only unlabeled images. We propose a self-evolving training framework with three internal roles: a P...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27376v1)

---

### 3. World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Manish Kumar Govind, Dominick Reilly, Smit Patel +2 more

Going beyond predicting robot actions, World Action Models (WAMs) can also generate future visual observations. We build on this generative capability to propose Recurrent Generative Replay (REGEN), a continual imitation learning framework that synthesizes pseudo-replay trajectories, enabling a robot policy to rehearse previously learned tasks without storing their original human demonstrations. D...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27374v1)

---

### 4. Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Shravan Venkatraman, Ritesh Thawkar, Omkar Thawakar +4 more

Recently, self-evolving large multimodal models (LMMs) have received attention for improving visual reasoning in a purely unsupervised setting. However, multi-role self-play and self-consistency reward schemes in existing self-evolving LMMs optimize answer agreement without ensuring the decoder attends to visual content, relying instead on statistical language priors to produce self consistent out...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27373v1)

---

### 5. DnA: Denoising Attention for Visual Tasks

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Ron Campos, Subhajit Maity, Xin Li +2 more

The softmax activation in multihead attention (MHA) is the de facto standard for attention-based models in visual perception tasks. However, standard softmax can produce noisy attention patterns that dilute relevant features and degrade its performance. In this paper, we propose Denoising Attention or DnA, in which, first, a positive query identifies which image features belong to the correct clas...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27372v1)

---

### 6. Don't Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow Models via Feature Self-Guidance

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Pradhaan S Bhat, Rishubh Parihar, Abhijnya Bhat +1 more

State-of-the-art flow models generate stunning images from text or image prompts. However, they suffer from diversity collapse when generating multiple samples under the same conditioning. Existing methods address this issue via either latent guidance, which has limited effectiveness, or sample selection, which relies on external reward models that incur significant inference-time overhead. In thi...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27371v1)

---

### 7. Reinforcement Learning without Ground-Truth Solutions can Improve LLMs

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-06-25 · ✍️ Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang +6 more

Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution is unknown. We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministi...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27369v1)

---

### 8. PhysiFormer: Learning to Simulate Mechanics in World Space

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Yiming Chen, Yushi Lan, Andrea Vedaldi

We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related n...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27364v1)

---

### 9. Autoregressive Boltzmann Generators

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-06-25 · ✍️ Danyal Rehman, Charlie B. Tan, Yoshua Bengio +2 more

Efficient sampling of molecular systems at thermodynamic equilibrium is a hallmark challenge in statistical physics. This challenge has driven the development of Boltzmann Generators (BGs), which allow rapid generation of uncorrelated equilibrium samples by combining a generative model with exact likelihoods and an importance sampling correction. However, modern BGs predominantly rely on normalizi...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27361v1)

---

### 10. When are likely answers right? On Sequence Probability and Correctness in LLMs

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-06-25 · ✍️ Johannes Zenn, Jonas Geiping

Many decoding methods for large language models can be understood as shifting probability mass toward outputs that are more likely under the model, either locally at the token level or globally at the sequence level. Therefore, their success depends on a fundamental question: when does sequence probability, that is, the conditional probability of a continuation given a prompt, actually align with ...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27359v1)

---

### 11. Error-Conditioned Neural Solvers

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Haina Jiang, Liam Wang, Peng-Chen Chen +4 more

Neural surrogate models offer fast approximate mappings from PDE parameters to solutions, but they typically treat solving as a purely statistical task: once trained, they struggle to correct their own constraint violations and extrapolate beyond the training distribution. Recent hybrid methods promote physical correctness by targeting the PDE residual via gradient descent or Gauss--Newton steps, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27354v1)

---

### 12. Mapping Political-Elite Networks in Europe with a Multilingual Joint Entity-Relation Extraction Pipeline

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-06-25 · ✍️ Kirill Solovev, Jana Lasser

Whether political elites organise into rent-seeking coalitions that capture public resources or civic networks that sustain governance is a central question in comparative politics. Yet observing these complex, informal, and adversarial ties at scale has historically required intensive manual coding, while automated text-as-data methods have largely been limited to simple co-occurrence. Recent lar...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27347v1)

---

### 13. RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Minghao Yin, Jiahao Lu, Wenbo Hu +3 more

Modern video diffusion transformers position their tokens through RoPE on the (u,v,t) axes -- a description of the camera's sampling grid that says nothing about the 3D structure of the scene. We observe that the geometric relation between two camera rays is captured by the Plucker reciprocal product, which is bilinear in the two rays -- the same algebraic form as the dot product in Transformer at...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27345v1)

---

### 14. Understanding Domain-Aware Distribution Alignment in Budgeted Entity Matching

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-06-25 · ✍️ Nicholas Pulsone, Gregory Goren, Roee Shraga

Entity Matching (EM) is a core operation in the data integration pipeline, where records from different sources are compared to determine whether they refer to the same real-world entity. Recent work has incorporated domain information and low-resource learning techniques to better adapt EM systems to realistic settings. While these approaches have demonstrated strong performance, it remains uncle...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27342v1)

---

### 15. SAM2Matting: Generalized Image and Video Matting

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-06-25 · ✍️ Ruiqi Shen, Guangquan Jie, Chang Liu +1 more

Despite impressive advances in image matting, video matting remains challenging due to the inherent gap between high-level tracking, which requires frame-wise understanding, and low-level matting, which focuses on extremely fine-grained details. Existing methods attempt this with expensive and narrowly-scoped video matting datasets, which may limit out-of-domain generalization and compromise track...

🔗 [Read on arXiv](http://arxiv.org/abs/2606.27339v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
