# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-12 07:58 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-10 · ✍️ Emre Kutlusan, Yongmin Li

Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new cl...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14519v1)

---

### 2. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-10 · ✍️ Sheethal Bhat, Bogdan Georgescu, Awais Mansoor +3 more

DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14518v1)

---

### 3. TorchCurves: Differentiable Parametric Curves

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Alex Shtoff

We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. T...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14516v1)

---

### 4. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-10 · ✍️ Zijian Zhang, Rizhen Hu, Jiangweizhi Peng +4 more

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14515v1)

---

### 5. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Ziang Liu, James J. Kim, Yijia Dai +1 more

LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which rep...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14514v1)

---

### 6. Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Megha Srivastava, Michael H. Lim, Allison M. Keys +2 more

Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-b...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14511v1)

---

### 7. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Yeyuan Liu

Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring m...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14508v1)

---

### 8. Continual-ARC: Measuring Skill Acquisition over a Working Lifetime

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Daniel Lenton

Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14505v1)

---

### 9. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Adi Mashiach

Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-ligand sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabili...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14504v1)

---

### 10. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-10 · ✍️ Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón +3 more

Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visu...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14498v1)

---

### 11. RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-10 · ✍️ Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan +2 more

Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, without manual labels. Existing self-supervised methods either reconstruct sensor-specific pixel detail, align each image only with its co-registered twin, or rely on large transformers with 118-173M parame...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14496v1)

---

### 12. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Howard Zhang, Chuck Arvin, Logan Brown +3 more

Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two a...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14493v1)

---

### 13. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya +6 more

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14492v1)

---

### 14. TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-10 · ✍️ Peng Chen, Yihang Wang, Zhongwen Rao +6 more

Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1) Most TSFMs mainly rely on stacking Transformer layers to increase parameter size, lacking the ability to adaptively model complex time series patterns from multi-domain data. 2) Current TSFMs are pri...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14491v1)

---

### 15. Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-10 · ✍️ Muhan Gao, Hangxiao Zhu, Xinqi Su +3 more

Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the format of Twenty Questions to research ideation: given only the research problem of a published pap...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.14487v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
