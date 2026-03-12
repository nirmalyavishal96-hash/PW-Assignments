# Docker Compose Multi-Container Application

## Author
Nirmalya Das

---

# Project Overview

This project demonstrates how Docker Compose can be used to define and run multi-container applications.

Two containers are used in this project:

- Nginx (Web Server)
- Redis (Caching Service)

---

# Technologies Used

| Tool | Purpose |
|-----|------|
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Nginx | Web server |
| Redis | Cache database |


---

# Docker Compose Configuration

```yaml
version: '3'

services:

  web:
    image: nginx:latest
    ports:
      - "8081:80"
    volumes:
      - ./index.html:/usr/share/nginx/html/index.html

  redis:
    image: redis:latest
```

---

# Run Application

```
docker compose up -d
```

---

# Check Running Containers

```
docker ps
```

---

# Access Application

Open browser:

```
http://localhost:8081
```

---

# Stop Containers

```
docker compose down
```

---

# Conclusion

Docker Compose simplifies the management of multi-container applications by defining services in a single configuration file.