# Kubernetes Practical Assignments (1–5)

## Author

**Name:** Nirmalya Das
**Course:** Kubernetes
**Environment Used:** Minikube (Local Kubernetes Cluster)

---

# Project Overview

This project demonstrates **basic Kubernetes resource management** using Minikube.
The assignments cover the following topics:

* Kubernetes cluster setup
* Deploying applications using Deployments
* Managing Pods and Services
* Scaling deployments
* Configuring NodePort and ClusterIP services
* Configuring Ingress for routing between services

---

# Tools and Technologies Used

| Tool       | Purpose                  |
| ---------- | ------------------------ |
| Kubernetes | Container orchestration  |
| Minikube   | Local Kubernetes cluster |
| kubectl    | Kubernetes CLI           |
| Docker     | Container runtime        |
| Nginx      | Web server               |

---

# Assignment 1 – Kubernetes Cluster Setup and Deployment

## Tasks

1. Deploy a Kubernetes cluster
2. Create an NGINX deployment with **3 replicas**

## Start Minikube Cluster

```
minikube start
```

## Verify Cluster

```
kubectl get nodes
```

## Create Deployment

```
kubectl create deployment nginx-deployment --image=nginx
```

## Scale Deployment to 3 Replicas

```
kubectl scale deployment nginx-deployment --replicas=3
```

## Verify Deployment

```
kubectl get deployments
kubectl get pods
```

---

# Assignment 2 – NodePort Service

## Tasks

1. Use the previous deployment
2. Create a **NodePort service**
3. Verify service in browser

## Create NodePort Service

```
kubectl expose deployment nginx-deployment --type=NodePort --port=80
```

## Verify Service

```
kubectl get services
```

## Access Service

```
minikube service nginx-deployment
```

Open the URL in browser.

---

# Assignment 3 – Scaling Deployment

## Task

Increase the deployment replicas to **5**

## Scale Deployment

```
kubectl scale deployment nginx-deployment --replicas=5
```

## Verify Pods

```
kubectl get pods
```

You should see **5 running pods**.

---

# Assignment 4 – Change Service Type

## Task

Change service type to **ClusterIP**

## Edit Service

```
kubectl edit service nginx-deployment
```

Change:

```
type: NodePort
```

to

```
type: ClusterIP
```

## Verify

```
kubectl get services
```

---

# Assignment 5 – Additional Deployment and Ingress

## Tasks

1. Use previous deployment
2. Deploy another NGINX deployment with **3 replicas**
3. Create ClusterIP service
4. Configure ingress routing

---

## Create Second Deployment

```
kubectl create deployment nginx-app2 --image=nginx
```

Scale deployment:

```
kubectl scale deployment nginx-app2 --replicas=3
```

---

## Create ClusterIP Service

```
kubectl expose deployment nginx-app2 --type=ClusterIP --port=80
```

Verify:

```
kubectl get services
```

---

## Enable Ingress Controller

```
minikube addons enable ingress
```

---

## Create Ingress

```
kubectl create ingress nginx-ingress \
--rule="nginx1.local/*=nginx-deployment:80" \
--rule="nginx2.local/*=nginx-app2:80"
```

Verify ingress:

```
kubectl get ingress
```

---

# Verify All Kubernetes Resources

Run the following command to view all cluster resources:

```
kubectl get all
```

This displays:

* Pods
* Deployments
* Services
* ReplicaSets

---

# Access Application

To access services in browser:

```
minikube service nginx-deployment
```

or

```
minikube service nginx-app2
```

---

# Screenshots for Assignment

Include screenshots of the following commands:

1. `kubectl get nodes`
2. `kubectl get deployments`
3. `kubectl get pods`
4. `kubectl get services`
5. `kubectl scale deployment nginx-deployment --replicas=5`
6. `kubectl get ingress`
7. `kubectl get all`
8. Browser output of Nginx service

---

# Stop Kubernetes Cluster

To stop Minikube:

```
minikube stop
```

To completely delete cluster:

```
minikube delete
```

---

# Conclusion

These assignments demonstrate fundamental Kubernetes operations including:

* Deployment creation
* Pod management
* Service exposure
* Deployment scaling
* Ingress configuration

Using Minikube allows developers to experiment with Kubernetes locally before deploying applications in production environments.
