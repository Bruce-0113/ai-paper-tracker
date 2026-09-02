# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-09-02 05:28 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-01 · ✍️ Penghao Wu, Haiwen Diao, Weichen Fan +3 more

While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretra...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01607v1)

---

### 2. Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-01 · ✍️ Himil Vasava, Ming Jiang

LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline t...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01604v1)

---

### 3. Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-01 · ✍️ Kefeng Duan, Dewu Zheng, Yanlin Wang +7 more

Evaluating software engineering agents on realistic benchmarks is costly, since each task may require multi-step code exploration, modification, and test execution. Existing efficient evaluation methods select representative subsets to estimate full-benchmark performance, but are largely result-only: they fit historical pass/fail response matrices or static task semantics, discarding how agents so...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01603v1)

---

### 4. Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-01 · ✍️ Kefeng Duan, Dewu Zheng, Yanlin Wang +8 more

The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context. Since real-world repositories often exceed the input length limits of LLMs, existing approaches commonly adopt retrieval-augmented generation (RAG) to provide repository-specific context. Despite improving repository-context retrieval,...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01601v1)

---

### 5. CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-01 · ✍️ Damien Sileo, Dimitri Kachler

Dynamic agent harnesses let language models change the software that shapes their own execution. This flexibility brings a new reasoning burden: a local plugin change can propagate through dependencies and cleanup. We introduce CordisBench, a 1,200-question benchmark of this lifecycle reasoning. It combines a controlled formal setting with programs executed against Cordis, a runtime that manages c...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01600v1)

---

### 6. UI-VISA: U-Net Initialized Vascular Image Segmentation Architecture

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-01 · ✍️ Asees Kaur, Suzanne S. Sindi, Erica M. Rutter

Accurate segmentation of vascular structures in digital subtraction angiography (DSA) images remains challenging due to the thin, elongated, and branching nature of blood vessels. Pixel-wise deep learning approaches such as U-Net achieve strong general-purpose segmentation performance but often produce fragmented or discontinuous predictions in fine vascular regions, since they do not explicitly e...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01598v1)

---

### 7. The Rise of Verbal Reinforcement Learning

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-01 · ✍️ Kshitij Tayal, Arun Sharma, Genta Indra Winata +2 more

Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01597v1)

---

### 8. Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-09-01 · ✍️ Haoyuan Deng, Haichao Liu, Wenkai Guo +6 more

Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning (RL) post-training around a joint action-wrench proposal: a causal...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01596v1)

---

### 9. Mechanism Design for Alignment and Control

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-09-01 · ✍️ Dirk Bergemann, Andrew Koh, Stephen Morris

We develop a framework for mechanism design with AI agents whose alignment (preferences) and capabilities (feasible actions and information) are unknown. We want such agents to act on our behalf so mechanisms must incentivize both honesty and obedience. A one-sided imitation structure---capabilities can be concealed but not counterfeited---yields a revelation principle, a characterization of imple...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01595v1)

---

### 10. StudentSim: Training LLM-based Student Simulators

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-01 · ✍️ Ke Yang, Chenglong Wang, Michel Galley +4 more

AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to collect from real learners. Student simulators can provide this signal as a proxy, yet existing approaches are limited: state-tracking models fit student behavior but struggle to process explanations or c...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01591v1)

---

### 11. Designing Proactive Thought Partners for Writing

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-01 · ✍️ Chao Zhang, Abe Davis, Chih-Wei Chen +1 more

Writing involves diverse cognitive activities, from ideation to revision, and writers' needs vary across individuals and moments. Proactive AI promises to provide the right support at the right time, yet existing proactive tools largely focus on generic textual assistance, such as autocomplete. This paper studies the design space of proactive thought partners: AI agents that proactively offer cust...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01588v1)

---

### 12. The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-01 · ✍️ Jundong Hu, Shekar Ramachandran

Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization damage occurs and how to allocate a small additional precision budget. Using causal mixed-precision intervention as ground truth (raise each layer to 8-bit in turn and measure the accuracy it recovers) ...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01587v1)

---

### 13. A Benchmark for Vehicle Attribute Classification in Cross-Domain Surveillance Scenarios

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-01 · ✍️ Sergio M. Silva, Otavio T. Remer, Gabriel E. Lima +3 more

Vehicle attribute analysis is a key component of Intelligent Transportation Systems (ITS), supporting applications such as vehicle identification, traffic monitoring, and forensic investigation. However, models trained under controlled conditions often degrade in real surveillance scenarios due to changes in viewpoint, occlusion, illumination, and sensor characteristics. This paper introduces Unco...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01584v1)

---

### 14. SpatialGuard: Harness-Guided Verifiable Spatial Reasoning for Text-to-Image Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-09-01 · ✍️ Ziyun Qian, Zizhi Chen, Yizhou Liu +3 more

Complex 3D spatial text to image generation requires models to convert natural language into stable visual geometry, not merely semantic appearance. Existing prompt-driven or layout-conditioned methods improve controllability, but often lack an optimizable and verifiable spatial intermediary before visual sampling. As a result, object relations, occlusion, visibility, and camera constraints can de...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01582v1)

---

### 15. Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-09-01 · ✍️ Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin +3 more

Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VL...

🔗 [Read on arXiv](http://arxiv.org/abs/2609.01575v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
