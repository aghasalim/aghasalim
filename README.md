# Hey there, I’m Aghasalim 👋

### [B.Sc](http://B.Sc). AI Student @ Howest | Head of IT @ Adscreen | Builder

---

🎓 Second-year **Artificial Intelligence** student at [Howest](https://www.howest.be/) (Kortrijk, Belgium)  
🏢 Currently managing IT infrastructure for **1,000+ AI tablets** at [Adscreen](https://adscreen.com)  
🏆 International Gold Medalist in Mathematics  
🚁 Built AI drone navigation system that secured venture investment  
📍 Based in **Kortrijk, Belgium**

---

## 🔭 What I’m Working On

-   Scaling AI-powered digital signage infrastructure at Adscreen
-   Computer vision models for real-time audience analytics
-   Deep learning coursework & research projects at Howest
-   Looking for **jobstudent / internship** opportunities in AI & Backend

## 🌱 Currently Learning

-   Advanced Deep Learning architectures
-   MLOps best practices (MLflow, model versioning)
-   Edge AI deployment & optimization
-   Dutch 🇧🇪 (daily practice in Kortrijk)

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

<table><tbody><tr><td valign="top" width="33%"><h3 id="ai-ml" class="md-heading" data-line="38">AI / ML</h3><div align="center"><a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50"></a> <a href="https://www.tensorflow.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/tensorflow-icon.svg" alt="TensorFlow" height="50"></a> <a href="https://pytorch.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/pytorch-icon.svg" alt="PyTorch" height="50"></a> <a href="https://opencv.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/opencv-icon.svg" alt="OpenCV" height="50"></a> <a href="https://keras.io/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/keras.png" alt="Keras" height="50"></a></div></td><td valign="top" width="33%"><h3 id="backend" class="md-heading" data-line="49">Backend</h3><div align="center"><a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50"></a> <a href="https://nodejs.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/nodejs-original-wordmark.svg" alt="Node.js" height="50"></a> <a href="https://www.postgresql.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/postgresql-original-wordmark.svg" alt="PostgreSQL" height="50"></a> <a href="https://www.mongodb.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/mongodb-original-wordmark.svg" alt="MongoDB" height="50"></a> <a href="https://www.mysql.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/mysql-original-wordmark.svg" alt="MySQL" height="50"></a> <a href="https://www.linux.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/linux-original.svg" alt="Linux" height="50"></a> <a href="https://github.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/git-scm-icon.svg" alt="Git" height="50"></a> <a href="https://www.gnu.org/software/bash/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/gnu_bash-icon.svg" alt="Bash" height="50"></a></div></td><td valign="top" width="33%"><h3 id="frontend-devops" class="md-heading" data-line="63">Frontend &amp; DevOps</h3><div align="center"><a href="https://reactjs.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/react-original-wordmark.svg" alt="React" height="50"></a> <a href="https://www.javascript.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/javascript-original.svg" alt="JavaScript" height="50"></a> <a href="https://www.w3schools.com/css/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/css3-original-wordmark.svg" alt="CSS3" height="50"></a> <a href="https://en.wikipedia.org/wiki/HTML5" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/html5-original-wordmark.svg" alt="HTML5" height="50"></a> <a href="https://www.docker.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/docker-original-wordmark.svg" alt="Docker" height="50"></a> <a href="https://kubernetes.io/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/kubernetes-icon.svg" alt="Kubernetes" height="50"></a> <a href="https://www.arduino.cc/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/arduino.png" alt="Arduino" height="50"></a> <a href="https://www.raspberrypi.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/raspberrypi.png" alt="Raspberry Pi" height="50"></a></div></td></tr></tbody></table>

---

## Connect with me

 [![github](https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/aghasalim)[![linkedin](https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white) ](https://linkedin.com/in/mustafazada)[![instagram](https://img.shields.io/badge/instagram-%23000000.svg?&style=for-the-badge&logo=instagram&logoColor=white) ](https://instagram.com/fwsalim)[![email](https://img.shields.io/badge/email-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white)](mailto:salim.mustafazada@student.howest.be)

---

## Github Stats

![](https://github-readme-stats.vercel.app/api?username=aghasalim&show_icons=true&count_private=true&hide_border=true&theme=tokyonight)

  

![](https://github-readme-streak-stats.herokuapp.com/?user=aghasalim&theme=tokyonight&hide_border=true)

  

![](https://github-readme-stats.vercel.app/api/top-langs/?username=aghasalim&hide_border=true&layout=compact&theme=tokyonight)

---

![Profile views](https://komarev.com/ghpvc/?username=aghasalim&style=flat-square&color=blue)

**If you’re hiring for AI / Backend / Full-stack roles in Belgium or the EU — let’s talk.**