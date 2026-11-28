# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-11-28 08:41 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. AnyCam: Anything Can Represent Camera for Video Generation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Weijie Lyu, Zhixin Shu, Yuntian Ke +1 more

Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an object-centric scene, remains difficult. Existing methods condition either on camera parameters, which are scale-ambiguous in monocular video, or on explicit geometry such as warped point clouds or depth, which breaks dow...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34944v1)

---

### 2. Tracking Any Point with Agentic Visual Reasoning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Xuweiyi Chen, Jin Yao, Linzhan Mou +8 more

A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challenging for VLMs since it goes beyond object-level recognition: it requires pixel-level localization of the same physical surface point across observations, even when appearance changes or the point disappe...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34943v1)

---

### 3. Spectrum Adaptation of AI-Native Autoencoder Communications with Transfer Learning

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-25 · ✍️ Yalin E. Sagduyu, Tugba Erpek

End-to-end physical-layer learning replaces separate modulation, coding, and detection operations with an autoencoder (AE) that consists of a jointly trained encoder-decoder pair at the transmitter and the receiver. This paper studies AI-native communications with AEs and quantifies the sensitivity to training-test mismatch in channel models. Models trained only on an AWGN channel achieve low bit ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34942v1)

---

### 4. Improving and Expanding Video Editing Capabilities Without Videos

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Ji Xie, Yanhao Jia, Xiangpeng Yang +4 more

Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible to transfer advanced image editing capabilities to video editors without new paired videos? We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to ne...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34941v1)

---

### 5. LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Yipengjing Sun, Chenyang Wang, Boyao Zhou +3 more

We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we factorize avatar synthesis into an animatable 3D intrinsic Gaussian proxy and a causal autoregressive neural shader. This proxy disentangles canonical geometry and reflectance attributes, rapidly rasteriz...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34940v1)

---

### 6. A Mesh for Every Moment

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman

We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34939v1)

---

### 7. Tokenisation is not in APX

![CL](https://img.shields.io/badge/cs.CL-green) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-25 · ✍️ Violeta Kastreva, Philip Whittington, Dennis Komm +1 more

In this paper, we prove that, unless P=NP, no polynomial-time algorithm can find a tokeniser whose objective is within any constant factor of the optimum, meaning that tokenisation is not in the APX complexity class. We prove this for direct and bottom-up tokenisation, under both a compression or unigram log-likelihood objectives, and for binary or larger alphabets. We further show that, even over...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34938v1)

---

### 8. Can image generation help visual reasoning? An empirical study

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Xueyang Yu, Yifan Jing, Taiming Lu +5 more

Language models think in words; then multimodal models might think in images. We test whether a generated helper improves the answer to a visual question. A model describes the helper it needs and then answers using the original and generated images together. Across 13 vision-language model and generator pairs, generation lowers mean accuracy by 3.7 percentage points, with declines on nine of ten ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34935v1)

---

### 9. Attack Policy Selection can Mislead Monitor Evaluators

![LG](https://img.shields.io/badge/cs.LG-purple) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-25 · ✍️ Charlie Griffin, Oliver Makins, Asa Cooper Stickland +4 more

AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34934v1)

---

### 10. DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular 4D Reconstruction and Motion Segmentation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Agelos Kratimenos, Yile Hua, Kostas Daniilidis

A single casual video leaves a moving scene under-determined: a point seen once from each place can slide toward or away from the camera and still match every frame. We constrain the reconstruction with the structure of the motion itself. Building on DynMF, we model a scene's motion as a handful of SE(3) trajectories, each rigid, and let every point follow one of them alone, never a blend. DynMF2 ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34931v1)

---

### 11. A gene informed benchmark for BioScoring of pathology foundation models

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-25 · ✍️ Paul Vilars, Vincent Quoc-Huy Trinh, Maria Vakalopoulou +3 more

Pathology foundation models are usually compared by their performance on downstream tasks such as classification and retrieval. While such benchmarks measure how useful a model is, they provide no insight into the biology it represents. We introduce BioScore, a benchmark that quantifies how well an image encoder captures cell identities, with spatial transcriptomics of the same tissue as the refer...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34930v1)

---

### 12. High-Fidelity Image Matting with Pixel-Space Diffusion Transformers

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-11-25 · ✍️ Baihan Yang, Xin Lin, Yufan Wei +5 more

Diffusion models have shown strong potential for image matting by transferring generative priors learned from large-scale pretraining. However, existing approaches largely rely on latent diffusion models, whose compressed representations and VAE-based reconstruction introduce a mismatch with the high-frequency precision required for matting. We present PixelMatte, a framework that adapts pretraine...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34929v1)

---

### 13. Diverse Alternative Reasoning Traces for Hard Math Problems

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-11-25 · ✍️ Lukas Aichberger, Adam Golinski, Arno Blaas +5 more

Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning ...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34928v1)

---

### 14. Mixture-of-Loops Transformer

![LG](https://img.shields.io/badge/cs.LG-purple) ![CL](https://img.shields.io/badge/cs.CL-green)

📅 2026-11-25 · ✍️ Lianghui Zhu, Shijie Wang, Xinggang Wang +3 more

Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops? We introduce Mixture-of-Loops Transformer (MoLT), whose Mixture-of-Loops Attention (MoLA) uses keys and values (KV) as memory for se...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34923v1)

---

### 15. $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents

![CL](https://img.shields.io/badge/cs.CL-green) ![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-11-25 · ✍️ Qihao Lin, Guanxu Chen, Shuhang Zheng +7 more

Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint task completion in closed-loop, full-duplex multi-user voice interaction. Simulated participants act from isolated prof...

🔗 [Read on arXiv](http://arxiv.org/abs/2611.34920v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
