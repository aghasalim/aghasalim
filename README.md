# Aghasalim Mustafazada

I work on computer vision and machine learning systems. Currently studying artificial
intelligence at Howest in Kortrijk, Belgium, and running the IT infrastructure at
Adscreen for a fleet of around 1,000 AI signage tablets.

My interests are anomaly detection, model interpretability, and the question of whether
a method that looks good on a benchmark still holds up once it has to make a decision.

Open to AI and backend internships.

### Selected projects

**Explainable Visual Defect Detector** ·
[code](https://github.com/aghasalim/explainable-defect-detector)

Industrial defect detection built from normal images only, with no labelled defects in
training. Reimplements PatchCore (Roth et al., CVPR 2022) and reproduces it across all
15 MVTec AD categories at 0.9874 mean image AUROC. Localisation is scored against pixel
ground truth with a random-heatmap control, which surfaced the more interesting result:
a supervised baseline reached 0.96 AUROC on one category while its Grad-CAM never
overlapped the actual defect.

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

Second-year B.Sc. Artificial Intelligence at Howest. Gold medal at the International
STEM Olympiad in mathematics (France, 2022) and bronze in German (Germany, 2023). Four
years teaching programming at STEP IT Academy, roughly 200 students. Azerbaijani,
English, Turkish, German, and learning Dutch.

Mostly Python and PyTorch, with Docker, FastAPI, PostgreSQL and Arduino alongside.

### Contact

salim.mustafazada@student.howest.be ·
[LinkedIn](https://linkedin.com/in/mustafazada)
