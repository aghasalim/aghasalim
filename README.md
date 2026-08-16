# Aghasalim Mustafazada

[![claims checked](https://github.com/aghasalim/aghasalim/actions/workflows/check-claims.yml/badge.svg)](https://github.com/aghasalim/aghasalim/actions/workflows/check-claims.yml)

Third-year B.Sc. Artificial Intelligence at Howest, Kortrijk. I run the IT
infrastructure at Adscreen for ~1,000 AI signage tablets.

I work on anomaly detection and model interpretability, and mostly on one
question: does a method that looks good on a benchmark still hold up once it has
to make a decision? Every number below is measured, reproducible from its repo,
and re-checked weekly by CI — including the ones that make me look bad.

**Open to AI and backend internships.**

## Projects

Each README carries the full reasoning: the methodology, the failures, and the
numbers I would rather state myself than have a reviewer find.

| project | the finding | |
|---|---|---|
| **Explainable defect detector** | PatchCore reproduced across all 15 MVTec categories, 0.9874 mean AUROC | [demo](https://explainable-defect-detector.streamlit.app/) · [code](https://github.com/aghasalim/explainable-defect-detector) |
| **EU AI Act RAG** | 90.2% faithfulness over 45 questions, graded by a separate model family | [demo](https://eu-ai-act-rag-eval.streamlit.app/) · [code](https://github.com/aghasalim/eu-ai-act-rag) |
| **Fraud decision trail** | 0.1044 AUC separates the flattering split from the defensible one | [demo](https://ieee-fraud-ml.streamlit.app/) · [code](https://github.com/aghasalim/ieee-fraud-ml) |
| **MLOps pipeline** | Prediction PSI correlates −0.709 with the AUC loss it should predict | [code](https://github.com/aghasalim/mlops-fraud-pipeline) |
| **RL reward shaping** | Six reward functions, two the agent exploited; 43.2% against a 73.5% oracle | [demo](https://rl-arm-reward-shaping.streamlit.app/) · [code](https://github.com/aghasalim/rl-arm-reward-shaping) |
| **Hallucination-aware captioning** | BLIP hallucinates on 4.5% of probes but misses 29% of objects present | [demo](https://vlm-hallucination-eval.streamlit.app/) · [code](https://github.com/aghasalim/vlm-hallucination-eval) |
| **A/B testing & causal inference** | mSPRT proved *more* conservative than specified: 0.9% error against a nominal 5% | [code](https://github.com/aghasalim/ab-causal) |
| **LoRA fine-tuning** | An adapter of 0.28% of parameters still degraded held-out behaviour | [code](https://github.com/aghasalim/lora-forgetting) |
| **Smart IVC cage platform** | Full stack, firmware to frontend; 173 of 204 commits mine on a 3-person client project | [code](https://github.com/aghasalim/smart-ivc-cage-platform) |

Benchmarks I built to prove something, which then refuted their own premise —
the reason they are here:

| | | |
|---|---|---|
| **SpuriousAD** | Image AUROC stays 1.000 at every confound correlation; the faithfulness collapse turned out to be an artefact | [code](https://github.com/aghasalim/spurious-ad) |
| **GraphCiteFaith** | 3,965 of 3,965 cited node ids real, while two models name the structure at chance | [code](https://github.com/aghasalim/graph-cite-faith) |
| **DriftHarm** | Harm-precision 0.512–0.593 against a 0.517 base rate — so it is not a ranking | [code](https://github.com/aghasalim/drift-harm) |
| **RingFaith** | Explainer overlap correlates r=+0.945 with its own random baseline | [code](https://github.com/aghasalim/ring-faith) |
| **LeakGraph** | Only 5 of 10 GNN cells resolve above noise; the metric mostly tracks graph size | [code](https://github.com/aghasalim/leak-graph) |
| **AI Act fairness audit** | Annex III exempts fraud detection, so the audit was never legally required | [code](https://github.com/aghasalim/ai-act-fairness-audit) |
| **Forecast backtesting** | The split costs 4.1% MASE where the horizon costs 42.1% | [code](https://github.com/aghasalim/forecast-backtest) |
| **M4 prediction intervals** | Nothing reaches nominal 95% coverage; the best is 86.6% | [code](https://github.com/aghasalim/m4-forecasting) |
| **ARC-AGI-2 attempt** | 3.9%, published because a negative result honestly reported is still a result | [code](https://github.com/aghasalim/arc-prize-2026) |
| **Offline vs online metrics** | An AUC of 0.5386 next to what the policy actually earns | [code](https://github.com/aghasalim/recsys-offline-online) |

Also: [RFID + face-recognition attendance terminal](https://www.instructables.com/Build-Your-Own-RFID-Face-Recognition-Attendance-Sy/)
(Raspberry Pi + Arduino, fully offline) and drone urban navigation coursework.

## Achievements

- **Gold medal**, International STEM Olympiad — mathematics, France 2022 · **bronze**, German, Germany 2023
- **0.9086 private leaderboard**, IEEE-CIS Fraud Detection — scored by Kaggle against labels I never saw
- Taught ~200 students over four years at STEP IT Academy
- ORCID [0009-0001-8746-4582](https://orcid.org/0009-0001-8746-4582)

## Stack

Python · PyTorch · scikit-learn · LightGBM · Transformers · SHAP · FastAPI ·
Streamlit · React · TypeScript · Docker · GitHub Actions · PostgreSQL ·
Raspberry Pi · Arduino

## Contact

[salim.mustafazada@student.howest.be](mailto:salim.mustafazada@student.howest.be) ·
[LinkedIn](https://linkedin.com/in/mustafazada)
