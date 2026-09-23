# 🎓 Student Feedback Management System using DevOps Automation

An end-to-end beginner-friendly web application designed to collect and manage college student feedback while demonstrating a complete modern CI/CD automation workflow with **Git/GitHub**, **Docker**, and **Jenkins**.

---

## 📌 Problem Statement

In many colleges and educational institutions, student feedback is either gathered on paper or through scattered forms with no unified visibility. This leads to:
- Loss of valuable student feedback.
- Manual effort in consolidating responses.
- Inconsistent and slow software deployment cycles when updating institutional tools.

**Solution:**
A lightweight, digital, file-backed web portal where students can submit ratings and reviews in seconds, paired with a robust DevOps pipeline that automates testing, container packaging, and deployment.

---

## 🎯 Objectives

1. **Digital Student Feedback**: Offer a simple, modern, responsive portal for students to submit department-level feedback.
2. **Zero-Database Overhead**: Store data cleanly and reliably inside `feedback.txt`, making it easy to inspect, back up, and demonstrate without database setup issues.
3. **Hands-On DevOps Integration**: Provide college students with a working demonstration of:
   - **Git & GitHub** for version control and commit tracking.
   - **Docker** for consistent application containerization.
   - **Jenkins** for Continuous Integration and Continuous Deployment (CI/CD).
4. **Quick 2-Hour Demonstration**: Allow students to explain, build, containerize, and run the entire system within an academic evaluation window.

---

## ✨ Features

- **Easy Feedback Submission**: Form with student name, department selection, college email, 1-to-5 star rating, and feedback text.
- **Input Validation**: Server-side checks ensure all fields are properly completed.
- **Organized Feedback Storage**: Saved into structured records in `feedback.txt` with timestamps.
- **Real-Time Feedback Viewer**: Responsive card grid displaying student reviews, ratings, and submission dates.
- **DevOps Workflow Showcase**: Interactive workflow visualizer directly on the homepage.
- **Dockerized Architecture**: Runs identically on Windows, Linux, and macOS without environment discrepancies.
- **Automated CI/CD Pipeline**: Declarative `Jenkinsfile` managing checkout, build, docker image creation, and deployment.

---

## 🛠️ Technologies Used

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | HTML5, CSS3, Google Fonts | Responsive, modern, clean user interface |
| **Backend** | Python 3, Flask | Routing, form validation, and file I/O |
| **Storage** | File Storage (`feedback.txt`) | Lightweight, human-readable data persistence |
| **Containerization** | Docker | Packaging app and runtime environment |
| **CI/CD Automation**| Jenkins | Automated pipeline execution |
| **Version Control** | Git & GitHub | Source code tracking and pipeline triggers |

---

## 🚀 DevOps Tools Breakdown

### 1. 🐙 Git and GitHub (Version Control)
- **Role**: Tracks all code commits, branches, and changes.
- **How it works**:
  - Developers push changes to a GitHub repository (`git push origin main`).
  - GitHub acts as the single source of truth and triggers Jenkins build webhooks upon new commits.

### 2. ⚙️ Jenkins (CI/CD Automation)
- **Role**: Automates testing, building, and deploying the Flask application.
- **How it works** via `Jenkinsfile`:
  1. **Checkout**: Pulls the latest commit from GitHub.
  2. **Build**: Runs syntax compilation checks (`python -m py_compile app.py`).
  3. **Docker Build**: Creates a new Docker image tagged with the build number (`student-feedback:${BUILD_NUMBER}`).
  4. **Deploy**: Stops old container instances and runs the fresh container on port `5000`.

### 3. 🐳 Docker (Containerization)
- **Role**: Encapsulates the Python runtime, dependencies (`Flask`), and application code inside a lightweight Linux container.
- **How it works** via `Dockerfile`:
  - Uses `python:3.10-slim`.
  - Installs `requirements.txt`.
  - Exposes port `5000`.
  - Launches `python app.py` on `0.0.0.0:5000`.

---

## 🔄 Project Workflow Architecture

```
+--------------------------------------------------------------------+
|                         DEVELOPER WORKSTATION                      |
|                                                                    |
|  1. Writes Flask Code & HTML Templates                             |
|  2. Commits & Pushes Changes                                       |
+---------------------------------+----------------------------------+
                                  |
                                  v
+---------------------------------+----------------------------------+
|                     1. GIT & GITHUB REPOSITORY                     |
|                                                                    |
|  Tracks versions & emits webhook on commit                         |
+---------------------------------+----------------------------------+
                                  |
                                  v
+---------------------------------+----------------------------------+
|                  2. JENKINS CI/CD AUTOMATION                       |
|                                                                    |
|  Stage 1: Checkout (Pull source code)                              |
|  Stage 2: Build & Test (Validate Python syntax)                    |
|  Stage 3: Docker Build (Compile image)                             |
|  Stage 4: Deploy (Launch Docker container)                         |
+---------------------------------+----------------------------------+
                                  |
                                  v
+---------------------------------+----------------------------------+
|                   3. DOCKER CONTAINER RUNTIME                      |
|                                                                    |
|  Image: student-feedback:latest                                    |
|  Port Mapping: 5000 -> 5000                                        |
+---------------------------------+----------------------------------+
                                  |
                                  v
+---------------------------------+----------------------------------+
|             4. RUNNING STUDENT FEEDBACK APPLICATION                |
|                                                                    |
|  Accessible at: http://localhost:5000                              |
|  Persists data in: feedback.txt                                    |
+--------------------------------------------------------------------+
```

---

## 📂 Project Structure

```
student-feedback-system/
│
├── app.py                # Main Flask backend application with routing & logic
├── requirements.txt      # Python dependencies list (Flask)
├── Dockerfile            # Container configuration for reproducible builds
├── feedback.txt          # File storage for student submissions
├── Jenkinsfile           # Declarative CI/CD pipeline definition
├── .gitignore            # Git ignore rules for clean repository
├── README.md             # Complete project and DevOps documentation
└── templates/            # HTML templates
    ├── base.html         # Base layout with navbar, footer, and styling
    ├── index.html        # Homepage with hero, features, workflow & about
    ├── feedback.html     # Feedback submission form with validation
    └── view_feedback.html# Display page for all student feedback
```

---

## 💻 How to Run the Project

### Method 1: Running Locally with Python

1. **Clone or Navigate to the Directory**:
   ```bash
   cd student-feedback-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and navigate to:
   [http://localhost:5000](http://localhost:5000)

---

### Method 2: Running with Docker (Recommended)

1. **Build the Docker Image**:
   ```bash
   docker build -t student-feedback .
   ```

2. **Run the Container**:
   ```bash
   docker run -d -p 5000:5000 --name student-feedback-app student-feedback
   ```

3. **Access the Containerized Application**:
   Open your browser at:
   [http://localhost:5000](http://localhost:5000)

4. **Useful Docker Commands**:
   - View running container:
     ```bash
     docker ps
     ```
   - View container logs:
     ```bash
     docker logs -f student-feedback-app
     ```
   - Stop the container:
     ```bash
     docker stop student-feedback-app
     ```
   - Remove the container:
     ```bash
     docker rm student-feedback-app
     ```

---

### Method 3: Running via Jenkins Pipeline

1. **Open Jenkins** (typically at `http://localhost:8080`).
2. Click **New Item** ➔ Choose **Pipeline** ➔ Name it `student-feedback-pipeline`.
3. In Pipeline configuration:
   - Under **Definition**, select **Pipeline script from SCM**.
   - Choose **Git** and enter your repository URL.
   - Set Script Path to `Jenkinsfile`.
4. Click **Save** and select **Build Now**.
5. Watch the stages:
   `Checkout` ➔ `Build` ➔ `Docker Build` ➔ `Deploy`.
6. Once complete, access the app at [http://localhost:5000](http://localhost:5000).

---

## 🎓 College Viva / Presentation Q&A Guide

**Q1: Why use a file (`feedback.txt`) instead of a SQL database?**  
*Answer:* For a beginner DevOps project, file storage eliminates database dependencies, external connection failures, and credential management, allowing the demonstration to focus 100% on core CI/CD automation concepts.

**Q2: What is the benefit of Docker in this project?**  
*Answer:* Docker guarantees that the Flask application runs identically on any system (Windows, Mac, Linux server) without having to manually install Python versions or matching packages on the host machine.

**Q3: What does the Jenkinsfile accomplish?**  
*Answer:* It defines the entire deployment pipeline as code (Pipeline-as-Code). Whenever changes are pushed to GitHub, Jenkins automatically verifies code syntax, builds a new Docker container, and restarts the live application with zero downtime.

---

## 📜 License
This project is open-source and intended for educational and academic demonstration purposes.
