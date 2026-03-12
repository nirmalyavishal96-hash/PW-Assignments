# Kubernetes Minikube Deployment

## Author
Nirmalya Das

---

# Project Overview

This project demonstrates how to deploy and manage applications on Kubernetes using Minikube.

The following tasks were performed:

- Setup Kubernetes cluster using Minikube
- Deploy application using Kubernetes Deployment
- Expose application using Service
- Manage Kubernetes resources
- Deploy application using Helm charts

---

# Technologies Used

| Tool | Purpose |
|-----|------|
| Kubernetes | Container orchestration |
| Minikube | Local cluster |
| kubectl | Kubernetes CLI |
| Helm | Kubernetes package manager |
| Docker | Container runtime |

---

# Start Minikube

```
minikube start
```

---

# Deploy Application

```
kubectl create deployment nginx-deployment --image=nginx
```

---

# Check Pods

```
kubectl get pods
```

---

# Expose Deployment

```
kubectl expose deployment nginx-deployment --type=NodePort --port=80
```

---

# Access Application

```
minikube service nginx-deployment
```

---

# Deploy using Helm

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx
```

---

# Check Helm Releases

```
helm list
```

---

# Conclusion

This project demonstrates Kubernetes deployment, resource management, and application packaging using Helm charts.clea