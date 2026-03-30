<div align="center">

<!-- Animated wave header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,50:16213e,100:0f3460&height=220&section=header&text=Aghasalim%20Mustafazada&fontSize=42&fontColor=e94560&fontAlignY=35&desc=AI%20Engineer%20%7C%20Head%20of%20IT%20%7C%20Builder&descSize=18&descColor=ffffff&descAlignY=55&animation=fadeIn" width="100%" />

<!-- Animated typing -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=E94560&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=80&lines=B.Sc.+AI+Student+%40+Howest+%F0%9F%87%A7%F0%9F%87%AA;Head+of+IT+%40+Adscreen+%7C+1%2C000%2B+AI+Tablets;International+Gold+Medalist+in+Mathematics+%F0%9F%A5%87;AI+Drone+Builder+%7C+Venture-Backed+Innovator+%F0%9F%9A%81)](https://git.io/typing-svg)

</div>

---

<img align="right" width="300" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWRiMm44bW5rNW9qZGpxZzF4b2RhZjNtaHFjOTdlcHV6NHlnZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qgQUggAC3Pfv687qPC/giphy.gif" alt="coding gif"/>

## 🧑‍💻 About Me

```yaml
name: Aghasalim Mustafazada
location: Kortrijk, Belgium 🇧🇪
education: B.Sc. Artificial Intelligence @ Howest (2nd year)
current_role: Head of IT @ Adscreen
experience: 4+ years in programming, teaching & IT infrastructure
status: Open to AI / Backend jobstudent & internship roles
fun_fact: "I manage 1,000+ AI tablets by day, study deep learning by night"
```

- 🎓 Second-year **Artificial Intelligence** student at [Howest](https://www.howest.be/) (Kortrijk, Belgium)
- 🏢 Managing IT infrastructure for **1,000+ AI-powered digital signage tablets** at [Adscreen](https://adscreen.com)
- 🏆 **Gold Medal** — International STEM Olympiad, Mathematics (France, 2022)
- 🥉 **Bronze Medal** — International STEM Olympiad, German Language (Germany, 2023)
- 🚁 Built an **AI drone navigation system** that secured venture investment
- 👨‍🏫 Former **Programming Instructor** at STEP IT Academy (4 years, 200+ students)
- 🌍 Multilingual: Azerbaijani, English (C1), Turkish, German (A2-B1), Dutch (learning)

<br clear="right"/>

---

## 🔭 What I'm Working On

| Project | Description | Stack |
|---------|-------------|-------|
| 🖥️ **Adscreen Infrastructure** | Scaling AI tablet fleet across Belgium & Netherlands | Python, Docker, SQL, CV models |
| 🧠 **Audience Analytics** | Real-time computer vision for driver/passenger engagement | TensorFlow, OpenCV, FastAPI |
| 📊 **ML Targeting Engine** | Recommendation system for personalized ad delivery | scikit-learn, PostgreSQL, REST APIs |
| 🎓 **Howest AI Projects** | Deep learning coursework, NLP classifiers, CV pipelines | PyTorch, Transformers, YOLO |

## 🌱 Currently Learning

| Domain | Topics |
|--------|--------|
| 🧬 Deep Learning | Advanced architectures, attention mechanisms, generative models |
| ⚙️ MLOps | MLflow, model versioning, automated retraining pipelines |
| 📦 Edge AI | Model optimization, ONNX, deployment on resource-constrained devices |
| 🗣️ Languages | Dutch (daily practice in Kortrijk 🇧🇪) |

---

## 🚀 Featured Projects

### 🚁 AI-Powered Drone Navigation System for Smart Cities
> *#AI #MachineLearning #SmartCities*

<a href="https://www.linkedin.com/posts/mustafazada_ai-machinelearning-smartcities-ugcPost-7423344619452547072-VDn0">
  <img src="https://img.shields.io/badge/Read%20on-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Post"/>
</a>

Designed and built an **autonomous drone navigation system** leveraging machine learning for intelligent urban routing. The project integrates real-time sensor fusion, computer vision, and path-planning algorithms to enable drones to navigate complex city environments safely and efficiently.

| Aspect | Details |
|---|---|
| **Problem** | Traditional GPS-only drone navigation fails in dense urban areas with signal occlusion, dynamic obstacles, and no-fly zone constraints |
| **Solution** | Multi-modal AI pipeline combining LiDAR/camera sensor fusion with reinforcement learning-based path planning |
| **Computer Vision** | Real-time obstacle detection & avoidance using convolutional neural networks for object classification |
| **Path Planning** | ML-driven route optimization accounting for wind patterns, building layouts, and restricted airspace |
| **Smart City Integration** | Designed for urban logistics, infrastructure inspection, and emergency response use cases |
| **Impact** | Secured **venture capital investment** from international investors based on the prototype demonstration |
| **Tech Stack** | Python, TensorFlow, OpenCV, ROS (Robot Operating System), Sensor Fusion, Reinforcement Learning |

---

### 🔐 RFID & Face Recognition Attendance System
> *Full hardware + software build — published on Instructables (730+ views)*

<a href="https://www.instructables.com/Build-Your-Own-RFID-Face-Recognition-Attendance-Sy/">
  <img src="https://img.shields.io/badge/Full%20Guide-Instructables-FFBF00?style=for-the-badge&logo=instructables&logoColor=black" alt="Instructables"/>
</a>

An end-to-end **automated attendance system** combining RFID card scanning with YOLOv8-based face recognition for dual-factor identity verification. Built from scratch with a custom 3D-printed enclosure, it runs entirely on local hardware — no cloud dependency.

| Aspect | Details |
|---|---|
| **Hardware** | Raspberry Pi 4, Arduino Mega 2560, RFID-RC522 module, TFT touchscreen display, USB webcam, custom 3D-printed enclosure |
| **Face Recognition** | YOLOv8 model (`best.pt`) trained for real-time face identification via the Pi's USB camera |
| **RFID Verification** | Dual-factor auth — RFID card UID must match the face detected by the camera before granting access |
| **Feedback System** | TFT display shows VERIFYING → GRANTED/DENIED; green/red LEDs + buzzer for audio-visual confirmation |
| **Web Dashboard** | Local HTTP server serving 3 interfaces: student management, raw access logs, and attendance analytics with charts |
| **Communication** | Raspberry Pi ↔ Arduino serial UART link with voltage-safe level shifting; SPI for RFID module |
| **Data Pipeline** | All events logged to local `logs.json` → parsed by JS dashboards in real time — fully offline, zero cloud |
| **Tech Stack** | Python, OpenCV, YOLOv8 (Ultralytics), Arduino C++, HTML/CSS/JS, Serial (PySerial), GPIO (gpiozero) |

<details>
<summary><b>System Architecture</b></summary>

```
┌─────────────────────┐     UART Serial      ┌──────────────────────┐
│   RASPBERRY PI 4    │◄────────────────────►│    ARDUINO MEGA      │
│                     │                       │                      │
│  ┌───────────────┐  │                       │  ┌────────────────┐  │
│  │  YOLOv8 Model │  │                       │  │  RFID-RC522    │  │
│  │  (best.pt)    │  │                       │  │  (SPI Bus)     │  │
│  └───────────────┘  │                       │  └────────────────┘  │
│  ┌───────────────┐  │                       │  ┌────────────────┐  │
│  │  USB Webcam   │  │                       │  │  TFT Display   │  │
│  │  (OpenCV)     │  │                       │  │  (MCUFRIEND)   │  │
│  └───────────────┘  │                       │  └────────────────┘  │
│  ┌───────────────┐  │                       └──────────────────────┘
│  │  GPIO LEDs    │  │
│  │  + Buzzer     │  │     ┌──────────────────────┐
│  └───────────────┘  │     │   WEB DASHBOARDS     │
│  ┌───────────────┐  │     │  ┌────────────────┐  │
│  │  HTTP Server  │◄─┼────►│  │ manage_students│  │
│  │  (port 8000)  │  │     │  │ logs.html      │  │
│  └───────────────┘  │     │  │ dashboard.html │  │
└─────────────────────┘     │  └────────────────┘  │
                            └──────────────────────┘
```

</details>

---

## 🛠️ My Skill Set

<div align="center">

<table>
<tr>
<td valign="top" width="25%">
<h3 align="center">AI / ML</h3>
<div align="center">
<a href="https://www.python.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>
<a href="https://www.tensorflow.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/tensorflow-icon.svg" alt="TensorFlow" height="50" /></a>
<a href="https://pytorch.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/pytorch-icon.svg" alt="PyTorch" height="50" /></a>
<a href="https://opencv.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/opencv-icon.svg" alt="OpenCV" height="50" /></a>
<a href="https://keras.io/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/keras.png" alt="Keras" height="50" /></a>
<a href="https://scikit-learn.org/" target="_blank"><img style="margin: 8px" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit-learn" height="50" /></a>
<a href="https://huggingface.co/" target="_blank"><img style="margin: 8px" src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" height="50" /></a>
<a href="https://numpy.org/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" height="50" /></a>
<a href="https://pandas.pydata.org/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="Pandas" height="50" /></a>
</div>
</td>
<td valign="top" width="25%">
<h3 align="center">Backend</h3>
<div align="center">
<a href="https://www.python.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>
<a href="https://nodejs.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/nodejs-original-wordmark.svg" alt="Node.js" height="50" /></a>
<a href="https://fastapi.tiangolo.com/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="FastAPI" height="50" /></a>
<a href="https://flask.palletsprojects.com/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="Flask" height="50" /></a>
<a href="https://www.postgresql.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/postgresql-original-wordmark.svg" alt="PostgreSQL" height="50" /></a>
<a href="https://www.mongodb.com/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/mongodb-original-wordmark.svg" alt="MongoDB" height="50" /></a>
<a href="https://www.mysql.com/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/mysql-original-wordmark.svg" alt="MySQL" height="50" /></a>
<a href="https://www.linux.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/linux-original.svg" alt="Linux" height="50" /></a>
<a href="https://github.com/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/git-scm-icon.svg" alt="Git" height="50" /></a>
<a href="https://www.gnu.org/software/bash/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/gnu_bash-icon.svg" alt="Bash" height="50" /></a>
</div>
</td>
<td valign="top" width="25%">
<h3 align="center">Frontend</h3>
<div align="center">
<a href="https://reactjs.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/react-original-wordmark.svg" alt="React" height="50" /></a>
<a href="https://www.javascript.com/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/javascript-original.svg" alt="JavaScript" height="50" /></a>
<a href="https://www.typescriptlang.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/typescript-original.svg" alt="TypeScript" height="50" /></a>
<a href="https://www.w3schools.com/css/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/css3-original-wordmark.svg" alt="CSS3" height="50" /></a>
<a href="https://en.wikipedia.org/wiki/HTML5" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/html5-original-wordmark.svg" alt="HTML5" height="50" /></a>
<a href="https://tailwindcss.com/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tailwindcss/tailwindcss-original.svg" alt="Tailwind CSS" height="50" /></a>
<a href="https://streamlit.io/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/streamlit/streamlit-original.svg" alt="Streamlit" height="50" /></a>
</div>
</td>
<td valign="top" width="25%">
<h3 align="center">DevOps & Hardware</h3>
<div align="center">
<a href="https://www.docker.com/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/docker-original-wordmark.svg" alt="Docker" height="50" /></a>
<a href="https://kubernetes.io/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/kubernetes-icon.svg" alt="Kubernetes" height="50" /></a>
<a href="https://www.nginx.com/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="Nginx" height="50" /></a>
<a href="https://www.arduino.cc/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/arduino.png" alt="Arduino" height="50" /></a>
<a href="https://www.raspberrypi.org/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/raspberrypi.png" alt="Raspberry Pi" height="50" /></a>
<a href="https://isocpp.org/" target="_blank"><img style="margin: 8px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="C++" height="50" /></a>
<a href="https://www.php.net/" target="_blank"><img style="margin: 8px" src="https://profilinator.rishav.dev/skills-assets/php-original.svg" alt="PHP" height="50" /></a>
<a href="https://powerbi.microsoft.com/" target="_blank"><img style="margin: 8px" src="https://img.icons8.com/color/48/power-bi.png" alt="Power BI" height="50" /></a>
</div>
</td>
</tr>
</table>

</div>

---

## 🤝 Connect with me

 [![github](https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/aghasalim)[![linkedin](https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white) ](https://linkedin.com/in/mustafazada)[![instagram](https://img.shields.io/badge/instagram-%23000000.svg?&style=for-the-badge&logo=instagram&logoColor=white) ](https://instagram.com/fwsalim)[![email](https://img.shields.io/badge/email-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white)](mailto:salim.mustafazada@student.howest.be)

---

## Github Stats

![](https://github-readme-stats.vercel.app/api?username=aghasalim&show_icons=true&count_private=true&hide_border=true&theme=tokyonight)

  

![](https://github-readme-streak-stats.herokuapp.com/?user=aghasalim&theme=tokyonight&hide_border=true)

  

![](https://github-readme-stats.vercel.app/api/top-langs/?username=aghasalim&hide_border=true&layout=compact&theme=tokyonight)

---

![Profile views](https://komarev.com/ghpvc/?username=aghasalim&style=flat-square&color=blue)

**If you’re hiring for AI / Backend / Full-stack roles in Belgium or the EU — let’s talk.**