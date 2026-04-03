
1. Project Overview 

Developed and deployed a Flask-based fitness web application that includes: 

Workout tracking  

Member management  

Calorie calculator  

Gym analytics dashboard  

REST APIs + UI  

This app evolved from multiple desktop versions into a modern web application with DevOps practices 

2. Infrastructure Setup (AWS) 

Created an EC2 instance (Linux)  

Connected via SSH  

Installed required tools:  

Docker  

Jenkins  

k3s (lightweight Kubernetes)  

Configured Security Groups: 

Opened ports:  

22 → SSH  

8080 → Jenkins  

30007 → Application (NodePort)  

 

3. Version Control (GitHub) 

Created a GitHub repository: 

introduction-to-devops-assignment-1-march2026 

Pushed:  

Flask app (app.py)  

Dockerfile  

Kubernetes manifests  

Jenkinsfile  

 This became the single source of truth 

4. Containerization (Docker) 

Created a Dockerfile for the Flask app  

Built image:  

docker build -t aceest-app . 

Result: 

Image stored locally in EC2  

Used by Kubernetes for deployment  

 

5. CI/CD Pipeline (Jenkins) 

Installed Jenkins on EC2  

Created a pipeline job  

Connected to GitHub repo  

Pipeline stages: 

1. Checkout → Pull code from GitHub 
2. Build Docker → Create Docker image 
3. Deploy K8s → Apply Kubernetes manifests 

Fully automated flow: 

Code change → Jenkins build → Deployment 

6. Kubernetes Deployment (k3s) 

Created: 

Deployment 

Runs Flask app container  

Ensures app is always running  

Service (NodePort) 

Exposes app externally  

NodePort: 30007 

Applied using: 

k3s kubectl apply -f deployment.yaml 
k3s kubectl apply -f service.yaml 

7. Debugging & Fixes (Key Learning) 

Solved multiple real-world DevOps issues: 

Issue 1: Jenkins Node Offline 

 Fixed by: 

Adding swap memory  

Cleaning disk space  

Issue 2: Git Branch Error 

Couldn't find revision to build 

Fixed by: 

Using correct branch (main instead of master)  

 

Issue 3: Docker Permission Error 

permission denied docker.sock 

Fixed by: 

Adding Jenkins user to Docker group  

Issue 4: sudo password in Jenkins 

Fixed by: 

Editing /etc/sudoers  

jenkins ALL=(ALL) NOPASSWD: ALL 

Issue 5: Kubernetes YAML path issue 

Fixed by: 

Correcting file paths:  

k3s/manifests/deployment.yaml 

Issue 6: App not accessible 

Root causes fixed: 

Security group port open  

Correct NodePort  

Correct public IP  

8. Final Deployment (SUCCESS) 

Application running: 

Pod: Running  

Service: NodePort exposed  

Jenkins: Pipeline successful  

Access URL: 

http://18.60.107.158:30007/ 

Successfully accessed the app in browser 

9. Architecture Flow 

GitHub → Jenkins → Docker → Kubernetes → Browser 

Code pushed to GitHub  

Jenkins pulls code  

Docker builds image  

Kubernetes deploys container  

App exposed via NodePort  

User accesses via browser  

10. Key DevOps Concepts Demonstrated 

CI/CD pipeline  

Containerization (Docker)  

Orchestration (Kubernetes)  

Infrastructure setup (AWS EC2)  

Automation (Jenkins pipeline)  

Debugging real-world issues  

 

Final Conclusion 

Successfully built a complete DevOps pipeline from scratch: 

Developed application 

Containerized with Docker 

Automated build using Jenkins 

Deployed using Kubernetes 

Exposed to internet via AWS 

 

 

 

Important Links Used in The Project 

1. GitHub Repository (Source Code) 

https://github.com/KollaNagaManasa/introduction-to-devops-assignment-1-march2026 

Contains: 

Flask app  

Dockerfile  

Kubernetes manifests  

Jenkinsfile  

GitHub Actions workflow  

2. GitHub Actions (CI Pipeline) 

 https://github.com/KollaNagaManasa/introduction-to-devops-assignment-1-march2026/actions 

Shows: 

Automated test execution (pytest)  

Build status (SUCCESS)  

 3. Jenkins (CD Pipeline) 

http://18.60.107.158:8080 

Used for: 

Pipeline automation  

Docker build  

Kubernetes deployment  

4. Kubernetes Deployment (CLI access) 

(No direct UI link — accessed via terminal) 

Commands used: 

k3s kubectl get pods 
k3s kubectl get svc 

5. Deployed Application (Final Output) 

 http://18.60.146.121:30007 

This is the live application 

6. AWS Console (Infrastructure) 

 https://ap-south-2.console.aws.amazon.com/ec2 

Used for: 

EC2 instance  

Security groups  

Networking 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Images: 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
