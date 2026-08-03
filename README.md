# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-08-03 04:29 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Toward Robust and 3D-Aware RGB-NIR Imaging in the Dark

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-31 · ✍️ Muyao Niu, Mingze Ma, Yifan Zhan +5 more

Robust low-light imaging remains challenging for the community. Recent studies have explored fusing Near-Infrared (NIR) with noisy RGB to achieve improved enhancement, yet most methods depend on carefully curated training data pairs, with limited robustness under different scenarios. This paper offers a new perspective for RGB-NIR low-light imaging by incorporating 3D-aware neural modeling. Withou...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29684v1)

---

### 2. Scaling Properties of Text Conditioning in Visual Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-31 · ✍️ Zilong Chen, Chaorui Deng, Kunchang Li +2 more

We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measur...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29679v1)

---

### 3. TokTier: Exact Stateful Tokenization for Agentic LLM Serving

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-31 · ✍️ Zhenyu Zhang, Zhichao Cao

LLM serving systems cache prompt KV state, yet most front ends still re-tokenize the full request text on every call. The cost lands on coding agents, which resubmit a long transcript after each small tool result, and reuse is hard because even a short append can change token boundaries near the end of the previous sequence. Across 153,951 calls from two agent ecosystems, the median call appends a...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29678v1)

---

### 4. ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-31 · ✍️ Boyang Zhang, Adrian Lyjak, Eli Stewart +2 more

Enterprise workflows increasingly rely on agents for \emph{schema-guided extraction}: given a document and a user-defined schema, the agent faithfully follows the schema to produce the correct output with source evidence as grounding metadata. We present ExtractBench, a benchmark for schema-guided extraction and, to our knowledge, the first to score value accuracy, record completeness at scale, gr...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29677v1)

---

### 5. Differentially Private Nonparametric Modal Learning with Applications to Regression and Clustering

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-31 · ✍️ Arkajyoti Bhattacharjee, Arnab Auddy

Density modes provide a localized and interpretable summary of multimodal distributions, but their estimation under rigorous differential privacy constraints remains largely unexplored. We study differentially private recovery of density modes for multivariate distributions under local smoothness, curvature, and separation conditions. We propose DP-GRAMS, a mean-shift inspired method that performs...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29675v1)

---

### 6. Sign compression for Muon: SignMuon, MuonSign, and the Limits of Error Feedback

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-31 · ✍️ Maria Smirnova, Alexey Kravatskiy

SignMuon compresses the Muon update to one bit per parameter by taking its elementwise sign, providing the most direct way to run a matrix-aware optimizer under an extremely low communication budget. It outperforms SignSGD in practice, yet it can ascend even on a linear function. Signing the gradient before the Linear Minimization Oracle (LMO), rather than after, does not repair this: we construct...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29674v1)

---

### 7. Freeze, Then Select: Structured Field Adapters and Stability-Validated Weak Selection for PDE Discovery from Sparse Observations

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-31 · ✍️ Juncheng Zhong, Chenghuang Shen, Jianfeng Liu +5 more

PDE discovery from sparse observations requires reconstructing a continuous field and selecting the correct differential terms. Our analysis of optimization paths in coupled neural PDE discovery reveals three behaviors: the exact support can persist to the end of training, appear only transiently, or fail to emerge. To decouple equation selection from neural optimization, we develop a freeze-then-...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29665v1)

---

### 8. GQ-FSL: Green Quantized Federated Split Learning

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-31 · ✍️ Idan Roth, Lutz Lampe

Deploying state-of-the-art deep neural networks (DNNs) at the wireless edge is severely bottlenecked by the strict energy and resource constraints of mobile devices. While federated split learning (FSL) mitigates on-device computation by offloading workloads to an edge server, this may introduce systemic overheads, while the continuous exchange of cut-layer data, and submodels still incurs signifi...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29659v1)

---

### 9. Development of FDD-ON: an Ontology for VAV HVAC System Fault Detection and Diagnostics

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-31 · ✍️ Yimin Chen, Brian Fricke, Bo Shen +10 more

Fault detection and diagnosis (FDD) technology is essential for improving HVAC system reliability, energy efficiency, and maintenance effectiveness. However, effective deployment of FDD solutions in buildings requires structured domain knowledge that can bridge heterogeneous data sources, diverse equipment types, and varied diagnostic outputs. Limited data interpretability and interoperability wit...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29657v1)

---

### 10. Evolving language compositionality in a frequency-structured meaning space

![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-31 · ✍️ Fabio De Ponte, Eloise Gaines-White, Conor Houghton +1 more

The iterated learning model was introduced to investigate language evolution: the way in which the characteristic properties of human languages have been shaped, at least partly, by repeated transmission from one language user to another. The key finding is that language compositionality can arise spontaneously as a consequence of language being passed repeatedly through a language learning bottle...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29642v1)

---

### 11. HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual Question Answering

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-31 · ✍️ Rongjian Gu, Wengang Zhou, Junyu Xiong +4 more

Multi-page document visual question answering requires locating sparse evidence at both the page and region levels. Existing approaches typically emphasize one level over the other: page-centric methods focus on page acquisition, with region operations serving mainly as navigation aids, whereas region-centric methods assume that the relevant pages have already been supplied. Consequently, page and...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29638v1)

---

### 12. CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-31 · ✍️ Wenxin Tang, Jingyu Xiao, Zhenyu Liu +6 more

Rendering source code as images offers a promising way to reduce the input costs of Multimodal Large Language Models (MLLMs). Adjusting image resolution can trade visual token cost against content fidelity. However, resolution scaling alone overlooks two sources of inefficiency: blank regions created by line breaks and indentation, and code regions irrelevant to the current instruction. Moreover, ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29637v1)

---

### 13. OASIS: Occlusion-aware Single-image Hand Avatar Reconstruction via 3D Gaussian Splatting

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-31 · ✍️ Zhisheng Han, Shiyao Wu, Jiayan Qiu +6 more

Single-image 3D hand avatar reconstruction is fundamentally ill-posed and particularly challenging due to limited visual evidence under severe self-occlusion and the complex pose-dependent deformation of highly articulated hands. Existing methods predominantly rely on implicit NeRF-style representations, whose volumetric fitting is computationally expensive and often struggles to preserve fine-gra...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29633v1)

---

### 14. FlexComposer: Unified Video Compositing from Images to Dynamic Footage with Flexible Trajectory Control

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-31 · ✍️ Songchun Zhang, Sitong Guo, Xianghao Kong +4 more

Generative video compositing, which involves inserting external assets seamlessly into existing video sequences, is essential for content creation and visual effects. However, existing approaches suffer from a control-fidelity trade-off: they either hallucinate motion from static images, failing to preserve the dynamics of pre-animated assets, or lack fine-grained spatial control for precise asset...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29627v1)

---

### 15. AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-31 · ✍️ Tianyu Huai, Tingshuo Fan, Xinchi Chen +5 more

As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter dec...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.29626v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
