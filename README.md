# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-08-25 02:17 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. How to Train a Critic Stably and Efficiently

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-24 · ✍️ Penghui Qi, Xiangxin Zhou, Wee Sun Lee

Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop \textbf{Best-Practice Critic Optimization (BPCO)}, a recipe th...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23566v1)

---

### 2. ReWorld: An Interactive World Model with Long-Horizon Memory

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Zhifei Chen, Luozhou Wang, Guibao Shen +8 more

An interactive world model must follow the user's actions, remember the places it has shown, and stream in real time. The tension is structural: control wants a short horizon, memory wants an unbounded one. ReWorld separates the two during training and bounds them at inference. Mixed per-head attention windows confine most heads to the recent past while a small set of global heads attends over the...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23565v1)

---

### 3. SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Deyao Hong, Yizhe Chi, Wenyi Li +7 more

Modern software systems accumulate technical debt over decades of development, which makes migration expensive and largely manual. As coding agents become increasingly capable at bug fixing, can they autonomously perform such migrations? Existing benchmarks cannot answer this question because they evaluate only behavioural correctness, not whether the migration actually occurred. This leads an eas...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23564v1)

---

### 4. EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Md Thamed Bin Zaman Chowdhury, Moazzem Hossain

Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and the high cost of large-scale field inspections. To address this problem, we propose Expert-Grounded Distillation (EGD), a novel artificial intelligence framework that transfers institutional road safety...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23563v1)

---

### 5. Physics-Constrained Deep Learning Model for Contactless Blood Pressure Monitoring from Triaxial Bodyseismography

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Yuanyuan Zhang, Yida Zhang, Jiahui Li +6 more

Ballistocardiography (BCG) is promising for unobtrusive long-term blood pressure (BP) monitoring in laboratory settings, but traditional BCG signals are vulnerable to the variations in body-bed interaction with shifted fiducial points in temporal or amplitude axis, and BP varies with personal hemodynamic changes, causing misaligned representations that affect model generalizability and robustness....

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23562v1)

---

### 6. Provably adaptive sampling with uniform and remasking discrete diffusion models

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-24 · ✍️ Daniil Dmitriev, Zhihan Huang, Yuting Wei

Discrete diffusion models offer a promising alternative to autoregressive generation by enabling parallel updates, but their sampling efficiency can depend strongly on the choice of the forward process and the sampler. For the uniform forward process, existing lower bounds for the standard $τ$-leaping sampler scale linearly with the ambient dimension $d$, raising the question of whether this depen...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23554v1)

---

### 7. Prime Agent: A Self-Improving RLM Harness

![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-08-24 · ✍️ Seth Karten, Alex L. Zhang, Kevin Thomas +8 more

Language models are sequential processors, but long-horizon agency requires external information and computation beyond model weights and active context. Prime Agent is an open-source harness for long-horizon evaluation and coding-agent workflows. A persistent IPython REPL follows the Recursive Language Model abstraction for programmatic context processing and test-time compute, while Continual Ha...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23552v1)

---

### 8. ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-24 · ✍️ Na Li, Yuchen Jiao, Changxiao Cai +1 more

Recent advances in continuous diffusion and flow-based language models (LMs) have achieved performance competitive with discrete LMs. However, existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce \textbf{ConvergeFlow}, an embedding-...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23551v1)

---

### 9. FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-08-24 · ✍️ Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan

Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target views lie far from the input. Recent work mitigates these artifacts using diffusion-based generative priors, but is specialized to individual representations and require custom architectures or extensi...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23549v1)

---

### 10. Robustness of Anomaly Detection Models for Industrial Control Systems under Training-Time Data Contamination

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-24 · ✍️ Mustafa Umut Ozbek, Taiwo Ojo, Pooria Madani +2 more

Machine-learning-based anomaly detection is increasingly used in industrial control systems (ICS), yet most studies assume that detector training data is trustworthy. In practice, training data may be corrupted through compromised logs, labeling errors, manipulated historian records, or unsafe retraining processes. This paper evaluates the robustness of offline ICS anomaly-detection pipelines on t...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23547v1)

---

### 11. Inertial Manifold Neural Operator for Dissipative Time-Dependent Partial Differential Equations

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-24 · ✍️ Xiaoyang Xie, Clarence W. Rowley

In this paper, we introduce the Inertial Manifold Neural Operator (IMNO) for solving dissipative time-dependent partial differential equations (PDEs). The long-time dynamics of such systems often exhibit an effective low-dimensional structure due to dissipation. Unlike standard neural operator architectures such as the Fourier Neural Operator (FNO), IMNO explicitly leverages the low-dimensional st...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23546v1)

---

### 12. How AI Assistance Affects Human Skill Development: A Study of Learning with Logic Puzzles

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Shang Wu, Catarina G Belem, Shuyuan Fu +2 more

While AI assistance can improve human task performance in the short term, it may also undermine the development of skills in the longer term. We examine this tension in a controlled logic-puzzle experiment involving on-demand AI assistance, where participants complete tasks before, during, and after AI is available. By experimentally varying AI request costs, we find that lower-cost assistance ind...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23543v1)

---

### 13. The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Summer Eunhyung Ann, Haokun Liu, Chenhao Tan

Does multi-agent LLM interaction help or hurt? Some work reports gains from debate (Du et al., 2024), critique loops (Chen et al., 2025), and mixture-of-agents synthesis (Wang et al., 2025), while other work finds that interaction adds cost without improving quality under equal budgets (Tran & Kiela, 2026; Xu et al., 2026; Jarrett et al., 2025), or that independent sampling already captures multi-...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23541v1)

---

### 14. Interpretable AI with Local Distillation

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-08-24 · ✍️ Erin Craig, Yiling Huang, Snigdha Panigrahi

Modern AI models such as tabular foundation models and gradient-boosted ensembles can outpredict classical methods, but provide little basis for reasoning about their predictions. High-stakes decisions call for models that are both accurate and interpretable as built. Local linear modeling offers a path forward: a smooth regression function is locally well approximated by a linear one, allowing a ...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23538v1)

---

### 15. Adapter-Based Few-Shot Continual Learning for Malicious Packet Recognition

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-08-24 · ✍️ Kyle Stein, Guillermo Francia, III Eman El-Sheikh +1 more

The continual evolution of malware variants necessitates detection systems that can adapt to new threats without retraining from scratch. However, continually updating models on new data often leads to catastrophic forgetting, where previously learned knowledge is overwritten. While continual learning has been increasingly explored for malware detection, the specific setting of Few-Shot Class-Incr...

🔗 [Read on arXiv](http://arxiv.org/abs/2608.23536v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
