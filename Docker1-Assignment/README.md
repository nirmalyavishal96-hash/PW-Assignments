# Docker Containerization Assignment

## Author
Nirmalya Das

---

# Project Overview

This project demonstrates how Docker can be used to containerize applications.

A simple web application is containerized using a Dockerfile and deployed using an Nginx container.

---

# Technologies Used

| Tool | Purpose |
|-----|------|
| Docker | Containerization |
| Nginx | Web Server |
| HTML | Web Page |

---


# Dockerfile

```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

---

# Build Docker Image

```
docker build -t docker-webapp .
```

---

# Run Container

```
docker run -d -p 8081:80 docker-webapp
```

---

# Verify Container

```
docker ps
```

Open browser:

```
http://localhost:8081
```

---

# Output

The browser displays the custom HTML page running inside the Docker container.

---

# Conclusion

Docker simplifies application deployment by packaging applications and their dependencies into containers. This ensures consistent environments across development, testing, and production.