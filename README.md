# Aghasalim Mustafazada

[![claims checked](https://github.com/aghasalim/aghasalim/actions/workflows/check-claims.yml/badge.svg)](https://github.com/aghasalim/aghasalim/actions/workflows/check-claims.yml)

## About me

I'm a third-year B.Sc. Artificial Intelligence student at Howest in Kortrijk, Belgium,
and I run the IT infrastructure at Adscreen for a fleet of around 1,000 AI signage
tablets. I work on computer vision and machine learning systems.

My interests are anomaly detection, model interpretability, and the question of whether
a method that looks good on a benchmark still holds up once it has to make a decision.
Every number below is measured, reproducible from its repository, and checked weekly by
CI against its source — including the ones that make me look bad.

**Open to AI and backend internships.**

## 💼 Projects

Eleven repositories, five with live demos. Each one's README carries the full
reasoning — the methodology, the failures, and the numbers I would rather state
myself than have a reviewer find.

| project | what it is | links |
|---|---|---|
| **Smart IVC cage platform** | Full stack for an instrumented lab-animal cage — FastAPI, React, Arduino firmware, Raspberry Pi, closed-loop volumetric water dosing, zero inbound ports. 173 of 204 commits mine on a 3-person client project | [code](https://github.com/aghasalim/smart-ivc-cage-platform) |
| **Explainable defect detector** | PatchCore reimplemented and reproduced across all 15 MVTec AD categories at 0.9874 mean image AUROC, with calibrated OK/DEFECT thresholds | [demo](https://explainable-defect-detector.streamlit.app/) · [code](https://github.com/aghasalim/explainable-defect-detector) |
| **EU AI Act RAG** | QA over Regulation (EU) 2024/1689 where the evaluation is the project: 90.2% faithfulness across all 45 questions, graded by a separate model family | [demo](https://eu-ai-act-rag-eval.streamlit.app/) · [code](https://github.com/aghasalim/eu-ai-act-rag) |
| **RL reward shaping** | Custom Gymnasium arm, PPO, six reward functions — two of which the agent exploited. Final policy 43.2% against a hand-written oracle's 73.5% | [demo](https://rl-arm-reward-shaping.streamlit.app/) · [code](https://github.com/aghasalim/rl-arm-reward-shaping) |
| **Hallucination-aware captioning** | Hand-verified adversarial set of 33 images; BLIP hallucinates on 4.5% of probes but misses 29% of objects that are present | [demo](https://vlm-hallucination-eval.streamlit.app/) · [code](https://github.com/aghasalim/vlm-hallucination-eval) |
| **Fraud detection decision trail** | IEEE-CIS worked end to end; 0.1044 AUC separates the flattering split from the defensible one, and I caught my own synthetic-data conclusion being backwards | [demo](https://ieee-fraud-ml.streamlit.app/) · [code](https://github.com/aghasalim/ieee-fraud-ml) |
| **MLOps pipeline** | Monitoring deliberately broken to prove the drift detector fires. The model loses 0.060–0.137 AUC to time alone, and prediction PSI correlates −0.709 with that loss | [code](https://github.com/aghasalim/mlops-fraud-pipeline) |
| **A/B testing & causal inference** | Estimators validated against simulations with known ground truth before meeting real data — mSPRT proved *more* conservative than specified, 0.9% error against a nominal 5% | [code](https://github.com/aghasalim/ab-causal) |
| **ARC-AGI-2 attempt** | A real attempt that scores 3.9% — published because a negative result honestly reported is still a result | [code](https://github.com/aghasalim/arc-prize-2026) |
| **LoRA fine-tuning** | The catastrophic-forgetting check most tutorials skip: an adapter of 0.28% of parameters, trained to a final loss of 0.0000, still degraded held-out behaviour | [code](https://github.com/aghasalim/lora-forgetting) |
| **Offline vs online metrics** | Where offline ranking gains and online lift disagree: a respectable-looking AUC of 0.5386 next to what the policy actually earns in simulation | [code](https://github.com/aghasalim/recsys-offline-online) |
| **Drone urban navigation** | Autonomous navigation coursework — perception and path planning | — |
| **RFID + face attendance terminal** | Two-factor identity check on Raspberry Pi + Arduino, fully offline | [build guide](https://www.instructables.com/Build-Your-Own-RFID-Face-Recognition-Attendance-Sy/) |

## 📄 Background & awards

Third-year B.Sc. Artificial Intelligence at Howest. Gold medal at the International
STEM Olympiad in mathematics (France, 2022) and bronze in German (Germany, 2023). Four
years teaching programming at STEP IT Academy, roughly 200 students. Azerbaijani,
English, Turkish, German, and learning Dutch.

## 🛠️ Tech stack

| | |
|---|---|
| **Languages** | Python · TypeScript · C++ (Arduino) · SQL · Bash |
| **ML / data** | PyTorch · scikit-learn · LightGBM · Hugging Face Transformers · Stable-Baselines3 · Gymnasium · SHAP · pandas · NumPy |
| **Backend / web** | FastAPI · React · Streamlit · SQLAlchemy · PostgreSQL · SQLite · WebSockets |
| **Infra / tooling** | Docker · GitHub Actions · Cloudflare Tunnel · Chroma · Raspberry Pi · Arduino · Git |


## 📫 Connect with me

- **Email:** [salim.mustafazada@student.howest.be](mailto:salim.mustafazada@student.howest.be)
- **LinkedIn:** [linkedin.com/in/mustafazada](https://linkedin.com/in/mustafazada)
