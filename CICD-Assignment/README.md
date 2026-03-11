# CI/CD & DevSecOps Pipeline Implementation

**Author:** Nirmalya Das
**Course:** PW Skills DevOps Assignment
**Topic:** Continuous Integration, Testing, Security, and Continuous Deployment

---

# Project Overview

This project demonstrates the implementation of a **complete CI/CD and DevSecOps pipeline** using GitHub Actions.

The pipeline automatically performs:

* Continuous Integration (CI)
* Automated Testing
* Performance Testing
* Security Scanning
* Continuous Deployment (CD)

The main objective is to ensure that **every code push is automatically built, tested, scanned for vulnerabilities, and deployed to a staging environment**.

---

# Tools & Technologies Used

| Category             | Tools          |
| -------------------- | -------------- |
| Version Control      | GitHub         |
| CI/CD Automation     | GitHub Actions |
| Programming Language | Python         |
| Web Framework        | Flask          |
| Containerization     | Docker         |
| Performance Testing  | k6             |
| Security Testing     | OWASP ZAP      |
| Build Automation     | Jenkins        |

---

# CI/CD Pipeline Architecture

The automated pipeline performs the following stages:

| Stage | Description                               |
| ----- | ----------------------------------------- |
| 1     | Checkout the repository                   |
| 2     | Setup Python environment                  |
| 3     | Install project dependencies              |
| 4     | Run Unit Tests                            |
| 5     | Run API Integration Tests                 |
| 6     | Execute Performance Testing               |
| 7     | Perform Security Vulnerability Scan       |
| 8     | Build Docker Image                        |
| 9     | Deploy Application to Staging Environment |

---


# CI/CD Workflow Configuration

The pipeline configuration file is located at:

```
.github/workflows/ci.yml
```

The workflow automatically triggers whenever code is pushed to the **main branch**.

---

# Testing Stages

## 1️⃣ Unit Testing

Unit tests validate individual components of the application.

**Testing Tool Used**

```
pytest
```

Purpose:

* Verify correctness of functions
* Detect bugs early in development

---

## 2️⃣ Integration Testing

Integration testing verifies API functionality and endpoint communication.

Example API endpoint tested:

```
http://127.0.0.1:5000/hello
```

This ensures that the application responds correctly to HTTP requests.

---

## 3️⃣ Performance Testing

Performance testing is implemented using:

```
k6
```

This tool simulates multiple user requests and measures:

* Response time
* Throughput
* Error rates

---

## 4️⃣ Security Testing

Security scanning is performed using:

```
OWASP ZAP
```

The scanner checks for vulnerabilities such as:

* Missing security headers
* Information disclosure
* Cross-site scripting risks
* insecure configurations

---

# Continuous Deployment

After successful completion of all testing stages, the pipeline automatically deploys the application.

Deployment process:

1. Build a Docker image of the application
2. Run the Docker container as a **staging environment**

Deployment command:

```
docker run -d devops-api
```

---

# Staging Environment

The application is deployed as a **Docker container**, which represents the staging environment.

Benefits:

* Replicates production environment
* Allows testing before production release
* Ensures containerized deployment consistency

---

# CI/CD Pipeline Execution Flow

```
Code Push
   ↓
GitHub Actions Pipeline Triggered
   ↓
Install Dependencies
   ↓
Run Unit Tests
   ↓
Run Integration Tests
   ↓
Run Performance Tests
   ↓
Run Security Scan
   ↓
Build Docker Image
   ↓
Deploy to Staging Environment
```

---

# Key Benefits of the Pipeline

| Feature               | Benefit                  |
| --------------------- | ------------------------ |
| Automated Testing     | Detect bugs early        |
| Security Scanning     | Identify vulnerabilities |
| Performance Testing   | Ensure system stability  |
| Continuous Deployment | Faster software delivery |
| Containerization      | Environment consistency  |

---

# Conclusion

This project demonstrates the implementation of a **complete DevSecOps pipeline**, integrating:

* Continuous Integration
* Automated Testing
* Performance Testing
* Security Scanning
* Continuous Deployment

The automated workflow ensures **faster, reliable, and secure software delivery**, making the development lifecycle more efficient.

---

⭐ This project highlights practical DevOps skills including CI/CD pipeline creation, automated testing, containerization, and security integration.
