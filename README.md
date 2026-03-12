# DevOps Practical Assignments Repository

## Author

**Name:** Nirmalya Das
**Role:** DevOps Learner
**Repository:** PW DevOps Assignments

---

# Repository Overview

This repository contains practical assignments completed while learning **DevOps tools and cloud-native technologies**.

The assignments demonstrate hands-on implementation of:

* Linux fundamentals
* Configuration management (Ansible)
* CI/CD pipelines (Jenkins)
* Containerization (Docker)
* Multi-container orchestration (Docker Compose)
* Container orchestration (Kubernetes)
* Kubernetes package management (Helm)

The goal of this repository is to build practical DevOps skills and maintain a structured portfolio of DevOps labs and projects.

---

# Repository Structure

```
PW-Assignments
│
├── Linux
├── CI-CD
├── Docker1-Assignment
├── Docker2-Assignment
├── Ansible-1-assignment
├── Ansible-2-assignment
├── configuration-management-assignment
└── Kubernetes-Assignments
```

Each folder contains:

* Implementation files
* Configuration scripts
* Documentation
* Screenshots (if required)

---

# Technologies Used

| Technology     | Purpose                         |
| -------------- | ------------------------------- |
| Linux          | Operating system fundamentals   |
| Git & GitHub   | Version control                 |
| Jenkins        | CI/CD automation                |
| Docker         | Containerization                |
| Docker Compose | Multi-container applications    |
| Ansible        | Configuration management        |
| Kubernetes     | Container orchestration         |
| Helm           | Kubernetes package manager      |
| Nginx          | Web server used for deployments |

---

# Linux Assignments

Linux exercises include:

* File system navigation
* File permissions
* Package management
* Basic Linux commands used in DevOps environments

---

# Configuration Management

Configuration management tasks demonstrate automation using tools such as:

* Ansible
* Puppet
* Chef (comparison)

Key tasks performed:

* Installing configuration management tools
* Writing automation scripts
* Automating software installation

---

# CI/CD Assignment

CI/CD pipelines were implemented using **Jenkins**.

Pipeline stages include:

1. Clone repository
2. Build Docker image
3. Deploy containers
4. Verify application deployment

Example pipeline command:

```
docker build -t webapp .
docker run -d -p 8080:80 webapp
```

---

# Docker Assignment

Docker was used to containerize a simple web application.

Steps performed:

1. Install Docker
2. Create Dockerfile
3. Build Docker image
4. Run container
5. Verify containerized application

Example Dockerfile:

```
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

Build image:

```
docker build -t docker-webapp .
```

Run container:

```
docker run -d -p 8080:80 docker-webapp
```

---

# Docker Compose Assignment

Docker Compose was used to deploy a **multi-container application**.

Services deployed:

* Nginx (web server)
* Redis (database)

Example compose command:

```
docker compose up -d
```

Check containers:

```
docker ps
```

---

# Ansible Assignments

Ansible was used for **configuration automation**.

Tasks performed:

* Installing Ansible
* Configuring inventory
* Writing playbooks
* Automating Nginx installation

Example playbook:

```
- name: Install nginx
  apt:
    name: nginx
    state: present
```

Run playbook:

```
ansible-playbook install_nginx.yml
```

---

# Kubernetes Assignments

Kubernetes cluster was created using **Minikube**.

Tasks performed:

* Cluster setup
* Deploying Nginx application
* Managing pods, services, and deployments
* Scaling replicas
* Configuring NodePort and ClusterIP services
* Creating Ingress resources

Example deployment:

```
kubectl create deployment nginx-deployment --image=nginx
```

Scale deployment:

```
kubectl scale deployment nginx-deployment --replicas=5
```

Check resources:

```
kubectl get all
```

---

# Helm Deployment

Helm was used to simplify Kubernetes application deployment.

Helm commands used:

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-nginx bitnami/nginx
```

Check Helm releases:

```
helm list
```

---

# Learning Outcomes

Through these assignments the following DevOps concepts were practiced:

* Infrastructure automation
* Containerization
* CI/CD pipeline implementation
* Kubernetes resource management
* Microservice deployment
* Infrastructure as Code

---

# Future Improvements

This repository will be expanded to include:

* Terraform infrastructure provisioning
* Advanced Kubernetes deployments
* Monitoring using Prometheus and Grafana
* Production-grade CI/CD pipelines
* Cloud deployments using AWS

---

# Conclusion

This repository serves as a **hands-on DevOps learning portfolio** demonstrating practical experience with modern DevOps tools and container-based application deployment workflows.
