# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-22 05:47 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Zhennan Wan, Jianfei Chen

Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30132v1)

---

### 2. Rethinking Video Autoencoders for Interactive World Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-21 · ✍️ Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour +2 more

Video world models predict future frames from past frames and actions. They serve as simulators in which agents train, plan or are evaluated, and that humans can control interactively. They generate in the latent space of a video autoencoder, whose compression sets their cost per frame and how long each action waits to take effect. Yet world models often reuse the autoencoders of text-to-video gen...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30129v1)

---

### 3. Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Zhanshuo Cao, Jiakai Tang, Yuqi Zhou +2 more

Existing sequential recommenders usually allocate a fixed computational budget to every item in a user's interaction history, regardless of the item's contribution to the final prediction. We challenge this de facto design with two diagnostic findings. (1) Non-uniform computational need: items within the same sequence vary drastically in how much computation they require. Most converge after shall...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30128v1)

---

### 4. VoxProg: 3D Spatial Reasoning through Voxel Programming

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-21 · ✍️ Zhichao Zhai, Menglei Zhao, Guikun Chen +4 more

Language models' abilities to interpret tasks and generate programs offer a promising basis for 3D spatial reasoning. Yet following spatial instructions in 3D scenes requires programs to construct geometric references that language leaves implicit. In this work, we introduce VoxProg, which formulates 3D object placement through voxel programming: a language model translates task interpretations in...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30127v1)

---

### 5. PhysiCalWorld: In-Context Physics Calibration for World Models

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-21 · ✍️ Yunhao Luo, Wentao He, Yinpei Dai +5 more

Existing world models typically perceive a scene through current visual frame or a narrow history window. However, these observations may not reveal the physics properties that determine transition dynamics, such as an object's mass distribution, joint damping, or surface friction. Without calibrating these physics factors for world models, predictions tend to regress toward an empirical prior and...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30125v1)

---

### 6. A Quasipolynomial Algorithm for $\ell_\infty$ Contractions

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Ashkan Soleymani, Gabriele Farina

We give an algorithm for computing an $\eps$-approximate fixed point of any $d$-dimensional nonexpansion with respect to the $\ell_\infty$ norm in time $\log(1/\eps)^{O(\log^2 d)}$. At its core, our method uses a boosting argument to geometrically shrink a search region. Among other consequences, our algorithm implies that simple stochastic games can be solved in quasipolynomial time....

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30122v1)

---

### 7. ALPS: Visual State Encoders for World Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-21 · ✍️ Yanqing Liu, Letian Zhang, Chengzhi Liu +5 more

World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment, and pixel reconstruction, so that a single representation can support prediction, instruction, and inspection. However, existing encoders typically specialize in only one or two of these capabilities; we therefore introdu...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30120v1)

---

### 8. Self-normalized Bernstein Inequalities for Regenerative Processes and Applications to Learning Without Independence

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Imon Banerjee, Pierre Alquier

We prove a self-normalized Bernstein inequality for bounded functions of a regenerative process with independent, identically distributed marked cycles of finite mean length. The bound uses observed cycle lengths and retains explicit terms for truncation and the cycle ending after the observation horizon. Selecting a tuning parameter from a finite deterministic collection gives a version of Bernst...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30119v1)

---

### 9. The role of locality and weight sharing in convolutional neural networks

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Francesco Mori, Melanie Weber

The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatial correlations of natural images, remain poorly understood. We address these questions in a teacher-student model with a convolutional teacher acting on $P$ input positions with correlation $c$ betwee...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30118v1)

---

### 10. Environment Duels: A Microcosm of LLM Co-Evolution

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-21 · ✍️ Shibo Jin, Zhiqiu Xu, Yiling Zou +2 more

Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each model play its role in this ecosystem, as a creator and as a solver? We introduce Environment Duels, a dynamic agentic benchmark that evaluates both capabilities on interactive environments. Each model...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30116v1)

---

### 11. The End of Consensus Research?

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-21 · ✍️ Clément Burgelin, Rachid Guerraoui, Zicong Hong +5 more

Consensus is a fundamental problem in distributed computing and at the core of state machine replication (SMR). Despite decades of active human research, discovering practical low-latency solutions to the problem is still open, as it requires combining protocol knowledge, correctness reasoning, implementation, and experimental evaluation. We report on how AI helped us discover A-greement, a new co...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30114v1)

---

### 12. Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-21 · ✍️ Houde Qian, Zheng Jiang, Wenyi Li +9 more

Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introdu...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30113v1)

---

### 13. Minimax Optimality of the NPMLE for Gaussian Mixtures in Hellinger Distance

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Shayan Hundrieser, Tudor Manole

We analyze the problem of estimating univariate Gaussian mixture densities using the nonparametric maximum likelihood estimator (NPMLE) based on $n$ independent and identically distributed samples. We show that the unconstrained NPMLE achieves the minimax optimal rate $\log(n)/n$ in squared Hellinger distance, when the true mixing measure is sub-Gaussian. In addition, we show that when the true mi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30109v1)

---

### 14. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-21 · ✍️ Yanzhe Chen, Ziyi Yang, Jifeng Zhu +14 more

Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisions from the resulting feedback. This rais...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30108v1)

---

### 15. Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-21 · ✍️ Yunpeng Mei, Xiaowen Zhu, Chenyu Wang +5 more

Flow matching trains a continuum of velocity regression problems but usually reports a loss averaged over interpolation time, obscuring which regions are limited by intrinsic ambiguity and which remain data-limited. We introduce the Velocity Ambiguity Profile (VAP), $\mathcal{A}_v(t)$, the time-local Bayes-risk floor of velocity prediction, and decompose time-resolved loss as $L_N(t)=\mathcal{A}_v...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.30107v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
