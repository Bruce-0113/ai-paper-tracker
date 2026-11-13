# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-13 07:37 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Back to Pixels: Lifting Latent Video Diffusion into Pixel Space

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-12 · ✍️ Yanke Song, Shuo Chen, Chris Rockwell +9 more

Frontier video generation models work in a VAE latent space that compresses video in both space and time. This compression made training tractable, but now limits high-resolution, controllable, and interactive generation -- doubling resolution quadruples token count, conditions apply to groups of frames rather than individual ones, and each response must wait for the rest of its multi-frame block....

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17336v1)

---

### 2. Unbundling Multimodal Vision Encoding

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-12 · ✍️ Ellis Brown, Chris Hoang, Shengyi Qian +9 more

How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e....

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17334v1)

---

### 3. TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-12 · ✍️ Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe +6 more

Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a ligh...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17331v1)

---

### 4. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-12 · ✍️ Jie Wang, Tong Zhu, JiaHao Kuang +8 more

Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17332v1)

---

### 5. ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-12 · ✍️ Guangyuan Sui, Yunzhong Hou, Chi Harold Liu

Vision language navigation (VLN) is very challenging for Unmanned Aerial Vehicles (UAVs) since small errors in 3D motion prediction can lead to navigation errors and collisions. Unable to fathom execution outcomes in 3D environments, existing methods often struggle to predict accurate navigation waypoints from language instructions. To solve this, we introduce the Prototypical Visual Imagination f...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17330v1)

---

### 6. Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-12 · ✍️ Zeynep Yıldız, Satchit Chatterji, Ercan Atam +1 more

Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gr...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17329v1)

---

### 7. K2V: Generative Keyframing For Physically Plausible Video Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-12 · ✍️ Felix O'Mahony, Daniel Olmeda Reino, Roberto Cipolla +1 more

Video diffusion models are able to generate samples with high-quality appearance and textural qualities. However, content produced by these methods is known to exhibit significant physical errors. This is because, in a classical video generation setting, all physical reasoning must take place simultaneously and exclusively within the diffusion process.We propose to resolve these issues by redistri...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17324v1)

---

### 8. AgentSSL: Can MLE Agents Leverage Unlabeled Data?

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-12 · ✍️ Ethan Lin, Akanksha Sarkar, Ziang Liu +2 more

Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we i...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17323v1)

---

### 9. BrickFlow: Connectivity-Guided Brick Reconstruction

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-12 · ✍️ Peter Kulits, Cordelia Schmid

Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires satisfying discrete physical constraints, which provide structure but render the problem combinatorial and highly sensitive to small pose errors. To learn a prior over how parts fit together, we train a s...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17321v1)

---

### 10. Learning When Diffusion Language Models Should Regenerate

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-12 · ✍️ Minhae Oh, Jeonghye Kim, Jinwoo Koo +4 more

Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces it when the surrounding context remains fixed. These findings motivate DiVR , a ve...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17320v1)

---

### 11. Spatial Foundry: A Multimodal Dataset for Spatial Intelligence

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-12 · ✍️ Ethan Lin, Yang Song

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configuratio...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17318v1)

---

### 12. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-12 · ✍️ Peiwen Li, Harshit Verma, Sophia Zhou +6 more

Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem)...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17316v1)

---

### 13. Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-12 · ✍️ Abigail L. Tenenbaum, R. Thomas McCoy

Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes a network to many related functions to facilitate its subsequent learning of similar functions. Pri...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17314v1)

---

### 14. Sketching Language Models for Context Attribution

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-12 · ✍️ Christopher Liaw, Aranyak Mehta, Grigoris Velegkas +1 more

Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17313v1)

---

### 15. Classical Energies Learn to Reason 1,000x Faster than Looped Models

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-12 · ✍️ Benjamin Hoover, Hugh Blayney, James C. R. Whittington

Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues but also offers advantages: built-in early stopping, compute that adapts to problem d...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.17309v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
