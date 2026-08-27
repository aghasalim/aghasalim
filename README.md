# Aghasalim Mustafazada

Third year AI student at Howest, Belgium. Mostly anomaly detection and
interpretability. I get suspicious of results that only work on the benchmark,
so I check my own numbers before anyone else does.

Open to AI and backend internships.

[![claims checked](https://github.com/aghasalim/aghasalim/actions/workflows/check-claims.yml/badge.svg)](https://github.com/aghasalim/aghasalim/actions/workflows/check-claims.yml)

## Work

**[SpuriousAD](https://github.com/aghasalim/spurious-ad)**: wanted to know if anomaly detectors look at the anomaly or cheat off a shortcut in the data. Mostly cheating, even on real MVTec images.

**[EU AI Act RAG](https://github.com/aghasalim/eu-ai-act-rag)**: retrieval over the actual regulation text, graded by a model that is not the one answering. **90.2%** faithful. [demo](https://eu-ai-act-rag-eval.streamlit.app/)

**[Fraud decision trail](https://github.com/aghasalim/ieee-fraud-ml)**: the IEEE-CIS Kaggle set done the honest way instead of the version that leaks future data. **0.1044 AUC** is what that difference costs. [demo](https://ieee-fraud-ml.streamlit.app/)

**[Groundcheck](https://github.com/aghasalim/groundcheck-mcp)**: an MCP tool so Claude or Gemini can check whether a quote, citation or number is real, without asking another model to vouch for it.

## Rebuilt from the papers

Eight systems, each with a test suite, measured benchmarks and a logbook of what
went wrong. All of it ran on a laptop CPU. Half of them ended in results I did
not want, and those are written up the same as the rest.

**[rlhf-ppo-from-scratch](https://github.com/aghasalim/rlhf-ppo-from-scratch)**: PPO, DPO, GRPO, RLOO and best-of-N against one reward model. Optimising the proxy drives its score up while the true objective peaks and then falls below where it started, and nothing visible during training tells you it happened.

**[rectified-flow-from-scratch](https://github.com/aghasalim/rectified-flow-from-scratch)**: conditional flow matching and reflow. One sampling step scores **0.034** against **0.031** at 128 steps, so 128 times less sampling compute for no measurable loss. Straightness is the metric that explains it.

**[mla-from-scratch](https://github.com/aghasalim/mla-from-scratch)**: DeepSeek-V2 latent attention. 120 GB of KV cache down to 8.44 GB at 128k context. Absorbed and naive inference are asserted equal to 6e-07, which is the only thing that caught my first index order being wrong.

**[latent-diffusion-from-scratch](https://github.com/aghasalim/latent-diffusion-from-scratch)**: a KL regularised autoencoder and a DDPM. Diffusion in a 4x compressed latent trains 5.3x faster and scores 6.2x better than the pixel baseline at matched steps.

**[vla-from-scratch](https://github.com/aghasalim/vla-from-scratch)**: four ways a robot policy can emit a continuous action. Trained on demonstrations that route around an obstacle both ways, a regression head learns the average of the two and drives straight into it.

**[flash-attention-from-scratch](https://github.com/aghasalim/flash-attention-from-scratch)**: is attention actually memory bound? Derived the roofline and measured it. My own out-of-memory prediction was 19% wrong until I counted the tensors a real implementation holds instead of the two in the textbook.

**[schrodinger-bridge-from-scratch](https://github.com/aghasalim/schrodinger-bridge-from-scratch)**: entropic optimal transport, IPF and bridge matching. The simpler method beat my diffusion bridge by 2x to 12x at a quarter of the compute, which is the result I did not want and the one worth reporting.

**[world-model-from-scratch](https://github.com/aghasalim/world-model-from-scratch)**: an RSSM and an actor critic trained entirely in imagination. Reconstruction measurably helps open-loop prediction for five steps and stops mattering after ten. The policy half never beat a random one.

## Everything else

34 repos in total, [the rest are here](https://github.com/aghasalim?tab=repositories).
Most of them started because I did not trust something I had assumed.

## Tools

Python, C++, SQL, Bash. PyTorch, scikit-learn, LightGBM, Transformers, SHAP.
FastAPI, Streamlit, Docker, GitHub Actions, PostgreSQL, Raspberry Pi, Arduino.

## Other

Gold medal at the International STEM Olympiad in mathematics, 2022. Scored
**0.9086** on the IEEE-CIS private leaderboard, which
[Kaggle](https://www.kaggle.com/aghasalimmustafazada) graded against labels I never
got to see.

## Contact

salim.mustafazada@student.howest.be

[Website](https://aghasalim.github.io/) ·
[LinkedIn](https://linkedin.com/in/mustafazada) ·
[Kaggle](https://www.kaggle.com/aghasalimmustafazada) ·
[ORCID](https://orcid.org/0009-0001-8746-4582)
