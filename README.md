# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-09-05 05:17 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-03 · ✍️ Shravan Venkatraman, Wenshuai Zhao, Mohammad Hassan Vali +1 more

We introduce S$^3$T (Self-Supervised Self-Distillation over Time), which, to the best of our knowledge, is the first fully self-contained framework for continuous video state tracking. Our method treats temporal sampling density as privileged information, based on the hypothesis that a denser view of the same clip recovers the running state more accurately. This view serves as the teacher, while a...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04203v1)

---

### 2. TokenMatch: 3D Mesh Correspondence Transformer with Curvature-Guided Tokenisation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-03 · ✍️ Adeela Islam, Zorah Lähner, Vittorio Murino +1 more

While data-driven 3D shape correspondence estimation has recently seen substantial progress, robust matching under partial observations and strong non-isometric deformations remains challenging. Existing learning-based approaches often rely on hand-crafted descriptors or template-based representations, whereas recent generative models over functional maps suffer from high inference cost, limited i...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04202v1)

---

### 3. Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-03 · ✍️ Chin-Yang Lin, Yang-Che Sun, Cheng Sun +5 more

Online 3D reconstruction models perform poorly on long videos. This happens because regressing poses relative to a fixed first-frame anchor forces extrapolation far beyond the training distribution. Small drifts accumulate and amplify into significant geometric collapse. However, we observe that per-frame depth remains stable throughout this failure. The backbone's local geometry remains intact; o...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04201v1)

---

### 4. Principia: Relational Physics Tests for Video Models

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-03 · ✍️ Varun Varma Thozhiyoor, Shivam Tripathi, Venkatesh Babu Radhakrishnan +1 more

Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavailable in generated video. We propose a different approach. When two objects in the same scene obey the same physical law, their motions must satisfy predictable relationships, and these relationships ho...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04200v1)

---

### 5. Compile by Training: Turning Natural-Language Specifications into Local Neural Functions

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-03 · ✍️ Yuntian Deng, Pengyu Nie, Stuart Shieber

Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider. We present compile by training, which turns a natural-language specification into a reusable neural function. At compile time, teacher models generate task-specific examples that are used to tra...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04199v1)

---

### 6. Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-03 · ✍️ Haoyaun Zhu, Jie Zhang

Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow. We audited that assumption in two preregistered campaigns with every threshold fixed in advance; neither got past validating its instrument. Across 52,988...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04198v1)

---

### 7. ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-03 · ✍️ Lihao Liu, Peng Tang, Kunwar Yashraj Singh +1 more

Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate. We trace this to three deficiencies - incomplete error observation, limited search diversity, and unreliable selection - and propose ESPO (Error-Structured Prompt Optimization), which decomposes prompt optimization into three...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04197v1)

---

### 8. Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-03 · ✍️ Kang Liao, Yihang Luo, Xiao-Ming Wu +7 more

We propose Puffin-World, a unified multimodal architecture that integrates physical understanding, spatial simulation, and 3D world generation and reconstruction without relying on external offline modules. To reliably construct and interact with 3D worlds, our framework jointly models three native world states: physics (gravity field and latitude), geometry (depth), and appearance (image), togeth...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04196v1)

---

### 9. Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-03 · ✍️ Kevin Du, Alexander Hoyle, Laura Ruis +1 more

Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, evaluate faithfulness, and provide step-level supervision via process reward models and generative critics. These practices rely on the text of a reasoning step carrying information about its function...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04194v1)

---

### 10. One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-03 · ✍️ Adheesh Sunil Juvekar, Onkar Kishor Susladkar, Kiet A. Nguyen +6 more

Video editing spans diverse editing paradigms, yet achieving high-quality instruction-guided and subject-guided editing within a single unified framework remains challenging. We introduce EditVid, a training-free framework combining sparse causal memory for local coherence, correspondence-based post-attention token injection for long-range identity preservation, and soft latent blending for edit l...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04190v1)

---

### 11. Robust PAC Learning of Concurrent Stochastic Games

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-03 · ✍️ Angel Y. He, David Parker

We introduce the first Probably Approximately Correct (PAC) learning framework for general-sum concurrent stochastic games (CSGs) with transition uncertainty, while addressing the challenge of Nash equilibrium (NE) existence. Our algorithm maintains data-driven $L^1$ confidence sets over transition kernels and solves a robust CSG to compute a social-welfare optimal $\varepsilon$-NE, using a robust...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04189v1)

---

### 12. Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-03 · ✍️ Ye-Chan Kim, Seunghee Choi, SeungJu Cha +4 more

Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions lack visual grounding and are rigidly assigned to every inter-event gap at a fixed location and durati...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04183v1)

---

### 13. Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-03 · ✍️ Joseph Lee, Yidi Huang, Dokyoon Kim +2 more

Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary for acquisition and clarify that paraphrasing helps only at smaller batch sizes. Second, holding the...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04180v1)

---

### 14. A Computationally Feasible Framework for Causal Probabilistic Explanation

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-03 · ✍️ Rafal Urbaniak, Sam Witty, Daniel Waxman +7 more

Explaining why a specific outcome occurred, and which inputs deserve the blame or credit, is central to philosophical, scientific, and policy analysis. Existing tools split into two camps. The theory of actual causality (AC) gives principled verdicts, but only for toy-sized models, because computing them requires enumerating counterfactual scenarios. Scalable attribution methods like SHAP (or even...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04177v1)

---

### 15. Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-03 · ✍️ Denis M. Akola, David F. Fouhey

3D Foundation Models (3DFMs) such as VGGT have recently pushed the boundaries of 3D vision by predicting rich unified representations with feed-foward transformers. The scene representations learned by these models enable strong performance on multiple 3D vision tasks. In this paper, we investigate using their internal representations to infer 3D in the scene from new views. Our hypothesis is that...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.04174v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
