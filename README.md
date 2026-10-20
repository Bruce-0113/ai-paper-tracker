# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-20 05:41 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Text-to-Image Generative Modeling Without Language Pretraining

![LG](https://img.shields.io/badge/cs.LG-purple) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas +5 more

Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26863v1)

---

### 2. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Yu Zhou, Cheng-Fu Yang, Rui Sun +8 more

Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements o...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26860v1)

---

### 3. Can It Actually Work? Synthesizing Functional CAD Mechanisms

![CV](https://img.shields.io/badge/cs.CV-blue) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-19 · ✍️ Wenqian Zhang, Yangyi Huang, Zigeng Xu +2 more

While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mec...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26861v1)

---

### 4. Reinforcement Learning with Visually Attributable On-Policy Self-Distillation

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-19 · ✍️ Shiao Xie, Siyu Chen, Jianwei Lv +2 more

Multimodal reinforcement learning with verifiable rewards (RLVR) provides reliable task-level supervision, yet offers limited guidance for localizing errors in visual reasoning. On-policy self-distillation (OPSD) complements this supervision with dense token-level corrections from a privileged teacher equipped with an evidence-centered visual view. However, the resulting corrections may conflate v...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26856v1)

---

### 5. VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Token

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Sangbeom Lim, Seoung Wug Oh, Heeji Yoon +2 more

Diffusion-based video matting has recently emerged as a leading approach, leveraging video diffusion priors from internet-scale pretraining to achieve strong zero-shot generalization from limited synthetic data. However, the heavy compute of these diffusion backbones limits inference to a short chunk of just 6 to 24 frames, so even ordinary videos span multiple chunks. Because each chunk is matted...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26857v1)

---

### 6. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Tianqi Liu, Hanfei Zhao, Qifeng Liang +12 more

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, compr...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26855v1)

---

### 7. InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang +3 more

Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively simple 3D assets, while sophisticated photorealistic procedural systems require extensive manual development. Existing VLM-guided procedural methods remain ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26853v1)

---

### 8. CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-19 · ✍️ Zehao Wang, Jianpeng Yao, Yuping Wang +9 more

Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusions and out-of-distribution (OOD) scenarios, where individual robots may overlook potential risks or make inaccurate pred...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26852v1)

---

### 9. Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou +3 more

Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly into video generation models, which misinterpret the manga's structure and produce incorrect storylines. In this paper, we propose Manga2Animate, a multi-...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26851v1)

---

### 10. GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Xi Hu, Martin Bell, Liang Zheng

Text-to-image models have made tremendous progress and can produce high-quality images. However, a question which would be asked in any other discipline is where the frontier models fall short. We introduce GenOlympiad, a benchmark which provides the most challenging text prompts from nine capability axes for stress-testing frontier text-to-image models. The assessed capabilities include generatin...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26850v1)

---

### 11. Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-19 · ✍️ Zekai Li, Jiayi Yu, Jinlu Zhang +8 more

In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Improvement from failure. Different VLMs are evaluated on 18 manipulation tasks under a fixed interaction budget. The analys...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26848v1)

---

### 12. WeAct: Dynamic Weight Switching as Agent Actions

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-10-19 · ✍️ Rui Shi, Xunjian Yin, Jiacheng Sang +2 more

Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration thro...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26847v1)

---

### 13. Train An Imaginative Agent

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-19 · ✍️ Jiaxin Ge, Junyi Zhang, Tianning Chai +9 more

A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agentic Imagination (Agima), a training framework that trains an agent to imagine before acting, i.e. to be imaginative. Agim...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26845v1)

---

### 14. AnyGoal: On World Model Generalization Beyond Expert Rollouts

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-19 · ✍️ Heejeong Nam, Divyat Mahajan, Quentin Le Lidec +2 more

The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26844v1)

---

### 15. LatComm: Reusable Context Compression for Latent Communication between Large Language Models

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-19 · ✍️ Huawei Lin, Jinting Liu, Tan Yu +1 more

Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.26840v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
