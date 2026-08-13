# Aghasalim Mustafazada

AI student at [Howest](https://www.howest.be/) in Kortrijk, Belgium, and Head of IT at
[Adscreen](https://adscreen.com), where I look after the infrastructure behind 1,000+
AI-powered signage tablets.

Currently looking for AI or backend internship / jobstudent roles.

- B.Sc. Artificial Intelligence at Howest, second year
- Gold medal, International STEM Olympiad (Mathematics), France 2022
- Bronze medal, International STEM Olympiad (German), Germany 2023
- Taught programming at STEP IT Academy for 4 years, around 200 students
- Azerbaijani, English (C1), Turkish, German (A2-B1), learning Dutch

## Projects

**[Explainable Visual Defect Detector](https://github.com/aghasalim/explainable-defect-detector)**

Finds defects in product photos and shows where they are. It is built from normal
images only, so it never sees a labelled defect. PatchCore implemented from the paper,
0.9874 mean image AUROC across all 15 MVTec AD categories. The heatmaps are checked
against pixel ground truth rather than eyeballed, which turned up a useful result: a
supervised classifier scored 0.96 AUROC on one category while its Grad-CAM never
pointed at the actual defect.

PyTorch · Streamlit · Docker · GitHub Actions

**AI Drone Navigation for Smart Cities** - [writeup](https://www.linkedin.com/posts/mustafazada_ai-machinelearning-smartcities-ugcPost-7423344619452547072-VDn0)

Autonomous drone navigation for dense urban areas, where GPS alone breaks down because
of signal occlusion and moving obstacles. Combines LiDAR and camera sensor fusion with
learned path planning. The prototype secured venture investment.

Python · TensorFlow · OpenCV · ROS

**[RFID and Face Recognition Attendance System](https://www.instructables.com/Build-Your-Own-RFID-Face-Recognition-Attendance-Sy/)**

An attendance terminal with a two-factor check: the RFID card has to match the face at
the camera. Raspberry Pi 4 talking to an Arduino Mega over serial, YOLOv8 for face
recognition, local web dashboard for students and logs, custom 3D-printed case. Runs
fully offline. Published on Instructables.

Python · OpenCV · YOLOv8 · Arduino C++

## Working on

- Scaling the Adscreen tablet fleet across Belgium and the Netherlands
- Real-time computer vision for audience analytics
- A recommendation engine for ad targeting
- Deep learning coursework at Howest, mostly CV and NLP

## Tools I use

**ML** Python, PyTorch, TensorFlow, OpenCV, scikit-learn, NumPy, Pandas
**Backend** FastAPI, Flask, Node.js, PostgreSQL, MongoDB, MySQL
**Ops** Docker, Kubernetes, Nginx, Linux, Git
**Hardware** Arduino, Raspberry Pi, C++

## Contact

[LinkedIn](https://linkedin.com/in/mustafazada) ·
[Email](mailto:salim.mustafazada@student.howest.be)

![](https://github-readme-stats.vercel.app/api?username=aghasalim&show_icons=true&count_private=true&hide_border=true&theme=tokyonight)
