# Configuration Management and CI/CD Assignment

## Overview

This project demonstrates the use of configuration management tools and the implementation of a CI/CD pipeline with a Blue-Green deployment strategy.

---

## Part 1: Configuration Management Tools Comparison

### Tools Covered

- Ansible
- Puppet
- Chef

### Comparison

| Feature | Ansible | Puppet | Chef |
|-------|-------|-------|-------|
| Architecture | Agentless | Agent-based | Agent-based |
| Language | YAML | Puppet DSL | Ruby |
| Learning Curve | Easy | Medium | Hard |
| Setup Complexity | Low | Medium | High |
| Best Use Case | Small/Medium Infrastructure | Large Enterprises | Complex Automation |

### Advantages

#### Ansible
- Agentless
- Easy YAML syntax
- Quick deployment

#### Puppet
- Strong enterprise support
- Scalable infrastructure management

#### Chef
- Highly customizable
- Powerful automation framework

---

## Part 2: CI/CD Pipeline with Blue-Green Deployment

### Tools Used

- Jenkins
- Docker
- Ansible
- GitHub

---

## CI/CD Pipeline Architecture

---

## Blue-Green Deployment

Blue-Green deployment reduces downtime by running two identical environments.

| Environment | Port |
|------------|------|
| Blue | 8081 |
| Green | 8082 |

Traffic is switched between environments after successful deployment.

---

## Running Containers

Blue Environment
Green Environment


docker run -d -p 8082:80 webapp


---


## Conclusion

This project demonstrates how configuration management and CI/CD pipelines can be integrated 