# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-07-20 04:35 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-17 · ✍️ Like Liu, Zhengzheng Xu, Haitao He +3 more

Multimodal large language models have achieved strong performance across diverse vision-language tasks, yet their capabilities in UAV scenarios remain insufficiently explored. Recent UAV-oriented benchmarks have begun to evaluate MLLMs in aerial scenarios, but they typically focus on scene understanding, event recognition, or navigation completion, rather than jointly assessing the dual-cognition ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16193v1)

---

### 2. MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-17 · ✍️ Homanga Bharadhwaj, Yash Jangir

Humans can infer how objects are likely to move from passive observation: a cup may be lifted, a drawer may slide, and a lid may rotate shut. Such predictions expose the physical consequences of interaction needed to act in the real world. We study how to learn this anticipation from ordinary monocular videos of human-object interaction. Given a short observed video context, MotionForesight predic...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16192v1)

---

### 3. FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-17 · ✍️ Hao Liu, Chenghuan Huang, Ye Huang +7 more

Video Diffusion Transformers process long spatio-temporal sequences, making self-attention the main bottleneck in high-resolution video generation. Training-free sparse attention reduces this cost, but adaptive Top-$p$ routing creates uneven per-head workloads under multi-GPU sequence parallelism. The resulting workload heterogeneity turns sparse attention into a rank-level straggler problem. We p...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16190v1)

---

### 4. Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-17 · ✍️ Ce Zhang, Ziyang Wang, Yulu Pan +6 more

Grounded long-video question answering (Grounded LVQA) requires answering a question about a long video while localizing the short evidence interval that supports the answer. Recent agentic methods frame this task as multi-turn exploration with a single crop_video(start, end) action, which supports coarse-to-fine narrowing but provides no primitive for fine-to-coarse backtracking. As a result, the...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16189v1)

---

### 5. PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-17 · ✍️ Yuchen Yang, Yifan Zhao, Anisha Dasgupta +1 more

Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy. However, in KV-cache-intensive serving scenarios, MoEs often exhibit a tension between the GPU memory requirements of the model weights and the growing KV cache. We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at ru...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16184v1)

---

### 6. A Blueprint for Equilibrium-Based Differentiable Continuous-Variable Thermodynamic Computing

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-17 · ✍️ Owen Lockwood, Jérémy Béjanin, Joost Bus +4 more

To address the escalating energy and latency demands of machine-learning workloads, we introduce a blueprint for an energy-efficient and fast thermodynamic computing stack that leverages stochastic analog processes in physical hardware. In this work, we focus on energy-based thermodynamic computing where the stochastic process is well described by Langevin dynamics with tunable energy potentials. ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16183v1)

---

### 7. Vision-Language Assistant for Emotional Reactions to Risky Driving

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-17 · ✍️ Harine Choi, Eun Hak Lee, Zhengzhong Tu

This study introduces a vision-language pipeline that detects risky driving behaviors and generates emotionally expressive responses to support driver awareness and comfort. Although vision-language models have advanced perception and reasoning in autonomous driving, existing systems rarely consider the emotional dimension or real-world user experience. Keep Yelling Assistant (KYA) detects high-ri...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16181v1)

---

### 8. Cluster-Aware Matching via Laplacian Optimal Transport

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-17 · ✍️ Gabriel Samberg, YoonHaeng Hur, Yuehaw Khoo +1 more

In many applications of matching, the point clouds to be matched are not merely unstructured sets of points but rather samples from distributions with an intrinsic cluster structure. In such cases, as individual points are often interchangeable within a coherent region, finding a robust region-to-region alignment is more desirable than establishing a precise point-to-point correspondence. To this ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16178v1)

---

### 9. Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-17 · ✍️ Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni +1 more

Reinforcement learning (RL) has recently emerged as a promising feedback control strategy for nonlinear and complex dynamical systems. However, RL algorithms are sample inefficient and require a large number of interaction with the environment to synthesize optimal control strategies. Consequently, applications of RL are typically limited to sparse sensors and actuators due to the curse of dimensi...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16177v1)

---

### 10. Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-17 · ✍️ Md Erfan, Ahmed Ryan, Md Kamal Hossain Chowdhury +1 more

Connected and Autonomous Vehicles (CAVs) rely on interconnected software and hardware components, including sensors, Electronic Control Units, in-vehicle infotainment systems, and telematics units, where vulnerabilities can compromise assets, users, and vehicle operations. These vulnerabilities are commonly documented as plain text in the Common Vulnerabilities and Exposures (CVE) database; howeve...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16175v1)

---

### 11. When Does Muon Help Agentic Reinforcement Learning?

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-07-17 · ✍️ Kai Ruan, Jinghao Lin, Zihe Huang +4 more

Muon is competitive with AdamW in large-scale pre-training, but its value for reinforcement-learning (RL) post-training remains unclear. We study vanilla Muon in sparse-reward agentic RL through matched single-seed comparisons with AdamW on ALFWorld using Qwen2.5-0.5B-Instruct. Under Group-in-Group Policy Optimization (GiGPO), applying Muon only to hidden weight matrices raises final-window valida...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16169v1)

---

### 12. Behaviour-Conditioned Neural Processes for Adaptive Residential Short-Term Load Forecasting

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-17 · ✍️ Ramin Soleimani, Andrea Visentin, Dirk Pesch

Residential short-term load forecasting (STLF) is challenging because household demand is heterogeneous, temporally variable, and shaped by diverse behavioural routines. This work investigates whether inferred behavioural structure can be embedded within the forecasting mechanism of a Neural Process-based probabilistic model, rather than used only as an external grouping signal, for context-condit...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16168v1)

---

### 13. An Exam for Active Observers

![CV](https://img.shields.io/badge/cs.CV-blue) ![AI](https://img.shields.io/badge/cs.AI-orange) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-07-17 · ✍️ Jiarui Zhang, Muzi Tao, Shangshang Wang +3 more

Human vision is a closed loop: gaze is continuously redirected by intermediate hypotheses rather than a single snapshot. Decades of psychophysics and cognitive science have argued that this active observation is essential for a wide range of tasks. Whether today's multimodal large language models (MLLMs) exercise active observation is an empirical question that current vision-language benchmarks d...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16165v1)

---

### 14. PRISA: Proactive Infrastructure LiDAR Framework for Intersection Safety Assessment

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-07-17 · ✍️ Tam Bang, Hussam Abubakr, Emiliano de la Garza Villarreal +6 more

Urban intersections are among the most hazardous locations in road networks, posing significant risks to vehicles and vulnerable road users (VRUs) such as pedestrians and cyclists. The complexity of multi-agent interactions demands continuous, real-time monitoring systems capable of anticipating conflicts before they escalate into crashes. We present PRISA, a modular infrastructure LiDAR framework...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16156v1)

---

### 15. CLIFE: Camera-LiDAR Fusion Framework for Edge-Deployable Roadside VRU Perception

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-07-17 · ✍️ Tam Bang, Hoang H. Nguyen, Lei Cheng +6 more

Reliable roadside perception of vulnerable road users (VRUs) remains challenging under occlusions, variable lighting, and diverse weather conditions, particularly under strict edge-computing and latency constraints. Existing multi-sensor fusion systems rely on cloud or server-grade infrastructure, creating a deployment gap at real-world intersections. We present CLIFE, an edge-native camera-LiDAR ...

🔗 [Read on arXiv](http://arxiv.org/abs/2607.16154v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
