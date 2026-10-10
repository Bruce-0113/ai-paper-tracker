# 🤖 Daily AI Papers

> Auto-updated every day at 09:00 Taipei time · Last sync: **2026-10-10 06:43 UTC**

Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`

---

### 1. Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Jusuk Lee, Sungha Kim, Yeonsoo Park +8 more

While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via reinforcement learning (RL) allows for br...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12470v1)

---

### 2. Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Ritesh Thawkar, Shubham Patle, Shravan Venkatraman +1 more

Instruction-guided image editors have become highly capable, yet improving them further still depends on human-edited training pairs or external reward models. Such supervision is costly to obtain and can reward plausible failures: a realistic output may leave the requested change undone or alter content that should be preserved. In this work, we strive to improve a pretrained image editor using o...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12469v1)

---

### 3. DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Junyan Li, Ruizhi Li, Yu Liu +6 more

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodimen...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12468v1)

---

### 4. CSF: Contextual Safety Filtering for Motion Generators

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-08 · ✍️ Lizhi Yang, Yiling Hou, Yao Tang +4 more

Text-conditioned motion generators produce trackable whole-body motion, but they have no notion of scene-dependent safety: the same action may target an object or a person. Existing safeguards either inspect the prompt, require labeled motion data, or enforce geometric constraints; therefore, they do not directly account for how scene context changes a motion's meaning. We introduce contextual saf...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12467v1)

---

### 5. On the estimation and validity of AI time horizons---a statistical look at the METR plot

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-08 · ✍️ Drew T. Nguyen, William Fithian

METR's 50\% time horizon measures the human completion time of software tasks that an AI solves with 50\% probability, allowing AI capabilities to be expressed in interpretable units. On 228 tasks and 26 AIs, we recompute the time horizons using splines and item-response theory to relax the assumption that the AI difficulty of a task depends linearly on the log of human time. Our fitted spline can...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12466v1)

---

### 6. A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control

![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-08 · ✍️ Octi Zhang, Mateo Guaman Castro, Patrick Yin +4 more

General-purpose robots must perform a wide range of tasks from agile locomotion to dexterous manipulation. While sim-to-real reinforcement learning (RL) has proven to be a useful tool for this goal, current RL pipelines depend on engineering-heavy, per-task structural priors such as shaped rewards and demonstrations. Recent work has shown that diverse simulator resets, combined with massively para...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12465v1)

---

### 7. From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents

![AI](https://img.shields.io/badge/cs.AI-orange)

📅 2026-10-08 · ✍️ Abbas Raftari

In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised parts of Hugging Face's production environment. Anthropic reported cases in which a misconfigured third-party environment exposed real systems t...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12463v1)

---

### 8. What 30,000 Hours of Ego-centric Video Does Not Teach

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Jiahua Dong, Anurag Bagchi, Yash Jangir +7 more

World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distr...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12464v1)

---

### 9. OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li +3 more

Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12461v1)

---

### 10. WorldGuide: Goal-Directed Video World Model for Procedural Task Execution

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Ankan Deria, Komal Kumar, Hisham Cholakkal +2 more

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12459v1)

---

### 11. OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Zhongyu Yang, Jiale Tao, Ruitao Chen +9 more

Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide coverage without localization, local probes provide localization without coverage, and...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12458v1)

---

### 12. Hybrid Cinematography: Previsualizing and Managing Hallucination Risk in Generative Video Reshooting

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️  Nhan,  Tran, Neal Wadhwa +2 more

On a film set, the camera move is committed during a take. Generative video reshooting lets filmmakers change it afterward, but may require hallucinating unrecorded content, a gap sometimes discovered only after leaving the set. We present Hybrid Cinematography, a workflow that bridges physical capture and generative reshooting to manage hallucination risk while filmmakers can still act on it. Usi...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12455v1)

---

### 13. BrickBench: Evaluating Agentic Brick Design

![AI](https://img.shields.io/badge/cs.AI-orange) ![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Peter Kulits, Yiqing Xu, R. Kenny Jones +2 more

We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12452v1)

---

### 14. VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

![CV](https://img.shields.io/badge/cs.CV-blue)

📅 2026-10-08 · ✍️ Boyao Han, Chen Shi, Jingjing Qian +2 more

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA ...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12451v1)

---

### 15. One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts

![CV](https://img.shields.io/badge/cs.CV-blue) ![LG](https://img.shields.io/badge/cs.LG-purple)

📅 2026-10-08 · ✍️ Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos

In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combination of a small shared expert bank. A continuous normalized-depth coordinate program...

🔗 [Read on arXiv](http://arxiv.org/abs/2610.12448v1)

---

_This README is generated automatically by [GitHub Actions](.github/workflows/fetch_papers.yml)._
