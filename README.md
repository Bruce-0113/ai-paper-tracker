# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-08-05 04:09 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

![CV](https://img.shields.io/badge/cs.CV-blue) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Yang Yang, Qinyu Zhao, Mouxiang Chen +5 more

Existing scaling strategies for Multimodal Large Language Models (MLLMs) typically expand either model parameters or sequential inference computation, incurring substantial memory or latency overhead. More importantly, most existing methods fail to alter the rigid, fixed computation allocation between the Vision Transformer and the Large Language Model components, limiting task-specific optimizati...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.04010v1)

---

### 2. SocietyBench: Forecasting Counterfactual Social-World Evolution

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Zhenran Wang, Zhonghan Bian, Jinsong Li +1 more

Large language models (LLMs), and the agents built on top of them, are now benchmarked heavily on whether they can finish a task -- fix a bug, drive a browser, operate a GUI. A complementary social ability, namely how well a model understands and forecasts the way real social events unfold, has barely been measured. We introduce SocietyBench, an end-to-end benchmark that takes a one-line event top...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.04009v1)

---

### 3. WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Zhenran Wang, Zhonghan Bian, Jinsong Li +1 more

Benchmarks that measure the forecasting ability of large language models are almost always retrospective: the event has happened, the answer is somewhere on the Web, and the evaluation must defend itself against memorisation. We report the opposite design. Over the 39 days of the 2026 FIFA World Cup, six frontier LLMs -- all with extended thinking and native server-side web search -- were asked be...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.04008v1)

---

### 4. TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-04 · ✍️ Changle Qu, Sunhao Dai, Hengyi Cai +4 more

Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions. However, existing reinforcement learning methods often rely on trajectory-level supervision, limiting fine-grained credit assignment in long-horizon TIR scenarios. On-policy self-distillation offers denser signals through teacher branches with privileged context, but existing approaches typical...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.04007v1)

---

### 5. PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Shuhan Xue, Zixin Ding, Yichen Shen +6 more

Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.04003v1)

---

### 6. Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-04 · ✍️ Mohsen Hariri, Weicong Chen, Nahal Shahini +11 more

Large language models can solve substantially harder reasoning problems with more inference-time compute. The term "test-time scaling," however, now covers diverse inference algorithms that extend deliberation along a single trajectory, sample completed candidates and aggregate them through voting or verification, or search over unfinished partial states. These algorithms differ in their statistic...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.04001v1)

---

### 7. Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Junhao Chen, Mingjin Chen, Jingjia Mao +12 more

Text-to-music language models begin with a choice usually made by default: how to tokenize music. Normally entangled with backbone, data, and recipe, its effect has never been measured in isolation. We fix pretrained Qwen3.5 (0.8B-27B), data, budget, and decoding, and swap only the representation across seven tokenizations, anchoring texture metrics to each representation's model-free ceiling. The...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03999v1)

---

### 8. When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Christopher Schröder, Lukas Gienapp, Ferdinand Schlatt +2 more

We identify a previously overlooked failure mode of ALiBi positional encoding: its linear bias scaling underflows floating-point precision, which zeroes out a large fraction of attention weights and renders the affected attention heads partially blind. We analyze this failure mode, characterize its impact, and examine four mitigation strategies. We further demonstrate its occurrence in state-of-th...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03994v1)

---

### 9. Perceptual Anchoring: Prototype-Guided Text Calibration for Training-free Open-Vocabulary Semantic Segmentation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-04 · ✍️ Wanli Ma, Jiangwen Lu, Qinmu Peng +1 more

Training-free open-vocabulary semantic segmentation (OVSS) partitions an image into semantically distinct regions based on arbitrary text descriptions, without learning any additional parameters. However, existing methods typically focus on improving visual representations while treating text embeddings that encode only generic category concepts as fixed classification references. The resulting se...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03991v1)

---

### 10. Assessment of Conditional Diffusion Model for Synthetic Histopathology Image Generation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-04 · ✍️ Seyed Kahaki, Shijie Li, Weijie Chen +1 more

Synthetic histopathology image generation has emerged as an approach that may address data scarcity in computational pathology, yet current evaluation methodologies may not fully assess synthetic data quality for medical applications. This work investigates and addresses limitations in existing evaluation metrics, investigating an approach for assessing synthetic histopathology image quality throu...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03990v1)

---

### 11. string2string Studio: An Interactive, In-Browser Platform for String-to-String Algorithms

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-04 · ✍️ Mirac Suzgun, James Zou, Stuart M. Shieber +1 more

We present string2string Studio, an interactive in-browser platform for string-to-string analysis across natural language processing, computational biology, and the digital humanities. The system integrates six main modules (alignment, distance, similarity, search, generation metrics, and BLAST homology search), operating at character, word, token, line, and residue levels. Its C++-based algorithm...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03984v1)

---

### 12. Can Large Language Models Recover Semantic Optimization Opportunities That Compilers Miss?

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-04 · ✍️ Hailong Jiang, Feng Yu, Emran Hossain +4 more

Optimizing compilers miss profitable transformations when their enabling semantics are absent from the analyzed program representation. We ask whether large language models (LLMs) can recover such semantics from heterogeneous C/C++ context and realize them as validated, contract-preserving artifacts. We introduce SeGaBench, an executable benchmark containing 100 synthetic and 20 source-backed case...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03983v1)

---

### 13. Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-04 · ✍️ Zhen Fang, Yu Zeng, Wenxuan Huang +17 more

We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03979v1)

---

### 14. JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-04 · ✍️ Yicheng Xiao, Wenxun Dai, Xinran Qin +22 more

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive a...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03974v1)

---

### 15. ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct Reasoning

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-04 · ✍️ Jinhe Bi, Chennan Zhou, Zengjie Jin +10 more

On-policy training has emerged as a powerful post-training paradigm for improving the reasoning capabilities of large language models, and is often enhanced by golden trajectories from stronger expert models. However, when the expert fails on harder problems, existing trajectory-guided methods lose their main source of supervision, and these failed trajectories are typically discarded as negative ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.03972v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
