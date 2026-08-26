# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-08-26 02:24 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-25 · ✍️ Sixiang Chen, Jiaming Liu, Jixian Wu +7 more

Action-conditioned world models are increasingly used as learned simulators for policy evaluation and improvement, yet their effectiveness rests on an unverified assumption: generated futures faithfully reflect arbitrary valid actions. Existing benchmarks are typically confined to expert demonstrations, leaving off-expert action following inadequately evaluated. To address this gap, we introduce W...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24885v1)

---

### 2. What FID Hides: Detecting, Ranking, and Diagnosing Deviations in Generative Evaluation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-25 · ✍️ Hao Chen

Generative models are commonly ranked by Fréchet Inception Distance (FID) and Kernel Inception Distance (KID), yet FID's first-two-moment summary can miss distributional differences, and a reported scalar gap alone is not a calibrated test against sampling variation. FID's moment restriction has concrete consequences: on ImageNet, visually unrecognizable images optimized only to match the referenc...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24881v1)

---

### 3. From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-25 · ✍️ Jiangning Zhang, Haojun Chen, Yong Liu

Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, audition, motion, and hand-object interaction, but must operate under tight energy, thermal, privacy, and feedback constraints. Despite rapid progress in a...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24877v1)

---

### 4. Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-25 · ✍️ Zhaochen Yu, Yingcheng Wu, Zhenfei Yin +5 more

Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Working Memory architecture for long-horizon agent harnesses, in which Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather th...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24876v1)

---

### 5. SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-25 · ✍️ Kai Ruan, Jinghao Lin, Qianshan Wei +2 more

Group-relative reinforcement learning waits for sibling rollouts of the same prompt, which is costly for long and variable tool-use trajectories. Single-stream Policy Optimization (SPO) removes this dependency with a persistent prompt-level value estimate, but its recipe whitens one advantage per trajectory before optimizing a token-mean actor loss. We show that trajectory centering generally does...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24870v1)

---

### 6. Parameterized Complexity of $L_p$-Lipschitz Constants for Input Convex Neural Networks and $L_p$-Norm Maximization over Zonotopes

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-25 · ✍️ Aritra Das, Vincent Froese, Moritz Grillo +6 more

Lipschitz constants are a standard way to quantify the sensitivity of neural networks to small input perturbations, but computing them is difficult even for shallow ReLU networks. We study this problem for two-layer input-convex neural networks (ICNNs), a restricted architecture where nonnegative output weights enforce convexity. Computing the $L_p$-Lipschitz constant for these networks is equival...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24865v1)

---

### 7. Improving Cross-Problem Vehicle Routing with Locally Augmented Preferences and Representation Disentanglement

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-25 · ✍️ Arthur Corrêa, Paulo Nascimento, Samuel Moniz

Multi-task vehicle routing problem (VRP) solvers seek to handle multiple VRP variants within a single unified model, avoiding the need to train a separate model for every variant. In spite of recent progress, current approaches remain limited on two fronts. On the training side, reinforcement learning suffers from reward-scale disparities and shrinking advantage signals as policies improve, wherea...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24859v1)

---

### 8. Bellman Calibration for Marginalized Importance Weighting in Offline Reinforcement Learning

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-25 · ✍️ Lars van der Laan, Nathan Kallus

Marginalized importance weighting evaluates a target policy by reweighting offline state-action samples with its discounted occupancy ratio, characterized by an adjoint Bellman equation. Existing minimax, primal-dual, and fitted fixed-point estimators can leave residual occupancy-balance violations because of function-class approximation, regularization, or incomplete optimization. These violation...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24858v1)

---

### 9. LeFlow: Generative Latent Flow Planning for World Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-25 · ✍️ Hsiang-Wei Huang, Jianxu Shangguan, Junbin Lu +1 more

Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every state-goal pair, an iterative optimizer is run from scratch to search for optimal action sequences, treating the world model as a black-box simulator. This approach pays the full iterative optimizati...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24855v1)

---

### 10. BrowserForge: Scaling Web Episode via Parallel Browser Sandboxes

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-25 · ✍️ Fei Tang, Huawen Shen, Zhiqiong Lu +7 more

Web agents that act from rendered pixels avoid the fragility and heavy token cost of reading a page's HTML or accessibility tree, but training them depends on large amounts of high-quality interaction trajectories, and how to produce such data at scale remains an open problem. Public datasets typically contain only a few thousand trajectories drawn from a fixed and narrow set of websites, and even...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24848v1)

---

### 11. FedV-KGQA: Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-25 · ✍️ Md Saikat Islam Khan Bappy, Oshani Seneviratne

Real-world data for knowledge graph question answering is often distributed across different organizations due to governance and data sovereignty constraints. While centralized systems exist, they cannot answer multi-hop questions when the required facts are split across vertically partitioned silos. In this paper, we propose FedV-KGQA, a framework for multi-hop reasoning over knowledge graphs in ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24846v1)

---

### 12. LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-25 · ✍️ Andreas Hochlehnert, Marianna Nezhurina, Mehdi Cherti +9 more

We present LAION-BVD, a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific video URLs collected from CommonCrawl. From these, we download 80M videos with a total duration of 10 million hours. The dataset is designed for multimodal pre-training across the video, audio, and image modalities. Using content-aware scene detection, we extract clips for which we...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24845v1)

---

### 13. Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-25 · ✍️ Miao Liu, Zhizhe Liu

Large language models (LLMs) are increasingly deployed as AI analysts to process financial disclosures and support AI-assisted investment decisions. Yet such systems are usually evaluated by what they can retrieve, not whether retrieved information affects their judgments. We identify a retrieval-integration gap in long-context financial analysis. Holding focal-firm information fixed and varying o...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24842v1)

---

### 14. A Dual-Dimensional LLM Framework for Automated Item Incidental Content Similarity Analysis in Large-Scale Assessments

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-25 · ✍️ Jing Huang, Jihong Zhang, Hua-Hua Chang

The rapid expansion of large-scale assessments and the growing adoption of automatic item generation have intensified concerns about incidental content redundancy, where construct-irrelevant elements such as wording or contextual framing become unintentionally repetitive across items. Traditional similarity metrics like BLEU or cosine similarity, often fail to capture the nuanced structural and se...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24825v1)

---

### 15. Constrained Entity Selection under Partial Knowledge for LLM-Based Knowledge Graph QA

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-25 · ✍️ Emanuel Kitzelmann

Large language models are increasingly used for knowledge graph question answering (KGQA), but can fail to correctly ground answers in the underlying graph. Current approaches to LLM-based KGQA either rely on full semantic parsing into executable queries such as SPARQL, which is brittle in practice due to complex schemas or incompleteness of real-world KGs, or on LLM-reasoning and answer generatio...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.24824v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
