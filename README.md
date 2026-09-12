# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-09-12 05:26 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. SenseNova-U1.5: Towards Native Unified Visual Intelligence

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-10 · ✍️ Haiwen Diao, Jiahao Wang, Chenjing Ding +62 more

We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11929v1)

---

### 2. GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-10 · ✍️ Boning Li, Longbo Huang

Counterfactual regret minimization (CFR) is one of the few large numerical workloads that still runs faster on CPUs than on GPUs. Each iteration sweeps a game tree with up to billions of states in millions of small, interdependent gather and scatter steps issued through a generic tree interface. On a GPU every kernel finishes in microseconds, so kernel launches and framework dispatch dominate the ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11923v1)

---

### 3. General Quantification of Covariate and Concept Shifts

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-10 · ✍️ Hongbo Chen, Li Charlie Xia

Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from samples. In this paper, we bridge the gap between theory and practical applications. We first show that existing definition of concept shift breaks when the source and target supports mismatch. Leveraging ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11918v1)

---

### 4. Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-10 · ✍️ Atindra Jha, Margaret Li, Jure Leskovec +2 more

As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetit...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11917v1)

---

### 5. Can Edge-Deployable Vision-Language Models Identify Species?

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-10 · ✍️ William Zhou, Mayukha Siripuram, Xiao Yan +2 more

Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relevant class to evaluate for species identification. We test whether models in this deployment-relevant 2--8B range carry genuine taxonomic knowledge, evaluating four such VLMs (Qwen3-VL 2B/4B/8B, Gemma3...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11916v1)

---

### 6. Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-10 · ✍️ Masahiro Kato, Daiki Honma, Taka Kato

Generative artificial intelligence changes how firms reach customers, but standard marketing data do not record how often users see and notice a firm's name in generated answers. We develop Generative Marketing Mix Modeling (GMMM) to estimate the causal effects of Generative Engine Optimization (GEO) and Generative Engine Marketing (GEM). For GEO, GMMM combines repeated generated answers with ques...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11915v1)

---

### 7. Distance generalization in transformers: why bother with positional encoding?

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-10 · ✍️ Daniel Henrik Nevermann, Claudius Gros

Out-of-distribution length generalization, namely to extrapolate a task from short to longer context, has been studied intensively for transformers. Here we focus on distance generalization, which probes performance when inter-token distances are changed between training and inference, while keeping a fixed context length. We construct two synthetic delay copy tasks, both involving finite distance...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11913v1)

---

### 8. Artificial Id: Drive and Persistent Alignment in Agentic AI

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-10 · ✍️ Yakov Pyotr Shkolnikov

Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current harnesses largely solve by hand: objectives, retries, verification, stopping rules and other behavioral transitions are specified externally. We propose an artificial id, an adaptive internal drive fo...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11911v1)

---

### 9. From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-10 · ✍️ Nitesh V. Chawla, Paulo Benanti

Artificial Intelligence does more than create a governance problem. It can also reveal where institutions have already failed to provide responsiveness, belonging, care, and accountability. Once deployed, AI becomes an intervention in those conditions. It can repair, compound, substitute for, or conceal the failures it encounters. Responsible AI must therefore evaluate both the system and the inst...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11910v1)

---

### 10. TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-10 · ✍️ Akshaj Gupta, Hwi Joo Park, Andrea Guzman +5 more

Automatic Music Transcription (AMT) for guitar remains limited by three challenges: existing systems often fail to capture expressive techniques such as slides, bends, and percussive hits; they often assign notes to incorrect string-fret combinations; and they are typically trained on clean recordings, limiting their generalization to noisy real-world audio. To address these challenges, we propose...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11904v1)

---

### 11. MindTopo: Can Foundation Models Reason in Topological Space?

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-10 · ✍️ Yunfei Ge, Anbang Liu, Qineng Wang +9 more

Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topolo...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11900v1)

---

### 12. Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-10 · ✍️ Weitong Cai, Hang Zhang, Yukai Huang +6 more

Long-video understanding on edge devices must reason over hours of content under tight compute and bandwidth budgets. Subsampling visual tokens loses temporal structure, while text-only video memories lose fine-grained visual attributes. We observe a visual-textual duality: language memories carry long-range temporal structure better than dense frames, while pixels remain decisive for attribute-le...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11899v1)

---

### 13. CausalArena: Benchmarking Causal Discovery in the Foundation Model Era

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-10 · ✍️ Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang +1 more

Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal models (SCMs), which specify a causal graph together with the mechanisms that generate data, yet existing studies differ substantially in graph families, mechanisms, and evaluation protocols. The emergence...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11897v1)

---

### 14. 3D Point Splatting for mmWave Radar Novel View Synthesis

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-10 · ✍️ Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar

Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11894v1)

---

### 15. Nuha-Speech: Building General-Purpose Arabic Speech-LLMs

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-10 · ✍️ Yingzhi Wang, Reem Alhazzani, Muhammad Alqurishi

As Speech Large Language Models (speech-LLMs) become increasingly multilingual, Arabic remains significantly underrepresented, highlighting the need for dedicated infrastructure to train and evaluate Arabic speech-LLMs.   To address this gap, we introduce Nuha-Speech, a comprehensive initiative to develop general-purpose Arabic speech-LLMs spanning dataset construction, model training, and systema...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.11892v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
