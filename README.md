# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-02 07:18 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. GazeRIB: Systematic Evaluation of Multi-Reader Gaze-Guided Chest X-ray Learning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-30 · ✍️ Nattakorn Kittisut, Roy M. Gabriel, Marly van Assen +4 more

Radiologists' visual attention can supervise medical image learning, but how reader panel composition affects its value remains untested. We evaluated GazeRIB (Gaze-guided Radiologist-Informed Blackout), which masks unviewed regions during training and uses unmasked images at inference. Eight experts repeatedly read the same 80 chest X-rays (CXRs). We compared individual readers with three-, five-...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42152v1)

---

### 2. Latent Reasoning in Continuous Space for Unified Multimodal Models

![CV](https://img.shields.io/badge/cs.CV-blue) ![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee +2 more

Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribut...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42149v1)

---

### 3. Flide: Accelerating Decision Inference with Exact State Forking

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-30 · ✍️ Bobo Li, Jiajia Song, Hao Fei +2 more

Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42148v1)

---

### 4. Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-30 · ✍️ Ales Kubicek, Andrea Caciolai, Liangzu Peng +7 more

Agentic workflows are increasingly shifting towards long-horizon tasks, such as open-ended scientific work, where models benefit from long context windows. However, at ultra-long context (above 1M tokens), full attention is prohibitively expensive. A promising approach is sparse attention, in which a dedicated indexer selects a subset of keys for the attention. Yet current methods of indexing eith...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42147v1)

---

### 5. Hierarchical World Models with Implicit Dynamics

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-30 · ✍️ Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui +4 more

Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to brittle representations and limited fine-grained control. We introduce ID-WM (Implic...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42146v1)

---

### 6. SemEllipsoid: Semantic-aware Shape Abstraction with Ellipsoid

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-30 · ✍️ Kuankuan Cheng, Haocheng Yuan, Changjian Li

Representing 3D shapes using a set of primitives - known as shape abstraction - is an actively studied problem in computer graphics with wide applications in shape understanding, analysis, and simulation due to the compactness and computational efficiency of the primitive-based representation. Prior work has primarily focused on geometry-aware shape abstraction, where the objective is to approxima...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42145v1)

---

### 7. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-30 · ✍️ Shengguang Wu, Suning Huang, Cherie Ho +3 more

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In Rob...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42141v1)

---

### 8. Counting on Dummies: Privacy Amplification with Observable Counts and Truncated Batches

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Vitaly Feldman, Audra McMillan, Kunal Talwar

In many practical deployments of Differentially Private Stochastic Gradient Descent (DP-SGD), the server processes data in batches. Randomly sampling these batches allows for better privacy bounds via privacy amplification results. Most sampling schemes with provable privacy amplification, including Poisson sampling and random allocation, result in variable batch sizes. The privacy guarantee of th...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42139v1)

---

### 9. ReLift: Dense 3D Tracking as Lifted Trajectory Repair

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-30 · ✍️ Assaf Singer, Maroun Khriesh, Noam Rotstein +2 more

Dense 3D tracking from monocular video requires establishing point correspondences over time, estimating their depth, and inferring their trajectories during occlusion. Existing methods typically learn these tasks jointly, a demanding objective given the scarcity of 4D supervision. We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectorie...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42136v1)

---

### 10. A Better Critic Matters for Distribution Matching Distillation

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Zongze Wu, Xianbang Wang, Zhengyang Geng +5 more

Distribution Matching Distillation (DMD) trains a few-step student using the difference between a teacher's score and an online critic's estimate of the student distribution's score. We investigate what the critic needs, in capacity and in information, to provide a reliable training signal. On the capacity side, controlled experiments across seven SiT model sizes on ImageNet show that increasing t...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42135v1)

---

### 11. Instance-dependent sequential limits as an exact information ledger

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Akshay Balsubramani

Instance-dependent limits for bandit regret, sequential tests, best-arm identification and Markov decision processes are proved by one chain. It runs from a divergence decomposition through data processing to a statistic, a testing step that turns a class guarantee into a requirement on the history, and optimization over alternatives and allocations. Only the first step is an identity. This work w...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42133v1)

---

### 12. DecisionRank: On-Policy Distillation for Decision-Model Rerankers

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-30 · ✍️ Yanran Wu, Dian Yu, Chongyang Bai +10 more

Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses preferences through a ranked list of document ID sequences, while the student determines the ranking using scores from the first-token position. To bridge...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42128v1)

---

### 13. Physiological Trajectories and Observation Patterns in ICU Mortality Prediction: Transportability Under Changing Measurement Conditions

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Benjamin T. Pike

Objective: To distinguish the transferable predictive value of physiological trajectories from that of observation patterns in ICU mortality prediction, and to assess whether measurement timing affects performance independently of observation quantity.   Materials and Methods: In-hospital mortality was predicted at 48 hours using MIMIC-III, MIMIC-IV, and eICU. Nested representations progressively ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42126v1)

---

### 14. Gradient Descent on Two ReLU Neurons: Global Landscape and Bifurcation Dynamics

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Binghua Li, Mengzhe Li, Denny Wu +1 more

Understanding how gradient descent learns features remains a central challenge in neural network theory. We study this question in a minimal multi-index setting that already exhibits rich multi-phase gradient dynamics: a well-specified two-neuron ReLU teacher-student model under isotropic Gaussian inputs, trained by population gradient flow from small initialization. We show that the dynamics are ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42118v1)

---

### 15. Fast Privacy Loss Accounting for Random Allocation via Multiscale FFT

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-30 · ✍️ Vitaly Feldman, Moshe Shenfeld

In the random allocation sampling scheme each user's data is used in $k$ steps chosen randomly and uniformly from a sequence of $t$ steps. This scheme is known to improve on Poisson sampling in private optimization and in communication-efficient aggregation. The existing privacy loss distribution (PLD) accountant for this scheme runs in time quadratic in the inverse of the accuracy parameter $α$ (...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.42117v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
