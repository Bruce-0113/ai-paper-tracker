# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-22 04:16 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-21 · ✍️ Lizhe Fang, Weizhou Shen, Tianyi Tang +1 more

Large language models that generate step-by-step reasoning traces have achieved strong performance on complex tasks, and extending them to long-context settings has emerged as an important frontier. However, we identify a critical failure mode in this regime: \emph{repetitive copying}, where models extensively copy text from the input into their reasoning traces rather than productively solving th...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19345v1)

---

### 2. Appearance Pointers -- Multimodal Region Control of Diffusion Transformers

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-21 · ✍️ Rahul Sajnani, Yulia Gryaditskaya, Radomír Měch +2 more

Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone. Diffusion Transformers (DiTs) can natively ingest heterogeneous tokens stemming from texts and images, but they lack mechanisms for determining where and ho...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19344v1)

---

### 3. Masked Visual Actions for Unified World Modeling

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-21 · ✍️ Hadi Alzayer, Wenlong Huang, Haonan Chen +8 more

Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. We introduce Masked Visual Actions, a p...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19343v1)

---

### 4. ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-21 · ✍️ Yuan Wang, Yongchao Du, Mengting Chen +3 more

Recent advances in multimodal generative models have enabled instruction-based image generation to move beyond semantic manipulation to knowledge-driven visual reasoning. However, these methods focus on explicit commonsense reasoning, shallow causal understanding, and direct knowledge recall, failing at knowledge-intensive generation. We develop \textbf{ExpertVerse}, a capability-centric benchmark...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19341v1)

---

### 5. OmniReasoner: Thinking with Long Audio-Video via Native Tool Use

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-21 · ✍️ Yu Chen, Caorui Li, Ziyu Xiong +8 more

Long audio-video reasoning is difficult for omnimodal LLMs because the decisive evidence is often sparse, cross-modal, and too expensive to preserve with uniformly high-fidelity inputs. We introduce OmniReasoner, a tool-use post-training framework for Thinking with Long Audio-Video: omni-modal LLMs learn, via supervised fine-tuning and reinforcement learning, to decide whether and where to call a ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19339v1)

---

### 6. CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-21 · ✍️ Qijia He, Jiayi Cheng, Chenqian Le +8 more

Coding agents increasingly operate in executable environments where a failed attempt produces actionable feedback rather than merely an incorrect answer. Existing cost-aware systems typically treat such failures as cascade decisions: try a cheap model first, then escalate hard cases to a stronger and more expensive model. In coding, however, execution feedback can also make further cheap-model rec...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19338v1)

---

### 7. Agents in the Wild: Where Research Meets Deployment

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-21 · ✍️ Grace Hui Yang, Pranav N. Venkit, Hooman Sedghamiz +3 more

Agentic systems large language model (LLM) based architectures capable of reasoning, planning, acting, and coordinating with tools and other agents are rapidly transitioning from research prototypes to production scale deployments across domains such as software engineering, scientific discovery, and finance. While academic work has emphasized benchmarks and algorithmic innovation, deployment rais...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19336v1)

---

### 8. 1-Lipschitz Neural Networks on Hadamard Manifolds

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-21 · ✍️ Davide Murari, Marta Ghirardelli, Ben Adcock +3 more

Controlling the Lipschitz constant of a neural network is a standard way to promote robustness and stability. Most existing constraining strategies are designed for Euclidean spaces. In this work, we construct and analyze a class of 1-Lipschitz neural networks on Hadamard manifolds. Our layers are of gradient-descent type, $1$-Lipschitz, and quasi-$α$-firmly nonexpansive. The core building blocks ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19335v1)

---

### 9. Fundamental limits of distributed multiclass classification from simple binary decisions

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-21 · ✍️ Ioannis Papageorgiou, Srinivas Nomula, Ayalvadi Ganesh +2 more

We consider the problem of constructing a $K$-class classifier from the combination of $O(\log K)$ simple binary classifiers -- this is a natural paradigm to construct a sophisticated classifier in a distributed manner with each agent performing a relatively straightforward task. We study the fundamental performance limits of such a classifier when the corresponding binary classifiers are hyperpla...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19334v1)

---

### 10. Provable diffusion-based posterior sampling for linear inverse problems via DDIM

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-21 · ✍️ Yuchen Jiao, Na Li, Changxiao Cai +2 more

Diffusion-based methods have achieved remarkable empirical success in solving inverse problems. However, many existing posterior samplers either lack rigorous theoretical guarantees or incur substantial computational overhead. We propose a simple and efficient algorithm, called \pddim, for solving linear inverse problems with diffusion priors via a DDIM-type sampler. Our method requires only light...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19333v1)

---

### 11. ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling

![LG](https://img.shields.io/badge/cs.LG-purple) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-21 · ✍️ Chirag Vashist, Ke Li

Generative models have undergone many generations of evolution, from VAEs/GANs to diffusion/flow matching. Along the way, the underlying techniques have become more complicated and various beliefs about what drives strong empirical performance have taken hold. Due to the success of diffusion models and flow matching, one of the more common beliefs is the importance of transforming the noise distri...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19332v1)

---

### 12. ISO: An RLVR-Native Optimization Stack

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-21 · ✍️ Hanqing Zhu, Wenyan Cong, Zhizhou Sha +8 more

Reinforcement learning with verifiable rewards (RLVR) is rapidly advancing the reasoning capabilities of language models, yet the optimization layer that converts reward feedback into weight-space updates remains poorly understood. Building on our prior analysis (Zhu et al., 2025), we study this missing layer through the singular structure of model weights and identify spectral inheritance: RLVR c...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19331v1)

---

### 13. Associative Emotional Learning in Convolutional Neural Networks

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-21 · ✍️ Seowung Leem, Andreas Keil, Mingzhou Ding +1 more

Associative emotional learning enables organisms to adaptively link pleasant or unpleasant outcomes to the presence of predictive stimuli. Whereas computational models such as the Rescorla-Wagner model have shed light on this important function, the limitations of these models are also known, especially when they are applied to neural data. The advent of deep neural networks has opened another ave...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19327v1)

---

### 14. Selective State-Space Adaptation and Retrieval for Language Model Reasoning

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-21 · ✍️ Atahan Dokme, Larry Heck

Low-rank adaptation introduces a static learned update applied identically to every input. The update provides task-level adaptation but does not explicitly represent token-level or instance-level state variation. A family of adapters is proposed that introduces selective state-space recurrence at two complementary granularities. At the token level, \textbf{MaLoRA} (Mamba-modulated low-rank adapta...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19326v1)

---

### 15. InstructMixup: Instruction-Guided Salient Patch Editing for Robust Data Augmentation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-21 · ✍️ Khawar Islam, Arif Mahmood, Xin Jin +1 more

In image and video technologies, data augmentation is widely used to improve the generalization of deep visual models, and mixup-based strategies that interpolate between samples have become the dominant approach. However, computing informative mixing regions adds substantial overhead, and blending content across different images frequently disrupts the semantic integrity of the resulting sample. ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.19324v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
