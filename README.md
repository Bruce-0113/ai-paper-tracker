# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-08-31 06:43 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Vaibhav Mehandiratta, Saket Ramchandra

We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations togeth...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28589v1)

---

### 2. Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Nan Wang, Mohit Yadav, Jonathan Wulff +5 more

Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are need...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28578v1)

---

### 3. Learning a Size-Weight Frontier for Synthetic-Augmented Inference

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Chengpiao Huang, Kaizheng Wang

Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our fra...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28576v1)

---

### 4. SignRR: Retrieve and Refine Real Motion for Sign Language Production

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-28 · ✍️ Fidel Omar Tito Cruz, Angie Sanchez Marquina, Summy Farfan +1 more

Sign language production (SLP) aims to generate continuous signing motion from spoken language, often through gloss-to-pose generation. Prior work mainly follows two paradigms. Generative models synthesize motion from a learned prior or from noise, without reference to an observed signing instance, making rare hand configurations and signer-specific articulation difficult to preserve. Retrieval-ba...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28568v1)

---

### 5. GeBDA: Building Damage Assessment as Text-Based Sequence Prediction

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-28 · ✍️ Olivier Dietrich, Krishna Sapkota, Konrad Schindler +1 more

Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28567v1)

---

### 6. On two proofs of $d^2$ mixing of weighted Dikin walks

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Yuansi Chen, Yunbum Kook

We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\barν$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-p...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28566v1)

---

### 7. Learning between the peaks: sharp asymptotics for kernel ridge regression under power-law anisotropy

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Lorenzo Rizzi, Arie Wortsman Zurich, Bruno Loureiro

We study kernel ridge regression under anisotropic Gaussian data, where the input covariance decays as a power law with exponent $α\geq 0$ for polynomial inner-product kernels. We derive asymptotically sharp expressions for the kernel spectrum and the generalization error in the polynomial high-dimensional regime $n=Θ(d^κ)$, revealing how anisotropy reshapes the learning curves. For weak anisotrop...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28564v1)

---

### 8. A Formal Limitation on Learning Human Language From Textual Corpora

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-28 · ✍️ Emily Cheng, Ryan Cotterell

Can a listener recover what a speaker means from the form of an utterance alone? We answer this question information-theoretically, and for a listener given by any featurizer of text, including the hidden states of contemporary large language models. Modeling language use as a joint distribution over meanings, contexts, and utterances, we derive upper bounds on the probability that a decoder recov...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28560v1)

---

### 9. Blog: Survey of Optimizers

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-28 · ✍️ Ruoran Xu

Neural-network optimization in 2025-2026 is no longer well described as a succession of new Adam variants. The design space has expanded from coordinates to matrices and layers, from fixed training horizons to policies over time, and from mathematical update rules to state representations that must survive sharding and low-precision computation. This survey organizes recent optimizers and training...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28557v1)

---

### 10. Logos: An Agent Harness on a Cross-Process Bus

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-28 · ✍️ Hanzhang Jia, Liheng Zeng, Hao Cheng +2 more

Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one phys...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28553v1)

---

### 11. Advancing Interaction-Sensitive Feature Selection: Novel Relief-Based Algorithms, Expanded Comparisons, and Recommendations for Biomedical Data Mining

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Kia Kazemi-Nia, Harsh Bandhey, Philip J. Freda +1 more

As a precursor to high-dimensional biomedical data modeling, reliable feature selection can reduce computational expense, improve modeling performance, and yield simpler, more interpretable models. However, most filter-based feature selection methods struggle to detect feature interactions, while wrapper or embedded feature selection methods are computationally expensive. Relief-based algorithms (...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28552v1)

---

### 12. Video Generative Models as Geometry Learner

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-28 · ✍️ Haosen Yang, Jifei Song, Zhensong Zhang +2 more

Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28549v1)

---

### 13. DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-28 · ✍️ Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian

Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightwe...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28547v1)

---

### 14. An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-28 · ✍️ Javier Aguilar Martín

A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the re...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28541v1)

---

### 15. InstructMesh: Selective Refinement of Generative 3D Models for Fabrication

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-28 · ✍️ Faraz Faruqi, Ahmed Katary, Demircan Tas +10 more

Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region select...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.28534v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
