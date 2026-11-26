# Aghasalim Mustafazada

Third year AI student at Howest, Belgium, and co-founder and CTO of
[SIBA](https://siba.az), a small company in Baku that builds AI assistants in
Azerbaijani. I work on language models and on how to evaluate them: retrieval,
groundedness, agents, guardrails, benchmarks and data leakage. I like rerunning my own
results before I believe them.

Open to remote AI engineering work.

## SIBA

- [chat.siba.az](https://chat.siba.az): an assistant in Azerbaijani, English
  and Russian, in text and voice.
- [SIBA Meristem Native 0.5B](https://huggingface.co/aghasalim/siba-meristem-native-0.5b-base):
  an Azerbaijani base model trained from scratch on 5.94 billion tokens
  (539 M parameters, Apache 2.0). It continues text, it does not follow
  instructions.
- [azbench](https://github.com/aghasalim/azbench): an open Azerbaijani
  benchmark of 2,148 questions, with a
  [leaderboard](https://siba.az/azbench).
- A WhatsApp and Telegram agent delivered for Zakher Travel, a tour operator
  in Baku.

## Selected work

- [eu-ai-act-rag](https://github.com/aghasalim/eu-ai-act-rag): question
  answering over the EU AI Act, with retrieval and faithfulness measured on 45
  hand-written questions.
- [groundedness](https://github.com/aghasalim/groundedness) and
  [groundcheck-mcp](https://github.com/aghasalim/groundcheck-mcp): check
  whether a model's claims are supported by its sources.
- [lora-forgetting](https://github.com/aghasalim/lora-forgetting): LoRA
  fine-tuning with the catastrophic-forgetting check next to the task score.
- [leak-graph](https://github.com/aghasalim/leak-graph),
  [splitcheck](https://github.com/aghasalim/splitcheck) and
  [drift-harm](https://github.com/aghasalim/drift-harm): measure leakage and
  drift instead of assuming them.
- [smart-ivc-cage-platform](https://github.com/aghasalim/smart-ivc-cage-platform):
  FastAPI, React, Arduino and Raspberry Pi platform for an instrumented lab
  cage.
- [ai-systems-from-scratch](https://github.com/aghasalim/ai-systems-from-scratch):
  eight pieces of modern AI rebuilt from the papers.

## In progress (private repositories)

- Kill switch for local LLM agents (bachelor research): a control plane that
  slows, suspends and stops a group of collaborating agents, then checks that
  nothing is left running.
- InternAgent (team of two): a local internship copilot with hybrid retrieval,
  MCP servers, human approval for every write, and guardrails measured on a
  held-out attack set.
- From notebook to device: a waste-sorting classifier with an Azure ML
  pipeline, a quality gate and FastAPI on Kubernetes, INT8 models on a
  Raspberry Pi 5, and ROS 2 navigation on an AgileX Limo Pro.

Mostly Python: PyTorch, scikit-learn, Transformers, LangGraph, MCP, FastAPI,
Docker, Kubernetes, Azure ML, ROS 2 and GitHub Actions.

## Papers and results

Three papers on SSRN in 2026:
[a groundedness detector that runs on a Raspberry Pi](https://doi.org/10.2139/ssrn.7497398),
[retrieval over an amended law](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7590363) and
[a from-scratch PatchCore on MVTec AD](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7590958).
Gold medal in mathematics at the International STEM Olympiad, 2022. 0.9086 on
the IEEE-CIS private leaderboard on
[Kaggle](https://www.kaggle.com/aghasalimmustafazada).

## Contact

salim.mustafazada@student.howest.be ·
[Website](https://aghasalim.com) ·
[LinkedIn](https://linkedin.com/in/mustafazada) ·
[ORCID](https://orcid.org/0009-0001-8746-4582)
