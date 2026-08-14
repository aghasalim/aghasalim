# Aghasalim Mustafazada

I work on computer vision and machine learning systems. Currently studying artificial
intelligence at Howest in Kortrijk, Belgium, and running the IT infrastructure at
Adscreen for a fleet of around 1,000 AI signage tablets.

My interests are anomaly detection, model interpretability, and the question of whether
a method that looks good on a benchmark still holds up once it has to make a decision.

Open to AI and backend internships.

### Selected projects

**Explainable Visual Defect Detector** ·
[live demo](https://explainable-defect-detector.streamlit.app/) ·
[code](https://github.com/aghasalim/explainable-defect-detector)

Industrial defect detection built from normal images only, with no labelled defects in
training. Reimplements PatchCore (Roth et al., CVPR 2022) and reproduces it across all
15 MVTec AD categories at 0.9874 mean image AUROC. Localisation is scored against pixel
ground truth with a random-heatmap control, which surfaced the more interesting result:
a supervised baseline reached 0.96 AUROC on one category while its Grad-CAM never
overlapped the actual defect.

Turning that into something that can actually say OK or DEFECT was the harder half. My
first threshold, a 99th percentile over a small held-out set of normal images, hit its 1%
false-alarm target in only 3 of 15 categories and flagged 43% of good carpet. The
empirical quantile of a small sample sits near its maximum, which estimates the 96th
percentile rather than the 99th. Replacing it with k-fold cross-calibration and a
one-sided nonparametric tolerance bound got 13 of 15 within target, at a measured cost of
8 points of recall. One category is left failing on purpose, because its test images are
genuinely more varied than anything in training and calibrating it any further would mean
using the test set.

**EU AI Act RAG, with an evaluation I actually ran** ·
[live demo](https://eu-ai-act-rag-eval.streamlit.app/) ·
[code](https://github.com/aghasalim/eu-ai-act-rag)

Question answering over Regulation (EU) 2024/1689, built so that the measurement is the
project and the chatbot is the side effect. 45 questions written by hand against 464
chunks cut on the Act's own article structure rather than a fixed token window, because
the answer to a legal question is a citation and a sliding window kept separating a
rule from its exceptions. Hybrid retrieval reaches 90.9% hit rate at k=6, and 41.7% full
recall on the questions that need two articles at once — that second number is the one
worth reporting, because a question needing two provisions cannot be answered from one.

Two results I did not expect. Keyword search beat embeddings on almost every metric:
legal text runs on exact phrases like "serious incident" and "putting into service", and
a 384-dimensional vector smooths over exactly those distinctions. And the 180 recitals
were sabotaging retrieval — they restate the rules in flowing prose, so they look more
like an answer to a plain question than the binding article does. Down-weighting them
moved MRR from 0.581 to 0.790.

Generation is graded by a different model family, so it is not marking its own work:
92.6% faithfulness, 100% citation validity, and 12 out of 12 out-of-scope questions
correctly refused with nothing hallucinated, including ones written to bait it. The
number I find most useful is that multi-hop answer accuracy (25.0%) tracks multi-hop
retrieval almost exactly — when only one of the two articles a question needs is
retrieved, the system produces a confident, well-cited, half-right answer that stays
*faithful to an incomplete set of passages*. That is the failure a faithfulness score
on its own would never surface.

**Reward shaping on a custom robot arm** ·
[code](https://github.com/aghasalim/rl-arm-reward-shaping)

A two-link torque-controlled arm that has to reach a target and *stop* there without
hitting an obstacle. Custom Gymnasium environment, PPO, six reward functions, two of
which the agent exploited. The first paid −distance every step and never penalised
collision, so the agent steered into the obstacle in 200 of 200 episodes — colliding ends
the episode, and ending the episode stops the cost. The second used textbook
potential-based shaping, which quietly pays a *stationary* agent (1−γ)·distance every
step: +20 per episode at 2 m, exactly the success bonus, at zero risk, and more the
further away it loiters. It parked at 1.39 m and collected.

The more useful lesson came from neither. After both fixes the agent still solved
nothing, so I wrote a PD controller with exact inverse kinematics as an oracle — and it
failed a third of episodes with the obstacle removed, because the arm was under-actuated.
I had been trying to fix physically impossible episodes with reward functions. The final
policy reaches 43.2% ± 5.8% across five seeds against that oracle's 73.5%: it loses on
success and wins only on collisions, 17.3% against 25.5%. Training it 2.7× longer more
than halved the score, which I report and cannot explain.

**Hallucination-aware captioning** ·
[code](https://github.com/aghasalim/vlm-hallucination-eval)

I set out to catch a vision-language model confidently describing things that are not
there, and found the opposite. Against 33 images selected for clutter and confusability
and then verified by eye — 172 objects confirmed present, 67 confirmed absent — BLIP
hallucinates on only 4.5% of adversarial probes but misses 29% of the objects that are
genuinely there. It is over-cautious, not over-confident. None of its 33 captions
hallucinate, because they are too vague to be wrong: a shelf of thirty ceramic pieces
got "a shelf filled with lots of different colored dishes".

Phrasing matters more than I expected — smuggling the object into the premise more than
doubles the rate, 6.0% to 13.4%. A CLIP grounding layer cuts hallucination by 33–40%
relative, but it only ever deletes a "yes", so on a model that already under-reports it
costs recall and net F1 drops. Reported as a trade-off curve rather than the one
operating point that flatters it. Building the set by hand caught a bug that would have
corrupted every number: "plate" is not one of COCO's 80 categories, so probing for it
would have measured the label vocabulary instead of the model.

**Fraud detection, with the decision trail as the deliverable** ·
[live demo](https://ieee-fraud-ml.streamlit.app/) ·
[code](https://github.com/aghasalim/ieee-fraud-ml)

The IEEE-CIS competition worked end to end: 590,540 transactions across 394 columns,
3.5% fraud, 172 columns between half and entirely missing. I built the validation
splitter before touching a model, because the number that matters here is not the score
but whether the score is real. Between the most flattering configuration and the most
defensible one — chronological folds, fold-local encodings, and a 30-day embargo that
matches the gap before the real test period — sits **0.1044 AUC**, 0.9557 against 0.8513.
That is roughly the distance from the top of the leaderboard to its middle, and all of it
is methodology rather than modelling.

The entry I would most want to be asked about is the one where I was wrong. I first ran
the leakage experiment on synthetic data and concluded the leaky feature outweighed the
bad split by 4.4×. Re-running it on all 590k real rows reversed the ratio to 0.72× — the
simulation had correctly predicted that both leaks were real, and got the relative
magnitudes backwards, which was exactly what I had used it to decide. Target encoding
turned out to be a bad feature in two separate ways: computed globally it inflates the
score by +0.045, computed correctly it lowers the honest one by −0.031, driving train AUC
to exactly 1.0000 by handing the model a near-unique key per customer. I also predicted a
leak from early stopping, measured it at +0.0006, and withdrew the claim — a trail
containing only confirmed hypotheses is a highlight reel.

**A/B testing and causal inference, checked against known answers** ·
[code](https://github.com/aghasalim/ab-causal)

A causal estimate has nothing to check against, because the "otherwise" never happened.
So the usual version of this project — a t-test and a p-value on a marketing dataset —
would look identical if the method were completely wrong. Everything here is run where
the true answer is known instead: simulations where I set the effect myself, and one
dataset where a randomised experiment already settled it.

Checking a test daily for two weeks turns a 5% error rate into **22.3%**, so a "95%
confident" result is wrong more than one time in five. The trap in that table is the
power column: naive peeking has the *highest* power, 84%, because it declares
significance more often whether or not anything is real, and a dashboard shows you that
column and not the one beside it. Pocock boundaries and always-valid mSPRT both fix the
error rate and neither is free — mSPRT also needs a `tau` that the usual advice omits,
and setting it 5× too small collapses power from 42% to 0.4%.

CUPED delivers its advertised 81% variance reduction at ρ=0.9, then fails silently. Give
it a covariate that treatment moved and it reports **exactly zero effect** on a feature
that works perfectly, with a standard error identical to the case where it is right —
nothing widens, nothing looks unstable, and you ship "no impact" with a tight interval. I
had that backwards at first and wrote a test asserting CUPED was biased; it was correctly
returning the direct effect while I was calling the total effect the truth. On LaLonde,
where the randomised answer is **+$1,794**, swapping in survey controls makes a programme
that raised earnings look like one that destroyed them, −$8,498 and −$15,205. Adjustment
pulls it back, but 20 adjusted estimates span $237 to $3,843 while every balance
diagnostic reads textbook-clean. Good balance is necessary, not sufficient: it says the
groups match on what you measured and is silent on everything else.

**Drone navigation for urban environments** ·
[writeup](https://www.linkedin.com/posts/mustafazada_ai-machinelearning-smartcities-ugcPost-7423344619452547072-VDn0)

Autonomous navigation for dense cities, where GPS alone degrades from signal occlusion
and moving obstacles. Sensor fusion over LiDAR and camera with learned path planning.
The prototype attracted venture funding.

**RFID and face recognition attendance terminal** ·
[build guide](https://www.instructables.com/Build-Your-Own-RFID-Face-Recognition-Attendance-Sy/)

Two-factor identity check: the card has to match the face at the camera. Raspberry Pi
and Arduino over serial, YOLOv8 for recognition, offline logging and a local dashboard,
custom enclosure. No cloud dependency.

### Background

Third-year B.Sc. Artificial Intelligence at Howest. Gold medal at the International
STEM Olympiad in mathematics (France, 2022) and bronze in German (Germany, 2023). Four
years teaching programming at STEP IT Academy, roughly 200 students. Azerbaijani,
English, Turkish, German, and learning Dutch.

Mostly Python and PyTorch, with Docker, FastAPI, PostgreSQL and Arduino alongside.

### Contact

salim.mustafazada@student.howest.be ·
[LinkedIn](https://linkedin.com/in/mustafazada)
